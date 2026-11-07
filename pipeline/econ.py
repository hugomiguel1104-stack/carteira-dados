#!/usr/bin/env python3
"""Economic series for the Stocks dashboard, read on GitHub Actions from public sources (no keys):
- BLS public API: CPI (all items, less energy, core, energy), producer prices, unemployment, payrolls, hourly earnings
- BEA tables through DBnomics: PCE prices (headline and core), real consumer spending, real disposable income,
  saving rate, real GDP and real consumer spending growth (quarterly)
- Eurostat: euro-area HICP (annual rate)
- University of Michigan: consumer sentiment index
(FRED does not answer requests from GitHub's runners, so it is not used.)

Raw observations go to <raw>/econ_raw.json; <out>/mk_econ.json gets one row per series with the transformed
history (year-on-year %, monthly change or level), latest value, previous one and observation date. A series
that fails keeps its last good copy, so one bad read never empties a chart.
Usage: python3 scraper/econ.py <raw dir> <out dir>
"""
import csv, io, json, os, sys, time, datetime as dt
import requests

RAW, OUT = sys.argv[1], sys.argv[2]
os.makedirs(RAW, exist_ok=True); os.makedirs(OUT, exist_ok=True)
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
H = {'User-Agent': UA}
NOW = dt.datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ')

# id, group, name, unit, transform (yoy | chg | lvl), frequency, source label, (fetcher, key)
SERIES = [
    ('CPIAUCSL', 'inflation', 'CPI, all items', '% y/y', 'yoy', 'M', 'BLS', ('bls', 'CUSR0000SA0')),
    ('CUSR0000SA0LE', 'inflation', 'CPI less energy', '% y/y', 'yoy', 'M', 'BLS', ('bls', 'CUSR0000SA0LE')),
    ('CPILFESL', 'inflation', 'Core CPI (less food and energy)', '% y/y', 'yoy', 'M', 'BLS', ('bls', 'CUSR0000SA0L1E')),
    ('CPIENGSL', 'inflation', 'CPI energy', '% y/y', 'yoy', 'M', 'BLS', ('bls', 'CUSR0000SA0E')),
    ('PCEPI', 'inflation', 'PCE prices', '% y/y', 'yoy', 'M', 'BEA', ('dbn', 'BEA/NIPA-T20804/DPCERG-M')),
    ('PCEPILFE', 'inflation', 'Core PCE prices', '% y/y', 'yoy', 'M', 'BEA', ('dbn', 'BEA/NIPA-T20804/DPCCRG-M')),
    ('PPIFIS', 'inflation', 'Producer prices (final demand)', '% y/y', 'yoy', 'M', 'BLS', ('bls', 'WPSFD4')),
    ('HICP_EA', 'inflation', 'Euro area HICP', '% y/y', 'lvl', 'M', 'ECB / Eurostat', ('estat', 'CP00')),
    ('PCEC96', 'consumer', 'Real consumer spending', '% y/y', 'yoy', 'M', 'BEA', ('dbn', 'BEA/NIPA-T20806/DPCERX-M')),
    ('DSPIC96', 'consumer', 'Real disposable income', '% y/y', 'cum12', 'M', 'BEA', ('dbn', 'BEA/NIPA-T20600/A067RM-M')),  # monthly % changes, compounded over 12 months
    ('PSAVERT', 'consumer', 'Personal saving rate', '%', 'lvl', 'M', 'BEA', ('dbn', 'BEA/NIPA-T20600/A072RC-M')),
    ('UMCSENT', 'consumer', 'Consumer sentiment (Michigan)', 'index', 'lvl', 'M', 'University of Michigan', ('umich', '')),
    ('UNRATE', 'jobs', 'Unemployment rate', '%', 'lvl', 'M', 'BLS', ('bls', 'LNS14000000')),
    ('PAYEMS', 'jobs', 'Nonfarm payrolls', 'k a month', 'chg', 'M', 'BLS', ('bls', 'CES0000000001')),
    ('CES0500000003', 'jobs', 'Average hourly earnings', '% y/y', 'yoy', 'M', 'BLS', ('bls', 'CES0500000003')),
    ('A191RL1Q225SBEA', 'growth', 'Real GDP', '% q/q, annualised', 'lvl', 'Q', 'BEA', ('dbn', 'BEA/NIPA-T10101/A191RL-Q')),
    ('DPCERL1Q225SBEA', 'growth', 'Real consumer spending', '% q/q, annualised', 'lvl', 'Q', 'BEA', ('dbn', 'BEA/NIPA-T10101/DPCERL-Q')),
]


