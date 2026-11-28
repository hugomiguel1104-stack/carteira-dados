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
CAMPOS = ["preco", "fv", "bear", "bull", "t1", "irr", "data", "decisao", "quarter", "moeda", "par", "perfil"]

# Perfis do template v6: (secção, padrão obrigatório, descrição). Ver "Perfis" em claude/Template_Ficha_v6.md.
PERFIS = {
    "geral": [(5, r"ROIC", "ROIC")],
    "plataforma": [(2, r"take rate|comiss", "take rate"), (4, r"float|working capital|NWC", "float/working capital")],
    "software": [(4, r"\bSBC\b", "SBC na ponte"), (2, r"ARR|cRPO|RPO|NRR|reten", "ARR/cRPO/retenção")],
    "rede": [(2, r"volume|GDV|cross-border", "volume e cross-border")],
    "capex": [(5, r"capex", "capex vs D&A"), (5, r"receita (nova|incremental) por", "receita nova por $ de capex")],
    "ciclico": [(4, r"ciclo|normaliz", "margens a meio do ciclo"), (2, r"book-to-bill|encomendas|bookings", "encomendas")],
    "banco": [(5, r"\bROE\b", "ROE"), (5, r"CET1|capital regulat", "CET1"), (5, r"NPL|incumpr|cobertura", "qualidade de crédito"), (10, r"residual income", "residual income")],
    "sotp": [(10, r"SOTP|soma das partes", "SOTP")],
    "pre_lucro": [(4, r"runway|queima", "runway"), (5, r"dilui", "diluição")],
}
PROIBIDO_BANCO = [(10, r"\bFCFF\b", "FCFF num banco"), (5, r"\bROIC\b", "ROIC num banco")]


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

    perfis = []
    if m:
        try:
            pf = json.loads(m.group(1)).get("perfil")
            perfis = [pf] if isinstance(pf, str) else list(pf or [])
        except json.JSONDecodeError:
            pass
    for pf in perfis:
        if pf not in PERFIS:
            erros.append(f"perfil desconhecido '{pf}' (ver a tabela de perfis do template)")
    sec_txt = lambda n: (re.search(rf"^## {n}\. .*?$(.*?)(?=^## \d{{1,2}}\. |\Z)", txt, re.M | re.S) or [None, ""])[1] or ""
    regras = [r for pf in perfis for r in PERFIS.get(pf, [])] + (PROIBIDO_BANCO if "banco" in perfis else [])
    for n, pat, desc in regras:
        hit = re.search(pat, sec_txt(n), re.I)
        if (desc.endswith("num banco") and hit):
            erros.append(f"secção {n}: {desc} (o perfil banco não usa)")
        elif not desc.endswith("num banco") and not hit:
            erros.append(f"secção {n} sem {desc} (obrigatório no perfil {', '.join(perfis)})")

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
    metrica = "ROE" if "banco" in perfis else "ROIC"
    if s5 and not re.search(rf"{metrica}\s+(marginal|incremental)", s5.group(1), re.I):
        erros.append(f"secção 5 sem {metrica} incremental/marginal")
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
