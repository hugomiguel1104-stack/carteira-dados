# Ficha de Empresa — Uber Technologies (UBER · NYSE)

<!-- dados {"preco": 66.63, "fv": 80.72, "bear": 43.24, "bull": 108.87, "t1": 62.51, "cheia": 57.30, "irr": 11.94, "upside": 0.211, "data": "27-11-2026", "decisao": "Esperar — a ordem do plano a ≤ $60 mantém-se (1.ª tranche = ponderado dos 4 cenários @required, $62,51)", "quarter": "Q3-26", "invalidadores": "0 de 6 disparados · 4 em vigilância", "moeda": "USD", "par": {"rf": 0.04936, "erp": 0.05, "rf_metodo": "C", "erp_fonte": "Kroll"}, "proximo_report": "2027-02-02", "perfil": "plataforma", "devolucao_fcf_max": 124, "divida_liquida_sobe": true, "ponderado": 71.05, "peso_max": 3.0} -->

`revista 28-11-2026` · `Q3-2026` · `fecho $ 66,63 (27-11-2026)` · `template v6 · plugin v2.2` · `modelo: UBER_DCF.xlsx (pipeline CITÁVEL: G12 verde, G15 OK, ponte fecha ao cêntimo; verificar_xlsx OK); Rf a confirmar no PC` · `fontes: SEC EDGAR (portal, 28-11), 10-Q e ER do Q3-26 (04-11), 10-K FY24/FY25, consenso e pares por web; sem Capital IQ`

---

## 1. Sumário executivo

| Preço | Fair value base @WACC | Ponderado (4 cenários AV) | Retorno implícito vs required | Decisão | 1.ª tranche / cheia | Próximo catalisador |
|---|---|---|---|---|---|---|
| $ 66,63 *(27-11)* | **$ 80,72** (+21%) | $ 71,05 @WACC · $ 62,51 @required | **11,94%** base · 10,91% ponderado vs **11,43%** | **Esperar — ordem T1 a ≤ $ 60 mantém-se** | < $ 62,51 / < $ 57,30 | Q4-26 (~02-02-2027) |

**Tese.** A Uber cobra uma portagem de ~3,5% (EBITDA GAAP, SBC dentro) sobre $ 226 mM de gross bookings que crescem 20%; o mercado paga-a como se o crescimento caísse para 6,6% ao ano durante dez anos.
**O que o preço exige:** a $ 66,63 o base rende 11,94% (o ponderado 10,91%); para render só o WACC (10,43%) bastava GB a 6,6%/ano com a margem a 4,5%, ou a margem do Y10 ficar em 3,8% com o crescimento do base.
**Maior risco:** robotáxis com app própria (Waymo sai da exclusividade em Austin/Atlanta em Jan-2028; Tesla) — 35% da probabilidade está em cenários que valem $ 21–43.
**Porque não é "comprar já":** o base rende o required, mas o ponderado não (−52 bp); a média é que decide sob incerteza. **Porque não é "evitar":** o ponderado passa a régua da carteira (10,5%) e a $ 60 rende 11,8% — acima do required.

---

## 2. Negócio e modelo de receita

A Uber é um marketplace de três lados (consumidores, motoristas/estafetas, comerciantes) em ~70 países. A unidade de receita é:

> **Receita = gross bookings × take rate** — onde o GB é o valor bruto da viagem ou da encomenda (com taxas e gorjetas) e o take rate é o que fica depois de pagar o motorista, o estafeta e os incentivos. Mais publicidade (dentro do Delivery; +$ 176 M YoY no Q3, 10-Q) e Uber One (50 M membros, ~metade do GB).

**Segmentos — Q3-26** *(10-Q; take rate = receita / GB)*

| Segmento | GB ($ M) | % GB | YoY | Receita ($ M) | Take rate | Op. income do segmento | % do GB |
|---|---|---|---|---|---|---|---|
| Mobility | 29.512 | 49% | +18% (+17% cc) | 7.520 *(−2%)* | 25,5% *(30,6% há um ano)* | 2.362 *(+27%)* | 8,0% |
| Delivery | 28.539 | 48% | +22% (+23% cc) | 5.488 *(+23%)* | 19,2% *(igual)* | 1.057 *(+30%)* | 3,7% |
| Freight | 1.768 | 3% | +35% | 1.758 | 99% | (33) | −1,9% |
| **Total** | **59.819** | 100% | **+20%** | **14.766** *(+10%)* | 24,7% | 3.386 → non-GAAP op. income 2,3 mM | 3,9% |

**Ponto 1 — porque é que a receita de Mobility caiu 2% com os bookings a +18%.** É **mudança de modelo de negócio, não contabilística nem de procura** (10-Q, nota de receita e MD&A):
- Desde **2-01-2026** a Uber mudou o modelo "em certos mercados do Reino Unido": deixou de ser responsável pelo serviço de transporte e concluiu que é **agente**. O pagamento ao motorista passa a abater à receita em vez de entrar no custo da receita. O 10-Q quantifica: **−$ 1,1 mM de receita no Q3** (−$ 3,2 mM nos 9M) e, no custo da receita, "−$ 1,1 mM em pagamentos e incentivos a motoristas". **Efeito no EBIT: zero.** Em paralelo, a Uber UK deixou de aplicar o regime de IVA sobre a margem (VAT Order 1987) — ver o litígio com o HMRC na secção 6.
- **Pro forma sem o UK**, a receita de Mobility cresceu **+12%** (7.682 → ~8.620) contra GB +17,5%. Os ~5–6 pp que sobram são **take rate a descer** (30,6% → ~29,2% pro forma): incentivos para recuperar oferta de motoristas fora dos EUA (a call fala de "international driver supply constraints"; o CEO diz que está a "investir significativamente" em motoristas) e mix. Também a 1-07-2026 mudou a imputação de custos de rede entre custo da receita e opex — mexe nas margens por linha, não na receita.
- **Leitura:** dois terços do gap são cosméticos (UK); um terço é económico — a Uber está a pagar mais para manter a oferta, o que aparece no take rate e não na margem do segmento (que subiu para 8,0% do GB). A comparação limpa volta no **Q1-27**, quando o UK fica no período homólogo. Invalidador 5 em vigilância.

**KPIs que movem a receita** *(ERs e 10-K; MAPCs e viagens anteriores a 2024 de memória dos ERs — confirmar no PC)*

| | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM Set-26 |
|---|---|---|---|---|---|---|---|---|
| Gross bookings ($ mM) | 65,0 | 57,9 | 90,4 | 115,4 | 137,9 | 162,8 | 193,5 | 225,7 *(+23% YoY)* |
| Receita ($ mM) | 13,0 | 11,1 | 17,5 | 31,9 | 37,3 | 44,0 | 52,0 | 56,5 |
| **Take rate** | 20,0% | 19,2% | 19,3% | 27,6% | 27,0% | 27,0% | 26,9% | 25,0% |
| Adj. EBITDA / GB | −4,2% | −4,4% | −0,9% | +1,5% | +2,9% | +4,0% | +4,5% | +4,8% |
| MAPCs no Q4 (M) | 111 | 93 | 118 | 131 | 150 | 171 | 202 | 215 *(Q3)* |
| Viagens (mM) | 6,9 | 5,0 | 6,4 | 7,6 | 9,4 | 11,3 | 13,6 | 15,3 |

*O que isto mostra:* o take rate não é uma série comparável — saltou em 2022 (UK passou a principal em Mar-22 e o Freight entrou consolidado) e cai em 2026 (UK volta a agente). **A variável que conta é a margem sobre o GB**, que passou de −4% para +4,8% em cinco anos, e o GB, que cresceu ~19%/ano desde 2023 por volume (viagens +16–20%) e frequência. Por isso o modelo (secção 7) projecta **GB × margem**, não receita.

**Concentração:** nenhuma de clientes. A concentração relevante é de **oferta**: motoristas (classificação laboral em vários países), seguradoras (reservas de $ 13,7 mM) e, nos robotáxis, parceiros de condução autónoma (Waymo, que está a sair; ~700 veículos AV na app no fim de 2026, > 2.000 em 2027). Aeroportos = 15% do GB de Mobility (risk factors).

---

## 3. Moat e concorrência

