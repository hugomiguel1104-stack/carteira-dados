# Ficha de Empresa — Mastercard (MA · NYSE)

<!-- dados {"preco": 625.59, "fv": 477.3, "bear": 316, "bull": 552, "t1": 460, "cheia": null, "upside": -0.237, "data": "20-11-2026", "decisao": "Esperar / manter — não reforçar", "quarter": "Q3-26", "invalidadores": "0 de 5 · 2 em vigilância", "moeda": "USD", "par": {"rf": 0.0491, "erp": 0.05, "rf_metodo": "A", "erp_fonte": "Kroll"}} -->

`Q3-2026` · `revista 23-11-2026` · `criada 23-11-2026` · `plugin v2.1 · template v5.0` · **RASCUNHO v0**

> **Estado do modelo:** v0, calculado com o motor `modelo_calc.py` do plugin a partir de `config_MA.json`. **Sem Excel e sem o G12 do `02`.** Serve para decidir o sentido; corre-se o pipeline no PC antes de citar como definitivo.
> **Fontes:** release do Q3-26 (8-K na SEC) e resultados do Q4-25 (release e call). Sem Capital IQ: o consenso, os múltiplos históricos, o short interest e os insiders estão n/d.

**Preço:** $ 625,59 *(fecho de 20-11-2026)* · **Market cap:** $ 548 mM *(876 M acções diluídas, Q3-26)* · **EV:** $ 561,5 mM · **Par Rf/ERP:** 4,91% / 5,0%

---

## Questões-chave

1. **O que é que o preço exige?** O preço oferece **8,24%** ao ano. Para render 9%, a receita tem de crescer **10,9% ao ano durante 10 anos**; para 10%, 13,1%. O base dá 9,2%.
2. **A assimetria.** Ao WACC de 8,63%: adverso $ 381 (−39%), base $ 582 (−7%), favorável $ 675 (+8%). **O preço já está perto do cenário favorável.**
3. **O beta decide quase tudo.** Com Information Services (0,76) o fair value é $ 582; com 50% Information Services e 50% Software (1,005), $ 477.
4. **O que contraria a tese?** A receita cresce ~2x o volume (o preço e o mix fazem o resto). Regulação de comissões ou alternativas à rede atacam exactamente esse diferencial.

---

## Resumo

| | Beta 0,76 *(Information Services)* | Beta 1,005 *(50/50 com Software)* |
|---|---|---|
| WACC | 8,63% | 9,85% |
| Fair value base @WACC | **$ 582,3 (−6,9%)** | **$ 477,3 (−23,7%)** |
| Cenários @WACC *(adverso / base / favorável)* | $ 381 / $ 582 / $ 675 | $ 316 / $ 477 / $ 552 |
| Ponderado 20/60/20 | **$ 561** | **$ 460** |
| Peso do TV | 62,3% | 56,8% |

| | |
|---|---|
| **Retorno que o preço oferece** | **8,24%** (motor A; não depende do beta) |
| **Beta que governa** | **β 1,005** (regra de 27-11: em sector ambíguo, o mais conservador) → **FV $ 477 (−24%)**, ponderado $ 460; β 0,76 fica como sensibilidade ($ 582) |
| **Decisão** | **ESPERAR / manter** — qualidade alta, preço acima até do favorável ($ 552); não reforçar |
| **Posição** | 5,6% da carteira (+~1% via ETFs) |
| **O que decide** | Guidance de 2027 no Q4-26 (fim de Jan-2027): receita, opex e crescimento dos serviços |

### Sumário executivo

