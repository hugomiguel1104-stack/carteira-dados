#!/usr/bin/env python3
"""Sincroniza as fichas da pasta Análise Ações com o repositório carteira-dados (pasta fichas/).

Corre no PC do Hugo (Windows), de 15 em 15 minutos, pela tarefa agendada do Windows "Carteira - fichas".
- Só LÊ a pasta Análise Ações: nunca altera, move ou apaga nada lá.
- Copia para fichas/ apenas o que o Terminal usa: {T}_Ficha.md, config_{T}.json, as versões datadas
  (_arquivo/ e Valuation(s)/) e, de _ferramentas/, o tracker.py, custo_capital.json e proximos_reports.json.
- Se nada mudou, não faz nada (nem commit nem push). Se mudou, faz commit e push; o GitHub Actions
  lê as fichas e a tarefa das 22:58 leva-as para a Carteira.
- Regista o que fez em tools/sync_fichas.log (na pasta do repositório).

Uso: python tools/sync_fichas.py            (normal)
     python tools/sync_fichas.py --dry-run  (mostra o que copiaria, sem copiar nem fazer push)
"""
import os, re, sys, shutil, subprocess, datetime as dt
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ORIGEM = Path(os.environ.get('ANALISE_ACOES', r'C:\Users\HugoPereiraAbreu\OneDrive - Blue Crow Capital\Desktop\Análise Ações\Analisar Stocks'))
DEST = REPO / 'fichas'
LOG = REPO / 'tools' / 'sync_fichas.log'
DRY = '--dry-run' in sys.argv
FERRAMENTAS = ['tracker.py', 'custo_capital.json', 'proximos_reports.json']


def log(msg):
    linha = f"{dt.datetime.now():%Y-%m-%d %H:%M} {msg}"
    print(linha)
    if not DRY:
        try:
            with open(LOG, 'a', encoding='utf-8') as f:
                f.write(linha + '\n')
            # o log não cresce para sempre
            linhas = LOG.read_text(encoding='utf-8').splitlines()
            if len(linhas) > 2000:
                LOG.write_text('\n'.join(linhas[-1000:]) + '\n', encoding='utf-8')
        except OSError:
            pass


def pastas_empresa():
    for base in (ORIGEM, ORIGEM / 'Diversos'):
        if not base.is_dir():
            continue
        for p in sorted(base.iterdir()):
            if p.is_dir() and not p.name.startswith(('_', '.')) and p.name != 'Diversos':
                yield p


def ficheiros():
    for p in pastas_empresa():
        nome = p.name.lower()
        for f in p.iterdir():
            if f.is_file() and (f.name.lower() == f'{nome}_ficha.md' or f.name.lower() == f'config_{nome}.json'):
                yield f
        arq = p / '_arquivo'
        if arq.is_dir():
            for f in arq.iterdir():
                if f.is_file() and (re.match(rf'{re.escape(nome)}_ficha.*\.md$', f.name.lower()) or f.name.lower().startswith('config_')):
                    yield f
        for sub in ('Valuation', 'Valuations'):
            d = p / sub
            if d.is_dir():
                for f in d.iterdir():
                    if f.is_file() and re.match(rf'{re.escape(nome)}_ficha_.*\.md$', f.name.lower()):
                        yield f
    for n in FERRAMENTAS:
        f = ORIGEM / '_ferramentas' / n
        if f.is_file():
            yield f


def git(*args):
    r = subprocess.run(['git', '-C', str(REPO), *args], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout + r.stderr).strip()


def main():
    if not ORIGEM.is_dir():
        log(f'ERRO: não encontro a pasta {ORIGEM}')
        return 1
    mudou = []
    for f in ficheiros():
        rel = f.relative_to(ORIGEM)
        alvo = DEST / rel
        try:
            novo = f.read_bytes()
        except OSError as e:   # ficheiro aberto/a sincronizar no OneDrive: tenta na próxima corrida
            log(f'aviso: não consegui ler {rel} ({e})')
            continue
        if alvo.exists() and alvo.read_bytes() == novo:
            continue
        mudou.append(rel.as_posix())
        if not DRY:
            alvo.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, alvo)
    if not mudou:
        return 0
    log(f'{len(mudou)} ficheiro(s) novo(s) ou alterado(s): ' + ', '.join(mudou[:10]) + (' …' if len(mudou) > 10 else ''))
    if DRY:
        return 0
    git('pull', '--rebase', '--autostash', '-q')
    git('add', 'fichas')
    c, out = git('commit', '-q', '-m', f'Fichas sincronizadas do PC ({len(mudou)} ficheiro(s))')
    if c != 0 and 'nothing to commit' not in out:
        log(f'ERRO no commit: {out[:300]}')
        return 1
    c, out = git('push', '-q')
    if c != 0:
        log(f'ERRO no push (tenta de novo na próxima corrida): {out[:300]}')
        return 1
    log('enviado para o GitHub')
    return 0


if __name__ == '__main__':
    sys.exit(main())