**Rivais de referência:** Lyft na Mobility dos EUA (GB $ 5,6 mM/trimestre, ~1/5 da Mobility da Uber; adj. EBITDA 3,6% do GB) e DoorDash no Delivery dos EUA e Europa (GOV $ 33,9 mM, +36% com a Deliveroo, ~+23% sem; adj. EBITDA 3,1% do GOV). Os dois no Q3-26.

**Onde a vantagem aparece nos números:** escala (215 M de MAPCs, 4,1 mM de viagens no trimestre), margem do segmento Mobility a 8,0% do GB — mais do dobro da Lyft, com SBC fora nas duas — e cross-sell (Uber One, 50 M membros). O Delivery cresce ao ritmo da DoorDash orgânica (22% vs ~23%): quota estável, não a ganhar.

**Onde não aparece:** no take rate de Mobility (a cair, para comprar oferta); no Brasil (concorrência local referida na call do Q2); no preço que o mercado paga (a DoorDash vale ~70x o lucro contra ~41x da Uber, Trefis 16-11).

**O que o erode e a que velocidade:** o software de condução concentra-se (Waymo, Tesla) e as frotas autónomas fragmentam-se. A app do consumidor é onde a Uber cobra a portagem — ou onde é contornada. **Sinais de 2026:** separação em Phoenix (Jun-26); Waymo notificou o fim da exclusividade em Austin e Atlanta a partir de **Jan-2028** e recusou uma opção de reserva dedicada de robotáxi dentro da app da Uber (Bloomberg, 04-11). Trajectória: **estável no humano, a estreitar no autónomo** — quatro cenários na secção 10.

---

## 4. Histórico: das vendas ao cash flow

**Ponte por ano** *(SEC EDGAR via portal, us-gaap; $ M. EBITDA = EBIT GAAP + D&A, **SBC dentro**. NOPAT a 21% nos anos com EBIT positivo, sem crédito fiscal nos negativos. FCF = CFO − capex. Float = variação das reservas de seguros no cash flow — 10-K FY23/FY24 e 10-Q; FY2025 pela variação do balanço)*

| | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM Set-26 |
|---|---|---|---|---|---|---|---|---|---|---|
| Gross bookings | 34.409 | 49.799 | 65.001 | 57.897 | 90.415 | 115.395 | 137.865 | 162.773 | 193.454 | 225.701 |
| Receita | 7.932 | 10.433 | 13.000 | 11.139 | 17.455 | 31.877 | 37.281 | 43.978 | 52.017 | 56.526 |
| **EBITDA** *(SBC dentro)* | −3.570 | −2.607 | −8.124 | −4.288 | −2.932 | −885 | 1.933 | 3.510 | 6.284 | 7.803 |
| *EBITDA / GB* | *−10,4%* | *−5,2%* | *−12,5%* | *−7,4%* | *−3,2%* | *−0,8%* | *1,4%* | *2,2%* | *3,2%* | *3,5%* |
| EBIT GAAP | −4.080 | −3.033 | −8.596 | −4.863 | −3.834 | −1.832 | 1.110 | 2.799 | 5.565 | 7.034 |
| NOPAT | −4.080 | −3.033 | −8.596 | −4.863 | −3.834 | −1.832 | 877 | 2.211 | 4.396 | 5.557 |
| + D&A | 510 | 426 | 472 | 575 | 902 | 947 | 823 | 711 | 719 | 769 |
| − Capex | −821 | −558 | −588 | −616 | −298 | −252 | −223 | −242 | −336 | −314 |
| **FCF (CFO − capex)** | −2.239 | −2.099 | −4.909 | −3.361 | −743 | 390 | 3.362 | 6.895 | 9.763 | **10.421** |
| − SBC | −124 | −170 | −4.596 | −827 | −1.168 | −1.793 | −1.935 | −1.796 | −1.826 | −2.074 |
| − Float de seguros | n/d | n/d | n/d | n/d | −516 | −730 | −2.230 | −2.819 | −2.667 | −1.841 |
| **FCF do dono** | n/d | n/d | n/d | n/d | **−2.427** | **−2.133** | **−803** | **2.280** | **5.270** | **6.506** |
| *FCF / EBITDA* | n/s | n/s | n/s | n/s | n/s | n/s | 174% | 196% | 155% | 134% |
| *FCF do dono / NOPAT* | | | | | | | n/s | 103% | 120% | 117% |

**Ponto 2 — o FCF do dono.** Dos **$ 10,4 mM** de FCF recorde do LTM, **$ 2,1 mM são SBC** (a Uber paga em acções, e o custo é real — 3,7% da receita) e **$ 1,8 mM são float de seguros**: reservas para sinistros que entram no CFO quando o prémio é cobrado à viagem e saem anos depois quando o sinistro é pago. O float é dinheiro de terceiros, não do accionista — e tem caixa e investimentos restritos de $ 11,4 mM atrás. **FCF do dono = $ 6,5 mM (62% do FCF reportado), 4,8% de yield ao preço.** Só é positivo desde 2024.

**Cascata do LTM Set-26** *(por $ 100 de gross bookings)*

| GB | − Pago a motoristas, estafetas, comerciantes | = Receita | − Opex cash (SBC dentro) | = EBITDA | − D&A | = EBIT | − Imposto | = NOPAT | + D&A − capex | + Float, WC e outros | = FCF | − SBC − float | = FCF do dono |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 225.701 | −169.175 | 56.526 | −48.723 | 7.803 | −769 | 7.034 | −1.477 | 5.557 | +455 | +4.409 | 10.421 | −3.915 | **6.506** |
| 100 | 75,0 | 25,0 | 21,6 | 3,46 | 0,34 | 3,12 | 0,65 | 2,46 | 0,20 | 1,95 | 4,62 | 1,73 | **2,88** |

*O que isto mostra:* de cada $ 100 que o consumidor paga, a Uber fica com $ 25 de receita, $ 3,46 de EBITDA e **$ 2,88 de caixa do dono**. O "+ Float, WC e outros" ($ 4,4 mM) é o SBC que volta (é não-caixa no CFO), o float e impostos diferidos — **o FCF reportado é 134% do EBITDA porque inclui estas três coisas**.

**Os ciclos — 2019–2020.** 2019 foi o pico de perdas (EBITDA −$ 8,1 mM, com $ 4,6 mM de SBC do IPO); 2020 foi o choque da COVID: GB −11% no total, mas **Mobility caiu ~45%** e o Delivery mais do que duplicou. O CFO foi −$ 4,3 mM e −$ 2,7 mM. Nesses anos não havia margem para proteger; hoje há — o stress de 2020 sobre a estrutura actual está na secção 6.

**O que mudou, e porquê.**
- **A margem sobre o GB subiu 15 pp desde 2019** (−12,5% → +3,5%): alavanca operacional (custos fixos de plataforma diluídos por um GB 3,5x maior), fim das guerras de subsídios (saída da China, Sudeste Asiático, Rússia) e publicidade no Delivery (margem alta; +$ 176 M YoY no Q3).
- **Q3-26: o GAAP piorou enquanto o non-GAAP melhorou.** EBITDA GAAP / GB **2,8%** no Q3 (3,9% no Q1, 3,6% no Q2) contra non-GAAP op. income 3,9%. A diferença: R&D +48% ($ 1.273 M; SBC de I&D $ 333 M, rede +$ 130 M, AV), SBC +28% YoY ($ 594 M) e custos da operação DH. Se o Q4 repetir os 2,8%, o Y1 do base (3,5%) fica optimista — invalidador 2.
- **A conversão em caixa está inflacionada e a descer:** 196% do EBITDA em 2024 → 134% no LTM, porque o float abranda (+$ 2,8 mM em 2024, +$ 1,8 mM no LTM) e os diferidos deixaram de ajudar.
- **A que custo:** capex de 0,6% da receita; sem factoring. O custo escondido é o **SBC** (−$ 2,1 mM/ano) e o **IVA do HMRC** ($ 1,9 mM já pagos e registados como conta a receber; mais $ 1,5 mM a pagar para recorrer, que reduzem o CFO e não passam pelo resultado).