- **Recomendação.** Manter, sem reforçar. O negócio é dos melhores do mundo, mas o preço oferece 8,2%, e o favorável vale só +8% acima do preço.
- **Tese.** A rede cresce com a passagem do dinheiro físico para cartão e o volume cross-border; os serviços (já ~41% da receita) crescem quase o dobro.
- **Financials.** Receita LTM ~$ 36,3 mM (+15%). Margem op. GAAP LTM ~58,4% (ajustada 60,8% nos 9M). FCF LTM ~$ 15,2 mM (estimado). Devolve mais do que gera: recompras de $ 11,9 mM e dividendos de $ 2,3 mM nos 9M.
- **DCF.** Fair value de $ 582 com beta de 0,76: receita a crescer 12,5% → 5% (CAGR 9,2%) e margem EBIT de 58,5% → 61,9%.
- **Reverse DCF.** O preço exige CAGR de 10,9% (@9%) ou 13,1% (@10%). A gestão guia "low teens" para 2026; dez anos seguidos a esse ritmo é o favorável.
- **Múltiplos.** P/E GAAP LTM ~32,7x. EV/EBIT LTM ~26,5x. FCF yield ~2,8%.
- **Risco principal.** Compressão do preço e do mix: crescimento −3 pp/ano leva o valor a $ 461 (−26%).

---

## Reverse DCF

| Motor | Resultado | Leitura |
|---|---|---|
| **A** — retorno ao preço | **8,24%** | Abaixo do WACC (8,63%) e de qualquer required ≥ 9% |
| **B** — crescimento exigido | **CAGR 10,9% @9%** · **13,1% @10%** | O base dá 9,2%; FY20–25 ~16,5% ao ano (com recuperação pós-COVID) |

**Veredicto.** O preço assume que a Mastercard cresce a ~11% ao ano durante uma década. É o que fez, mas com a recuperação pós-COVID e o preço a subir mais do que o volume. Não é heróico; também não deixa margem de segurança.

---

## Cenários *(probabilidades do Hugo: 20/60/20, declaradas antes dos valores)*

| Cenário | p | A história | Receita | Margem op. Y10 | @WACC 8,63% | @WACC 9,85% |
|---|---|---|---|---|---|---|
| A rede é contornada | 20% | Regulação (CCCA ou routing) + conta-a-conta e stablecoins comprimem o preço | base −4,5 pp (~8% → 0,5%) | ~58% | $ 381 | $ 316 |
| **Compounder regular** | **60%** | Cash-to-card, serviços ~15%, preço moderado | 12,5% → 5% *(CAGR 9,2%)* | ~62% | **$ 582** | **$ 477** |
| Serviços e pagamentos agentic | 20% | Serviços em high-teens, tokenização e agentes de IA passam pela rede | +2 pp nos primeiros 5 anos | ~64% | $ 675 | $ 552 |

O preço ($ 625,59) fica entre o base e o favorável. Com o beta de 0,76, a descida até ao adverso é **~5x maior** do que a subida até ao favorável.

---

## Negócio

| Linha (Q3-26) | Crescimento | Leitura |
|---|---|---|
| Net revenue | +14% | $ 9.807 M |
| Payment network | +11% | Preço e mix acima do volume |
| Value-added services | +19% | Segurança, dados, autenticação |
| Volume total (GDV, moeda local) | +7% | |
| Cross-border | +11% | A abrandar face a 2025 |
| Transacções processadas | +9% | |

**Do lucro ao FCF.** O OCF dos 9M caiu para $ 11.859 M (de $ 12.646 M), com o lucro +18%. **A explicar no 10-Q**: pagamentos do acordo de interchange, incentivos a clientes ou working capital. O capex mais o software capitalizado são ~4% da receita.

**Ciclo de capex.** Não se aplica.

---

## Valuation

### Pressupostos do DCF

| Pressuposto | Y1 → Y10 | Âncora |
|---|---|---|
| Crescimento | 12,5% · 12% · 11,5% · 11% · 10% → 5% *(CAGR 9,2%)* | Guidance 2026: high end de "low double digit" + 1–1,5 pp de FX |
| Cash opex ex-D&A *(SBC dentro)* | 38,5% → 34,5% (EBIT 58,5% → 61,9%) | Margem ajustada 9M-26 de 60,8%; +~1 pp/ano nos últimos anos |
| Capex / receita | 4,4% → 4,0% | 9M-26 |
| Imposto · NWC | 20% · 0 | ETR 9M de 19,6% |
| WACC · g | 8,63% (β 0,76) ou 9,85% (β 1,005) · 2,5% | Rf 4,91% · ERP 5% · Kd 4,8% |

