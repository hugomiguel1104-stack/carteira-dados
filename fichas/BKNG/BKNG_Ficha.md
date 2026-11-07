# Ficha de Empresa — Booking Holdings (BKNG · NasdaqGS)

> **Documento único e vivo.** Não se cria cópia por trimestre — actualiza-se este.
> **Secções 1–7:** estrutura. Escritas uma vez, revistas anualmente ou quando um invalidador dispara.
> **Blocos A–D:** infraestrutura. Actualizados a cada análise trimestral.
> Todo o número de valuation lê-se de uma célula do `BKNG_DCF.xlsx` (G12). Recalculado no Excel a 23-Out-2026 e, com o custo de capital novo, a 30-Out-2026.
> **Revisão de 30-10-2026 — regra de custo de capital da carteira** (Rf UST 10Y à data do preço, ERP do estudo Kroll mais recente, CRP só se relevante): ERP 4,5% → 5,0%. Actualizados o ESTADO, o capítulo REVERSE DCF (novo), o log e o changelog. **O sumário executivo e a §7 continuam a ERP 4,5%** (versão de 23-10 em `_arquivo\BKNG_Ficha_20261023.md`).

`Criada:` 23-Out-2026 · `Última revisão estrutural:` 23-Out-2026 · `Último quarter processado:` Q2-2026

---

## ESTADO

| | | | |
|---|---|---|---|
| **Preço** | $ 161,10 | **Data** | 22-10-2026 *(fecho; CapIQ export de 23-Out)* |
| **Market cap** | $ 121.469 M *(754 M acções diluídas)* | **EV** | $ 125.357 M *(inclui $ 1.070 M de contingências regulatórias)* |
| **Valor DCF** *(base, ao WACC de 9,09%)* | **$ 236,03** | **Upside** | +46,5% |
| **Fair value ao required return de 10,08%** | $ 203,62 *(+26,4%)* | **Valor esperado ponderado** | $ 227,26 @WACC · $ 196,20 @required |
| **Amplitude bull–bear** *(2 eixos)* | $ 200,62 a $ 277,11 | **Drivers dominantes** | Crescimento da receita · cash opex |
| **IRR implícita** *(reverse DCF, motor A)* | **11,97%** | **vs required return** | spread **+189 bp** vs 10,08%; +289 bp vs WACC |
| **Growth implícito** *(@ required return)* | CAGR receita **3,43%** a 10 anos | **vs CAGR histórico** | 10,2% FY19-25 · 12,2% FY23-25 · consenso FY25-30 8,6% |
| **Decisão** | **Entrada faseada — T1 e T2 abertas; T3 condicionada a Q3-26** | **Gates** | 1ª tranche < $ 203,62 · 2ª tranche < $ 173,85 · cheia < $ 159,66 *(30-10: a cheia passou para baixo do preço)* |
| **Invalidadores disparados** | 0 de 7 · 2 em vigilância | **Último report** | Q2-2026 (04-Ago-2026) |
| **ROIC marginal** *(sobre o capital deployado)* | não definido — NOPAT +$ 3.260 M FY22→FY25 com capital fixo a **cair** $ 356 M | **vs WACC** | ROIC s/ capital fixo 121% LTM; capital investido total **negativo** |
| **Próximo catalisador** | Resultados Q3-26 a 03-11-2026 (pós-mercado) · FTC/Priceline · DSA UE | **O que decide** | Room nights ≥ 3% e marketing/GB ≤ 5,0% |
| **Consenso sell-side** | PT médio $ 233 (n=35, mín. $ 170) | **vs o meu DCF** | DCF @WACC 1,3% acima; @required 12,6% abaixo · FV/PT 1,01 |
| **Ke** *(regra da carteira: Rf UST 10Y + ERP Kroll; CRP 0)* | 9,90% *(4,96% + 0,987 × 5,0%)* · WACC 9,09% | **Ke ±100 bp** | $ 272,99 / $ 207,63 por acção |
| **Peers** *(múltiplo âncora)* | P/E NTM 14,5x | **vs pares maduros** | EXPE ~8-9x EV/EBITDA LTM · ABNB 33x P/E fwd |
| **Short interest** | n/d — sem export Charting | **vs mediana 5 anos** | n/d |
| **Posição actual** | — | **% da carteira** | — |

**Múltiplos-chave** — os que decidem *nesta* empresa. Justificação na §7.

| Múltiplo | Actual | Mediana 3 anos | vs mediana | Leitura |
|---|---|---|---|---|
| P/NTM EPS *(âncora, forward)* | 14,5x | 21,3x | −32% | Mínimo de 5 anos. Mas a mediana formou-se com o UST 10Y a ~4%, não a 5% |
| TEV/NTM EBITDA *(forward)* | 11,0x | 16,4x | −33% | EBITDA na mesma base que o modelo (o Adj. EBITDA não soma SBC) |
| Market cap / LTM levered FCF | 15,7x | 21,3x | −26% | FCF yield de 6,4% para um negócio a crescer ~8% |
| *(o que contraria a tese)* TEV/LTM EBITDA vs EXPE | 11,7x | — | ~+35% vs EXPE | A Expedia, com o mesmo risco de IA e pior execução, está a 8-9x — o "chão" de um OTA desintermediado é baixo |

---

## REVERSE DCF — o que o preço exige *(30-10-2026, ERP 5,0%)*

*Calculado sobre o `modelo_calc` do `config_BKNG.json` (Excel verificado a 30-10). Preço $ 161,10.*

**0. A grelha simples — valor por acção ao WACC (9,09%)** *(crescimento × margem EBITDA do Y10; todas acima do preço)*

| CAGR 10a ＼ Margem EBITDA Y10 | 33% | 36% | **39% (base)** | 42% | 44% |
|---|---|---|---|---|---|
| 3,4% *(base −3 pp)* | $ 154,7 | $ 169,8 | $ 184,9 | $ 200,1 | $ 210,2 |
| 4,9% | $ 175,1 | $ 192,0 | $ 209,0 | $ 225,9 | $ 237,2 |
| **6,4% (base)** | $ 198,2 | $ 217,1 | **$ 236,0** | $ 255,0 | $ 267,6 |
| 7,9% | $ 224,2 | $ 245,3 | $ 266,5 | $ 287,7 | $ 301,8 |
| 9,4% *(base +3 pp)* | $ 253,4 | $ 277,1 | $ 300,8 | $ 324,5 | $ 340,3 |