**GAAP vs non-GAAP.** O Adjusted EBITDA ($ 10,7 mM LTM, 4,8% do GB) **soma o SBC** ($ 2,1 mM) e exclui reservas legais, fiscais e regulatórias, custos de aquisições e reavaliações de investimentos. **Add-backs questionados:** o SBC é recorrente (3,5–4% da receita há três anos) — o modelo cobra-o; as reservas legais recorrem (G&A −$ 320 M no Q3 por *menos* reservas, um benefício que não se repete); as reavaliações de investimentos (−$ 1,5 mM no Q1, +$ 1,6 mM no Q2, −$ 0,5 mM no Q3) estão fora do EBIT e o EPS GAAP é inútil para valuation. O modelo usa o EBIT GAAP.

---

## 5. Investimento e retorno

**Sem ciclo de capex: capex 0,6% da receita (0,14% do GB).**

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM |
|---|---|---|---|---|---|---|
| Capex / receita | 1,7% | 0,8% | 0,6% | 0,6% | 0,6% | 0,6% |
| D&A / receita | 5,2% | 3,0% | 2,2% | 1,6% | 1,4% | 1,4% |
| SBC / receita | 6,7% | 5,6% | 5,2% | 4,1% | 3,5% | 3,7% |

O "investimento" da Uber não está no capex: está no **marketing** (S&M $ 1,6 mM no Q3, +22%), nos **incentivos** (contra-receita) e, a partir de agora, em **M&A**: Careem (consolidada a ~60% desde 31-07), Trendyol Go, ezCater ($ 2,3 mM, Out-26), Blacklane e **Delivery Hero** (~$ 15 mM a 100%). G20 não se aplica.

**ROIC — com o float fora do capital** *(perfil plataforma)*. O capital investido mede-se sobre o **capital fixo operacional** (goodwill + intangíveis + PP&E + ROU), sem caixa, sem investimentos e sem as reservas de seguros e os activos restritos que as cobrem:

| | FY2025 | LTM Set-26 |
|---|---|---|
| NOPAT | 4.396 | 5.557 |
| Goodwill + intangíveis | 9.979 | 11.947 |
| PP&E + ROU *(estimativa; CapIQ no PC)* | ~3.400 | ~3.900 |
| **Capital fixo** | **~13.400** | **~15.800** |
| **ROIC s/ capital fixo** | **~33%** | **~35%** |

**ROIC incremental:** de Dez-25 a Set-26 o NOPAT LTM subiu **+$ 1.161 M** com o capital fixo a subir **~$ 2,4 mM** (Careem e aquisições) → **ROIC marginal ~48%**, mas a descer com o M&A. **A Delivery Hero muda a conta:** a € 41,50 a Uber paga ~$ 15 mM de equity (+ ~$ 1,7 mM de dívida líquida da DH) por um adj. EBITDA de € 903 M em 2025 (1,8% do GMV; guidance 2026 € 910–960 M) e FCF de € 250 M. NOPAT da DH de ~$ 0,4 mM sobre ~$ 17 mM = **ROIC de ~2–3% no fecho** — abaixo do WACC até haver sinergias de ~$ 1 mM/ano. O ROIC consolidado cai de ~35% para ~25% no primeiro ano consolidado. É o maior teste de alocação da Uber (invalidador 6).

**De onde veio o dinheiro (9M-26):** CFO $ 7,9 mM + dívida nova $ 9,1 mM (− $ 4,0 mM reembolsados) → recompras $ 4,3 mM, DH (acções $ 2,3 mM + TRS $ 1,6 mM), aquisições $ 1,6 mM, títulos $ 1,6 mM líquidos, caixa +$ 2,5 mM. Sem emissão de acções; diluídas −3,5% YoY (2.124 → 2.050 M).

---

## 6. Balanço e estrutura de capital

| $ M, 30-Set-2026 *(10-Q)* | |
|---|---|
| Dívida (principal): notes USD 8.750 + Euro notes (Set-26, € 4,5 mM) 5.112 + convertíveis 2028 1.725 + exchangeable 2028 1.200 | 15.787 |
| Passivos tipo dívida: IVA HMRC por pagar 1.500 + NCI (Careem e outros) 1.304 + prémio da oferta DH sobre o mercado ~610 | 3.414 |
| − Caixa e investimentos de curto prazo | −10.068 |
| − Participações: DH 24,5% a mercado 3.100 + TRS 4,2% ~548 + 50% de outros investimentos de 7.975 (Didi, Grab, Aurora…) | −7.636 |
| **Dívida líquida da ponte** | **1.497** |
| *Fora da ponte (dos dois lados):* reservas de seguros 13.709 · caixa e investimentos restritos 11.372 | |

- **Revolver de $ 7,7 mM** (Ago-26, até 2031) e **term loan de € 4,0 mM** para a DH, ambos por sacar; bridge reduzido. Sem papel comercial. Primeiras maturidades: convertíveis e exchangeable em 2028 ($ 2,9 mM).
- **HMRC (IVA, Mar-2022 a Dez-2025):** liquidações de ~$ 3,4 mM (£ 2,6 mM); $ 1,9 mM pagos (conta a receber, não no resultado), $ 1,5 mM a pagar para recorrer. Na ponte só entram os $ 1,5 mM; os $ 1,9 mM são opção de recuperação (+$ 0,9/acção se a Uber ganhar).
- **Austrália:** o High Court decidiu contra a Uber em payroll tax (Nov-26) — acréscimo sem valor divulgado no 10-Q. Classificação de motoristas: risco recorrente, sem provisão quantificável.
- **Rating** e covenants: por confirmar no PC (CapIQ).

### Alocação de capital

**Fontes e usos** *($ M)*

| | FY2023 | FY2024 | FY2025 | 9M-26 |
|---|---|---|---|---|
| CFO | 3.585 | 7.137 | 10.099 | 7.852 |
| Dívida líquida nova (emissões − reembolsos) | n/d | ~0 | ~1.000 | 5.136 |
| → Capex | 223 | 242 | 336 | 239 |
| → M&A e participações (inclui DH e TRS; FY24 só participações) | n/d | 289 | 1.491 | ~6.300 |
| → **Recompras** | 0 | 1.252 | 6.523 | 4.279 |
| **Recompras / FCF do dono** | 0% | 55% | **124%** | 90% |
| *(Recompras + M&A) / FCF do dono* | — | 68% | **152%** | **~220%** |
| Dívida líquida simples (dívida − caixa e CP) | 4.880 | 3.682 | 2.888 | **5.719** |

**Ponto 5 — as recompras contra o FCF, e o "corte de 83%" do Q2.**

| | Q1-26 | Q2-26 | Q3-26 |
|---|---|---|---|
| FCF | 2.286 | 2.792 | 2.535 |
| Recompras | 3.011 | **518** *(−83% QoQ)* | 750 *(10,0 M acções)* |
| Compras de DH (acções + TRS) | — | **~3.940** | — |
| Recompras / FCF | 132% | 19% | 30% |
| (Recompras + DH) / FCF | 132% | **160%** | 30% |

O corte de 83% **não foi uma redução da devolução — foi uma troca**: o dinheiro das recompras foi para acções da Delivery Hero no mercado secundário e swaps ($ 3,9 mM no Q2; "mover depressa sobre a oportunidade", na call). Somando, o Q2 usou 160% do FCF. Desde então, recompras de $ 750 M/trimestre (~30% do FCF) e a gestão diz que volta às recompras "nos próximos meses". Autorização disponível: **$ 15,0 mM**.

**Preço médio de recompra contra o FV** *(10-Q nos 9M-26; FY2024–25 estimados pelo fecho médio de cada trimestre ponderado pelo valor recomprado, marcado como estimativa)*

| Período | Recomprado ($ M) | Preço médio | vs FV base @WACC $ 80,72 | vs ponderado $ 71,05 |
|---|---|---|---|---|
| FY2024 *(estimativa)* | 1.252 | ~$ 71 | −12% | 0% |
| FY2025 *(estimativa)* | 6.523 | ~$ 85 | +5% | +19% |
| 9M-26 *(10-Q: 56,6 M acções)* | 4.279 | **$ 75,6** | −6% | +6% |
| Q3-26 *(10-Q: 10,0 M acções)* | 750 | $ 75,0 | −7% | +6% |
| **Acumulado 2024–9M-26** | **12.054** | **~$ 80** | **~0%** | **+12%** |

*O que isto mostra:* a Uber recomprou **ao nosso fair value base**, não com desconto; contra o valor ponderado pelos robotáxis, pagou 12% a mais — destruição de valor por acção pequena se o base se confirmar, relevante se a cauda AV acontecer. O FY2025 foi o pior ano (~$ 85, 124% do FCF do dono).