### Drivers dominantes (beta 0,76)

| Driver | Choque | Valor | Δ |
|---|---|---|---|
| **Crescimento** | −3 pp/ano | $ 461 | −$ 121 |
| WACC | +1 pp | $ 493 | −$ 89 |
| Cash opex | +3 pp | $ 553 | −$ 29 |

### Múltiplos

| Múltiplo | Valor | Nota |
|---|---|---|
| P/E GAAP LTM | ~32,7x | EPS LTM $ 19,11 = 9M $ 14,59 + Q4-25 $ 4,52 |
| EV/EBIT LTM | ~26,5x | EBIT LTM ~$ 21,2 mM (Q4-25 estimado) |
| FCF yield | ~2,8% | FCF LTM ~$ 15,2 mM, estimado |
| Contra a própria história | n/d | Sem CapIQ |

### Escada *(beta 1,005; hoje sem compras — provisória até recalcular no PC ao required de 10,85%)*

| Degrau | Preço |
|---|---|
| 1.ª tranche — ponderado @WACC (provisório) | ~$ 460 |
| 2.ª e cheia | a recalcular no pipeline (ao required) |
| Pensar em reduzir | acima de ~$ 675 *(favorável com β 0,76)* |

*Escada antiga com β 0,76 (revogada a 27-11): 1.ª ~$ 526 · 2.ª ~$ 467 · cheia ~$ 461.*

---

## Invalidadores

| # | Afirmação | Invalidador | Estado |
|---|---|---|---|
| 1 | O preço e o mix acrescentam ~5–6 pp sobre o volume | Receita da rede a crescer menos de 2 pp acima do GDV durante dois trimestres | OK (11% vs 7%) |
| 2 | Os serviços são o motor | Serviços abaixo de 12% durante dois trimestres | OK (19%) |
| 3 | A regulação é gerível | CCCA ou routing obrigatório aprovado nos EUA | Em vigilância |
| 4 | O cross-border é estrutural | Cross-border abaixo de 8% durante dois trimestres | OK (11%) |
| 5 | O FCF acompanha o lucro | OCF LTM a cair com o EBIT a subir durante mais dois trimestres | **Em vigilância** |

---

## Log

| Data | Quarter | Preço | FV (β 0,76 / 1,005) | IRR impl. | Decisão | Racional |
|---|---|---|---|---|---|---|
| 23-11-2026 | Q3-26 | $ 625,59 | $ 582 / $ 477 | 8,24% | Esperar · manter | Qualidade máxima, mas o preço está perto do favorável e a assimetria é negativa |

## Changelog

| Data | O que mudou |
|---|---|
| 27-11-2026 | Regra do beta da carteira (decisão do Hugo): governa o β 1,005 (FV $ 477, ponderado $ 460); β 0,76 passa a sensibilidade. Escada provisória até ao pipeline. A decisão não muda |
| 23-11-2026 | Criação (rascunho v0), com dados públicos e o motor `modelo_calc` |

## Notas de método

| | |
|---|---|
| Custo de capital | Rf 4,91% · ERP 5% · β Information Services 0,76 (Damodaran Jan-2026, corrigido de caixa); alternativa 50/50 com Software (System & Application) 1,25 → 1,005 · Kd 4,8% · CRP 0 |
| Estimativas | Q4-25: receita $ 8,8 mM e EBIT GAAP ~$ 4,85 mM (estimado a partir do EPS GAAP de $ 4,52); D&A pela regra de vintage (PP&E ~$ 3,5 mM, estimado); FCF LTM derivado |
| Limites | Sem consenso, múltiplos históricos nem passivos contingentes de litígio (interchange) na ponte. Sem o 10-Q completo |