Só a célula de 3,4% de CAGR com 33% de margem fica abaixo do preço. Capex na linha do base: −0,5 pp → $ 239,3 · +1 pp → $ 229,5 · +2 pp → $ 222,9. **Para valer $ 161,10 ao WACC**, com a margem do base o CAGR teria de ser **1,7%**; com o crescimento do base, a margem EBITDA do Y10 teria de ser **27,1%**.

**1. Retorno que o preço oferece (motor A)** — inalterado pelo ERP

| | IRR |
|---|---|
| Bull · **base** · bear eixo único · stress IA · ponderado | 13,40% · **11,97%** · 10,67% · 8,82% · 11,65% |
| Base com crescimento −3 pp / cash opex +3 pp / g −1 pp | 10,06% / 11,24% / 11,50% |

**2. Crescimento exigido (motor B) — CAGR a 10 anos, por retorno exigido × margem EBITDA do Y10**

| Retorno exigido ＼ Margem Y10 | 33% | 36% | **39% (base)** | 42% |
|---|---|---|---|---|
| WACC + 25 bp (9,34%) | 4,34% | 3,20% | 2,14% | 1,16% |
| **Required 10,08% (nível 2)** | 5,66% | 4,50% | **3,43%** | 2,42% |
| 11% | 7,18% | 6,00% | 4,91% | 3,88% |
| 12% | 8,75% | 7,55% | 6,43% | 5,39% |

Âncoras: CAGR do base 6,39% · histórico FY19-25 10,2% · consenso FY25-30 8,6%.

**3. Em números falsificáveis** — Y4 com Y1–Y2 no base: o preço exige receita de **$ 35.506 M** (base $ 38.243 M), EBITDA **$ 13.670 M** (base $ 14.724 M), FCFF **$ 10.199 M** (base $ 11.182 M), NOPAT/acção **$ 13,33** (base $ 14,38) — crescimento de ~4% no Y3 a cair para ~0% no Y10.

**Leitura:** mesmo com o ERP mais alto, o preço pede 3,4% de crescimento a 10 anos para render o required, contra um consenso de 8,6% e um histórico de 10%. O teste continua a ser o Q3-26 (03-11): room nights ≥ 3%.

---

## SUMÁRIO EXECUTIVO

**Recomendação: entrada faseada — primeira e segunda tranches abertas ao preço actual, terceira condicionada aos resultados de Q3-26 a 3 de Novembro.** Fair value de $ 252,98 ao WACC de 8,66% e de $ 216,27 ao meu required return de 9,66%, contra um preço de $ 161,10 — +57% e +34%, respectivamente. Não é "posição cheia já" porque o degrau de posição cheia ($ 169,29, cauda conjunta ao required return) está só 5% acima do preço e desce para $ 161,87 — o próprio preço — se trocar o beta do sector Damodaran (0,99 realavancado) pelo beta de regressão da empresa (1,07); um gate que depende da escolha do beta não é um gate. Não é "esperar" porque ao preço de hoje o cenário base rende 11,97% e o bear de eixo único 10,67%, ambos acima do required return.

### A tese numa frase

O mercado está a pagar a Booking como se a IA fosse desintermediar o canal de reserva — preço que exige só 2,7% de crescimento anual da receita durante dez anos — enquanto os números reportados ainda mostram 5% de room nights, canal directo estável em mid-fifties e reservas via agentes de IA abaixo de 1%; a tensão é entre um risco real mas ainda não observado e um múltiplo que já o desconta quase todo.

### Os financials, em vinte segundos

Receita LTM de $ 28.241 M, a crescer 8% em Q2-26 (7% em moeda constante), com o mix a deslocar-se para merchant — já 70% da receita do trimestre, com gross bookings merchant a +14,5% contra agency a −3,3%. É receita transaccional, não contratada: a métrica de retenção é o canal directo, que a empresa diz estar em "mid-fifties" de room nights há quatro trimestres. A margem não tem fosso GAAP/non-GAAP relevante: o Adjusted EBITDA (36,0% em Q2-26, 36,9% em FY25) **não** soma o SBC de volta, que pesa só 2,1% da receita; as diferenças GAAP são a imparidade de $ 457 M na KAYAK em Q3-25 (aquisição de clientes encarecida pela IA a absorver tráfego de pesquisa) e os custos do Transformation Program (~$ 190 M LTM). Cash opex LTM de 63,5% da receita, a melhorar de 70,3% (FY23). CFO LTM de $ 9.859 M, capex de apenas 1,1–1,8% da receita, e working capital como **fonte** de caixa (média de 3 anos 26% da receita incremental) porque os clientes pagam antes de o hotel receber. Balanço: $ 20.180 M de senior notes (94% em euros) contra $ 17.214 M de caixa; capital próprio contabilístico de −$ 10.783 M por recompras de $ 6,4–10,4 mM/ano. O que mudou de natureza: o room night growth desacelerou de 9,0% (4Q25) para 5,3% (2Q26) com guidance de 3–5% para Q3, e voos passaram de +28,5% para +3,7% — efeito indirecto do conflito no Médio Oriente sobre o long-haul.

### O DCF — pressupostos e resultado

| Pressuposto | Y1 → Y10 | Âncora histórica |
|---|---|---|
| Crescimento da receita | 7,5% → 8,5% → fade a 4,0% (CAGR 6,39%) | Guidance FY26 "high single digits" cc; Q3 +5–7% cc; tendência FY24-25 ~10,5% cc; consenso FY26-28 +8,7/+9,3/+8,4% |
| Cash opex ex-D&A (com SBC) | 63,0% → 61,0% | LTM 63,5%; FY25 62,4% ex-transformation; consenso FY30 59,3% |
| Capex / receita | 1,5% | FY23-25: 1,6 / 1,8 / 1,2% |
| Imposto | 23,5% → 24,0% | ETR 2026 YTD 23,4% (BBB Act); FY25 20,9% |
| NWC / Δ receita | −15% (fonte de caixa) | Média FY23-25 −26,2% |
| WACC · g perpétuo | 8,66% · 2,5% | rf 4,96% (UST 10Y, 22-Out); β 0,99; ERP 4,5% |