def bls_all(codes):
    out = {}; y = dt.date.today().year
    for a, b in ((y - 9, y), (y - 19, y - 10)):
        try:
            r = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', json={'seriesid': codes, 'startyear': str(a), 'endyear': str(b)}, headers=H, timeout=40)
            j = r.json(); print('BLS', a, b, j.get('status'))
            for sr in (j.get('Results') or {}).get('series', []):
                for o in sr.get('data', []):
                    if o.get('period', '').startswith('M') and o['period'] != 'M13' and o.get('value') not in ('-', ''):
                        out.setdefault(sr['seriesID'], {})[o['year'] + '-' + o['period'][1:] + '-01'] = float(o['value'])
        except Exception as e:
            print('BLS error', type(e).__name__, str(e)[:120])
        time.sleep(1)
    return {k: sorted([[d, v] for d, v in m.items()]) for k, m in out.items()}


def dbn(key):
    r = requests.get('https://api.db.nomics.world/v22/series/' + key + '?observations=1', headers=H, timeout=40)
    d = r.json()['series']['docs'][0]; out = []
    for p, v in zip(d['period'], d['value']):
        if v in (None, 'NA'): continue
        if '-Q' in p: p = p[:4] + '-%02d' % (int(p[-1]) * 3 - 2)
        out.append([p[:7] + '-01', float(v)])
    return [o for o in out if o[0] >= '2004']


def estat(coicop):
    best = None
    try:  # ECB data portal first (euro area, changing composition, annual rate), Eurostat as the fallback
        r = requests.get('https://data-api.ecb.europa.eu/service/data/ICP/M.U2.N.000000.4.ANR?format=csvdata&startPeriod=2004-01', headers={'User-Agent': UA, 'Accept': 'text/csv'}, timeout=40)
        rows = list(csv.DictReader(io.StringIO(r.text)))
        obs = sorted([[x['TIME_PERIOD'] + '-01', float(x['OBS_VALUE'])] for x in rows if x.get('OBS_VALUE') not in (None, '', 'NaN')])
        print('ECB', r.status_code, len(obs), obs[-1] if obs else r.text[:120])
        if obs: best = obs
    except Exception as e:
        print('ECB error', type(e).__name__, str(e)[:100])
    # Eurostat: the classic table, then the COICOP 2018 table that replaced it in 2026; total index of whatever
    # classification the table uses
    extra = None
    for ds, flt in (('prc_hicp_minr', '&coicop18=TOTAL&unit=RCH_A'), ('prc_hicp_manr', '&coicop=CP00')):
        for geo in ('EA20',) if ds.endswith('minr') else ('EA20', 'EA'):
            try:
                r = requests.get('https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/' + ds + '?geo=' + geo + flt + '&sinceTimePeriod=' + ('2024-01' if ds.endswith('minr') else '2004-01'), headers=H, timeout=60)
                j = r.json()
                if 'dimension' not in j: print('Eurostat', ds, geo, r.status_code, str(j)[:120]); continue
                ids, size, dim = j['id'], j['size'], j['dimension']
                pick = {}
                for d in ids:
                    cats = dim[d]['category']['index']
                    if d == 'time': continue
                    if len(cats) == 1: pick[d] = 0; continue
                    want = [k for k in ('RCH_A', 'CP00', 'TOTAL', 'M') if k in cats]
                    if not want: break
                    pick[d] = cats[want[0]]
                if len(pick) != len(ids) - 1: print('Eurostat', ds, geo, 'no total index', {d: list(dim[d]['category']['index'])[:5] for d in ids}); continue
                stride = [1] * len(ids)
                for k in range(len(ids) - 2, -1, -1): stride[k] = stride[k + 1] * size[k + 1]
                ti = ids.index('time'); base = sum(pick[d] * stride[k] for k, d in enumerate(ids) if d != 'time')
                obs = sorted([[t + '-01', float(j['value'][str(base + i * stride[ti])])] for t, i in dim['time']['category']['index'].items() if str(base + i * stride[ti]) in j['value']])
                print('Eurostat', ds, geo, len(obs), obs[-1] if obs else None)
                if obs and ds.endswith('minr') and extra is None: extra = obs
                elif obs and (best is None or obs[-1][0] > best[-1][0]): best = obs
            except Exception as e:
                print('Eurostat', ds, geo, 'error', type(e).__name__, str(e)[:100])
    if extra and best:  # the new table carries the recent months; the old one the long history
        m = {d: v for d, v in best}; m.update({d: v for d, v in extra}); best = sorted([[d, v] for d, v in m.items()])
    elif extra: best = extra
    return best


