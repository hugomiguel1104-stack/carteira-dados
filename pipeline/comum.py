"""Partes comuns do pipeline: pedidos HTTP com retry, leitura da config, escrita dos JSON, estado das fontes."""
import json, os, sys, time, datetime as dt
import requests

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
from status import mark  # noqa: E402  (do kit do amigo: estado por fonte em raw/status.json)

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
SES = requests.Session()
SES.headers.update({'User-Agent': UA, 'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'en-US,en;q=0.9'})
HOJE = dt.datetime.now(dt.timezone.utc).date()
AGORA = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')


def cfg(nome):
    return json.load(open(os.path.join(RAIZ, 'cfg', nome), encoding='utf-8'))


def get(url, hdr=None, tries=4, kind='json', timeout=30):
    ultimo = None
    for i in range(tries):
        try:
            r = SES.get(url, headers=hdr or {}, timeout=timeout)
            if r.status_code == 200:
                return r.json() if kind == 'json' else r.text
            ultimo = r.status_code
            if r.status_code == 404:
                return None
        except Exception as e:  # noqa: BLE001
            ultimo = type(e).__name__
        time.sleep(1.5 * (i + 1))
    print('falhou', url[:120], ultimo, file=sys.stderr)
    return None


def guardar(pasta, nome, obj):
    os.makedirs(pasta, exist_ok=True)
    with open(os.path.join(pasta, nome), 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, separators=(',', ':'))


def ler(pasta, nome, defeito=None):
    try:
        return json.load(open(os.path.join(pasta, nome), encoding='utf-8'))
    except Exception:  # noqa: BLE001
        return defeito


def rd(x, n=6):
    return None if x is None else float(f'%.{n}g' % x)