**Caixa livre vs caixa operacional**

| $ M | 31-Dez-2025 | 30-Set-2026 |
|---|---|---|
| Caixa e investimentos CP | 7.633 | 10.068 |
| − Reservas de seguros não cobertas por activos restritos (13.709 − 11.372 / 12.463 − 11.416) | −1.047 | −2.337 |
| **Caixa livre** | **6.586** | **7.731** *(dos quais $ 4,0 mM em subsidiárias no estrangeiro; ~$ 5,2 mM das Euro notes para a DH)* |
| Dívida + IVA HMRC por pagar | 10.521 | 17.287 |
| **Dívida líquida ajustada** | **3.935** | **9.556** |
| / EBITDA GAAP LTM *(SBC dentro)* | 0,63x | **1,22x** |
| / adj. EBITDA LTM | 0,45x | 0,89x |

**Ponto 3 — o que muda com a Delivery Hero (66,56%) quando consolidar.**
- **Hoje:** 24,5% em equivalência patrimonial ($ 3,4 mM contabilísticos; ~$ 3,1 mM a mercado) + TRS sobre 4,2%. Os 66,56% são **direitos de compra** (24,52% já detidos + 34,63% entregues na oferta, incluindo a Prosus); a segunda janela fechou a 24-11 (resultado por publicar). Com os TRS, > 70%. **O fecho depende de aprovações de concorrência e regulatórias: 2.º semestre de 2027.**
- **Dívida:** a Uber paga em caixa ~$ 5–6 mM pelos 34,6% (+ a segunda janela), com a caixa das Euro notes já emitidas ($ 5,2 mM) e o term loan de € 4,0 mM. Consolida a dívida da DH — convertíveis de € 2,9 mM (com mudança de controlo, conversão ajustada para € 48,63 na de 2030; provável put ao par) e term loan de ~$ 1,4 mM, contra ~€ 2,7 mM de caixa pro forma: **~$ 1,7 mM líquidos**. **Dívida bruta pro forma ~$ 22–25 mM; dívida líquida ajustada ~$ 17–18 mM, ~1,4–1,6x o EBITDA combinado.**
- **Balanço:** entram goodwill e intangíveis de ~$ 13–14 mM (a base de diferença já é de $ 3,0 mM só nos 24,5%), **interesses minoritários de ~30%** da DH (e os minoritários da Talabat) e a reavaliação dos 24,5% a € 41,50 no fecho (ganho contabilístico, não económico).
- **Perímetro:** a Uber fica com a DH em 50 mercados (~$ 42 mM de GB em 2025; 14 mercados vendidos à SSW Partners por ~$ 1,6 mM, condicionado ao fecho). GB pro forma 2025: **$ 236 mM** (+22%). Mas o adj. EBITDA da DH é **1,8% do GMV** contra 4,5% da Uber: a margem consolidada cai ~0,5 pp (4,5% → ~4,0% em adj. EBITDA/GB). **Os números da Uber de 2028 não comparam com os de 2026** — os invalidadores 1, 2 e 6 passam a ler-se ex-DH até haver dois trimestres consolidados.
- **No valor desta ficha:** a DH entra a mercado (24,5% + TRS) e a compra do resto é tratada como troca de caixa por acções a preço de mercado, menos o prémio da oferta (−$ 0,61 mM, −$ 0,30/acção). Sem sinergias e sem destruição adicional. A tese da gestão (sinergias de plataforma) é opção, não base.

**Trajectória da alavancagem a 2–3 anos** *(base; recompras ao ritmo do FCF do dono; ezCater no Y1, DH no Y2; $ mM)*

| | Set-26 | Y1 *(Set-27)* | Y2 *(Set-28)* | Y3 *(Set-29)* |
|---|---|---|---|---|
| FCF do dono (FCFF do base) | 6,5 | 7,1 | 8,5 | 9,8 |
| Recompras a 100% do FCF do dono | | 7,1 | 8,5 | 9,8 |
| M&A em caixa | | 2,3 *(ezCater)* | ~6,0 *(DH)* | — |
| Dívida líquida ajustada — Uber | 9,6 | 11,9 | 17,9 | 17,9 |
| + dívida líquida da DH consolidada | | | ~1,7 | ~1,7 |
| EBITDA GAAP (base + DH a partir do Y2) | 7,8 | 9,3 | ~12,1 | ~14,0 |
| **Dívida líquida ajustada / EBITDA** | **1,22x** | **1,28x** | **~1,62x** | **~1,40x** |
| *Se as recompras voltarem a 124% (FY2025)* | | *1,46x* | *~1,93x* | *~1,84x* |

*O que isto mostra:* com a DH, a Uber passa de ~0,6x (Dez-25) para ~1,6x no fecho; se repetir 2025 nas recompras, chega a ~1,9x — perto de 2x numa empresa sem rating de topo (a confirmar) e com $ 2,9 mM a vencer em 2028. Não é um problema de solvência; é o fim da folga que justificava recomprar acima do valor ponderado.

**Stress do pior ano (2020) na estrutura de hoje.** Choque de 12 meses: Mobility −45% de GB (como em 2020), Delivery +20%; GB total ~−13%.

| $ mM | |
|---|---|
| Adj. EBITDA: Mobility ~8,9 → ~1,8 (margem 3% sobre GB a −45%); Delivery ~4,3 → ~5,2; corporate −3,0 | **~4,0** *(de 10,7)* |
| − Juros (~0,7) − impostos (~0,3) − IVA HMRC (1,5) | −2,5 |
| − Float de seguros que se inverte (sinistros pagos com menos viagens novas) | ~−2,5 |
| − Capex | −0,3 |
| **FCF no ano de stress** | **~−1,3** |
| Necessidades: FCF −1,3 + maturidades 2028 (2,9) + DH (~6,0) + ezCater (2,3) | **~12,5** |
| Fontes: caixa 10,1 + revolver 7,7 (+ term loan DH € 4,0 = 4,6) | 17,8 (22,4) |
| **Cobertura** | **1,4x (1,8x com o term loan)** |

**No valor** *(DCF: GB −15% no Y1, +20% no Y2, depois o base; margem 1,5% e 2,8% nesses anos)*: **$ 59,14 @WACC e $ 51,67 @WACC+1 pp** (−27% e −36% contra o base). A Uber aguentava um 2020 sem emitir acções — pararia as recompras, como em qualquer cenário. O risco está no **preço de mercado** (em 2020 a acção foi a $ 14–21) e em coincidir com o fecho da DH.

---

## 7. Projecções

**Topo = gross bookings, não receita** (a receita GAAP traz −8 a −9 pp de crescimento em 2026 pelo UK e mudaria outra vez com qualquer novo mercado em modelo de agente). Custos = 1 − EBITDA/GB, **SBC dentro**. Float fora (NWC = 0). Y1 = Out-26 a Set-27.

| Driver | Y1 | Y2 | Y3 | Y4 | Y5 | Y10 | Âncora (histórico · guidance · consenso) |
|---|---|---|---|---|---|---|---|
| Crescimento do GB | 17,5% | 14,0% | 12,0% | 10,5% | 9,0% | 4,0% | LTM +23%; 5 trimestres ≥ 20% cc; Q4-26 guiado +18–22% cc; Mobility com restrição de oferta. CAGR 10a 9,2% |
| EBITDA / GB *(SBC dentro)* | 3,50% | 3,67% | 3,83% | 4,00% | 4,17% | 4,50% | LTM 3,46%; Q3 2,8% (GAAP) / 3,9% (non-GAAP); segmentos FY25: Mobility 8,1%, Delivery 3,9% |
| Capex / GB | 0,15% | | | | | 0,15% | LTM 0,14% |
| Imposto | 21% | 21% | 22% | 23% | 24% | 24% | NOL federal de $ 4,1 mM ilimitado |
| Float / NWC | 0 | | | | | 0 | Fora do FCF, por construção |

