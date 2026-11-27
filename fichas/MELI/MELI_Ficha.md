# Ficha de Empresa — MercadoLibre (MELI · NasdaqGS)

<!-- dados {"preco": 1355, "fv": 1675, "bear": 765, "bull": 2396, "t1": 1460, "cheia": 1131, "upside": 0.2362, "data": "20-11-2026", "decisao": "Entrada faseada — preço abaixo da 1.ª tranche ($1.460)", "quarter": "Q3-26", "invalidadores": "0 de 5", "moeda": "USD", "par": {"rf": 0.049100000000000005, "erp": 0.05, "rf_metodo": "A", "erp_fonte": "Kroll"}} -->

> Substitui a versão de Agosto-2026 (FCFF, pré-Q3, ERP 5,5% com só 100 bp de CRP). Mudança de método: **FCFE / equity**, porque o Mercado Pago é um credor (carteira $ 17,9 mM) e no FCFF o crescimento da carteira não era tratado como consumo de capital.

## REVERSE DCF — o que o preço exige *(preço $ 1.355,00, fecho 20-11-2026)*

| | Valor | Leitura |
|---|---|---|
| **IRR implícita (base)** | **13,7%** | +158 bp vs Ke 12,14% · +58 bp vs required 13,14% |
| **Margem líquida terminal exigida @Ke** | **7,5%** (≈ EBIT 10,4%) | vs 8% no base (≈ EBIT 11%) · EBIT 11,1% FY25 · 12,4% FY24 · 7,4% TTM |
| **IRR por cenário** | bear 8,6% · base 13,7% · bull 16,8% | |

**Leitura:** a $ 1.355 o preço pede EBIT ~10,4% no longo prazo — abaixo do FY25, mas com um mix (crédito) que já não é o do FY25. Preço ≈ valor ponderado: sem margem de segurança, sem excesso.

## Custo de capital *(regra da carteira)*
Ke = Rf 4,91% (UST 10Y 20-11) + β 0,81 × ERP 5,0% + **CRP Brasil 3,18%** (Damodaran Jan-26) = **12,14%** · required = Ke + 100 bp = 13,14%.
β 0,81 = 57% commerce (Retail General 0,78 — o Damodaran Jan-26 não tem Retail Online) + 43% fintech (β 0,82, igual à NU).

## Dados de partida *(Q3-26, 10-Q / carta Q3-26 via sec-api.io — IR e EDGAR bloqueados nesta sessão; confirmar no PC)*

| | Q3-26 | Q3-25 | Δ |
|---|---|---|---|
| Receita + financial income | $ 10.750 M | $ 7.409 M | +45% USD · +41% FX-neutral |
| Commerce / Fintech | 6.141 / 4.609 | 4.174 / 3.235 | +47% / +42% |
| Income from operations | 676 (6,3%) | 720 (9,8%) | −350 bp |
| Provision for doubtful accounts | 1.342 | 815 | +65% |
| Net income | 448 | 420 | +7% (taxa efectiva 25,5% vs 33,8%: o lucro sobe pela taxa) |
| Carteira de crédito | 17.900 | 11.000 | +62% · cartão 47% |
| NPL 15–90 | 7,0% | — | 8,0% no Q1-26 |
| NIMAL | 20,1% | 21,0% | |
| Adjusted FCF (non-GAAP, após crédito) | 285 | — | TTM 1.210 |

TTM: receita $ 38.520 M · NI $ 1.900 M · equity $ 8.200 M · dívida $ 13.190 M (inclui funding fintech) · ações 50,70 M.
Margem directa por país Q3-26 vs Q3-25: Brasil 8,0% (11,8%) · México 14,2% (18,5%) · Argentina 33,7% (39,7%). **A compressão é generalizada, não só Brasil.**

## Porque caiu a acção
De ~$ 1.832 (Out) para $ 1.355 (−26%). −12% a 05-11 com o Q3: EPS GAAP $ 8,83 abaixo do esperado, quarto trimestre seguido de margem a descer (free shipping no Brasil ~60 bp, capacidade logística +20%, cohorts de cartão de crédito a pesar nas provisões). O mercado deixou de acreditar que a margem é investimento temporário.

## Modelo *(FCFE, 15 anos — crescimento Y10 ainda > 2×g)*
FCFE = NI − 12¢ por $ de receita adicional (capex líquido ~7,8¢ + capital da carteira ~4¢; NI TTM 1,9 mM − adjusted FCF 1,2 mM confirma a ordem de grandeza). Margem líquida ≈ EBIT × 0,72. Terminal: g 3% USD, payout = 1 − g/ROE, ROE terminal 30%.