**Resultado:** enterprise value de $ 194.636 M contra $ 125.357 M de mercado; valor por acção de $ 252,98. Na mesma respiração, o reverse DCF: o preço de hoje oferece **11,97%** (motor A), e para eu ganhar 9,66% basta que a receita cresça **2,71% ao ano** durante dez anos (motor B) — menos de metade do meu base e menos de um terço do consenso.

**Três honestidades obrigatórias.** O terminal value pesa **59,2%** do EV, e o Gordon implica um EV/EBITDA de saída de **12,4x** — praticamente o múltiplo de hoje (11,7x LTM), por isso o valor não depende de re-rating no terminal. A margem EBIT do modelo salta de 35,6% para 37,2% no Y4 porque a amortização dos intangíveis da carteira corre off — efeito em FCFF é negativo (menos escudo fiscal), não positivo; não há alavanca escondida. E a amplitude por driver:

| Driver | Cenário adverso | Valor/ação | Δ vs base |
|---|---|---|---|
| WACC *(não é eixo)* | +1,0 pp | $ 216,18 | −14,5% |
| **Crescimento da receita** | −2,0 pp/ano | $ 214,61 | −15,2% |
| **Cash opex / receita** | +3,0 pp | $ 232,72 | −8,0% |
| g perpétuo *(não é eixo)* | −0,5 pp | $ 240,83 | −4,8% |
| Imposto | +3,0 pp | $ 243,06 | −3,9% |
| Capex / receita | +1,5 pp | $ 242,45 | −4,2% |
| NWC / Δ receita | +15 pp (float acaba) | $ 246,65 | −2,5% |

**Frase obrigatória do G15:** repor nos factos os três drivers onde estou abaixo deles (crescimento na guidance, imposto na ETR de 2026, NWC na média de 3 anos) leva o valor a $ 270,99, **+7,12%** — o base está inclinado para o lado cauteloso, parcialmente compensado pelo opex terminal (61,0%), que é melhor do que o melhor ano próprio (62,4%) e vale −$ 9,46. Contra o consenso a reversão é **+16,25%** ($ 294,09), toda ela de pressupostos (crescimento +$ 28,44, margem +$ 11,48) e nada de base contabilística, porque o EBITDA do consenso está na mesma base que o meu cash opex.

### Os múltiplos — e se contradizem o DCF

Contra a mediana própria de 3 anos, todos os múltiplos estão no mínimo do período: P/NTM EPS 14,5x contra 21,3x, TEV/NTM EBITDA 11,0x contra 16,4x. Contra peers, a BKNG está entre a Expedia (~8-9x EV/EBITDA LTM, o que o mercado paga a um OTA com execução fraca) e a Airbnb (33x P/E forward, o que paga a crescimento de oferta própria). Contra o trimestre corrente anualizado o teste não serve — a sazonalidade é extrema (margem de EBITDA de 23% em Q1 e 47% em Q3) — por isso usa-se LTM e NTM, que dão o mesmo veredicto. Os múltiplos não contradizem o DCF: ambos dizem barato. O que contradiz é a Expedia, que mostra até onde o mercado está disposto a levar um OTA quando duvida do moat.

### Qual das fontes é mais credível aqui

**Governa o DCF**, por três razões específicas a este caso. Primeira: a mediana de múltiplos de 3 anos formou-se com o 10 anos americano entre 3,8% e 4,5%; com o rf a 4,96% (máximo de 5,31% a 5-Out) parte do de-rating é a taxa de desconto e não o negócio, portanto "voltar à mediana" não é um nível de reversão defensável — o DCF incorpora o rf de hoje explicitamente. Segunda: o múltiplo desceu de 21,6x (Jun-25) para 11,7x EV/EBITDA LTM com uma única interrupção (13,0x → 13,5x em Q2-26), o que faz da mediana a média de um de-rating em curso. Terceira: o DCF tem só 59% no terminal e um exit multiple implícito igual ao de hoje, logo não está a importar optimismo de saída. O **cross-check independente** é o motor B: 2,71% de crescimento exigido é uma afirmação falsificável e muito abaixo de tudo o que a empresa já entregou, incluindo 2020-21.

### Se comprar a X, ganho quanto por ano?

Horizonte de 5 anos, cenário base. Valor da acção no ano 5 = o mesmo DCF refeito no ano 5 ao WACC = **$ 385,91**, com o FCFF dos anos 1–5 reinvestido à taxa de desconto (a BKNG devolve tudo em recompras e dividendos). Verificação: ao fair value dá 8,81% ≈ WACC de 8,66%.

| Preço | P/E NTM à entrada | Retorno total | **Anualizado (re-rating ao FV)** | Sem re-rating | Re-rating |
|---|---|---|---|---|---|
| **$ 161,10** *(preço actual)* | 14,5x | +139,5% | **19,09%** | 12,28% | +6,81 pp |
| $ 252,98 *(fair value @WACC)* | 22,8x | +52,5% | 8,81% ≈ WACC | 8,81% | 0 |
| $ 216,27 *(1ª tranche)* | 19,5x | +78,4% | 12,28% | 9,85% ≈ required | +2,43 pp |
| $ 184,30 *(2ª tranche)* | 16,6x | +109,4% | 15,93% | 11,09% | +4,84 pp |
| $ 169,29 *(posição cheia)* | 15,3x | +128,0% | 17,92% | 11,82% | +6,09 pp |