| $ M | Y1 | Y2 | Y3 | Y4 | Y5 | Y10 |
|---|---|---|---|---|---|---|
| Gross bookings | 265.199 | 302.326 | 338.606 | 374.159 | 407.834 | 545.531 |
| EBITDA | 9.282 | 11.085 | 12.980 | 14.966 | 16.993 | 24.549 |
| Capex | 398 | 453 | 508 | 561 | 612 | 818 |
| **FCFF** *(= FCF do dono)* | **7.089** | **8.482** | **9.830** | **11.073** | **12.431** | **18.023** |
| ROIC s/ capital fixo *(standalone, sem M&A)* | ~43% | | | | ~70% | |

**Onde diverge, e porquê:** o Y1 fica abaixo do guidance do Q4 (17,5% vs ≥ 18%) e o fade é rápido (4% no Y10) — Mobility com oferta apertada e a entrada dos robotáxis em cidades onde a Uber não é a app. A margem sobe só 1 pp em dez anos, abaixo do que a estrutura de segmentos permite (o favorável vai a 5,5%). **Coerência:** a alavanca operacional é modesta (EBITDA/GB +0,1–0,17 pp/ano contra +1 pp/ano em 2023–25). **G15** *(04_reversao.py)*: crescimento conservador contra o facto (Y1 18%: +3,9% no valor), capex conservador (+0,25%), margem em linha com a âncora provisória — **OK, abaixo de 5%**. G20/G21 não se aplicam.

---

## 8. Métricas do sector e múltiplos

**As métricas certas para a UBER:**
- **FCF yield do dono** (SBC e float fora) — a única que trata as duas distorções do FCF reportado.
- **EV / EBITDA GAAP** (SBC dentro) — o adj. EBITDA soma $ 2,1 mM de SBC e não é comparável com o modelo.
- **EV / gross bookings** e **EBITDA / GB** só como contexto contra Lyft e DoorDash (definições de GB/GOV diferentes).

| Múltiplo | UBER hoje | Lyft | DoorDash |
|---|---|---|---|
| EV / EBITDA GAAP LTM | 17,7x | n/s | — |
| EV / adj. EBITDA LTM · NTM (Y1 do modelo, GAAP) | 12,9x · 14,9x | — | — |
| P / E forward | ~17x *(TIKR, Nov-26)* | n/s | ~70x LTM *(Trefis, 16-11)* |
| FCF yield LTM · do dono | 7,6% · 4,8% | ~18% *(FCF LTM $ 1,1 mM / market cap $ 6,2 mM, Trefis 14-10)* | — |
| Adj. EBITDA / GB (Q3-26) | 5,0% | 3,6% | 3,1% |
| EV / GB LTM | 0,61x | — | — |

*EV de mercado $ 138,1 mM (market cap $ 136,6 mM + dívida líquida da ponte). Pares da web, datas diferentes — contexto, não âncora (Comps do CapIQ no PC). Sem mediana própria fiável: a Uber só tem EBITDA positivo desde 2023; market cap/FCF ~18x no fim de 2024 e de 2025 (estimativa).*

**Leitura:** a Uber negocia a ~13x adj. EBITDA e ~17x lucro com o GB a +20% — o desconto contra a DoorDash não é de margem (a Uber tem mais), é de **duração**: o mercado não acredita que a Mobility sobreviva aos robotáxis na forma actual. O FCF yield do dono (4,8%) é o número honesto: não é barato sem a tese.

---

## 9. Custo de capital

| Componente | Valor | Fonte e porquê |
|---|---|---|
| Rf | 4,94% | UST 10Y a 27-11-2026 (portal, ^TNX; Treasury.gov inacessível desta sessão — confirmar no PC) |
| ERP | 5,0% | Kroll (regra da carteira) |
| CRP | 0 | Regra da carteira: só com exposição material a emergentes; a Uber é diversificada (EUA e Canadá, Europa, LatAm, APAC) — a confirmar com a geografia do 10-K no PC |
| β desalavancado | **1,15** | Regra de 27-11 (sector ambíguo → governa o mais conservador): 50% Transportation 0,71 + 50% Software (Internet) 1,59, Damodaran US Jan-2026. Sensibilidade: Transportation 0,71 |
| β realavancado | 1,25 | D/E de mercado 11,6% (dívida $ 15,8 mM / market cap $ 136,6 mM), imposto 24% |
| **Ke** | **11,19%** | 4,94% + 1,25 × 5,0% |
| Kd (depois de imposto) | 5,0% (3,80%) | Notes USD a 4,15–5,35%; Euro notes 3,75–5,25% |
| Pesos | 90% equity / 10% dívida | De mercado |
| **WACC** | **10,43%** | |
| **Required** | **11,43%** | Nível 2 (WACC + 100 bp): FCF positivo e crescente desde 2023, alocação de capital em teste (DH). **Não sobe para nível 3 pelo risco AV**: esse risco está nos quatro cenários com probabilidade; cobrá-lo também no hurdle seria duplo prémio |

**Prémios aplicados**

| Prémio | Aplicado? | Valor | Risco que cobre | Sobrepõe-se a outro? |
|---|---|---|---|---|
| CRP | Não | 0 | — | — |
| Hurdle (nível 2) | Sim | +100 bp | Execução da DH, alocação de capital, regulação laboral | Não |
| Fade terminal abaixo da âncora | Não | Margem Y10 = âncora provisória (4,5%) | — | Não |
| Cenários AV (profundo adverso + adverso, 35%) | Sim | no ponderado | Desintermediação pelos robotáxis | Não — fora do hurdle de propósito |

**Com β 0,71 (Transportation):** WACC 8,28%, fair value **$ 113,54** (+70%). **Com β 1,59 (Software puro):** WACC 12,57%, $ 62,07. A escolha do beta vale ±$ 30 — mais do que qualquer driver menos o crescimento. Por isso a decisão ancora-se no retorno implícito, que não depende do beta.

---

## 10. Valuation

**Ponto 4 — os quatro cenários de robotáxis** *(probabilidades declaradas antes dos valores, as do ER de 16-10: 10 / 25 / 45 / 20)*

| Cenário | p | A história | GB CAGR 10a | EBITDA/GB Y10 | @WACC | @required | IRR ao preço |
|---|---|---|---|---|---|---|---|
| **Profundo adverso — um vencedor fora da Uber** | 10% | Uma stack (Tesla ou Waymo) ganha escala com app própria nas 20 maiores cidades; a Mobility da Uber encolhe a partir de 2029 e fica com o resto do mundo e o Delivery | 0,5% *(GB −4/−5% em 2030–31)* | 1,8% | **$ 21,47** | $ 19,67 | 4,49% |
| **Adverso — duopólio integrado** | 25% | Waymo e Tesla verticalizadas nos EUA; a Uber agrega o resto das frotas a take rate mais baixo; crescimento a 3–5% depois de 2029 | 5,6% | 3,0% | **$ 43,24** | $ 38,53 | 7,59% |
| **Base — oligopólio em camadas** | 45% | A Waymo directa nas melhores cidades; as restantes stacks (Nuro/Lucid, WeRide, Pony, May, Avride…) e os humanos na Uber; margem a subir com a escala | 9,2% | 4,5% | **$ 80,72** | **$ 70,89** | **11,94%** |
| **Favorável — stacks licenciáveis** | 20% | O software de condução comoditiza-se; a procura agregada e a utilização da frota valem mais do que a condução; a Uber é o sistema operativo das frotas | 10,8% | 5,5% | **$ 108,87** | $ 95,05 | 14,62% |
| **Ponderado** | | | | | **$ 71,05** | **$ 62,51** | **10,91%** |
| *Stress aritmético* | — | GB −5 pp/ano, margem −1 pp, WACC +1 pp | 4% | 3,5% | *$ 37,49 (−44%)* | | |

*Comparação com o ER de 16-10 ($ 16 / $ 35 / $ 86 / $ 126; ponderado $ 74):* o base aqui é $ 5 mais baixo (g 2,5% em vez de 3%; IVA HMRC e prémio da DH na ponte) e as caudas são menos fundas ($ 21 e $ 43 contra $ 16 e $ 35) porque o Delivery (48% do GB) fica de pé em todos os cenários. Ponderado **$ 71 contra $ 74**.