| Cenário *(p declaradas antes dos valores)* | Crescimento USD | Margem líquida | Valor @Ke | @required |
|---|---|---|---|---|
| **Bear — "a margem é estrutural"** (30%) | 22% → 3% | 4,5% → 6% (EBIT ~8,5%) | $ 765 | $ 675 |
| **Base — "investimento que dilui"** (50%) | 32% → 3,5% | 5% → 8% (EBIT ~11%) | **$ 1.675** | $ 1.460 |
| **Bull — "Amazon da LatAm"** (20%) | 38% → 4% | 5,5% → 9,4% (EBIT ~13%) | $ 2.396 | $ 2.084 |
| **Ponderado** | | | **$ 1.546** | **$ 1.349** |

Porquê 30/50/20 e não 25/50/25: quatro trimestres seguidos de margem a cair, compressão em todos os países, concorrência (Shopee, Temu, Amazon) e risco BRL. A cauda negativa tem mais evidência do que a positiva.
Valor terminal: 36% do total (base) — aceitável (15 anos).

## Sensibilidades (base ao Ke antigo de 13,14%, $ 1.460)
| Driver | Valor |
|---|---|
| Reinvestimento 6¢ / 21¢ por $ | $ 1.565 / $ 1.303 |
| Ke 12,5% (taxa da casa BlueCrow) | $ 1.592 |
| g terminal 4% | $ 1.501 |

## Escada de entrada *(ao required 13,14%)*
| Degrau | Preço | vs $ 1.355 |
|---|---|---|
| 1.ª tranche — base (escada trocada: ponderado abaixo do base) | **$ 1.460** | +7,7% (preço abaixo) |
| 2.ª tranche — ponderado | $ 1.349 | −0,4% |
| Cheia — bear de eixo único (margem −1,5 pp) | $ 1.131 | −17% |
Bear conjunto: **$ 601 (−56%)** → peso ≤ ~3,5% da carteira.

## Invalidadores (falsificáveis)
1. Margem operacional < 6% no Q4-26 (época alta, deve diluir custos) → bear ganha peso.
2. NPL 91–360 dias / carteira de 6 meses antes > 23,8% no 10-K (era 22,4% em Dez-25), ou NPL 15–90 > 8%, ou NIMAL < 18% → o crédito é a origem da margem perdida.
5. Mais métricas a desaparecer da carta (já saíram 5 no Q3: NIMAL do cartão, cross-border, MELI+, sellers, quota de ads).
3. Crescimento FX-neutral < 30% com margem a descer → deixa de ser investimento.
4. BRL/USD a depreciar > 15% em 12 meses.

## Catalisadores
Q4-26 / FY26 (fim de Fev-2027) · carta anual · cohorts do cartão de crédito em 2027.

## O que confirmar no PC
β Retail Online Damodaran Jan-26 · números do Q3-26 no 10-Q original · D&A e capex por segmento · LTRP.

## Changelog
- 27-11-2026: escada corrigida — a 1.ª tranche estava ao ponderado ($ 1.349) e a 2.ª ao base ($ 1.460), a subir. Com o ponderado abaixo do base, a 1.ª vai ao base. **O preço ($ 1.355) passa a estar abaixo da 1.ª tranche.**
- 24-11-2026 (noite): β corrigido 1,01 → 0,81 — o Damodaran Jan-26 não tem Retail Online (o 1,10 era suposição minha). Ke 13,14% → 12,14%. Base $ 1.460 → $ 1.675; ponderado $ 1.349 → $ 1.546.
- 24-11-2026 (tarde): corrigido após a nota da equipa BlueCrow (05-11). Dois erros meus que se compensavam: margem líquida terminal de 10% equivalia a EBIT ~14% (acima do pico FY24); reinvestimento de 21–25% da receita adicional era ~2x o real. Base $ 1.629 → $ 1.460; ponderado $ 1.524 → $ 1.349. Adicionado invalidador do NPL 91–360 ajustado.
- 24-11-2026: refeita de raiz. Método FCFF → FCFE; 10 → 15 anos; ERP 5,5% (CRP 1%) → ERP 5% + CRP Brasil 3,18%; β 1,31 → 1,01; dados Q3-26. FV $ 1.696 → $ 1.629 (base) / $ 1.524 (ponderado). **Erro registado:** a 23-11 estimei ~$ 1.050 por interpolação da sensibilidade de WACC da ficha antiga — com método e horizonte errados. Não se usa.
