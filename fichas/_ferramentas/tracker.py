#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tracker.py — gera _Tracker_Valuations.xlsx a partir dos blocos ESTADO das fichas.

A ficha e a fonte. Este script le, nunca escreve nela. O xlsx e regenerado a cada
corrida: editar a mao e sobrescrito.

Uso:
    python tracker.py                    # escreve Analisar Stocks/_Tracker_Valuations.xlsx
    python tracker.py --dry-run          # imprime o que leu, nao escreve nada
    python tracker.py --saida FICH.xlsx  # destino alternativo

Nao faz chamadas de rede. As datas do proximo report saem do campo "Proximo
catalisador" da propria ficha quando trazem data explicita; caso contrario fica o
texto. O Alpha Vantage serve para datas, nunca para valores — a serie de EPS do
ultimo trimestre vem contaminada (verificado na AAPL, Jul-2026).
"""

import sys
import re
import json
import unicodedata
import datetime as dt
from pathlib import Path

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

RAIZ = Path(__file__).resolve().parent.parent          # ...\Analisar Stocks
# As fichas descobrem-se sozinhas (v1.4): {PASTA}_Ficha.md em Analisar Stocks/* e em
# Analisar Stocks/Diversos/*. Pastas comecadas por "_" ou "." ficam de fora.
GRUPOS = ["", "Diversos"]


def ficha_de(pasta):
    """O {PASTA}_Ficha.md da pasta, sem olhar a maiusculas (Meta/META_Ficha.md)."""
    alvo = f"{pasta.name.lower()}_ficha.md"
    for f in pasta.iterdir():
        if f.is_file() and f.name.lower() == alvo:
            return f
    return None


def fichas_com_data(pasta):
    """v1.9: fichas gravadas com sufixo (META_Ficha_29102026.md) fora de _arquivo — o tracker nao as le."""
    pref = f"{pasta.name.lower()}_ficha_"
    return sorted(f.relative_to(RAIZ).as_posix() for f in pasta.rglob("*.md")
                  if f.name.lower().startswith(pref)
                  and not any(parte.startswith("_") for parte in f.relative_to(pasta).parts[:-1]))


def descobrir():
    out = []
    for g in GRUPOS:
        base = RAIZ / g if g else RAIZ
        if not base.is_dir():
            continue
        for p in sorted(base.iterdir(), key=lambda x: x.name.lower()):
            if not (p.is_dir() and not p.name.startswith(("_", ".")) and p.name not in GRUPOS):
                continue
            datadas = fichas_com_data(p)
            if ficha_de(p):
                out.append(p.relative_to(RAIZ).as_posix())
                if datadas:
                    print(f"AVISO: {p.name} tem fichas com data fora de _arquivo ({', '.join(datadas)}) — "
                          f"o tracker le {ficha_de(p).name}; mover as outras para _arquivo.", file=sys.stderr)
            elif datadas:
                print(f"AVISO: {p.name} SEM {p.name}_Ficha.md — so fichas com data ({', '.join(datadas)}). "
                      f"Fica fora do tracker: renomear a mais recente para {p.name}_Ficha.md (nomes fixos, v1.9).",
                      file=sys.stderr)
    return out
SAIDA_PADRAO = RAIZ / "_Tracker_Valuations.xlsx"

ND = "n/d"

# Paleta alinhada com o pipeline do dcf-reverso.
AZUL = "FF1F3864"
CINZA = "FFF2F2F2"
VERDE = "FFC6EFCE"
AMBAR = "FFFFEB9C"
VERMELHO = "FFFFC7CE"
BRANCO = "FFFFFFFF"

FINA = Side(style="thin", color="FFD9D9D9")
GRELHA = Border(left=FINA, right=FINA, top=FINA, bottom=FINA)


# ----------------------------------------------------------------------------- texto

def limpar(s):
    """Normaliza sinais unicode que aparecem nas fichas para equivalentes ASCII."""
    if s is None:
        return ""
    s = unicodedata.normalize("NFKC", s)
    for mau, bom in [("−", "-"),   # MINUS SIGN, usado nos upsides negativos
                     ("–", "-"),   # EN DASH, separador das amplitudes
                     ("—", "-"),   # EM DASH
                     (" ", " ")]:  # NBSP
        s = s.replace(mau, bom)
    return s


def desmarcar(s):
    """Tira markdown de enfase e comentarios em italico, para comparar rotulos."""
    s = limpar(s)
    s = re.sub(r"\*+", "", s)
    s = re.sub(r"\s*\([^)]*\)\s*$", "", s)   # sufixo explicativo no fim do rotulo
    return s.strip().strip(":").strip()


def numero(txt):
    """
    '$ 613,37' -> 613.37 | '-$209' -> -209.0 | '€ 140,20' -> 140.2
    '$102.125 M' -> 102125.0   (ponto e separador de milhares, virgula e decimal)
    Devolve None se nao houver numero inequivoco.
    """
    if txt is None:
        return None
    t = limpar(str(txt))
    t = re.sub(r"\*+", "", t)
    m = re.search(r"(-?)\s*[\$€]?\s*(-?)\s*(\d[\d.\s]*(?:,\d+)?)", t)
    if not m:
        return None
    negativo = "-" in (m.group(1) + m.group(2))
    corpo = m.group(3).replace(" ", "").replace(".", "").replace(",", ".")
    try:
        v = float(corpo)
    except ValueError:
        return None
    return -v if negativo else v


def percentagem(txt):
    """'-14,9%' -> -14.9 ; '+13,2% vs 542 - ...' -> 13.2 (le so a primeira)."""
    if txt is None:
        return None
    t = limpar(str(txt)).replace("*", "")
    m = re.search(r"([+-]?\s*\d+(?:,\d+)?)\s*%", t)
    if not m:
        return None
    try:
        return float(m.group(1).replace(" ", "").replace(",", "."))
    except ValueError:
        return None


MESES = {"jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6,
         "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12}
MESES_EN = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
            "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}


def data(txt):
    """Aceita 2026-10-28, 26-07-2026, 30/07/2026 e 27-Jul-2026. Devolve date ou None."""
    if txt is None:
        return None
    t = limpar(str(txt)).replace("*", "")
    m = re.search(r"\b(\d{4})-(\d{2})-(\d{2})\b", t)        # ISO, usado no JSON
    if m:
        a, mes, d = (int(x) for x in m.groups())
        try:
            return dt.date(a, mes, d)
        except ValueError:
            return None
    m = re.search(r"\b(\d{1,2})[-/](\d{1,2})[-/](\d{4})\b", t)
    if m:
        d, mes, a = (int(x) for x in m.groups())
        try:
            return dt.date(a, mes, d)
        except ValueError:
            return None
    m = re.search(r"\b(\d{1,2})[-/ ]([A-Za-z]{3})[a-z]*[-/ ](\d{4})\b", t)
    if m:
        d, nome, a = int(m.group(1)), m.group(2).lower(), int(m.group(3))
        mes = MESES.get(nome) or MESES_EN.get(nome)
        if mes:
            try:
                return dt.date(a, mes, d)
            except ValueError:
                return None
    return None


# ----------------------------------------------------------------------------- ficha

def bloco_estado(texto):
    """Devolve so as linhas de tabela do bloco ESTADO."""
    m = re.search(r"^##\s*ESTADO(\s*[—-].*)?\s*$", texto, re.M)   # v3.4: "## ESTADO — detalhe"
    if not m:
        return []
    resto = texto[m.end():]
    fim = re.search(r"^(##\s|\*\*Múltiplos|---\s*$)", resto, re.M)
    if fim:
        resto = resto[:fim.start()]
    return [l.strip() for l in resto.splitlines() if l.strip().startswith("|")]


def pares(linhas):
    """
    Achata as linhas da tabela em {rotulo: valor}.
    Trata os dois formatos: 4 colunas (NOW/Meta/MSFT/CRWV) e 2 colunas (SAP).
    """
    out = {}
    for linha in linhas:
        celulas = [c.strip() for c in linha.strip("|").split("|")]
        if not celulas or all(set(c) <= set("-: ") for c in celulas):
            continue                                   # separador da tabela
        for i in range(0, len(celulas) - 1, 2):
            rot, val = desmarcar(celulas[i]), celulas[i + 1].strip()
            if rot and val:
                out.setdefault(rot.lower(), limpar(val))
    return out


def procurar(campos, *chaves):
    """Primeira chave cujo rotulo comece por uma das dadas (case-insensitive)."""
    for chave in chaves:
        c = chave.lower()
        for rot, val in campos.items():
            if rot.startswith(c):
                return val
    return None


def amplitude(txt):
    """'$52,60 - $99,61' -> (52.6, 99.61) | '-$209 a +$160' -> (-209.0, 160.0)"""
    if not txt:
        return None, None
    t = limpar(txt).replace("*", "")
    m = re.search(r"(-?\s*[\$€]?\s*-?\s*[\d.,\s]+?)\s*(?:-|a)\s*"
                  r"([+-]?\s*[\$€]?\s*[+-]?\s*[\d.,\s]+)", t)
    if not m:
        return None, None
    return numero(m.group(1)), numero(m.group(2))


# Padroes de escada de entrada, por ordem de tentativa. A Meta nao usa o rotulo
# "1a tranche" — chama-lhe "gate disciplinado de IRR=10% a $X".
PAD_TRANCHE1 = [
    r"1[ª°a]?\s*tranche\s*<\s*([\$€]?\s*[\d.,]+)",
    r"gate\s+disciplinado[^$€]*?([\$€]\s*[\d.,]+)",
]
PAD_CHEIA = [
    r"cheia\s*<\s*([\$€]?\s*[\d.,]+)",
]


def escada(txt):
    if not txt:
        return None, None
    t = limpar(txt).replace("*", "")
    t1 = c = None
    for p in PAD_TRANCHE1:
        m = re.search(p, t, re.I)
        if m:
            t1 = numero(m.group(1))
            break
    for p in PAD_CHEIA:
        m = re.search(p, t, re.I)
        if m:
            c = numero(m.group(1))
            break
    return t1, c


def ler_ficha(pasta):
    caminho = ficha_de(pasta)
    if caminho is None:
        return None
    bruto = caminho.read_text(encoding="utf-8", errors="replace")
    campos = pares(bloco_estado(bruto))
    dados = bloco_dados(bruto)          # v2.0: bloco gerado pelo pipeline — manda sobre o regex
    if not campos and not dados:
        return None

    empresa, ticker, bolsa = pasta.name, pasta.name.upper(), ND
    m = re.search(r"^#\s*Ficha de Empresa\s*[-—]\s*(.+?)\s*\(\s*([A-Za-z.]+)\s*"
                  r"[·|]\s*(.+?)\s*\)", limpar(bruto), re.M)
    if m:
        empresa, ticker, bolsa = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()

    # --- preco e data. Formato A: "Preco" + "Data". Formato B (SAP): "Preco de
    #     referencia" traz o valor, e a data vem de "Data desta revisao".
    preco_txt = procurar(campos, "preço de refer", "preço", "preco")
    data_txt = procurar(campos, "data desta revis", "data")

    # --- fair value base. O SAP nao tem "Valor DCF": governa o required return de 9%.
    fv_txt = procurar(campos, "valor dcf", "valor residual income",
                      "fair value ao required return de 9",
                      "fair value")
    base = ("required return 9%" if procurar(campos, "valor dcf") is None
            and procurar(campos, "fair value ao required return de 9") else "DCF base")

    upside = percentagem(fv_txt) or percentagem(procurar(campos, "upside"))

    bear, bull = amplitude(procurar(campos, "amplitude bull"))
    t1, cheia = escada(procurar(campos, "gates"))

    decisao = procurar(campos, "decisão", "recomendação") or ND
    quarter = (procurar(campos, "último report", "trimestre analisado") or ND)
    invalid = procurar(campos, "invalidadores") or ND
    catal = procurar(campos, "próximo catalisador") or ND

    moeda = "EUR" if "€" in (preco_txt or "") else "USD"

    reg = {
        "empresa": empresa,
        "ticker": ticker,
        "bolsa": bolsa,
        "moeda": moeda,
        "preco": numero(preco_txt),
        "data_preco": data(data_txt),
        "fv": numero(fv_txt),
        "base_fv": base,
        "upside": upside,
        "bear": bear,
        "bull": bull,
        "tranche1": t1,
        "cheia": cheia,
        "decisao": re.sub(r"\*+", "", decisao).strip(),
        "quarter": re.sub(r"\*+", "", quarter).strip(" *-"),
        "invalidadores": re.sub(r"\*+", "", invalid).strip(),
        "catalisador": re.sub(r"\*+", "", catal).strip(),
        "proximo_report": data(catal),
        "ficha": caminho.relative_to(RAIZ).as_posix(),
    }
    if dados:
        reg["fonte_campos"] = "bloco dados"
        mapa = {"preco": "preco", "fv": "fv", "bear": "bear", "bull": "bull", "tranche1": "t1", "cheia": "cheia"}
        for k, kd in mapa.items():
            if dados.get(kd) is not None:
                reg[k] = dados[kd]
        if dados.get("upside") is not None:
            reg["upside"] = dados["upside"] * 100
        if dados.get("data"):
            reg["data_preco"] = data(str(dados["data"]))
        if dados.get("proximo_report"):
            reg["proximo_report"] = data(str(dados["proximo_report"]))
        if dados.get("decisao"):
            reg["decisao"] = str(dados["decisao"])
        # v2.1 (template v5.0): sem bloco ESTADO — quarter, invalidadores e catalisador vem do bloco dados
        if dados.get("quarter"):
            reg["quarter"] = str(dados["quarter"])
        if dados.get("invalidadores"):
            reg["invalidadores"] = str(dados["invalidadores"])
        if dados.get("proximo_report") and reg["catalisador"] == ND:
            reg["catalisador"] = f"Report {dados['proximo_report']}"
        if dados.get("moeda"):
            reg["moeda"] = dados["moeda"]
        reg["base_fv"] = "residual income" if dados.get("metodo") == "banco_ri" else "DCF base"
    else:
        reg["fonte_campos"] = "ESTADO (regex)"
    reg["par"] = par_rf_erp(pasta, dados)
    return reg


def bloco_dados(bruto):
    """v2.0: <!-- dados {...} --> gerado pelo blocos.py. None se a ficha nao o tiver."""
    m = re.search(r"<!--\s*dados\s*(\{.*?\})\s*-->", bruto, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return None


def _central():
    p = RAIZ / "_ferramentas" / "custo_capital.json"
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def par_rf_erp(pasta, dados=None):
    """v1.9.1: o par Rf/ERP da ficha, lido do config (a copia gravada pelo custo_capital.py), contra o central.
    A calibracao entre nomes so compara fichas no mesmo par."""
    w = None
    for f in pasta.iterdir():
        if f.is_file() and f.name.lower() == f"config_{pasta.name.lower()}.json":
            try:
                c = json.loads(f.read_text(encoding="utf-8"))
                w = c.get("custo_capital") if c.get("metodo") == "banco_ri" else c.get("wacc")
                moeda = (c.get("mercado") or {}).get("moeda") or "USD"
            except (OSError, ValueError):
                w = None
            break
    if not w and dados and dados.get("par"):
        w, moeda = dados["par"], dados.get("moeda") or "USD"
    if not w or w.get("erp") is None or w.get("rf") is None:
        return "sem config"
    txt = f"{w.get('rf_metodo') or '?'} · Rf {w['rf']*100:.2f}% + ERP {w['erp']*100:.2f}%".replace(".", ",")
    cen = _central()
    if cen and moeda in cen.get("moedas", {}):
        e = cen["moedas"][moeda]
        kroll = "kroll" in str(w.get("erp_fonte", "")).lower()
        txt += " · carteira" if (abs(w["erp"] - e["erp"]) < 5e-5 and kroll) else " · FORA DO PAR"
    return txt


# ----------------------------------------------------------------------------- datas

CAL = Path(__file__).resolve().parent / "proximos_reports.json"


def calendario():
    """Datas do proximo report que a ficha nao fixa. Ver o _leia_me do JSON."""
    if not CAL.exists():
        return {}, None
    try:
        bruto = json.loads(CAL.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"AVISO: {CAL.name} ilegivel ({e}); datas so das fichas.", file=sys.stderr)
        return {}, None
    return bruto.get("empresas", {}), bruto.get("obtido_em")


def resolver_data(ficha, cal):
    """
    A ficha ganha sempre. O JSON so preenche o que ela nao fixa.
    Devolve (data|None, fonte).
    """
    if ficha["proximo_report"]:
        return ficha["proximo_report"], "ficha"
    entrada = cal.get(ficha["ticker"].upper(), {})
    d = data(entrada.get("data"))
    if d:
        return d, entrada.get("fonte", "calendario")
    return None, entrada.get("fonte", ND)


# ----------------------------------------------------------------------------- pipeline
# Fila de espera, revista em Agosto de 2026. Actualizar a mao quando a ordem mudar.
#
# Eixos pedidos pelo Hugo:  P = pagamentos  |  N = nao-EUA  |  A = beneficiario de AI
# nos EUA que nao seja mainstream.  Fora, por decisao dele: Apple, CoreWeave, Oracle, Palantir.
#
# Coluna "Pasta": so conta como coberto o que tem ficha .md em Analisar Stocks.
#   canonica   ficha + DCF          documentos  so PDFs na pasta          nenhuma  nada
# Os .docx da pasta "Equity research" NAO sao trabalho do Hugo e nao contam.
#
# Datas: so se afirmam as confirmadas. "a confirmar" e literal — confirmar com
# EARNINGS_CALENDAR quando o nome entrar em analise, nao antes.

PIPELINE = [
    (1, "A", "Micron", "MU", "a confirmar", "a confirmar", "nenhuma",
     "A factura do capex dos hyperscalers a aterrar na receita do fornecedor: a Amazon subiu o capex "
     "FY26 para ~$220 mil M citando explicitamente custos de memoria. Capacidade de HBM vendida ate ao "
     "fim de 2026 sob contratos nao cancelaveis, ~25% de quota. A pergunta do DCF: mudanca estrutural "
     "ou o melhor ciclo de sempre num negocio historicamente brutal?", "alta"),
    (2, "P", "Visa", "V", "a confirmar", "a confirmar", "nenhuma",
     "O melhor setup de reverse DCF da lista. De-rating real (~22x forward, abaixo da media de longo "
     "prazo, -19% no ano) assente numa tese especifica e falsificavel: stablecoins e agentes de AI a "
     "contornar os 2-3% de interchange. O reverse DCF responde a pergunta certa — que erosao de "
     "take-rate e que o preco ja embute? Zero exposicao a capex de AI.", "alta"),
    (3, "A", "Vertiv", "VRT", "a confirmar", "a confirmar", "nenhuma",
     "A alavanca mais directa ao buildout fisico: +34% de receita e +47% de lucro projectados para 2026, "
     "e co-desenvolvimento da arquitectura de 800V DC com a Nvidia. Testa a tese de infraestrutura sem "
     "comprar um megacap. Amplitude bull-bear vai sair larga.", "alta"),
    (4, "P N", "Adyen", "ADYEN", "a confirmar", "a confirmar", "nenhuma",
     "Pagamentos e nao-EUA no mesmo nome (NL, EUR -> dataset Damodaran Europe). Esta do lado certo da "
     "mudanca que castiga o #2: foi um dos arquitectos do OUSD, lancado em Jun-2026 com Stripe, Visa, "
     "Mastercard, BNY e Coinbase. O contraste com o #2 e metade da analise.", "alta"),
    (5, "-", "Alphabet", "GOOGL", "Q2-2026", "a confirmar", "ficha 26-10",
     "O unico mainstream da lista, e nao e por ser AI: a ficha da Meta usa a Alphabet como comp ancora "
     "para decidir (25,3x vs META 17,4x) sem ter valuation propria. E o unico nome do top 10 que melhora "
     "cobertura ja existente. Pasta tem 3 earnings releases, zero analise.", "alta"),
    (6, "A", "Constellation Energy", "CEG", "a confirmar", "a confirmar", "nenhuma",
     "A forma mais diferente da lista: gerador nuclear cujo valor depende do preco e da duracao dos PPA "
     "com datacenters. Drivers — factor de capacidade, preco de energia, prazo contratual — nao tem nada "
     "a ver com nada do que esta coberto. Diversificacao real, nao cosmetica.", "media"),
    (7, "N", "ASML", "ASML", "a confirmar", "a confirmar", "nenhuma",
     "Nao-EUA (NL, EUR), monopolio de EUV. Problema de valuation genuinamente diferente: como se desconta "
     "um monopolio com backlog plurianual e ciclo de encomendas volatil.", "media"),
    (8, "P N", "Nubank", "NU", "a confirmar", "a confirmar", "documentos",
     "Nao-EUA (Brasil) e fintech. Ja tem 5 results presentations na pasta e zero analise. Ciclo de credito "
     "ao consumo LatAm: o unico nome da lista onde o risco e de credito e nao de multiplo.", "media"),
    (9, "A", "Eaton", "ETN", "a confirmar", "a confirmar", "nenhuma",
     "O controlo do #3. Mesma tese de electrificacao, mas com end-markets diversificados. Se a tese vale, "
     "vale nos dois; se so aparecer no Vertiv, o que se esta a pagar e premio de narrativa. Correr o par "
     "e que da a resposta — nenhum dos dois sozinho da.", "media"),
    (10, "N", "MercadoLibre", "MELI", "a confirmar", "a confirmar", "documentos",
     "Nao-EUA, LatAm, e-commerce mais fintech. Fecha o eixo geografico com o #8. Pasta tem 4 PDFs "
     "trimestrais, sem analise em .md.", "media"),
]

# Banco de suplentes, se algum cair: Prysmian (nao-EUA + cabos/rede, acumula dois eixos),
# GE Vernova (turbinas), Comfort Systems (empreiteiro de datacenters, pouco seguido),
# Arista (networking), UnitedHealth (saude — o maior buraco do mapa).


# ----------------------------------------------------------------------------- excel

COLUNAS = [
    ("Empresa", 22, None), ("Ticker", 9, None), ("Bolsa", 11, None), ("Moeda", 8, None),
    ("Preco ref.", 12, "#,##0.00"), ("Data preco", 12, "DD-MM-YYYY"),
    ("FV base", 12, "#,##0.00"), ("Base do FV", 17, None), ("Upside %", 11, "+0.0;-0.0"),
    ("Bear", 11, "#,##0.00"), ("Bull", 11, "#,##0.00"),
    ("1a tranche", 12, "#,##0.00"), ("Cheia", 12, "#,##0.00"),
    ("Decisao", 34, None), ("Ultimo quarter", 24, None), ("Invalidadores", 24, None),
    ("Proximo catalisador", 46, None), ("Proximo report", 14, "DD-MM-YYYY"),
    ("Fonte da data", 15, None), ("Par Rf/ERP", 34, None), ("Campos lidos de", 16, None), ("Ficha", 26, None),
]

COLS_PIPELINE = [
    ("#", 5, None), ("Eixo", 7, None), ("Empresa", 22, None), ("Ticker", 10, None),
    ("Ultimo report", 14, None), ("Proximo report", 14, None),
    ("Pasta", 12, None), ("Racional", 92, None), ("Prioridade", 11, None),
]


def cabecalho(ws, colunas, titulo, subtitulo):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(colunas))
    c = ws.cell(row=1, column=1, value=titulo)
    c.font = Font(bold=True, size=13, color=BRANCO)
    c.fill = PatternFill("solid", fgColor=AZUL)
    c.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[1].height = 24

    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(colunas))
    c = ws.cell(row=2, column=1, value=subtitulo)
    c.font = Font(italic=True, size=9, color="FF808080")
    c.alignment = Alignment(vertical="center", indent=1)

    for i, (nome, larg, _) in enumerate(colunas, start=1):
        c = ws.cell(row=4, column=i, value=nome)
        c.font = Font(bold=True, size=10)
        c.fill = PatternFill("solid", fgColor=CINZA)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = GRELHA
        ws.column_dimensions[get_column_letter(i)].width = larg
    ws.row_dimensions[4].height = 28
    ws.freeze_panes = "A5"


def escrever(ws, colunas, linhas, primeira=5):
    for r, valores in enumerate(linhas, start=primeira):
        for i, (v, (_, _, fmt)) in enumerate(zip(valores, colunas), start=1):
            c = ws.cell(row=r, column=i, value=v)
            c.border = GRELHA
            c.alignment = Alignment(vertical="top",
                                    wrap_text=isinstance(v, str) and len(v) > 30)
            c.font = Font(size=10)
            if fmt and isinstance(v, (int, float)):
                c.number_format = fmt


def cor_decisao(ws, coluna, primeira, ultima):
    """Verde entrada faseada, ambar esperar, vermelho evitar. Sem regra = sem cor."""
    for r in range(primeira, ultima + 1):
        v = (ws.cell(row=r, column=coluna).value or "").lower()
        cor = (VERDE if "faseada" in v or "t1 aberta" in v
               else VERMELHO if "evitar" in v
               else AMBAR if "esperar" in v else None)
        if cor:
            ws.cell(row=r, column=coluna).fill = PatternFill("solid", fgColor=cor)


def construir(fichas, saida, cal, obtido_em):
    wb = openpyxl.Workbook()
    hoje = dt.date.today().strftime("%d-%m-%Y")

    ws = wb.active
    ws.title = "Avaliacoes"
    cabecalho(ws, COLUNAS, "Avaliacoes fechadas",
              f"Gerado a partir dos blocos ESTADO das fichas em {hoje}. "
              f"Editar a mao e sobrescrito na proxima corrida — a ficha e a fonte.")

    linhas = []
    for f in fichas:
        prox, fonte = resolver_data(f, cal)
        linhas.append([
            f["empresa"], f["ticker"], f["bolsa"], f["moeda"],
            f["preco"] if f["preco"] is not None else ND,
            f["data_preco"] or ND,
            f["fv"] if f["fv"] is not None else ND,
            f["base_fv"],
            f["upside"] if f["upside"] is not None else ND,
            f["bear"] if f["bear"] is not None else ND,
            f["bull"] if f["bull"] is not None else ND,
            f["tranche1"] if f["tranche1"] is not None else ND,
            f["cheia"] if f["cheia"] is not None else ND,
            f["decisao"], f["quarter"], f["invalidadores"],
            f["catalisador"], prox or ND, fonte, f.get("par", ND), f.get("fonte_campos", ND), f["ficha"],
        ])
    escrever(ws, COLUNAS, linhas)
    cor_decisao(ws, 14, 5, 4 + len(linhas))

    notas = [
        "n/d = a ficha nao publica o campo nesse formato — nao e zero nem falha do script.",
        "SAP: bloco ESTADO de 2 colunas, sem amplitude bull-bear nem escada de entrada. O fair value "
        "citado e o do required return de 9%, que e o que governa a ficha.",
        "CRWV: o bear e negativo (-209) e nao ha preco de posicao cheia — a propria ficha diz que "
        "'o bear nao tem preco de seguranca'.",
        f"Proximo report: a ficha ganha sempre; o resto vem de _ferramentas/proximos_reports.json "
        f"(obtido em {obtido_em or 'data desconhecida'}). 'por agendar' = a empresa ainda nao marcou.",
    ]
    for i, txt in enumerate(notas):
        c = ws.cell(row=6 + len(linhas) + i, column=1, value=txt)
        c.font = Font(italic=True, size=9, color="FF808080")

    wp = wb.create_sheet("Pipeline")
    cabecalho(wp, COLS_PIPELINE, "Fila de espera",
              "Ordenada por valor da proxima analise, nao por dimensao.  Eixo:  P pagamentos  ·  "
              "N nao-EUA  ·  A beneficiario de AI nao-mainstream.  Actualizar a mao quando a ordem mudar.")
    escrever(wp, COLS_PIPELINE, [list(p) for p in PIPELINE])

    nota = wp.cell(row=6 + len(PIPELINE), column=1,
                   value="Pasta: 'canonica' = ficha .md + DCF · 'documentos' = so PDFs na pasta · "
                         "'nenhuma' = nada. Os .docx da pasta 'Equity research' nao contam. "
                         "Datas 'a confirmar' sao literais — confirmar com EARNINGS_CALENDAR quando o "
                         "nome entrar em analise.")
    nota.font = Font(italic=True, size=9, color="FF808080")

    wb.save(saida)
    return saida


# ----------------------------------------------------------------------------- main

def main(argv):
    saida = Path(argv[argv.index("--saida") + 1]) if "--saida" in argv else SAIDA_PADRAO
    seco = "--dry-run" in argv

    fichas, falhas = [], []
    for nome in descobrir():
        f = ler_ficha(RAIZ / nome)
        (fichas if f else falhas).append(f or nome)

    if falhas:
        print(f"AVISO: sem bloco ESTADO legivel em: {', '.join(falhas)}", file=sys.stderr)
    if not fichas:
        print("ERRO: nenhuma ficha lida. Nada escrito.", file=sys.stderr)
        return 1

    cal, obtido_em = calendario()
    hoje = dt.date.today()

    for f in fichas:
        em_falta = [k for k in ("preco", "fv", "data_preco") if f[k] is None]
        marca = f"  <- em falta: {', '.join(em_falta)}" if em_falta else ""
        prox, fonte = resolver_data(f, cal)
        print(f"{f['ticker']:>5}  {f['moeda']}  preco={f['preco']}  fv={f['fv']}  "
              f"bear={f['bear']}  bull={f['bull']}  t1={f['tranche1']}  "
              f"cheia={f['cheia']}  data={f['data_preco']}  "
              f"proximo={prox or ND} ({fonte}){marca}")
        if prox and prox < hoje:
            print(f"       AVISO: o proximo report do {f['ticker']} ja passou "
                  f"({prox}). A avaliacao esta por refrescar.", file=sys.stderr)

    if seco:
        print("\n--dry-run: nada escrito.")
        return 0

    destino = construir(fichas, saida, cal, obtido_em)
    print(f"\nEscrito: {destino}  ({len(fichas)} avaliacoes, {len(PIPELINE)} na fila)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