Ao preço de hoje, 12,28% é **negócio** (o mercado continua a exigir o mesmo que exige hoje) e 6,81 pp é **re-rating** — que não está garantido e é exactamente a aposta contra a narrativa da IA. Sem re-rating nenhum ainda bate o required return por 262 bp. *Nota de convenção: com o FCFF acumulado a render zero, todos os anualizados caem 0,7–0,9 pp (ao preço actual 18,13%).*

### Porque não é a recomendação adjacente, e o que a mudaria

| Banda | Preço | Racional | Assimetria bull:bear |
|---|---|---|---|
| Preço actual | $ 161,10 | IRR de 11,97% no base; 10,67% no bear de eixo único | 24,8 : 1 |
| **1ª tranche** | **< $ 216,27** | IRR = required return (9,66%) no cenário **base** — aberta | 0,5 : 1 no limiar |
| **2ª tranche** | **< $ 184,30** | **bear de eixo único** (crescimento −2 pp todos os anos) rende o required — aberta | 6,6 : 1 |
| **Posição cheia** | **< $ 169,29** | **cauda conjunta** (crescimento −2 pp e cash opex +3 pp) rende o required — tecnicamente disparada, mas a $ 161,87 com β de regressão | 14,9 : 1 |

*Desvio ao texto da skill, mesma convenção da SAP:* "bear não perde" é degenerado num DCF com perpetuidade; usa-se "rende o required return". Assimetria = valor esperado acima do preço sobre valor esperado abaixo, com os cenários ao required return e probabilidades 20/45/25/10 (bull/base/bear/stress).

