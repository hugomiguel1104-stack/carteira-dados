#!/usr/bin/env python3
"""Fichas de avaliacao: numeros da ficha atual, versoes anteriores e o comparador entre versoes.

Le as copias em fichas/ (sincronizadas da pasta Analise Acoes do Hugo; nunca se editam).
- Numeros: o parser do proprio tracker.py do Hugo (bloco dados v5.0 quando existe, ESTADO por regex
  nas fichas antigas). Nada se recalcula aqui.
- Versoes: a ficha atual + as datadas em _arquivo/ e Valuation(s)/, cada uma lida pelo mesmo parser.
- Porque mudou o fair value: diferenca entre os config_{T}.json de cada versao, so nos pressupostos
  (custo de capital, drivers, base, mercado, escada). Os resultados (cenarios, grelhas) ficam de fora,
  porque mudam por consequencia.
- Texto: as seccoes Log / Changelog da ficha, tal como estao escritas.
Uma ficha que falha nao parte as outras: fica com erro e a ultima leitura boa.

Uso: python pipeline/fichas.py <raw> <out>
"""
import sys, re, json, shutil, tempfile, importlib.util, traceback
from pathlib import Path
from comum import cfg, guardar, ler, mark, AGORA, RAIZ

RAW, OUT = sys.argv[1], sys.argv[2]
FICHAS = Path(RAIZ) / 'fichas'

spec = importlib.util.spec_from_file_location('tracker', FICHAS / '_ferramentas' / 'tracker.py')
tracker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tracker)

# prefixos de config que sao pressupostos (o resto sao resultados ou texto)
CATEGORIAS = [('wacc.', 'Custo de capital'), ('custo_capital.', 'Custo de capital'), ('drivers.', 'Drivers'),
              ('base.', 'Base e balanço'), ('mercado.', 'Mercado'), ('escada.', 'Escada e probabilidades'),
              ('ancoras.', 'Âncoras do reverse'), ('switches.', 'Opções do modelo'), ('tv_activo', 'Valor terminal')]
IGNORAR = ('leia_me', 'referencias', 'resultados_guardados', 'cenarios.', 'grelha', 'tabela_wacc_g', 'titulo',
           'subtitulo', 'passthrough', 'seeds')


def achatar(d, p=''):
    o = {}
    if isinstance(d, dict):
        for k, v in d.items():
            o.update(achatar(v, f'{p}{k}.'))
    elif isinstance(d, list) and any(isinstance(x, (dict, list)) for x in d):
        for i, v in enumerate(d):
            o.update(achatar(v, f'{p}{i}.'))
    else:
        o[p[:-1]] = d
    return o


def categoria(chave):
    if any(chave.startswith(i) for i in IGNORAR):
        return None
    for pref, nome in CATEGORIAS:
        if chave.startswith(pref):
            return nome
    return None


def diff_config(a, b):
    if not a or not b:
        return None
    fa, fb = achatar(a), achatar(b)
    out = []
    for k in sorted(set(fa) | set(fb)):
        cat = categoria(k)
        va, vb = fa.get(k), fb.get(k)
        if cat is None or va == vb or isinstance(va, str) or isinstance(vb, str):
            continue
        if isinstance(va, list) or isinstance(vb, list):
            if va is not None and vb is not None and not all(isinstance(x, (int, float)) for x in (va or []) + (vb or [])):
                continue
        out.append({'cat': cat, 'campo': k, 'antes': va, 'depois': vb})
    return out[:60]


def data_nome(nome):
    m = re.search(r'(20\d{2})(\d{2})(\d{2})', nome)
    if m:
        return f'{m.group(1)}-{m.group(2)}-{m.group(3)}'
    m = re.search(r'(\d{2})(\d{2})(20\d{2})', nome)
    if m:
        return f'{m.group(3)}-{m.group(2)}-{m.group(1)}'
    return None


def ler_json(p):
    try:
        return json.loads(Path(p).read_text(encoding='utf-8'))
    except Exception:  # noqa: BLE001
        return None


def limpo(reg):
    if not reg:
        return None
    r = {}
    for k, v in reg.items():
        r[k] = v.isoformat() if hasattr(v, 'isoformat') else v
    return r


def ler_versao(pasta_nome, ficha, config):
    """Le uma ficha arquivada com o parser do tracker, numa pasta temporaria com os nomes fixos."""
    base = FICHAS / '_versoes_tmp'          # dentro de fichas/ (o tracker exige); comeca por _, fica fora da descoberta
    base.mkdir(exist_ok=True)
    tmp = Path(tempfile.mkdtemp(dir=base)) / pasta_nome
    tmp.mkdir()
    shutil.copy(ficha, tmp / f'{pasta_nome}_Ficha.md')
    if config:
        shutil.copy(config, tmp / f'config_{pasta_nome}.json')
    try:
        return limpo(tracker.ler_ficha(tmp))
    finally:
        shutil.rmtree(tmp.parent, ignore_errors=True)


