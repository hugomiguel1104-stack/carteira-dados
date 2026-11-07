#!/usr/bin/env python3
"""Calendario de resultados (Nasdaq) so para as empresas do universo.

- Datas: o calendario diario de resultados da Nasdaq, de 100 dias para tras a 100 dias para a frente
  (hora: antes da abertura / depois do fecho; EPS reportado, consenso e surpresa quando ja reportou).
- Historico: as ultimas surpresas de EPS por empresa (earnings-surprise).
Empresas sem cotacao nos EUA (Adyen) ficam so com a data da ficha, que e juntada na pagina.
Sem ex-dividend, pagamentos nem feriados (decisao do Hugo).

Uso: python pipeline/calendario.py <raw> <out>
"""
import sys, datetime as dt
from concurrent.futures import ThreadPoolExecutor
from comum import cfg, get, guardar, ler, mark, AGORA, HOJE

RAW, OUT = sys.argv[1], sys.argv[2]
NQ = {'Origin': 'https://www.nasdaq.com', 'Referer': 'https://www.nasdaq.com/'}


def num(x):
    if x in (None, '', 'N/A', '--'):
        return None
    try:
        return float(str(x).replace('$', '').replace(',', '').replace('(', '-').replace(')', ''))
    except ValueError:
        return None


def main():
    uni = [e for e in cfg('universo.json')['empresas'] if e.get('us')]
    quer = {e['us'].upper(): e['t'] for e in uni}
    velho = ler(OUT, 'calendario.json', {}) or {}
    dias = [HOJE + dt.timedelta(days=k) for k in range(-100, 101)]
    dias = [d for d in dias if d.weekday() < 5]
    lidos = [0]

    def dia(d):
        j = get('https://api.nasdaq.com/api/calendar/earnings?date=' + d.isoformat(), hdr=NQ, tries=3)
        rows = ((j or {}).get('data') or {}).get('rows')
        if j and (j.get('data') is not None) and d <= HOJE:
            lidos[0] += 1   # so conta os dias passados: a Nasdaq nao responde a datas futuras sem eventos confirmados
        out = []
        for r in rows or []:
            s = (r.get('symbol') or '').upper()
            if s in quer:
                out.append({'t': quer[s], 'data': d.isoformat(), 'hora': r.get('time'),
                            'eps': num(r.get('eps')), 'eps_consenso': num(r.get('epsForecast')),
                            'surpresa_pct': num(r.get('surprise')), 'n_estimativas': num(r.get('noOfEsts')),
                            'trimestre_fiscal': r.get('fiscalQuarterEnding'), 'eps_ano_anterior': num(r.get('lastYearEPS'))})
        return out

    with ThreadPoolExecutor(4) as ex:
        eventos = [x for lst in ex.map(dia, dias) for x in lst]

    def surpresa(e):
        j = get(f"https://api.nasdaq.com/api/company/{e['us']}/earnings-surprise", hdr=NQ, tries=3)
        rows = ((((j or {}).get('data') or {}).get('earningsSurpriseTable') or {}).get('rows')) or []
        return e['t'], [{'trimestre_fiscal': r.get('fiscalQtrEnd'), 'data': r.get('dateReported'),
                         'eps': num(r.get('eps')), 'eps_consenso': num(r.get('consensusForecast')),
                         'surpresa_pct': num(r.get('percentageSurprise'))} for r in rows]

    with ThreadPoolExecutor(4) as ex:
        hist = dict(ex.map(surpresa, uni))

    passados = sum(1 for d in dias if d <= HOJE)
    ok = lidos[0] >= 0.8 * passados
    if not ok and velho:  # leitura fraca: fica a copia anterior para as datas que nao vieram
        vist = {(x['t'], x['data']) for x in eventos}
        eventos += [x for x in velho.get('eventos', []) if (x['t'], x['data']) not in vist]
        for t, h in (velho.get('historico') or {}).items():
            if not hist.get(t):
                hist[t] = h
    eventos.sort(key=lambda x: x['data'])
    guardar(OUT, 'calendario.json', {'lido': AGORA, 'eventos': eventos, 'historico': hist})
    mark(RAW, 'calendario', ok, f'{lidos[0]} de {passados} dias passados lidos; {len(eventos)} eventos')
    print('calendario:', lidos[0], 'dias,', len(eventos), 'eventos,', sum(1 for v in hist.values() if v), 'historicos')


if __name__ == '__main__':
    main()
