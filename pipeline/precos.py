#!/usr/bin/env python3
"""Precos (Yahoo Finance) das empresas do universo, dos indices e dos setores.

Por simbolo: ultimo fecho, variacao 1d / 1s / 1m / 3m / YTD / 12m, maximo historico (ATH) e distancia,
maximo e minimo de 52 semanas, RSI 14 (Wilder). Series: diaria de 2 anos para todos; semanal de 10 anos
para as empresas (o grafico de 10 anos da pagina de cada empresa).
Um simbolo que falha mantem a ultima copia boa e fica marcado como 'velho'.

Uso: python pipeline/precos.py <raw> <out>
"""
import sys, time, datetime as dt
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote
from comum import cfg, get, guardar, ler, mark, rd, AGORA

RAW, OUT = sys.argv[1], sys.argv[2]


def serie(sim):
    j = get(f'https://query1.finance.yahoo.com/v8/finance/chart/{quote(sim)}?period1=0&period2={int(time.time())}&interval=1d')
    try:
        r = j['chart']['result'][0]
        ts, cl = r['timestamp'], r['indicators']['quote'][0]['close']
    except Exception:  # noqa: BLE001
        return None, None
    pts = [(dt.datetime.fromtimestamp(t, dt.timezone.utc).date().isoformat(), c) for t, c in zip(ts, cl) if c is not None]
    meta = r.get('meta') or {}
    # a serie longa por vezes ainda nao traz a ultima sessao: acrescenta-a a partir do preco de mercado
    px, tt = meta.get('regularMarketPrice'), meta.get('regularMarketTime')
    if pts and px and tt:
        d = dt.datetime.fromtimestamp(tt, dt.timezone.utc).date().isoformat()
        if d > pts[-1][0]:
            pts.append((d, px))
        elif d == pts[-1][0]:
            pts[-1] = (d, px)
    return pts, meta


def rsi(cl, n=14):
    if len(cl) <= n:
        return None
    g = [max(cl[i] - cl[i - 1], 0) for i in range(1, len(cl))]
    p = [max(cl[i - 1] - cl[i], 0) for i in range(1, len(cl))]
    ag, ap = sum(g[:n]) / n, sum(p[:n]) / n
    for i in range(n, len(g)):
        ag, ap = (ag * (n - 1) + g[i]) / n, (ap * (n - 1) + p[i]) / n
    return 100.0 if ap == 0 else round(100 - 100 / (1 + ag / ap), 1)


def metricas(pts, meta):
    d = [x[0] for x in pts]
    c = [x[1] for x in pts]
    ult, data = c[-1], d[-1]

    def var(k):
        return rd(ult / c[-1 - k] - 1, 5) if len(c) > k and c[-1 - k] else None

    ano = str(int(data[:4]) - 1)
    base_ytd = next((c[i] for i in range(len(d) - 1, -1, -1) if d[i][:4] <= ano), None)
    i_ath = max(range(len(c)), key=lambda i: c[i])
    um_ano = (dt.date.fromisoformat(data) - dt.timedelta(days=365)).isoformat()
    j52 = [x for x in c[next((i for i, x in enumerate(d) if x >= um_ano), 0):]]
    return {
        'ult': rd(ult), 'data': data, 'moeda': meta.get('currency'),
        'd1': var(1), 's1': var(5), 'm1': var(21), 'm3': var(63), 'a1': var(252),
        'ytd': rd(ult / base_ytd - 1, 5) if base_ytd else None,
        'ath': rd(c[i_ath]), 'ath_data': d[i_ath], 'dd_ath': rd(ult / c[i_ath] - 1, 5),
        'max52': rd(max(j52)), 'min52': rd(min(j52)),
        'rsi14': rsi(c[-300:]),
    }


def semanal(pts, anos=10):
    corte = (dt.date.fromisoformat(pts[-1][0]) - dt.timedelta(days=365 * anos)).isoformat()
    out, semana = [], None
    for d, c in pts:
        if d < corte:
            continue
        k = dt.date.fromisoformat(d).isocalendar()[:2]
        if k != semana:
            out.append([d, rd(c)])
            semana = k
        else:
            out[-1] = [d, rd(c)]
    return out


def main():
    uni, mk = cfg('universo.json')['empresas'], cfg('mercado.json')
    pedidos = [(e['yahoo'], 'empresa', e['t'], e['nome']) for e in uni]
    pedidos += [(s, 'indice', s, n) for s, n, _ in mk['indices']]
    pedidos += [(s, 'setor_eua', s, n) for s, n in mk['setores_eua']]
    pedidos += [(s, 'setor_europa', s, n) for s, n in mk['setores_europa']]

    velho = ler(OUT, 'precos.json', {}) or {}
    velho = {x['id']: x for x in velho.get('linhas', [])}

    def um(p):
        sim, tipo, ident, nome = p
        pts, meta = serie(sim)
        if not pts or len(pts) < 30:
            v = velho.get(ident)
            if v:
                v = dict(v, velho=True)
            return v
        corte2 = (dt.date.fromisoformat(pts[-1][0]) - dt.timedelta(days=730)).isoformat()
        linha = {'id': ident, 'yahoo': sim, 'tipo': tipo, 'nome': nome, **metricas(pts, meta),
                 'diaria': [[d, rd(c)] for d, c in pts if d >= corte2]}
        if tipo == 'empresa':
            linha['semanal10'] = semanal(pts)
        return linha

    with ThreadPoolExecutor(6) as ex:
        linhas = [x for x in ex.map(um, pedidos) if x]
    frescos = sum(1 for x in linhas if not x.get('velho'))
    guardar(OUT, 'precos.json', {'lido': AGORA, 'linhas': linhas})
    mark(RAW, 'precos', frescos >= 0.9 * len(pedidos), f'{frescos} de {len(pedidos)} simbolos lidos')
    print('precos:', frescos, 'de', len(pedidos))


if __name__ == '__main__':
    main()