**O teste de Austin/Atlanta.** É o primeiro dado limpo sobre qual cenário está a acontecer:
- **O facto:** a exclusividade da Waymo na Uber nessas duas cidades acaba em **Jan-2028**; a frota actual fica na app da Uber pelo menos até **Mai-2028** (fim do contrato) e "enquanto as duas quiserem"; a Uber fica livre para pôr outros AV nessas cidades. A Waymo recusou uma opção dedicada de robotáxi dentro da app da Uber.
- **O que distingue os cenários:** no **base**, a Uber mantém o GB de Mobility nessas cidades a crescer perto da média dos EUA e mete lá outra frota AV em 2028; no **adverso**, o GB da Uber em Austin/Atlanta cresce > 5 pp abaixo da média dos EUA nos dois trimestres seguintes e a Waymo tira a frota em Mai-2028; no **profundo adverso**, o mesmo acontece em Phoenix, São Francisco e Los Angeles (onde a Waymo já tem app própria) e a Tesla escala em app própria.
- **Como se lê:** a Uber não divulga GB por cidade. Lê-se nos comentários da call (Q1-28, ~Mai-2028), nos dados de painel de cartões e na contagem de veículos AV na app. **Antes disso**, o sinal antecipado é o número de veículos AV de terceiros na Uber (700 no fim de 2026; > 2.000 prometidos para 2027): se ficar abaixo de 2.000 em 2027, sobe o peso do adverso.

**Peso do terminal:** 54% do EV no base (47% no adverso). EV/EBITDA de saída implícito no ano 5: 11,1x (abaixo dos 14,9x NTM de hoje — o valor não depende de re-rating).

**Ponte EV → equity:** EV $ 166.973 M − dívida $ 15.787 M − passivos tipo dívida $ 3.414 M + caixa $ 10.068 M + participações $ 7.636 M = equity $ 165.476 M ÷ 2.050 M acções = **$ 80,72**.

**Reverse DCF** *(motores A e B, G12 verde)*

| | Valor |
|---|---|
| **Retorno que o preço oferece** (motor A) | **11,94%** no base · **10,91%** no ponderado · 7,59% no adverso |
| Crescimento do GB que o preço exige para render o WACC · o required (motor B) | **6,6%** · 8,4% ao ano durante 10 anos *(base 9,2%; 2023–25 +19%)* |
| EBITDA/GB do Y10 que o preço implica (crescimento do base) | **3,78%** @WACC · 4,25% @required *(LTM 3,46%)* |
| Capex do Y10 que o preço implica | 0,8% do GB *(hoje 0,14%)* |

**Em números falsificáveis — o Y4 (Set-2030) que o preço exige para render 11,43%:** GB $ 366,5 mM (base $ 374,2 mM), EBITDA $ 14,66 mM ($ 14,97 mM), FCFF $ 10,85 mM ($ 11,07 mM), NOPAT por acção $ 5,33 ($ 5,44). **Ou seja: o preço de hoje exige quase o nosso base para render o required — a margem de segurança está no base contra o ponderado, e esta é negativa.**

**Ponte do fair value face à revisão anterior**

| | FV base | Δ | Porquê |
|---|---|---|---|
| Ficha de 29-10 *(config gravado: receita × margem, β 0,75)* | $ 129,40 | | Margem EBITDA 22% da receita sem SBC nem float; sem programa AV |
| Ficha de 23-11 *(ER adoptado, β 1,24 → regime único 1,15; sem config)* | $ 86 (~$ 91 com o Q3, estimativa) | −$ 38 a −$ 43 | SBC cobrado, float retirado, AV, beta |
| **Esta ficha** *(GB × margem, β 1,15, g 2,5%)* | **$ 80,72** | −$ 5 a −$ 10 | g 3,0% → 2,5% (−$ 3,2); IVA HMRC (−$ 0,73); prémio DH (−$ 0,30); participações a 50% (+$ 3,7); margem e crescimento próprios (resto) |

*O 08_ponte.py fecha ao cêntimo contra o config de 29-10, mas a decomposição não tem leitura: o topo do modelo mudou de receita para GB (o passo "receita LTM" sozinho vale +$ 418). A mudança é de método, e está escrita aqui.*

---

## 11. Sensibilidades

**Tornado (G13)** *(bandas definidas antes: crescimento ±3 pp, EBITDA/GB ±0,5 pp, capex −0,05/+0,15 pp, imposto ±3 pp, NWC ±2 pp, WACC ±1 pp, g ±0,5 pp)*

| Driver | Favorável | Adverso | Amplitude |
|---|---|---|---|
| **Crescimento do GB** | $ 100,50 | $ 64,86 | **$ 35,64** |
| WACC *(taxa)* | $ 93,45 | $ 70,89 | $ 22,56 |
| **EBITDA / GB** | $ 90,47 | $ 70,96 | **$ 19,51** |
| Imposto | $ 83,91 | $ 77,53 | $ 6,38 |
| Float / NWC | $ 83,82 | $ 77,62 | $ 6,20 |
| g perpétuo *(taxa)* | $ 83,93 | $ 77,88 | $ 6,05 |
| Capex / GB | $ 81,74 | $ 77,67 | $ 4,07 |
| Vida do capex novo | $ 80,68 | $ 80,76 | ~0 |

**Os dois dominantes — CAGR do GB × EBITDA/GB do Y10** *(@WACC; ▼ abaixo do preço de $ 66,63)*

| CAGR 10a ＼ EBITDA/GB Y10 | 3,5% | 4,0% | **4,5%** | 5,0% | 5,5% |
|---|---|---|---|---|---|
| 6,2% | ▼ $ 52,3 | ▼ $ 58,6 | ▼ $ 64,9 | $ 71,1 | $ 77,4 |
| 7,7% | ▼ $ 58,1 | ▼ $ 65,2 | $ 72,3 | $ 79,5 | $ 86,6 |
| **9,2%** | ▼ $ 64,7 | $ 72,7 | **$ 80,7** | $ 88,7 | $ 96,8 |
| 10,7% | $ 72,0 | $ 81,0 | $ 90,1 | $ 99,1 | $ 108,2 |
| 12,2% | $ 80,1 | $ 90,3 | $ 100,5 | $ 110,7 | $ 120,9 |

**WACC × g**

| WACC ＼ g | 1,5% | 2,0% | **2,5%** | 3,0% | 3,5% |
|---|---|---|---|---|---|
| 9,43% | $ 86,0 | $ 89,5 | $ 93,5 | $ 98,0 | $ 103,4 |
| **10,43%** | $ 75,4 | $ 77,9 | **$ 80,7** | $ 83,9 | $ 87,6 |
| 11,43% | $ 66,9 | $ 68,8 | $ 70,9 | $ 73,2 | $ 75,8 |

**O que move o valor:** o crescimento do GB (cada 1 pp/ano vale ~$ 6), depois a margem (cada 0,1 pp de EBITDA/GB no Y10 vale ~$ 1,6) e a taxa (o beta sozinho vale ±$ 30). Os robotáxis mexem nos dois primeiros ao mesmo tempo — por isso os cenários e não o tornado são a ferramenta de decisão.

**Se comprar a X, ganho quanto?** *(base e ponderado, sem re-rating)*

| Preço | IRR do base | IRR do ponderado | vs required 11,43% |
|---|---|---|---|
| $ 66,63 *(hoje)* | 11,94% | 10,91% | ponderado −52 bp |
| $ 62,51 *(1.ª tranche)* | 12,51% | 11,43% | = required |
| **$ 60,00** *(ordem do plano)* | **12,88%** | **11,77%** | **+34 bp** |
| $ 57,30 *(cheia)* | 13,33% | 12,17% | +74 bp |

A 5 anos, com o preço a convergir para o fair value do base (saída implícita a 11,1x EV/EBITDA, abaixo dos 14,9x NTM de hoje): 14,7% anualizado ao preço de hoje (06_retorno.py). A 8,9x de saída, 10,9%.

---

## 12. Decisão

**Esperar. A ordem do plano a ≤ $ 60 continua certa.**

| Degrau | Preço | Regra | Assimetria fav:adv @WACC |
|---|---|---|---|
| Hoje | $ 66,63 | IRR 11,94% no base, 10,91% no ponderado; 7,59% no adverso | 1,81x |
| **1.ª tranche** | **< $ 62,51** | O ponderado dos quatro cenários rende o required (11,43%) | 2,41x |
| 2.ª tranche | por informação | Recompras de volta a ≤ 100% do FCF do dono **e** ≥ 2.000 AV de terceiros na app em 2027, **ou** o teste de Austin/Atlanta a favor do base | — |
| **Posição cheia** | **< $ 57,30** | O base com o crescimento −3 pp/ano (driver dominante do G13) rende o required | 3,67x |