def seccoes(md, palavras=('log', 'changelog')):
    """Texto das seccoes cujo titulo contem as palavras, tal como esta na ficha."""
    linhas, out, dentro, nivel = md.splitlines(), [], False, 0
    for ln in linhas:
        m = re.match(r'^(#{1,6})\s+(.*)', ln)
        if m:
            n, tit = len(m.group(1)), m.group(2).lower()
            if dentro and n <= nivel:
                dentro = False
            if not dentro and any(re.search(rf'\b{p}\b', tit) for p in palavras):
                dentro, nivel = True, n
        if dentro:
            out.append(ln)
    return '\n'.join(out)[:8000]


def uma(e):
    pasta = FICHAS / e['ficha']
    nome = pasta.name
    atual = limpo(tracker.ler_ficha(pasta))
    if not atual:
        raise ValueError('o parser do tracker nao leu a ficha')
    ficha_md = tracker.ficha_de(pasta).read_text(encoding='utf-8', errors='replace')
    cfg_atual = next((f for f in pasta.iterdir() if f.name.lower() == f'config_{nome.lower()}.json'), None)

    versoes = []
    arquivo = [f for f in pasta.rglob('*.md') if f.name.lower().startswith(f'{nome.lower()}_ficha_')]
    configs = [f for f in pasta.rglob('config_*.json') if f != cfg_atual]
    for f in arquivo:
        d = data_nome(f.name)
        if not d:
            continue
        cf = next((c for c in configs if data_nome(c.name) == d), None)
        try:
            reg = ler_versao(nome, f, cf)
        except Exception as ex:  # noqa: BLE001
            reg = None
            print(e['t'], f.name, 'erro', ex, file=sys.stderr)
        # o nome do arquivo tem a data em que foi substituida; a data da propria versao e a do preco da ficha
        arq = d
        d = (reg or {}).get('data_preco') or d
        versoes.append({'data': d, 'arquivada_em': arq, 'ficheiro': f.relative_to(FICHAS).as_posix(),
                        'config': cf.relative_to(FICHAS).as_posix() if cf else None,
                        'num': reg, '_cfg': ler_json(cf) if cf else None})
    versoes.sort(key=lambda v: (v['data'], v['arquivada_em']))
    versoes.append({'data': atual.get('data_preco') or AGORA[:10], 'ficheiro': tracker.ficha_de(pasta).relative_to(FICHAS).as_posix(),
                    'config': cfg_atual.relative_to(FICHAS).as_posix() if cfg_atual else None, 'num': atual,
                    '_cfg': ler_json(cfg_atual) if cfg_atual else None, 'atual': True})

    comparacoes = []
    for a, b in zip(versoes, versoes[1:]):
        na, nb = a['num'] or {}, b['num'] or {}
        comparacoes.append({
            'de': a['data'], 'para': b['data'],
            'fv': [na.get('fv'), nb.get('fv')], 'preco': [na.get('preco'), nb.get('preco')],
            'upside': [na.get('upside'), nb.get('upside')], 'decisao': [na.get('decisao'), nb.get('decisao')],
            'quarter': [na.get('quarter'), nb.get('quarter')], 'par': [na.get('par'), nb.get('par')],
            'pressupostos': diff_config(a['_cfg'], b['_cfg']),
        })
    for v in versoes:
        v.pop('_cfg', None)
    return {'t': e['t'], 'pasta': e['ficha'], 'atual': atual, 'versoes': versoes, 'comparacoes': comparacoes,
            'log': seccoes(ficha_md), 'md': ficha_md, 'lido': AGORA}


def main():
    uni = [e for e in cfg('universo.json')['empresas'] if e.get('ficha')]
    velho = {x['t']: x for x in (ler(OUT, 'fichas.json', {}) or {}).get('fichas', [])}
    fichas, erros = [], []
    for e in uni:
        try:
            fichas.append(uma(e))
        except Exception as ex:  # noqa: BLE001
            traceback.print_exc()
            erros.append(f"{e['t']}: {ex}")
            if e['t'] in velho:
                fichas.append(dict(velho[e['t']], erro=str(ex)[:200]))
    guardar(OUT, 'fichas.json', {'lido': AGORA, 'fichas': fichas, 'erros': erros})
    mark(RAW, 'fichas', not erros, f'{len(fichas) - len(erros)} de {len(uni)} fichas lidas' + (f"; erro: {'; '.join(erros)[:100]}" if erros else ''))
    print('fichas:', len(fichas), 'erros:', erros)


if __name__ == '__main__':
    main()
