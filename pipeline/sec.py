#!/usr/bin/env python3
"""Historico das empresas a partir da SEC EDGAR (gratis, sem chave; a SEC pede identificacao no User-Agent).

- companyfacts: o que cada empresa reporta em XBRL nos 10-K / 10-Q (us-gaap) e 20-F (ifrs-full).
  Anual: ate 10 exercicios. Trimestral: ate 40 trimestres; o 4.o trimestre e os fluxos de caixa que as
  empresas so reportam em acumulado (6 e 9 meses) obtem-se por diferenca e ficam marcados como derivados.
- submissions: os filings (10-K, 10-Q, 8-K, 20-F, 6-K) com o link para o documento.
Empresas que nao reportam a SEC (Adyen) ficam de fora: os financials delas vem do CapIQ, via ficha.
Uma empresa que falha mantem a ultima copia boa.

Uso: SEC_UA="nome email" python pipeline/sec.py <raw> <out>
"""
import os, sys, time, datetime as dt
from comum import cfg, get, guardar, ler, mark, AGORA

RAW, OUT = sys.argv[1], sys.argv[2]
UA = os.environ.get('SEC_UA') or 'carteira-dados contacto-em-falta@example.com'
H = {'User-Agent': UA, 'Accept': 'application/json'}

# metrica -> (tipo, conceitos us-gaap por prioridade, conceitos ifrs-full por prioridade, unidade)
METRICAS = {
    'receita': ('fluxo', ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax',
                          'RevenueFromContractWithCustomerIncludingAssessedTax', 'SalesRevenueNet',
                          'RevenuesNetOfInterestExpense'],
                ['Revenue', 'RevenueFromContractsWithCustomers'], 'moeda'),
    'lucro_bruto': ('fluxo', ['GrossProfit'], ['GrossProfit'], 'moeda'),
    'i_d': ('fluxo', ['ResearchAndDevelopmentExpense', 'ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost'],
            ['ResearchAndDevelopmentExpense'], 'moeda'),
    'ebit': ('fluxo', ['OperatingIncomeLoss'], ['ProfitLossFromOperatingActivities'], 'moeda'),
    'lucro_liquido': ('fluxo', ['NetIncomeLoss', 'ProfitLoss'],
                      ['ProfitLossAttributableToOwnersOfParent', 'ProfitLoss'], 'moeda'),
    'eps_diluido': ('eps', ['EarningsPerShareDiluted'], ['DilutedEarningsLossPerShare'], 'eps'),
    'cfo': ('fluxo', ['NetCashProvidedByUsedInOperatingActivities',
                      'NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
            ['CashFlowsFromUsedInOperatingActivities'], 'moeda'),
    'capex': ('fluxo', ['PaymentsToAcquirePropertyPlantAndEquipment', 'PaymentsToAcquireProductiveAssets'],
              ['PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities', 'PurchaseOfPropertyPlantAndEquipment'],
              'moeda'),
    'd_a': ('fluxo', ['DepreciationDepletionAndAmortization', 'DepreciationAmortizationAndAccretionNet',
                      'DepreciationAndAmortization'], ['DepreciationAndAmortisationExpense'], 'moeda'),
    'sbc': ('fluxo', ['ShareBasedCompensation', 'AllocatedShareBasedCompensationExpense'],
            ['ExpenseFromSharebasedPaymentTransactionsWithEmployees'], 'moeda'),
    'recompras': ('fluxo', ['PaymentsForRepurchaseOfCommonStock'], ['PaymentsToAcquireOrRedeemEntitysShares'], 'moeda'),
    'dividendos': ('fluxo', ['PaymentsOfDividends', 'PaymentsOfDividendsCommonStock'],
                   ['DividendsPaidClassifiedAsFinancingActivities'], 'moeda'),
    'caixa': ('stock', ['CashAndCashEquivalentsAtCarryingValue',
                        'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'],
              ['CashAndCashEquivalents'], 'moeda'),
    'divida_lp': ('stock', ['LongTermDebt', 'LongTermDebtNoncurrent'], ['NoncurrentPortionOfNoncurrentBorrowings', 'Borrowings'],
                  'moeda'),
    'capital_proprio': ('stock', ['StockholdersEquity'], ['EquityAttributableToOwnersOfParent'], 'moeda'),
    'acoes_diluidas': ('acoes', ['WeightedAverageNumberOfDilutedSharesOutstanding'],
                       ['WeightedAverageShares', 'AdjustedWeightedAverageShares'], 'acoes'),
}
FORMS = ('10-K', '10-K/A', '10-Q', '10-Q/A', '20-F', '20-F/A', '40-F')
FILINGS = ('10-K', '10-Q', '8-K', '20-F', '6-K', '10-K/A', '20-F/A')


def dias(a, b):
    return (dt.date.fromisoformat(b) - dt.date.fromisoformat(a)).days


def unidade(units, tipo, moeda_pref):
    if tipo == 'eps':
        ks = [k for k in units if '/shares' in k]
    elif tipo == 'acoes':
        ks = [k for k in units if k == 'shares']
    else:
        ks = [k for k in units if k.isalpha() and len(k) == 3]
    if not ks:
        return None, None
    k = moeda_pref if moeda_pref in ks else max(ks, key=lambda x: len(units[x]))
    return k, units[k]