- **Ponto 6 — os $ 60.** Com a ficha nova, a 1.ª tranche é **$ 62,51** (ponderado @required). **$ 60 fica 4% abaixo**: rende 11,8% no ponderado e 12,9% no base. Mantém-se — a folga cobre o IVA do HMRC, o payroll tax australiano sem valor e o risco de o Q4 confirmar a margem GAAP de 2,8%. Subir a ordem para ~$ 62 seria defensável, mas não há razão para o fazer antes do Q4 (~02-02-2027), e a regra da casa é evitar comprar antes de resultados.
- **Desvio declarado ao 07_cenarios.py:** o script troca a escada (ponderado abaixo do base) e põe a 1.ª tranche no **base @required ($ 70,89)** — acima do preço, o que daria "comprar já". Não se aplica aqui: com 35% da probabilidade em cenários −35% a −70%, o base não é o critério de decisão sob incerteza; o ponderado é (required-return.md). A escada desce sem a troca: $ 62,51 → $ 57,30. *(Proposta ao método: a troca só quando a distância entre base e ponderado for < 5%.)*
- **Peso máximo: 3%** da carteira — pela regra (2% de perda / adverso @WACC+1 pp, −42%) daria 4,7%; com o profundo adverso @WACC+1 pp (−70%) dá 2,8%. Governa o mais conservador porque o profundo é um cenário nomeado com 10%. Hoje 1,9%; a ordem de $ 700 cabe.
- **Régua de compra (plano v3.2):** índice 8% + 250 bp = 10,5%. Hoje o ponderado rende 10,91% → passa por 41 bp; o base passa por 144 bp. Mas a régua é o mínimo, e a ficha exige o required (11,43%) no ponderado — que só se cumpre abaixo de $ 62,51.
- **Regra de venda aplicada:** (1) tese partida? Não — nenhum invalidador disparou; quatro em vigilância. (2) acima do tecto? Não (1,9% contra 15%). (3) overvalued? Não — preço abaixo do favorável @WACC ($ 108,87) e retorno 11,94% > 8%. **Manter a posição; não vender.**

**Invalidadores** *(revistos 28-11-2026; o 6 é novo)*

| # | Afirmação | Invalidador observável | Onde | Estado |
|---|---|---|---|---|
| 1 | O compounding continua | GB abaixo de 15% cc dois trimestres seguidos (ex-DH depois do fecho) | ER | OK — 20% no Q3; Q4 guiado 18–22% |
| 2 | A margem sobe | EBITDA GAAP / GB (SBC dentro) abaixo de 3,0% dois trimestres seguidos, **ou** non-GAAP op. income / GB abaixo de 3,5% | 10-Q / ER | **Em vigilância** — Q3 2,8% GAAP (1 de 2); non-GAAP 3,9% |
| 3 | A Uber capta a procura AV (principal) | Austin/Atlanta: GB da Uber > 5 pp abaixo da média dos EUA dois trimestres após Jan-2028, **ou** < 2.000 AV de terceiros na app no fim de 2027 | Call / ER | **Em vigilância** — Waymo sai da exclusividade; Phoenix separada |
| 4 | O capital é bem alocado | Recompras > 100% do FCF do dono dois anos seguidos **com** preço médio acima do ponderado, ou (recompras + M&A) > 150% do FCF do dono dois anos com dívida líquida ajustada > 1,5x | 10-Q / 10-K | **Em vigilância** — FY25 124% a ~$ 85; 2026 ~220% com a DH; alavancagem 1,22x |
| 5 | Mobility monetiza | Receita de Mobility pro forma (ex-UK) a crescer > 5 pp abaixo do GB mais dois trimestres | 10-Q | **Em vigilância** — Q3 +12% vs +18% (6 pp) |
| 6 | A DH paga o custo de capital | Adj. EBITDA / GMV da DH abaixo de 2,5% em 2028, **ou** dívida líquida ajustada / EBITDA > 2,0x dois trimestres depois do fecho | 10-Q pós-fecho | Por saber (fecho no 2.º semestre de 2027) |

**Catalisadores com data:** 09-12 FOMC (não comprar nesse dia) · 10-12 CPI · fecho da ezCater (Q4-26/Q1-27) · **~02-02-2027 resultados Q4-26** (margem GAAP, recompras, guidance FY27) · Q1-27 (o UK sai da comparação de receita) · recurso do IVA no Reino Unido (sem data) · fecho da DH no 2.º semestre de 2027 · **Jan-2028 fim da exclusividade da Waymo em Austin/Atlanta; Mai-2028 fim do contrato** · 2028 maturidades de $ 2,9 mM.

---

## A. Séries completas e reconciliações

**Trimestres** *($ M; SEC EDGAR e ERs)*

| | Q4-24 | Q1-25 | Q2-25 | Q3-25 | Q4-25 | Q1-26 | Q2-26 | Q3-26 |
|---|---|---|---|---|---|---|---|---|
| Gross bookings | 44.197 | 42.818 | 46.756 | 49.740 | 54.140 | 53.720 | 58.022 | 59.819 |
| Receita | 11.959 | 11.533 | 12.651 | 13.467 | 14.366 | 13.203 | 14.191 | 14.766 |
| EBIT GAAP | 770 | 1.228 | 1.450 | 1.113 | 1.774 | 1.923 | 1.890 | 1.447 |
| EBITDA GAAP / GB | 2,13% | 3,27% | 3,48% | 2,62% | 3,62% | 3,92% | 3,58% | 2,77% |
| Adj. EBITDA | 1.842 | ~1.870 | 2.119 | 2.258 | ~2.490 | ~2.470 | 2.819 | 2.960 |
| SBC | 419 | 435 | 475 | 465 | 451 | 473 | 556 | 594 |
| CFO | 1.750 | 2.324 | 2.564 | 2.328 | 2.883 | 2.351 | 2.862 | 2.639 |
| FCF | 1.706 | 2.250 | 2.475 | 2.230 | 2.808 | 2.286 | 2.792 | 2.535 |
| Recompras | 555 | 1.785 | 1.363 | 1.463 | 1.912 | 3.011 | 518 | 750 |
| Caixa (fim) | 5.893 | 5.132 | 6.438 | 8.432 | 7.105 | 5.558 | 4.870 | 9.558 |
| Dívida LP (fim) | 9.575 | 8.350 | 9.578 | 10.615 | 10.521 | 10.514 | 12.723 | 15.664 |
| Acções diluídas (M) | — | 2.123 | 2.126 | 2.124 | — | 2.071 | 2.050 | 2.050 |

*~ = estimativa (Q1-25 e Q1-26 do guidance e do non-GAAP op. income; Q4-25 do crescimento de 35% anunciado). Confirmar no CapIQ.*

**Reconciliação do non-GAAP do Q3-26:** EBIT GAAP 1.447 + SBC 594 + outros (aquisições, reservas legais, amortização de intangíveis adquiridos) ~259 = non-GAAP op. income ~2.300; + D&A non-GAAP ~660 = adj. EBITDA 2.960. Segmentos: Mobility 2.362 + Delivery 1.057 − Freight 33 = 3.386; corporate G&A e Platform R&D ~−1.090.

**Mobility pro forma do UK:** Q3-26 7.520 + 1.100 = 8.620 (+12,2% vs 7.682); 9M-26 21.681 + 3.200 = 24.881 (+15,9% vs 21.466).

## B. Gráficos de suporte

As tabelas das secções 2, 4, 6 e 11 substituem os gráficos nesta versão. O `UBER_DCF.xlsx` traz a cascata (`Projecoes`), a grelha viva (`Cenarios`) e os motores (`Reverse`). Os quatro cenários AV foram calculados com a réplica do modelo (`modelo_calc`, mesma mecânica do Excel); o Excel só tem três (o adverso a 35% junta o profundo) — ver G.

## C. SWOT e legal, regulatório e fiscal