**A diferença para "posição cheia já"** é o T3 estar dentro do ruído do beta, um G14 activo (room nights a desacelerar três trimestres seguidos) e um evento binário a 11 dias. **O que mudaria a recomendação já** — os mesmos invalidadores do bloco A: room nights abaixo de 3% num trimestre (#1), marketing acima de 5,0% dos gross bookings (#2), canal directo descrito abaixo de "mid-fifties" (#3), ou um remédio regulatório que toque nas cláusulas de paridade fora de Espanha (#6). No sentido oposto, um Q3 com room nights dentro da guidance e marketing/GB ≤ 4,8% abre o T3.

**Próximo catalisador:** resultados Q3-26 a 03-11-2026, pós-mercado — o preço de 22-Out deixa de passar o G17 nesse dia e a ficha tem de ser refeita.

---

## 1. Negócio — o que vende

A Booking é o maior intermediário de alojamento do mundo: liga ~325 M de room nights por trimestre a hotéis independentes e, cada vez mais, a alojamento alternativo, cobrando uma comissão sobre o valor da reserva. O dinheiro vem de dois modelos — **agency** (o viajante paga ao hotel, a Booking factura a comissão depois) e **merchant** (a Booking cobra o viajante, paga ao hotel mais tarde, e fica com a margem mais o rendimento de facilitar o pagamento). A migração de agency para merchant é o motor da última década: dá controlo do pagamento, permite o "Connected Trip" (voos, carros, atracções no mesmo carrinho) e gera o float que financia o negócio.

**Linhas de receita** *(LTM Jun-26, CapIQ As Presented)*

| Linha | % receita | O que é | Cliente-tipo |
|---|---|---|---|
| Merchant revenues | ~68% | Reservas pagas através da Booking; inclui payments e voos | Viajante lazer, hotéis independentes |
| Agency revenues | ~28% | Comissão sobre reservas pagas no hotel | Hotéis, sobretudo Europa |
| Advertising & other | ~4% | KAYAK (metasearch), OpenTable | Anunciantes, restaurantes |

Marcas: Booking.com (o grosso), Priceline (EUA), Agoda (Ásia), KAYAK, OpenTable.

**Métricas de escala** *(ER Q2-26)*: room nights 325 M no trimestre (+5,3%); gross bookings $ 51,0 mM (+9%, +8% cc); receita $ 7.352 M; take rate implícito ~14,4%; marketing 4,7% dos gross bookings; canal directo "mid-fifties" de room nights (LTM); alternative accommodation room nights +4%.

**Exposição geográfica:** maioritariamente Europa (Booking.com, receita e dívida em euros), depois Ásia (Agoda) e EUA (Priceline, onde a Booking é subponderada face à Expedia). **Concentração de clientes:** nenhuma — centenas de milhares de propriedades e milhões de viajantes.

---

## 2. Vantagem competitiva — porquê esta e não a rival

**Rival de referência:** Expedia Group (EXPE) — o único outro OTA global de escala, com o mesmo modelo de comissão e a mesma exposição a Google e aos agentes de IA. A Airbnb compete em alojamento alternativo mas é marketplace de oferta própria, não OTA.

| Dimensão | Booking | Expedia | Quem ganha, e porquê |
|---|---|---|---|
| Produto / tecnologia | Booking.com, uma marca global, app-first | Várias marcas (Expedia, Hotels.com, Vrbo), replatforming lento | **Booking** — uma plataforma, um programa de fidelização (Genius) |
| Distribuição | Canal directo mid-fifties de room nights | Maior dependência de B2B e de pesquisa paga nos EUA | **Booking** — menos custo marginal por reserva |
| Pricing power | Take rate ~14% estável | Take rate mais baixo, mais mix B2B | **Booking** |
| Escala | 325 M room nights/trimestre | Menos de metade em room nights | **Booking** — liquidez dos dois lados |
| Custo de mudança | Baixo para o viajante, alto para o hotel independente na Europa | Idem, mas menos relevante nos EUA (cadeias) | **Booking** na Europa; empate nos EUA |
| Economia unitária | Margem EBITDA 36–37%, capex 1,5% | Margem EBITDA ~20–25% | **Booking** |

**Onde o diferencial aparece nos números:** margem EBITDA de 36,9% (FY25) com marketing a só 4,7% dos gross bookings, ROIC sobre capital fixo de 113% (FY25), e um múltiplo que se manteve acima da Expedia mesmo neste de-rating (11,7x contra ~8-9x).

**Onde NÃO aparece:** nos EUA, onde a Priceline é pequena e a quota é da Expedia e das cadeias hoteleiras com programas de fidelização; e na KAYAK, onde a imparidade de $ 457 M (Q3-25) já mostra o que acontece a um activo que depende de tráfego de pesquisa quando a pesquisa muda de forma. A assimetria é o achado: o moat da Booking é **oferta fragmentada + marca directa**, não tráfego — a parte do grupo que vivia de tráfego já foi imparizada.

---

## 3. Monetização — de onde vem exactamente o dinheiro

| Fluxo | % receita | Unidade cobrada | Quem paga | Recorrente? | Preço/unidade |
|---|---|---|---|---|---|
| Comissão merchant | ~68% | % do valor da reserva + spread de pagamento | Hotel (via margem) e viajante | Transaccional, com repetição alta via Genius | ~14% take rate médio do grupo |
| Comissão agency | ~28% | % do valor da reserva, facturada ao hotel | Hotel | Transaccional | ~15% em hotéis independentes europeus |
| Publicidade e outros | ~4% | CPC (KAYAK), reservas OpenTable | Anunciantes, restaurantes | Recorrente-ish | — |

**Mecânica do fluxo principal:** o viajante paga à Booking no momento da reserva (merchant), o dinheiro fica como deferred merchant bookings ($ 10.121 M em Jun-26, pico sazonal) e só sai para o hotel depois da estadia — daí o working capital negativo e o float. **Alavancas de preço:** programas de visibilidade pagos pelos hotéis (Preferred, Genius), payments, e cross-sell no Connected Trip. **Onde o dinheiro NÃO vem:** de subscrições ou contratos — não há backlog; a receita de amanhã depende da reserva de amanhã. **Qualidade da receita:** zero RPO, mas repetição comportamental elevada (canal directo mid-fifties). **Assimetria de monetização vs custo:** o custo marginal relevante é o marketing de performance (Google). Se os agentes de IA cobrarem "portagem" pelo tráfego, aparece primeiro no rácio marketing/gross bookings — por isso é o invalidador #2.

---

## 4. Moat — porque é que isto não é replicável

| Tipo de moat | Presente? | Evidência quantitativa | Força |
|---|---|---|---|
| Network effects | Sim | Mais oferta → melhor conversão → mais procura; 325 M room nights/trimestre | **Forte** |
| Switching costs | Parcial | Hotel independente europeu depende do canal; viajante não tem custo de mudança | Médio |
| Economias de escala | Sim | Marketing 4,7% dos GB vs muito acima em rivais pequenos; capex 1,5% da receita | Forte |
| Intangíveis (marca, dados) | Sim | Canal directo mid-fifties; Genius | Médio-forte |
| Vantagem de custo estrutural | Sim | Float: capital investido total negativo (−$ 7.051 M Jun-26) | Forte |
| Eficiência de distribuição | Sim | Direct mix estável há 4 trimestres | Médio |

**Teste do capital ilimitado**

> Se um competidor com € 10 mil milhões e cinco anos copiasse isto amanhã, **o que é que o dinheiro não compra?**

Não compra a cauda longa de oferta — centenas de milhares de hotéis independentes e alojamento alternativo, cada um com o seu contrato, conteúdo e integração de disponibilidade — nem o hábito de mais de metade dos viajantes irem directamente à app. **Mas atenção:** a Google e a OpenAI não precisam de comprar a oferta se a puderem *ler* da Booking. É por isso que o risco relevante não é um novo OTA, é um agente que fique com a relação com o viajante e trate a Booking como fornecedor de inventário — com take rate menor.

**O que erode o moat, e a que velocidade:** (1) agentes de IA como interface de reserva — hoje <1% das room nights; (2) regulação das cláusulas de paridade e do ranking (CNMC, DMA/DSA) — já em curso em Espanha; (3) cadeias hoteleiras a puxarem reserva directa. **Trajectória:** estável — canal directo mid-fifties em 4 trimestres seguidos, take rate estável; a erosão é um risco de cauda, ainda não um número.

### O moat converte-se em economia? O teste do ROIC

O capital investido total é **negativo** desde 2023 — o negócio é financiado pelos clientes — e o ROIC convencional não tem significado. Apresento-o sobre capital fixo (PP&E + goodwill + intangíveis + ROU + outros activos), com NOPAT = EBIT ex-imparidades × (1 − 22%; 23,4% no LTM).

| | FY22 | FY23 | FY24 | FY25 | LTM Jun-26 |
|---|---|---|---|---|---|
| NOPAT normalizado | 3.980 | 4.551 | 5.893 | 7.240 | 7.462 |
| Capital fixo investido | 6.774 | 6.868 | 6.681 | 6.418 | 6.177 |
| NWC operacional | −4.572 | −7.018 | −9.575 | −9.757 | −13.228 |
| **Capital investido total** | 2.202 | −150 | −2.894 | −3.339 | −7.051 |
| **ROIC s/ capital fixo** | 59% | 66% | 88% | 113% | 121% |
| Spread vs WACC 8,66% | +50 pp | +58 pp | +79 pp | +104 pp | +112 pp |

Capital de fim de período; a base média e a base com NOPAT normalizado da amortização de aquisições dão números ainda mais altos, porque o capital fixo está a cair. CapIQ *Return on Capital %* (Ratios, Q2-26) dá 61% — base diferente (inclui caixa), mesma conclusão.

| | |
|---|---|
| Capital fixo acrescentado FY22→FY25 | **−$ 356 M** |
| Δ NOPAT normalizado | **+$ 3.260 M** |
| **ROIC marginal** | não definido — crescimento sem capital |
| WACC | 8,66% |

O crescimento da Booking não consome capital; consome marketing. Por isso o ROIC marginal relevante é o retorno do marketing incremental — que se lê no rácio marketing/gross bookings (4,6% → 4,7% YoY): estável.

---

## 5. SWOT

**Forças:** 325 M room nights/trimestre e a maior oferta de alojamento independente na Europa; margem EBITDA 36,9% com capex de 1,5%; float de $ 10 mM em pico que financia o negócio; devolução de capital de ~$ 7,7 mM/ano (recompras $ 6,4 mM + dividendos $ 1,2 mM em FY25), com share count a cair ~4% ao ano (838 M → 751 M em 8 trimestres).

**Fraquezas:** posição fraca nos EUA (Priceline); dependência de marketing de performance pago à Google; KAYAK imparizada ($ 457 M) por perda de tráfego; dívida 94% em euros contra capital próprio negativo de −$ 10.783 M.

**Oportunidades:** alojamento alternativo (+4% room nights, abaixo do total — oportunidade não capturada); payments e Connected Trip (voos +28% em FY25 antes do choque); $ 650 M de poupanças run-rate do Transformation Program até fim-2027 (~2% da receita de 2027); Ásia via Agoda.

**Ameaças:** agentes de IA como interface de reserva (probabilidade relevante, horizonte 3–7 anos; hoje <1%); regulação UE — DMA (gatekeeper) e investigação formal DSA aberta a 21-Out-2026 com coima máxima de 6% da receita (~$ 1,7 mM); FTC/Priceline (potencial >$ 500 M); conflito no Médio Oriente a pesar no long-haul (Q3 room nights guidance 3–5%); taxas reais altas a pressionarem procura discricionária.

---

## 6. Legal, regulatório e fiscal

| Matéria | Tipo | Estado | Exposição máx. | % market cap | Timeline |
|---|---|---|---|---|---|
| CNMC Espanha | Antitrust (paridade, ranking) | Coima suspensa em recurso; **$ 472 M provisionados** | $ 472 M + remédios | 0,4% | Tribunal Nacional |
| FTC / Priceline | Consumer protection (taxas, apoio, facturação) | Staff recomenda queixa (Jul-26); em negociação | >$ 500 M (Reuters) + compromissos | ~0,4% | 2026-27 |
| DSA — Comissão Europeia | Plataforma muito grande (VLOP) | **Investigação formal aberta 21-Out-2026** | até 6% da receita (~$ 1,7 mM) | ~1,4% | 12–24 meses |
| DMA | Gatekeeper | Designada; obrigações sobre paridade e dados | Remédios de negócio | — | Contínuo |
| Swiss PSO | Nível de comissões na Suíça | Ordem de redução suspensa em recurso | Receita suíça | Imaterial | Recurso |

Na ponte EV→equity entram **$ 1.070 M** de contingências: CNMC 472 (já passivo) + FTC ~350 esperado + DSA ~250 esperado. **Regime regulatório:** o risco não é a coima, é o remédio — a perda das cláusulas de paridade em toda a UE seria o canal pelo qual a regulação chega ao take rate. **Risco fiscal:** Netherlands Innovation Box (taxa de 9% sobre parte do lucro) sob escrutínio; Pillar 2 e BBB Act já subiram a ETR de 20,9% para 23,4%; $ 302 M de unrecognized tax benefits. **Factores de risco novos face ao 10-K anterior:** a linguagem sobre agentes de IA a evoluírem para plataformas de reserva completas e a desintermediarem OTAs.

---

## 7. Enquadramento de valuation

### Que métricas são as certas

| Múltiplo | Usar? | Porquê / porque não |
|---|---|---|
| P/E GAAP | Com reserva | Distorcido por FX sobre a dívida em euros (outros gastos de −$ 962 M em Q2-25) e pela imparidade |
| P/E ajustado | Sim | O ajustado não soma SBC; o fosso para o GAAP é FX, imparidade e transformation |
| EV/EBITDA | **Sim** | Mesma base do modelo; capex ínfimo, logo EBITDA ≈ caixa |
| EV/Receita | Não | Mix merchant/agency muda a receita sem mudar a economia |
| P / NTM EPS | **Sim — âncora de mercado** | É o múltiplo que o sell-side usa e o que mostra o de-rating |
| EV/FCF | Sim | FCF yield de 6,4% é a forma mais limpa de ler o preço |
| Específico | Marketing/gross bookings, take rate | Saúde do moat, não valuation |

**Métrica âncora:** DCF de FCFF, com P/NTM EPS e EV/FCF como cross-check. **Peers:** Expedia (mesmo modelo, pior execução) e Airbnb (alojamento alternativo). **Armadilhas:** EPS do CapIQ mistura bases pré e pós split; TEV do CapIQ soma operating leases; FX sobre a dívida em euros entra no resultado GAAP.

### O múltiplo é barato porque o preço caiu, ou porque o lucro caiu?

Porque o **preço** caiu. Receita do H1-26 +11,5% YoY, Adjusted EBITDA +9% em Q2, EPS ajustado +15% — o denominador está a subir. O trimestre corrente anualizado não serve (em FY25, Q2 foi ~25% da receita anual e Q3 ~33%); LTM e NTM dão a mesma leitura.

| | LTM *(As Presented)* | Mediana 3 anos | Trimestre corrente anualizado |
|---|---|---|---|
| EV / Receita | 4,4x | 6,3x | n/a — sazonalidade |
| EV / EBITDA | 11,7x | 18,4x | n/a |
| EV / EBIT | 12,6x | 20,6x | n/a |

### Decomposição de qualquer colapso de margem

Não há colapso. Margem operacional GAAP de Q2-26 34,0% contra 33,1% em Q2-25 (homólogo). O único salto é Q3-25, onde a imparidade de $ 457 M da KAYAK corre off e já está fora do cash opex do modelo.

### Três lentes, três veredictos

| Lente | Veredicto |
|---|---|
| vs história própria de múltiplos | Barata — mínimo de 5 anos, com a ressalva do rf |
| vs peers | Entre EXPE e ABNB; prémio à EXPE justificado pela margem, mas mostra o chão |
| DCF | Barata — +57% ao WACC, +34% ao required return |

As lentes concordam; a divergência está entre elas e o mercado, que precifica um cenário de desintermediação que os números ainda não mostram. **Governa o DCF**, porque é o único que trata o risco de IA como um cenário explícito com probabilidade em vez de o deixar escondido num múltiplo.

### Os drivers dominantes — por sensibilidade, não por intuição (G13)

Bandas BKNG definidas antes de olhar: crescimento ±2 pp, cash opex ±3 pp, capex −0,5/+1,5 pp, imposto ±3 pp, NWC −11/+15 pp, vida do capex ±1 ano, WACC ±1 pp, g ±0,5 pp. Os dois operacionais mais sensíveis são **crescimento** (amplitude $ 83,38) e **cash opex** ($ 40,53). O capex, que é o driver que mais discussão gera noutras empresas, é o 6.º aqui.

**Grelha viva** (`Cenarios!B31:G36`, tabela de dados do Excel; eixo das linhas reapontado para o cash opex — ver Leia-me):

| Cash opex ＼ Crescimento | −2 pp | −1 pp | **base** | +1 pp | +2 pp |
|---|---|---|---|---|---|
| −3 pp | 232,02 | 251,81 | 273,24 | 296,45 | 321,58 |
| −1,5 pp | 223,32 | 242,42 | 263,11 | 285,52 | 309,79 |
| **base** | 214,61 | 233,03 | **252,98** | 274,59 | 298,00 |
| +1,5 pp | 205,90 | 223,63 | 242,85 | 263,66 | 286,20 |
| +3 pp | 197,20 | 214,24 | 232,72 | 252,73 | 274,41 |

Ao WACC. Toda a grelha está acima do preço de $ 161,10.

**Cenários discretos** (`Cenarios!A41:I45`)

| Cenário | Prob. | CAGR receita 10a | Cash opex Y10 | Valor @WACC | Valor @required | IRR ao preço de hoje |
|---|---|---|---|---|---|---|
| Bull (+1,5 pp cresc., −1,5 pp opex) | 20% | 7,89% | 59,5% | $ 297,42 | $ 253,47 | 13,40% |
| **Base (modal)** | **45%** | **6,39%** | **61,0%** | **$ 252,98** | **$ 216,27** | **11,97%** |
| Bear — eixo único (cresc. −2 pp) | 25% | 4,39% | 61,0% | $ 214,61 | $ 184,30 | 10,67% |
| Cauda conjunta (cresc. −2 pp, opex +3 pp) | — | 4,39% | 64,0% | $ 197,20 | $ 169,29 | 10,02% |
| Stress — disrupção por IA (CAGR 3%, opex +5 pp) | 10% | 3,00% | 66,0% | $ 164,37 | $ 141,27 | 8,79% |
| **Valor esperado** | | | | **$ 243,41** | **$ 208,22** | |

**Stress test de downside, aritmético.** Receita **plana dez anos**, cash opex +6 pp (67% — agentes de IA a cobrarem a portagem do tráfego), WACC +100 bp e g a 1,5%: FCFF Y1 $ 6.425 M, margem EBIT Y10 31,5%, valor **$ 99,02 (−38,5%)**. Ao WACC e g de 2,5%, o mesmo cenário dá $ 122,67 (−23,9%). É o que se perde se a tese estiver errada em tudo ao mesmo tempo.

**Porquê cada eixo, e porquê o valor do base.** O crescimento é o eixo porque compõe dez anos e arrasta o terminal; o opex porque é onde a portagem da IA aparece. O base de crescimento fica entre a tendência (FY24-25 ~10,5% cc) e o trimestre (Q3 guidance 5–7% cc), como manda o G14 quando o desvio tem explicação identificável (Médio Oriente) — e há um invalidador ligado (#1). Não há alavanca agressiva numa curva a desacelerar: o opex melhora 2 pp em dez anos, menos do que os 7 pp de FY23→LTM e do que o consenso. Contagem do G15: três drivers do lado cauteloso face a factos (crescimento, imposto, NWC), um favorável (opex terminal), um em linha (capex) — não é um bear mal rotulado; e o crescimento conta como **duas** marcações, porque está abaixo da guidance e do consenso ao mesmo tempo.

---

## A. Invalidadores da tese

**Regras:** número legível numa fonte pública sem estimar; threshold que a série já quase tocou; frequência compatível com a fonte.

| # | Afirmação (secção) | Invalidador — condição observável | Onde verifico | Definido | Estado | Revisto |
|---|---|---|---|---|---|---|
| 1 | Procura resiliente; desaceleração é choque do Médio Oriente (§DCF, G14) | Room nights YoY **< 3,0%** num trimestre | ER, tabela Statistical Data | 23-10-2026 | **Vigiar** — 5,3% em Q2, guidance Q3 3–5% | 23-10-2026 |
| 2 | Moat de distribuição; IA não cobra portagem (§3, §4) | Marketing / gross bookings **> 5,0%** num trimestre | ER, Additional Highlights | 23-10-2026 | **Vigiar** — 4,7% em Q2 (4,6% em Q2-25) | 23-10-2026 |
| 3 | Canal directo estável (§2) | ER deixa de descrever o direct mix como "mid-fifties" (passa a "low fifties" ou abaixo) | ER, Additional Highlights | 23-10-2026 | OK | 23-10-2026 |
| 4 | Agentes de IA marginais (§4) | Gestão divulga room nights via LLMs/agentes **≥ 5%** | Transcript | 23-10-2026 | OK — "significativamente abaixo de 1%" | 23-10-2026 |
| 5 | Margem a melhorar com o Transformation (§DCF opex) | Adjusted EBITDA margin anual **< 35,0%** | ER de Q4 | 23-10-2026 | OK — FY25 36,9% | 23-10-2026 |
| 6 | Regulação não chega ao take rate (§6) | Remédio que proíba cláusulas de paridade ou imponha ranking em **toda a UE** (DMA/DSA), ou coima única > $ 2 mM | 10-Q / 8-K, nota de litígio | 23-10-2026 | OK | 23-10-2026 |
| 7 | Crescimento acima de room nights via merchant/payments (§1, §3) | Gross bookings cc YoY **abaixo** do room night growth num trimestre | ER, Statistical Data | 23-10-2026 | OK — 8% vs 5,3% | 23-10-2026 |

**Disparados — o que fiz a seguir**

| # | Data | O que disparou | Decisão tomada |
|---|---|---|---|
| — | — | Nenhum | — |

**Regra de saída** — sete maneiras de estar errado; a de estar certo: **trim** de uma tranche quando o preço passar o fair value ao WACC ($ 252,98) — aí o base rende menos do que o custo de capital — e saída de mais uma quando o motor A cair abaixo do WACC.

---

## B. Log de fair value e decisões

| Data | Quarter | Preço | FV DCF | IRR impl. | Growth impl. | Decisão | Racional (1 linha) |
|---|---|---|---|---|---|---|---|
| 30-10-2026 | Q2-26 | $ 161,10 | $ 236,03 | 11,97% | CAGR 3,43% @required | Entrada faseada (T1 e T2) | Regra de custo de capital da carteira: ERP 4,5% → 5,0% (Kroll); Rf 4,96% igual. Ponte: só ERP, −$ 16,95. A cheia passou para $ 159,66, abaixo do preço |
| 23-10-2026 | Q2-26 | $ 161,10 | $ 252,98 @WACC · $ 216,27 @req | 11,97% | 2,71% | **T1 + T2 abertas; T3 depois de 03-Nov** | Preço exige quase nenhum crescimento; T3 dentro do ruído do β e com G14 activo |

**Verificação retrospectiva** — de seis em seis meses. Primeira: Abr-2027.

---

## D. Sentimento e posicionamento

**Reacção e narrativa.** A acção caiu de ~$ 214 em Agosto (pós-Q2) para $ 161,10 — −25% face ao máximo de 52 semanas de $ 220,81 e +7% acima do mínimo de $ 150,14. Três camadas: (1) **regulatória** — a Reuters noticiou a 7-Out que o FTC prepara acção contra a Priceline com coima potencial >$ 500 M, e a 21-Out a Comissão Europeia abriu investigação formal ao abrigo do DSA (−3,3% nesse dia); (2) **narrativa de IA** — "vítima da IA", com a imparidade da KAYAK como prova; a contra-narrativa (CNBC, Set-26) é que a Google e a OpenAI não querem ser merchant of record e devolvem o checkout ao OTA, com a Booking como parceiro de lançamento nos dois; (3) **macro** — UST 10Y a 4,96% depois de 5,31% a 5-Out, mercado a dar ~76% de probabilidade a uma *subida* de 25 bp em Dezembro, e sell-off de tecnologia a 22-Out. **Ligação aos drivers:** a camada 1 está na ponte ($ 1.070 M) e no invalidador #6; a camada 2 é o eixo de opex e o cenário de stress; a camada 3 está no rf de 4,96%.

**O que o mercado pode estar a assumir errado.** Que a desintermediação é linear e próxima. O que se observa é <1% de room nights via agentes e canal directo estável. Se a IA vier, chega primeiro ao rácio marketing/gross bookings — que é público e trimestral. O mercado está a descontar hoje o que ainda pode ser lido amanhã.

**Insider** — 0 compras e 30 vendas em 12 meses (GuruFocus), $ 17,4 M vendidos nos últimos 90 dias (MarketBeat), **todas ao abrigo de planos 10b5-1**: CFO 20.000 acções a ~$ 211 (12-Ago), VP P. Millones 50.050 a ~$ 208 (17-Ago), CHRO 1.500 a ~$ 163 (15-Out, plano adoptado a 1-Jun). Sem sinal de convicção para nenhum lado; a ausência de compras em mínimos é nota, não alarme.

**Short interest** — n/d. Sem export Charting do CapIQ. **Pedir na próxima ronda.**

**Sell-side** — PT médio $ 233, mediano $ 236, intervalo $ 170–301, desvio-padrão $ 28, n=35. 24 Buy, 6 Outperform, 7 Hold, 0 Sell. Cortes recentes: Wells Fargo $ 220 → $ 190 (Equal Weight, 7-Out), Jefferies $ 200 → $ 185 (19-Out). EPS LT growth do consenso 17,5% (n=7) — inclui recompras.

| Base | Fair value | Governa a decisão? |
|---|---|---|
| DCF, SBC como custo real, ao WACC | $ 252,98 | **Sim** |
| DCF ao required return | $ 216,27 | Sim — define o T1 |
| Consenso sell-side (PT 12 meses) | $ 233 | Não — referência |
| Mínimo do intervalo sell-side | $ 170 | Coincide com o T3 |

**Decomposição do gap ao consenso:** zero de base contabilística (o EBITDA do consenso não soma SBC, como o meu). Pôr os pressupostos de crescimento e margem do consenso no meu DCF dá $ 294,09 — acima do PT de $ 233. O gap entre o modelo do consenso e o PT do consenso é o sell-side a aplicar um múltiplo que já embute o de-rating, não uma diferença de previsão.

**Estrutura accionista** — dispersa, institucional; sem activistas conhecidos.

---

## C. Changelog

| Data | Quarter | O que mudou | Secções |
|---|---|---|---|
| 30-10-2026 | Q2-26 | Regra de custo de capital da carteira (decisão do Hugo): Rf UST 10Y à data do preço (4,96%, igual), ERP Kroll 5,0% (era 4,5%), CRP 0. FV $ 252,98 → $ 236,03; motor A inalterado (11,97%); motor B 2,71% → 3,43%; escada $ 203,62 / $ 173,85 / $ 159,66. Escada pré-v1.3 mantida (bull/base/bear eixo único/cauda/stress IA como shifts, agora no bloco `escada` do config); o stress IA recalculado com um shift uniforme até CAGR 3% (a ficha de 23-10 dava $ 164,37; o mesmo método dá $ 165,25 ao ERP antigo). Excel regerado e verificado | ESTADO, REVERSE DCF (novo), B, C |
| 23-10-2026 | Q2-26 | **Criação.** Pasta reorganizada na estrutura canónica. G3 (split 25:1), G14 (room nights) e G18 (operating leases no TEV do CapIQ) dispararam e foram resolvidos. G15 vs factos +7,12% (frase no sumário). Recálculo final via Excel COM, G12 verde. Grelha reapontada para opex × crescimento. | Todas |

---

*Template v3.0 — Julho 2026. Camada 1 de três: ficha estrutural · análise trimestral em chat · DCF em Excel.*