def factos(cf, conceitos, tax, tipo, moeda_pref):
    """{(inicio|None, fim): (valor, entregue)} juntando os conceitos por prioridade (o primeiro manda por periodo)."""
    out, uni = {}, None
    for c in conceitos:
        no = (cf.get('facts', {}).get(tax, {}) or {}).get(c)
        if not no:
            continue
        k, obs = unidade(no.get('units', {}), tipo, moeda_pref)
        if not obs:
            continue
        uni = uni or k
        if k != uni:
            continue
        este = {}
        for o in obs:
            if o.get('form') not in FORMS or o.get('val') is None:
                continue
            chave = (o.get('start'), o['end'])
            if chave not in este or o.get('filed', '') > este[chave][1]:
                este[chave] = (o['val'], o.get('filed', ''), 0)   # dentro do conceito: a entrega mais recente (restatements)
        for chave, v in este.items():
            out.setdefault(chave, v)                              # entre conceitos: o de maior prioridade manda
    return out, uni


def anual(f, tipo):
    linhas = {}
    for (ini, fim), (v, _, _) in f.items():
        if tipo == 'stock':
            continue
        if ini and 340 <= dias(ini, fim) <= 380:
            linhas[fim] = v
    return linhas


def trimestral(f, tipo):
    """Trimestres discretos: valores de 3 meses diretos; o resto por diferenca entre acumulados com o mesmo inicio."""
    direto, derivado = {}, {}
    porinicio = {}
    for (ini, fim), (v, _, _) in f.items():
        if not ini:
            continue
        n = dias(ini, fim)
        if 80 <= n <= 100:
            direto[fim] = v
        if any(a <= n <= b for a, b in ((80, 100), (170, 190), (260, 285), (340, 380))):
            porinicio.setdefault(ini, []).append((fim, v))
    if tipo != 'eps':
        for ini, lst in porinicio.items():
            lst.sort()
            for (f0, v0), (f1, v1) in zip(lst, lst[1:]):
                if 80 <= dias(f0, f1) <= 100 and f1 not in direto:
                    derivado[f1] = v1 - v0
    out = {k: [v, False] for k, v in direto.items()}
    for k, v in derivado.items():
        out.setdefault(k, [v, True])
    return out


def stocks(f):
    return {fim: v for (ini, fim), (v, _, _) in f.items() if ini is None}


def empresa(e, cik, moeda_pref):
    cf = get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json', hdr=H)
    time.sleep(0.2)
    sub = get(f'https://data.sec.gov/submissions/CIK{cik:010d}.json', hdr=H)
    time.sleep(0.2)
    if not cf:
        return None
    tax = 'us-gaap' if 'us-gaap' in cf.get('facts', {}) else 'ifrs-full'
    res = {'t': e['t'], 'cik': cik, 'nome_sec': cf.get('entityName'), 'taxonomia': tax, 'anual': {}, 'trimestral': {},
           'unidades': {}, 'lido': AGORA}
    stock_cache = {}
    for m, (tipo, us, ifrs, _) in METRICAS.items():
        f, uni = factos(cf, us if tax == 'us-gaap' else ifrs, tax, tipo, moeda_pref)
        if not f:
            continue
        res['unidades'][m] = uni
        if tipo == 'stock':
            st = stocks(f)
            stock_cache[m] = st
            res['trimestral'][m] = [[d, st[d], False] for d in sorted(st)[-44:]]
        else:
            a = anual(f, tipo)
            res['anual'][m] = [[d, a[d]] for d in sorted(a)][-10:]
            q = trimestral(f, tipo)
            res['trimestral'][m] = [[d, q[d][0], q[d][1]] for d in sorted(q)][-40:]
    fins = [d for d, _ in (res['anual'].get('receita') or res['anual'].get('lucro_liquido') or [])]
    for m, st in stock_cache.items():
        res['anual'][m] = [[d, st[d]] for d in fins if d in st]
    moedas = [u for u in res['unidades'].values() if u and len(u) == 3]
    res['moeda'] = max(set(moedas), key=moedas.count) if moedas else None

    fil = []
    rec = ((sub or {}).get('filings') or {}).get('recent') or {}
    for i, form in enumerate(rec.get('form', [])):
        if form not in FILINGS:
            continue
        acc = rec['accessionNumber'][i].replace('-', '')
        doc = rec['primaryDocument'][i]
        fil.append({'form': form, 'data': rec['filingDate'][i], 'periodo': rec.get('reportDate', [''] * (i + 1))[i],
                    'itens': rec.get('items', [''] * (i + 1))[i],
                    'url': f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{doc}',
                    'indice': f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/'})
        if len(fil) >= 60:
            break
    res['filings'] = fil
    return res


def main():
    uni = [e for e in cfg('universo.json')['empresas'] if e.get('us')]
    mapa = get('https://www.sec.gov/files/company_tickers.json', hdr=H) or {}
    ciks = {v['ticker'].upper(): int(v['cik_str']) for v in mapa.values()}
    velho = {x['t']: x for x in (ler(OUT, 'sec.json', {}) or {}).get('empresas', [])}
    out, falhas = [], []
    for e in uni:
        cik = ciks.get(e['us'].upper())
        r = None
        if cik:
            try:
                r = empresa(e, cik, 'EUR' if e['yahoo'].endswith(('.DE', '.AS', '.PA')) else 'USD')
            except Exception as ex:  # noqa: BLE001
                print(e['t'], 'erro', type(ex).__name__, ex, file=sys.stderr)
        if r:
            out.append(r)
        else:
            falhas.append(e['t'])
            if e['t'] in velho:
                out.append(dict(velho[e['t']], velho=True))
        print(e['t'], 'ok' if r else 'FALHOU', (r or {}).get('taxonomia'), len((r or {}).get('filings', [])))
    guardar(OUT, 'sec.json', {'lido': AGORA, 'empresas': out})
    mark(RAW, 'sec', len(falhas) <= 1, f'{len(uni) - len(falhas)} de {len(uni)} empresas lidas' + (f'; falharam {", ".join(falhas)}' if falhas else ''))


if __name__ == '__main__':
    main()