**Forças:** escala (215 M de MAPCs, 4,1 mM de viagens/trimestre); duas linhas de negócio do tamanho uma da outra; margem de segmento acima dos pares; Uber One; FCF do dono de $ 6,5 mM. **Fraquezas:** FCF reportado inflacionado por SBC e float; GAAP ruidoso (reavaliações); take rate de Mobility a comprar oferta; recompras ao fair value, não abaixo. **Oportunidades:** agregação de frotas AV de terceiros; publicidade; DH (100 mercados, quase o dobro com Mobility e Delivery); viagens (Expedia, Blacklane). **Ameaças:** robotáxis com app própria (Waymo, Tesla, Zoox); classificação laboral; IVA/impostos sobre plataformas; integração e preço da DH; aeroportos (15% do GB de Mobility).

| Matéria | Estado | Exposição | Na ponte |
|---|---|---|---|
| IVA HMRC (UK, Mar-22 a Dez-25) | Liquidações de ~$ 3,4 mM; $ 1,9 mM pagos (a receber), $ 1,5 mM a pagar para recorrer | $ 3,4 mM | $ 1.500 M |
| Payroll tax Austrália | High Court contra a Uber (Nov-26); acréscimo sem valor divulgado | n/d | — |
| Classificação de motoristas (vários países) | Recorrente; pode mudar a apresentação da receita e do custo | n/d | — |
| Concorrência — DH | Aprovações de fusão pendentes; venda de 14 mercados à SSW | Remédios | Prémio $ 610 M |

**Fiscal:** NOL federal de $ 4,1 mM sem prazo e estaduais de $ 7,0 mM (10-Q); taxa de 21% nos Y1–Y2, 24% depois.

## D. Sentimento

- **Sell-side:** PT médio **$ 100,77** (24/7 Wall St, 09-11-2026); intervalo $ 82–150 (Evercore ISI $ 150; Goldman Sachs Buy $ 110, 05-11). FV / PT = **0,80**. EPS normalizado de consenso: FY25 $ 2,45 → FY28 $ 5,51 (TIKR); FY27 revisto ligeiramente em baixa em três meses. Consenso Q4-26 EPS $ 1,02 (chartmill) contra guidance $ 0,95–0,99.
- **Reacção aos resultados:** de $ 69,87 (04-11) ao mínimo de 52 semanas de $ 63,47 (20-11); −20% no ano, −33% do máximo ($ 100,10, 06-10-2025). Os agregadores leram o Q3 como "falha de 75% no EPS" por compararem o EPS GAAP ($ 0,25, com −$ 476 M de reavaliações) com o consenso non-GAAP ($ 0,87–0,94).
- **Insiders e short interest:** n/d nesta revisão (CapIQ no PC).

## E. Log de fair value e decisões

| Data | Preço | FV base | Ponderado | IRR implícita | Decisão |
|---|---|---|---|---|---|
| 29-10-2026 | $ 65,74 | $ 129,40 | — | 13,7% | Entrada faseada |
| 23-11-2026 | $ 63,47 | $ 86 (~$ 91 com Q3) | $ 74 | ~13,0% | Manter; reforço a ~$ 60 ou por informação |
| **28-11-2026** | **$ 66,63** | **$ 80,72** | **$ 71,05 · $ 62,51 @req** | **11,94% · 10,91% ponderado** | **Esperar; T1 a ≤ $ 60 mantém-se; cheia < $ 57,30; peso máx. 3%** |

## F. Changelog

**28-11-2026 — ficha refeita no template v6 (perfil plataforma).** A versão de 23-11 vai para `_arquivo/UBER_Ficha_20261123.md`; o config de 29-10 para `_arquivo/config_UBER_20261029b.json`. Mudanças:
- **Estrutura:** secções 0–12 do v6; histórico FY2017–LTM com 2019–2020; alocação de capital com os quatro testes.
- **Modelo:** novo `config_UBER.json` e `UBER_DCF.xlsx` (pipeline v2.2, citável). **Topo = gross bookings** e custos = 1 − EBITDA/GB com SBC dentro; float de seguros fora (NWC 0; reservas e activos restritos fora da ponte). IVA HMRC, NCI e prémio da DH na ponte; participações a mercado (DH) e a 50% (resto).
- **Conclusões novas:** (1) a receita de Mobility −2% é o UK em modelo de agente (−$ 1,1 mM, efeito zero no EBIT) mais ~6 pp de take rate a comprar oferta; (2) FCF do dono $ 6,5 mM = 62% do FCF reportado; (3) DH: dívida líquida ajustada para ~1,6x no fecho, margem consolidada −0,5 pp, ROIC da compra ~2–3% sem sinergias; (4) quatro cenários $ 21 / $ 43 / $ 81 / $ 109, ponderado $ 71; (5) o corte de 83% nas recompras foi troca por acções da DH (Q2 a 160% do FCF); recompras acumuladas a ~$ 80, ao FV base e 12% acima do ponderado; (6) **$ 60 confirmado** (1.ª tranche $ 62,51).
- **Invalidadores:** 2 redefinido para a margem GAAP; 4 redefinido (preço médio vs ponderado; M&A); 5 pro forma do UK; 6 novo (DH).

## G. Notas de método e gates

| Gate | Estado |
|---|---|
| G1 GAAP vs non-GAAP | OK — modelo sobre EBIT GAAP (SBC dentro); adj. EBITDA só para comparar com pares |
| G2 Share count | 2.050 M diluídas (Q3-26); capa 2.041,9 M a 30-10 |
| G12 | **Verde** — 02_motores_reverse e verificar_xlsx OK; ponte fecha ao cêntimo |
| G13 | Crescimento ($ 35,64) e margem ($ 19,51) são os eixos |
| G15 | OK — +3,9% contra o facto (Y1 18% do guidance) e +0,25% no capex; margem contra **âncora provisória** (estrutura de segmentos; pares abaixo) até aos Comps do CapIQ |
| G17 | OK — fecho de 27-11 posterior ao 10-Q (04-11) e ao anúncio da DH (10-11) |
| G18 | Topo do modelo = GB (a receita tem a mudança do UK); dívida = principal da nota do 10-Q |
| G19 | Método C; **Rf a confirmar**: UST 10Y 4,94% do portal; o `custo_capital.py` não chegou ao Treasury.gov desta sessão — usou-se a regra do pedido do Hugo (Rf à data do último fecho verificado) |
| Cenários | O Excel (07) tem três cenários (adverso a 35% junta o profundo; ponderado do Excel $ 73,23). **A decisão usa os quatro** calculados com `modelo_calc` (ponderado $ 71,05 / $ 62,51) |
| Escada | Desvio ao 07: sem a troca base/ponderado (ver secção 12) |
| Calibração | FV / PT 0,80 |

*Fontes:* [10-Q Q3-26 (SEC)](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000041/uber-20260930.htm) · [10-K FY2025 (SEC)](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm) · [10-K FY2024 (SEC)](https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/uber-20241231.htm) · [10-K FY2023 (SEC)](https://www.sec.gov/Archives/edgar/data/1543151/000154315124000012/uber-20231231.htm) · [ER Q3-26](https://investingnews.com/uber-announces-results-for-third-quarter-2026/) · [ER Q2-26](https://www.barchart.com/story/news/3659266/uber-announces-results-for-second-quarter-2026) · [ER Q1-26](https://www.businesswire.com/news/home/20260506718774/en/Uber-Announces-Results-for-First-Quarter-2026) · [Börsen-Zeitung — DH 66,56%](https://www.boersen-zeitung.de/unternehmen-branchen/uber-sichert-sich-zwei-drittel-der-anteile-an-delivery-hero-2) · [The Next Web — Waymo Austin/Atlanta](https://thenextweb.com/news/waymo-uber-exclusivity-ends-austin-atlanta-robotaxi) · [Delivery Hero FY2025](https://ir-api.eqs.com//media/document/9e289f1f-e210-4e7d-bc0e-77c3f86814ee/assets/Delivery_Hero_FY_2025_Results.pdf) · [DoorDash 10-Q Q3-26](https://www.sec.gov/Archives/edgar/data/0001792789/000179278926000070/dash-20260930.htm) · [Lyft 8-K Q3-26](https://www.sec.gov/Archives/edgar/data/0001759509/000162828026071043/lyft-20260930xpressrelease.htm) · [24/7 Wall St — PT](https://247wallst.com/investing/2026/11/09/wall-street-sees-more-than-100-for-uber-the-stock-is-under-70/) · [TIKR — consenso](https://www.tikr.com/blog/could-uber-actually-climb-61-or-is-goldman-sachs-totally-wrong)
