#!/usr/bin/env python3
"""Prepara os dados do ramo `data` para a base de dados do artefacto Carteira Hugo e Je (coleção `terminal`).

Parte os JSON de out/ em documentos de menos de 256 KiB e agrupa-os em lotes de escrita
(no máximo 50 documentos e ~900 KB por lote), prontos para o ArtifactData `batch`.

Uso:
  python pipeline/artefacto.py <out_dir> <destino> [versoes.json]

  versoes.json (opcional): {"doc_id": versao, ...} lido da coleção `terminal` antes de escrever.
  Documentos que já existem levam if_version; os novos não.

Escreve <destino>/docs/<doc_id>.json e <destino>/lotes.json:
  [[{"op": "set", "collection": "terminal", "doc_id": ..., "file_path": ..., "if_version": ...}, ...], ...]
"""
import json, os, re, sys

OUT, DEST = sys.argv[1], sys.argv[2]
VERS = json.load(open(sys.argv[3])) if len(sys.argv) > 3 and os.path.exists(sys.argv[3]) else {}
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIM_DOC = 250_000
LIM_LOTE = 900_000


def ler(n, d=None):
    try:
        return json.load(open(os.path.join(OUT, n), encoding='utf-8'))
    except Exception:  # noqa: BLE001
        return d


def doc_id(s):
    return re.sub(r'[^A-Za-z0-9_\-.~:@+]', lambda m: {'^': '_I_', '=': '_E_'}.get(m.group(0), '_'), s)


docs = {}
cfg = lambda n: json.load(open(os.path.join(RAIZ, 'cfg', n), encoding='utf-8'))
precos = ler('precos.json', {}) or {}
docs['meta'] = {'lido': precos.get('lido'), 'estado': ler('estado.json', {}), 'uni': cfg('universo.json')['empresas'],
                'mercado': cfg('mercado.json')}
docs['cal'] = ler('calendario.json', {}) or {}
econ = ler('mk_econ.json', []) or []
docs['econ'] = {'linhas': [dict(r, h=[h for h in r['h'] if h[0] >= '2016']) for r in econ]}

for x in precos.get('linhas', []):
    docs['px-' + doc_id(x['id'])] = x

for e in (ler('sec.json', {}) or {}).get('empresas', []):
    fil = [f for f in e.get('filings', []) if re.match(r'^(10-K|10-Q|20-F|40-F)', f['form'])
           or (f['form'] == '8-K' and '2.02' in (f.get('itens') or ''))][:30]
    docs['sec-' + doc_id(e['t'])] = {'t': e['t'], 'moeda': e.get('moeda'), 'tax': e.get('taxonomia'), 'nome': e.get('nome_sec'),
                                     'anual': e.get('anual', {}), 'trim': {k: v[-12:] for k, v in e.get('trimestral', {}).items()},
                                     'filings': fil, 'velho': e.get('velho', False)}

for f in (ler('fichas.json', {}) or {}).get('fichas', []):
    docs['ficha-' + doc_id(f['t'])] = {
        't': f['t'], 'atual': f['atual'], 'log': (f.get('log') or '')[:6000], 'md': f.get('md') or '', 'erro': f.get('erro'),
        'versoes': [{'data': v['data'], 'arq': v.get('arquivada_em'), 'ficheiro': v['ficheiro'], 'atual': v.get('atual', False),
                     'num': {k: (v.get('num') or {}).get(k) for k in ('fv', 'preco', 'bear', 'bull', 'tranche1', 'cheia', 'decisao', 'quarter', 'par', 'upside')}}
                    for v in f.get('versoes', [])],
        'comp': f.get('comparacoes', [])}

os.makedirs(os.path.join(DEST, 'docs'), exist_ok=True)
lotes, atual, tam = [], [], 0
for k, d in docs.items():
    txt = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
    if len(txt.encode('utf-8')) > LIM_DOC and k.startswith('ficha-'):   # ficha demasiado grande: corta o texto, mantém os números
        d['md'] = d['md'][:max(0, len(d['md']) - (len(txt.encode('utf-8')) - LIM_DOC) - 2000)] + '\n\n…(ficha cortada no Terminal; abre o ficheiro original)'
        txt = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
    n = len(txt.encode('utf-8'))
    if n > LIM_DOC:
        print('AVISO: documento grande de mais, fica de fora:', k, n, file=sys.stderr)
        continue
    p = os.path.join(DEST, 'docs', k + '.json')
    open(p, 'w', encoding='utf-8').write(txt)
    w = {'op': 'set', 'collection': 'terminal', 'doc_id': k, 'file_path': os.path.abspath(p)}
    if k in VERS:
        w['if_version'] = VERS[k]
    if atual and (len(atual) >= 50 or tam + n > LIM_LOTE):
        lotes.append(atual)
        atual, tam = [], 0
    atual.append(w)
    tam += n
if atual:
    lotes.append(atual)
json.dump(lotes, open(os.path.join(DEST, 'lotes.json'), 'w'), indent=1)
print(f'{len(docs)} documentos em {len(lotes)} lotes;', sum(os.path.getsize(os.path.join(DEST, 'docs', f)) for f in os.listdir(os.path.join(DEST, 'docs'))) // 1024, 'KB')
