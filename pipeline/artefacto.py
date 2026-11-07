#!/usr/bin/env python3
"""Prepara os dados do ramo `data` para a base de dados do artefacto Carteira Hugo e Je (coleção `terminal`).

Parte os JSON de out/ em documentos de menos de 256 KiB e agrupa-os em lotes de escrita
(no máximo 50 documentos e ~900 KB por lote), prontos para o ArtifactData `batch`.

Uso:
  python pipeline/artefacto.py <out_dir> <destino> <geracao> [geracao_anterior]

Cada corrida escreve uma geração nova (documentos novos, sem if_version) na coleção
terminal/<geracao>/d; o documento terminal/atual aponta para a geração em uso e a página lê só essa.
Escreve <destino>/docs/<doc_id>.json, <destino>/lotes.json (escrita) e, com geracao_anterior,
<destino>/apagar.json (lotes de delete da geração anterior, if_version 1, porque cada documento
de uma geração só é escrito uma vez).
"""
import json, os, re, sys

OUT, DEST = sys.argv[1], sys.argv[2]
GEN = sys.argv[3]
ANT = sys.argv[4] if len(sys.argv) > 4 else None
COL = f'terminal/{GEN}/d'
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
# empacota: px-*, sec-* e ficha-* vão juntos em documentos de até ~240 KB (menos documentos = menos escritas)
tam = lambda o: len(json.dumps(o, ensure_ascii=False, separators=(',', ':')).encode('utf-8'))
final = {k: d for k, d in docs.items() if not k.startswith(('px-', 'sec-', 'ficha-'))}
for pref in ('px', 'sec', 'ficha'):
    itens = [(k, d) for k, d in docs.items() if k.startswith(pref + '-')]
    pack, n, i = [], 0, 1
    for k, d in itens:
        t = tam(d)
        if t > LIM_DOC - 2000:
            if d.get('md'):
                d['md'] = d['md'][:max(0, len(d['md']) - (t - LIM_DOC) - 6000)] + '\n\n…(ficha cortada no Terminal; abre o ficheiro original)'
                t = tam(d)
            if t > LIM_DOC - 2000:
                print('AVISO: fica de fora (grande de mais):', k, t, file=sys.stderr)
                continue
        if pack and n + t > 240_000:
            final[f'{pref}-{i}'] = {'itens': pack}
            pack, n, i = [], 0, i + 1
        pack.append(d)
        n += t
    if pack:
        final[f'{pref}-{i}'] = {'itens': pack}
lotes, atual, tl = [], [], 0
for k, d in final.items():
    txt = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
    nb = len(txt.encode('utf-8'))
    p = os.path.join(DEST, 'docs', k + '.json')
    open(p, 'w', encoding='utf-8').write(txt)
    w = {'op': 'set', 'collection': COL, 'doc_id': k, 'file_path': os.path.abspath(p)}
    if atual and (len(atual) >= 50 or tl + nb > LIM_LOTE):
        lotes.append(atual)
        atual, tl = [], 0
    atual.append(w)
    tl += nb
if atual:
    lotes.append(atual)
json.dump(lotes, open(os.path.join(DEST, 'lotes.json'), 'w'), indent=1)
if ANT and ANT != GEN:
    ids = [w['doc_id'] for l in lotes for w in l]
    apagar = [[{'op': 'delete', 'collection': f'terminal/{ANT}/d', 'doc_id': i, 'if_version': 1} for i in ids[j:j + 50]] for j in range(0, len(ids), 50)]
    json.dump(apagar, open(os.path.join(DEST, 'apagar.json'), 'w'), indent=1)
print(f'{len(final)} documentos em {len(lotes)} lotes;', sum(os.path.getsize(os.path.join(DEST, 'docs', f)) for f in os.listdir(os.path.join(DEST, 'docs'))) // 1024, 'KB')