MON = {m: i + 1 for i, m in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])}


def umich(_):
    r = requests.get('https://www.sca.isr.umich.edu/files/tbmics.csv', headers=H, timeout=40)
    rows = list(csv.reader(io.StringIO(r.text)))
    out = [['%s-%02d-01' % (y.strip(), MON[m.strip()]), float(v)] for m, y, v, *_ in rows[1:] if m.strip() in MON and v.strip()]
    return sorted(o for o in out if o[0] >= '2004')


def transform(obs, how):
    if how in ('lvl', 'lvlk'):
        return [[d, round(v / (1000 if how == 'lvlk' else 1), 2)] for d, v in obs]
    if how == 'cum12':
        out = []
        for i in range(11, len(obs)):
            f = 1.0
            for d, v in obs[i - 11:i + 1]: f *= 1 + v / 100
            out.append([obs[i][0], round((f - 1) * 100, 2)])
        return out
    if how == 'chg':
        return [[obs[i][0], round(obs[i][1] - obs[i - 1][1], 1)] for i in range(1, len(obs))]
    m = {d[:7]: v for d, v in obs}; out = []
    for d, v in obs:
        y = str(int(d[:4]) - 1) + d[4:7]
        if y in m and m[y]: out.append([d, round((v / m[y] - 1) * 100, 2)])
    return out


def main():
    path = os.path.join(RAW, 'econ_raw.json')
    old = json.load(open(path)) if os.path.exists(path) else {}
    B = bls_all([s[7][1] for s in SERIES if s[7][0] == 'bls'])
    raw, rows, bad = {}, [], []
    for sid, grp, name, unit, how, freq, src, (kind, key) in SERIES:
        obs = None
        try:
            obs = B.get(key) if kind == 'bls' else dbn(key) if kind == 'dbn' else estat(key) if kind == 'estat' else umich(key)
        except Exception as e:
            print(sid, kind, 'error', type(e).__name__, str(e)[:120])
        if obs: raw[sid] = {'at': NOW, 'obs': obs}
        elif sid in old: raw[sid] = old[sid]; bad.append(sid)
        else: bad.append(sid); continue
        h = transform(raw[sid]['obs'], how)
        if not h: continue
        rows.append({'id': sid, 'grp': grp, 'name': name, 'unit': unit, 'how': how, 'freq': freq, 'src': src,
                     'date': h[-1][0], 'last': h[-1][1], 'prev': h[-2][1] if len(h) > 1 else None,
                     'yago': next((v for d, v in reversed(h) if d[:4] == str(int(h[-1][0][:4]) - 1) and d[5:7] == h[-1][0][5:7]), None),
                     'read': raw[sid]['at'], 'h': h})
        print(sid, len(h), h[-1])
        time.sleep(0.3)
    json.dump(raw, open(path, 'w'))
    json.dump(rows, open(os.path.join(OUT, 'mk_econ.json'), 'w'), separators=(',', ':'))
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from status import mark
    fresh = sum(1 for r in raw.values() if isinstance(r, dict) and r.get('at') == NOW)
    mark(RAW, 'econ', fresh >= 0.8 * len(SERIES), '%d of %d series read' % (fresh, len(SERIES)))
    print('mk_econ:', len(rows), 'series; kept old or missing:', bad)


if __name__ == '__main__':
    main()
