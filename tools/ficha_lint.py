#!/usr/bin/env python3
"""Verificador de fichas — template v6 (proposta de 28-11-2026).

Uso:  python tools/ficha_lint.py fichas/BKNG/BKNG_Ficha.md [outra.md ...]
Sai com código 1 se alguma ficha falhar. Não altera ficheiros.
"""
import json
import re
import sys
from pathlib import Path

SECCOES = [
    (1, "Sumário executivo"),
    (2, "Negócio"),
    (3, "Moat"),
    (4, "Histórico"),
    (5, "Investimento e retorno"),
    (6, "Balanço"),
    (7, "Projecções"),
    (8, "Métricas"),
    (9, "Custo de capital"),
    (10, "Valuation"),
    (11, "Sensibilidades"),
    (12, "Decisão"),
]
CAMPOS = ["preco", "fv", "bear", "bull", "t1", "irr", "data", "decisao", "quarter", "moeda", "par"]


def verificar(path: Path) -> list[str]:
    txt = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    erros = []

    if not re.match(r"# Ficha de Empresa — .+\(([A-Z0-9.]+) · .+\)", txt.split("\n", 1)[0]):
        erros.append("título fora do formato '# Ficha de Empresa — Nome (TICKER · Bolsa)'")

    m = re.search(r"<!--\s*dados\s*(\{.*?\})\s*-->", txt, re.S)
    if not m:
        erros.append("falta o bloco <!-- dados {...} -->")
    else:
        try:
            d = json.loads(m.group(1))
            falta = [c for c in CAMPOS if c not in d]
            if falta:
                erros.append(f"bloco dados sem: {', '.join(falta)}")
            t1, cheia = d.get("t1"), d.get("cheia")
            if t1 is not None and cheia is not None and cheia > t1:
                erros.append(f"escada a subir: cheia {cheia} > 1.ª tranche {t1}")
        except json.JSONDecodeError as e:
            erros.append(f"bloco dados não é JSON válido ({e})")

    if re.search(r"^#{1,2} *Versão anterior", txt, re.M):
        erros.append("tem uma 'Versão anterior' colada — vai para _arquivo")

    h2 = [(int(n), t.strip()) for n, t in re.findall(r"^## (\d{1,2})\. (.+)$", txt, re.M)]
    nums = [n for n, _ in h2]
    for n, nome in SECCOES:
        if n not in nums:
            erros.append(f"falta a secção {n}. {nome}")
    if nums != sorted(nums):
        erros.append(f"secções fora de ordem: {nums}")

    sec = lambda n: re.search(rf"^## {n}\. .*?$(.*?)(?=^## \d{{1,2}}\. |\Z)", txt, re.M | re.S)
    s1 = sec(1)
    if s1:
        linhas = [l for l in s1.group(1).strip().split("\n") if l.strip() and not l.lstrip().startswith("|")]
        if len(linhas) > 8:
            erros.append(f"sumário com {len(linhas)} linhas de texto (máx. 8)")
    s4 = sec(4)
    if s4:
        anos = set(re.findall(r"\b(?:FY)?(20\d{2})\b", s4.group(1)))
        if len(anos) < 5:
            erros.append(f"secção 4 com {len(anos)} anos de histórico (mín. 5)")
    s5 = sec(5)
    if s5 and not re.search(r"ROIC\s+(marginal|incremental)", s5.group(1), re.I):
        erros.append("secção 5 sem ROIC incremental/marginal")
    return erros


def main(args: list[str]) -> int:
    if not args:
        print(__doc__)
        return 2
    falhou = False
    for a in args:
        erros = verificar(Path(a))
        print(f"{'OK ' if not erros else 'FALHA'}  {a}")
        for e in erros:
            print(f"   - {e}")
        falhou |= bool(erros)
    return 1 if falhou else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
