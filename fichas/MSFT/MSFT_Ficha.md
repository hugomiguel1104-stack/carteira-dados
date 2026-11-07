# Ficha de Empresa — Microsoft Corporation (MSFT · NasdaqGS)

> **Documento único e vivo.** Não se cria cópia por trimestre — actualiza-se este.
> **Secções 1–7:** estrutura. Escritas uma vez, revistas anualmente ou quando um invalidador dispara.
> **Blocos A–D:** infraestrutura. Actualizados a cada análise trimestral.
> Todo o número de valuation lê-se de uma célula do `MSFT_DCF.xlsx` ou da saída dos scripts `02`–`07` (G12). Modelo **reconstruído a 29-Out-2026 com o pipeline `dcf-reverso` v1.7**: 798 fórmulas, zero erros no recálculo headless, detectores do G12 verdes (motor A 0,00000000%, B 0,00000002%, D 0,00000001%).
> **Migração de estrutura (rev.2):** a ficha de Julho estava no template v3.0. Passa ao v3.3 / plugin v1.7 — resumo, ciclo de capex, cenários nomeados, escada por valor esperado, hurdle escalado ao risco, prémios aplicados, ponte do fair value. As secções 1–7 foram revistas só no que o trimestre mudou.

`Criada:` 30-07-2026 · `Última revisão estrutural:` 29-10-2026 · `Último quarter processado:` FY27-Q1 (30-09-2026)

---

## RESUMO

| | |
|---|---|
| **Preço** | $ 545,00 *(29-10-2026, pós-resultados)* |
| **Market cap · EV** | $ 4.058.070 M · $ 4.100.015 M *(com finance leases; $ 3.997.775 M sem a participação na OpenAI)* |
| **Fair value DCF (base)** | **$ 404,02 → upside −25,9%** |
| **Cenários** *(25 / 50 / 25)* | Infraestrutura comoditizada $ 308,45 · **O ciclo paga com atraso $ 404,02** · Os agentes monetizam $ 491,35 |
| **Retorno que o preço oferece** | 8,78% ao ano, contra 11,47% exigido |
| **Decisão** | **esperar** — 1ª tranche a $ 346,38 |
| **O que decide** | Guidance de capex do 2º semestre e crescimento do Azure no Q2-27 (28-01-2027) |

---

## ESTADO — detalhe

| | | | |
|---|---|---|---|
| **Preço** | $ 545,00 | **Data** | 29-10-2026 *(indicado pelo Hugo; posterior ao 10-Q de 28-10 — G17. Memo: fecho de 28-10 $ 531,01, pré-resultados)* |
| **Market cap** | $ 4.058.070 M *(7.446 M acções diluídas)* | **EV** | $ 4.100.015 M *(mkt cap + dívida 35.481 + finance leases 70.973 − caixa e ST 64.509)*. Operacional, sem a OpenAI: $ 3.997.775 M (`Inputs!B15`) |
| **Valor DCF** *(base "O ciclo paga com atraso", ao WACC de 10,47%)* | **$ 404,02** (`DCF!B27`) | **Upside** | −25,9% (`DCF!B29`) |
| **Cenários nomeados** *(p declaradas antes)* | $ 308,45 / $ 404,02 / $ 491,35 · ponderado $ 401,96 | **IRR esperada** | 8,79% vs required 11,47% |
| **Ciclo de capex** | pico transitório, nível estrutural | **Impacto no valor** | médio — ±$ 24 só pelo caminho do capex |
| **Δ FV vs revisão anterior** | +$ 1,51 ($ 402,51 → $ 404,02) | **Atribuição** | taxa de desconto −$ 80,22 *(dos quais −$ 28,08 são o erro de Rf de Julho)* · business plan e método +$ 57,02 · ano-base +$ 16,49 · mercado, balanço e SOTP +$ 8,23 |
| **Ke** *(G19: método A; Rf 4,99% UST 10Y 27-10; ERP 5,0% por decisão do Hugo; β 1,13 CapIQ; CRP 0)* | 10,64% | **Ke ±100 bp** | valor/acção $ 479,23 / $ 346,36 |
| **Amplitude bull–bear** *(2 eixos)* | $ 272 – $ 584 | **Drivers dominantes** | crescimento da receita · capex/receita |
| **IRR implícita** *(motor A)* | **8,78%** | **vs required return** | spread **−269 bp**; −169 bp vs WACC |
| **Crescimento que o preço exige** *(motor B)* | CAGR **19,23%** a 10 anos para render 11,47% *(17,08% para render o WACC)* | **vs** | base 13,08% · histórico FY22-26 13,74% · receita Y10 de $ 1.184.066 M no base |
| **Decisão** | **esperar** | **Gates** | 1ª < $ 346,38 (base) · 2ª < $ 344,67 (ponderado) · cheia < $ 277,19 (crescimento −3 pp) — *a escada trocou os dois primeiros degraus* |
| **Peso máximo da posição** | 3,89% | **Cenário de cauda** | Infraestrutura comoditizada @WACC+1 pp: −51,4% vs preço |
| **Invalidadores disparados** | 0 de 8 · 3 em vigilância (#1, #2, #6) | **Último report** | FY27-Q1, 10-Q e call de 28-10-2026 |
| **ROIC marginal** | **14,8%** *(LTM Jun→Set-26: Δ NOPAT 5.942 / Δ capital 40.022)*; 14,35% FY25→FY26 | **vs WACC** | +4,4 pp. ROIC LTM 25,6% (capital fim de período) |
| **Próximo catalisador** | FY27-Q2 a 28-01-2027 | **O que decide** | Se o capex de "mais de $ 50 mM" vem com Azure nos 49–50% guiados e com a capacidade de terceiros entregue |
| **Consenso sell-side** | PT médio $ 605,12 (n=52, mín. $ 440, máx. $ 870) | **vs o meu DCF** | −33,2% · rácio FV/PT **0,67** → calibração corrida (§7) |
| **Peers** *(múltiplo âncora)* | n/a — sem comparáveis limpos em mega-caps multi-negócio (decisão do Hugo, 29-10-2026, como na GOOGL) | **vs pares maduros** | n/a |
| **Short interest** | 1,244% *(29-07-2026; sem export novo)* | **vs mediana 5 anos** | 0,657% — ~97% do máximo de 5 anos em Julho |
| **Posição actual** | 0 acções | **% da carteira** | 0% |

**Múltiplos-chave** — os que decidem *nesta* empresa. Justificação na §7.

| Múltiplo | Actual | Mediana própria *(6 trimestres)* | vs mediana | Leitura |
|---|---|---|---|---|
| EV/EBITDA LTM (GAAP, âncora) | 19,5x | 19,5x | em linha | Voltou ao nível de 2025, depois de ter descido a 14,2x em Junho |
| NTM EV/EBITDA *(forward, TEV CapIQ)* | 15,6x | 16,6x | −6% | O EBITDA do consenso tem D&A de 14–15% da receita com capex de 50%: subestima a depreciação que vem (§ Ciclo de capex) |
| **EV/FCF LTM — capex da gestão** *(contraria a tese)* | **99,3x** | n/d | — | Era 78,1x em Julho. O FCF na definição da gestão é $ 40.278 M LTM; o Q1-27 anualizado dá 78,1x |

<!-- SIGLAS. RPO (remaining performance obligations): receita contratada ainda não reconhecida — mede backlog, não
     vendas do trimestre. Microsoft Cloud: desde FY27 = Azure + M365 commercial cloud + Industry solutions cloud
     (definição recast). Finance lease: arrendamento capitalizado — entra no capex e na dívida. Operating lease:
     não entra em nenhum dos dois, mas a renda passa pelo EBIT. Foundry: plataforma de modelos e agentes do Azure. -->

---

## TÓPICOS-CHAVE

- **O preço subiu mais do que o negócio.** A acção passou de $ 390,54 para $ 545 (+40%) desde Julho. O fair value mexeu $ 1,51, porque o business plan mais forte (+$ 57,02) foi absorvido pela taxa de desconto (−$ 80,22). A $ 545 o mercado oferece 8,78% ao ano e exige um CAGR de receita de 17,1% durante dez anos só para render o WACC.
- **Mais de metade do Δ é taxa, não tese.** Ao WACC de Julho (9,12%) o base valeria $ 511 (matriz cenário × taxa). A mudança de "esperar com 1ª tranche a $ 345" para "esperar com 1ª tranche a $ 346" esconde duas correcções opostas: o crescimento subiu para o consenso e o custo de capital foi corrigido (Rf de 4,25% para 4,99%; ERP de 4,5% para 5,0%).
- **A Microsoft passou a ter um cliente acima de 10%.** A OpenAI pagou $ 10,0 mM no Q1-27, 10,8% da receita, com $ 7,2 mM em contas a receber. É ao mesmo tempo investida a 24%, fornecedora de modelos e o maior cliente do Azure. Em Julho a ficha dizia que não havia concentração de clientes.
- **O consenso não fecha consigo próprio.** Tem capex de 50% da receita em FY27-29 e D&A de 14–15%. Com a depreciação por classe de activo (servidores a 6 anos), o D&A chega a 24,6% no Y4 e a margem EBIT cai para 38,4%, contra os 46% do consenso. Esta linha vale $ 22 por acção.
- **O que contraria a tese.** O trimestre foi bom em tudo o que a tese pedia: Azure +48%, guidance de 49–50%, margem operacional de 49,8%, eficiência da frota a libertar capacidade sem capex. Ao ERP implícito do Damodaran de Outubro (4,20%, o usado na GOOGL) o base vale $ 469,12, e a diferença para o preço cai para 14%.

---

## CICLO DE CAPEX — transitório ou estrutural?

### Onde está a empresa no ciclo

*Capex na definição da gestão (inclui finance leases). FY = ano fiscal a Junho. Consenso: capex cash do CapIQ × 1,12 (rácio gestão/cash do Q1-27, 1,15, a descer com a reclassificação para operating leases).*

| | FY22 *(pré-ciclo)* | FY23 | FY24 | FY25 | FY26 | **LTM Set-26** | FY27E | FY28E | FY29E |
|---|---|---|---|---|---|---|---|---|---|
| Capex ($ mM) | 29,2 | 31,9 | 55,7 | 88,2 | 145,3 | **155,6** | ~218 | ~248 | ~283 |
| Capex / receita | 14,7% | 15,1% | 22,7% | 31,3% | 43,8% | **44,9%** | 55,8% | 52,9% | 49,7% |
| D&A / receita | 7,3% | 6,5% | 8,6% | 10,4% | 11,6% | 12,2% | 14,0% *(cons.)* · 14,5% *(modelo Y1)* | 14,8% · 18,8% | 14,9% · 21,9% |
| FCF cash ($ mM) | 65,1 | 59,5 | 74,1 | 71,6 | 67,0 | 60,0 | 33,2 *(cons.)* | 49,1 | 93,6 |
| Margem EBIT | 42,1% | 41,8% | 44,6% | 45,6% | 46,8% | 47,1% | 46,6% *(cons.)* · 47,0% *(modelo)* | 46,4% · 43,2% | 46,3% · 40,6% |

Fase: **subida, perto do pico em intensidade.** O Q1-27 foi 49,0% da receita (56% somando os ROU de operating leases, $ 6,5 mM). A gestão guia aceleração no 2º semestre do FY27, e o consenso só tem a intensidade a descer a partir do FY28.

### Transitório ou estrutural — a evidência

| Sinal | O que diz | Aponta para |
|---|---|---|
| Composição do capex | ~3/4 em activos de vida curta (CPUs, GPUs, memória) no Q1-27, contra ~2/3 no FY26 e ~1/2 no Q1-26 (deck, slide 6). Servidores a 6 anos | **Estrutural no nível:** o parque tem de ser reposto a cada ~6 anos |
| Compromissos e leases por iniciar | **$ 364,6 mM** de leases ainda não iniciadas, sobretudo datacenters, de FY27 a FY34, com prazos de 1 a 20 anos (10-Q, Nota 12). ≈1,05x a receita LTM | **Estrutural:** o capex dos próximos 3–4 anos já está contratado |
| Calendário da gestão | CY2026 em "~$ 170 mM" (era ~$ 175 mM) só por atrasos de capacidade de terceiros; "capex to accelerate" no 2º semestre do FY27 | Subida, sem data de pico |
| Precedente próprio | No FY23 o capex ficou plano (31,9 vs 29,2) depois de dois anos a crescer. A gestão já fez uma pausa | Transitório possível |
| Indústria | Corrida generalizada: GOOGL 40–49% da receita, META ~54% | **Estrutural:** ninguém corta sozinho |
| Retorno até agora | $ 0,47 de receita incremental por $ de capex (FY22-26); ROIC marginal de 14,8% LTM, acima do WACC de 10,47% | Ainda cria valor, mas a menos de metade do ROIC médio |
| Financiamento | CFO LTM $ 195,9 mM contra capex de $ 155,6 mM mais $ 48 mM de distribuições. A caixa caiu $ 12,3 mM num trimestre. A CFO anunciou que vai "access additional sources of funding" | O CFO deixou de chegar para tudo |

**Veredicto: pico transitório, nível estrutural.** A intensidade deve descer de ~56% para ~20% ao longo da década — está no consenso, nos compromissos que vencem e na eficiência da frota. Mas não volta aos 15% de antes do ciclo: três quartos do capex são servidores de seis anos, e o base fica com 19,5% no Y10. A pergunta que decide o valor não é se o capex desce: é **quanta receita cada dólar compra** — o crescimento tem amplitude de $ 183,84, contra $ 125,68 do capex.

**Para que serve o capex.** A gestão declara quatro usos: (i) capacidade Azure para terceiros, incluindo a OpenAI (10,8% da receita); (ii) Foundry e inferência de modelos próprios e de terceiros (receita "mais do que triplicou", sem número); (iii) Copilot e M365 (throughput +50% QoQ, sem número de receita); (iv) I&D própria (MAI-Base-2) e substituição de servidores em fim de vida. Só o primeiro tem retorno demonstrado em receita divulgada — Azure $ 33,2 mM no trimestre, +48%.

### Impacto no valor

| Hipótese sobre o ciclo *(tudo o resto do base igual)* | Capex Y2 → Y4 → Y10 | Valor/acção | vs base |
|---|---|---|---|
| Corta depressa (−5 pp do Y2 ao Y6, a convergir no Y10) | 47,9% → 35,4% → 18,5% | $ 428,33 | +$ 24,31 |
| **Base** | 52,9% → 40,4% → 19,5% | **$ 404,02** | — |
| Prolonga-se (+5 pp do Y2 ao Y6) | 57,9% → 45,4% → 20,5% | $ 379,72 | −$ 24,30 |

**Impacto: médio.** Só o caminho do capex move o valor ±$ 24 (6%), porque metade do capex volta pelo escudo fiscal do D&A e o terminal quase não muda. O que o desloca de verdade é a receita que o capex compra (G13).

**G21 — margem terminal contra o pré-ciclo.** EBIT Y10 de 44,1% contra 41,8% de média em FY21-23: +2,3 pp, porque a alavanca operacional de FY24-26 é facto (LTM 47,1%). A margem FCFF do Y10 é 34,2%, contra ~27% económico antes do ciclo (FCF cash de 31,4% menos o SBC). **Está 7 pp acima, e é preciso dizê-lo:** no Y10 o investimento líquido (capex − D&A) é só 0,6% da receita, contra ~8% antes do ciclo, porque o crescimento cai para 6% e o capex fica a 1,03x o D&A. Em estado estacionário a g = 2,5%, com vida média de 10,75 anos, o rácio seria ~1,13x; levado lá, o base desce para **$ 381,68 (−$ 22,34)**. Mantenho 1,03x porque passa a regra da casa (capex ≥ D&A) e é a mesma convenção da GOOGL (1,00x) — mas é a escolha favorável mais fraca do modelo.

### O que vai dizer qual é

| Observável | Quando | Transitório | Estrutural |
|---|---|---|---|
| Capex do Q2-27 (definição da gestão + ROU de op. leases) | 28-01-2027 | < $ 50 mM com Azure ≥ 49% | > $ 60 mM, ou guidance FY28 a subir |
| Leases por iniciar (10-Q, Nota 12) | Trimestral | A descer de $ 364,6 mM | A subir |
| Mix de vida curta | Trimestral (deck) | Volta para ~2/3 | Fica em ≥ 3/4 |
| Receita incremental por $ de capex (LTM) | Trimestral | ≥ 0,40 | < 0,30 |

---

## CENÁRIOS — três, nomeados, com os pressupostos à vista

*Probabilidades 25/50/25, declaradas antes de ver os valores (default; sem justificação de desvio). Calculados com `07_cenarios.py`. O base é o cenário da folha DCF.*

### 1. Infraestrutura comoditizada *(25%)*

**A história.** A procura de AI continua, mas concentra-se em poucos clientes que compram capacidade ao melhor preço — a OpenAI já é 10,8% da receita e a Microsoft vende-lhe a mesma GPU que a AWS e as neoclouds. O preço por token cai mais depressa do que a eficiência da frota. O capex já está contratado ($ 364,6 mM em leases por iniciar) e não pode ser cortado. A receita cresce 3 pp abaixo do consenso todos os anos e a margem perde 1,5 pp de cash opex para energia, capacidade de terceiros e partilha de receita.

| Pressuposto | Valor | Porquê |
|---|---|---|
| Crescimento | 15,5% → 3,0% *(CAGR 10,07%)* | −3 pp sobre o consenso: o Azure desacelera para ~30% em FY28 |
| Capex / receita | como no base (55,8% → 19,5%) | Comprometido em leases e encomendas |
| Cash opex / receita | 40,0% → 38,5% | +1,5 pp: pricing por token e mix de capacidade de terceiros |
| Resultado | margem EBIT mínima 35,3% (Y7), 40,5% no Y10; FCFF/receita Y10 33,5%; 1º FCFF positivo no Y3 | |
| **Valor** | **$ 308,45** @WACC · $ 265,09 @required | IRR ao preço de hoje: 7,50% |

**Sinais de que estamos aqui:** Azure cc abaixo de 35% num trimestre; Microsoft Cloud GM abaixo de 63%; receita OpenAI acima de 15% da receita; bookings negativos dois trimestres seguidos sem efeito de base.

### 2. O ciclo paga com atraso *(base, 50%)*

**A história.** O capex segue o consenso: ~56% da receita em FY27, a descer para ~35% em FY31. A receita acompanha, também como no consenso: +18,5% no Y1, +20% nos dois anos seguintes com o Azure perto de 50%, e um fade para 6% no Y10. A depreciação chega antes do lucro — a margem EBIT cai de 47% para 38,4% no Y4 —, e o capital investido ainda rende acima do custo. O ciclo paga, mas com atraso e com um parque de servidores maior para repor.

| Pressuposto | Valor | Porquê |
|---|---|---|
| Crescimento | 18,5% · 19,9% · 20,5% · 15,5% · 14,0% → 6,0% *(CAGR 13,08%)* | Q1-27 +18,8%; guidance Q2 +18–19%; consenso FY27-31 18,0 / 19,7 / 21,7 / 13,0 / 14,6% |
| Capex / receita | 55,8% · 52,9% · 49,7% · 40,4% · 35,3% → 19,5% | Consenso cash FY27-31 × 1,12; terminal ≥ D&A |
| Cash opex ex-D&A / receita | 38,5% → 37,0% | Q1-27 37,5% (sazonalmente baixo); guidance Q2 implica ~39,7%; LTM 40,6% |
| D&A | endógeno, por classe: 14,5% → 24,6% (Y4) → 18,9% | 75% a 6 anos, 25% a 25 anos, meio ano |
| Resultado | margem EBIT mínima 38,4% (Y4), 44,1% no Y10; FCFF/receita Y10 34,2%; 1º FCFF positivo no Y2 | |
| **Valor** | **$ 404,02** @WACC · $ 346,38 @required | IRR ao preço de hoje: 8,78% |

**Sinais de que estamos aqui:** Azure entre 35% e 50%; capex/receita LTM a estabilizar entre 45% e 55% até meados de 2027; RPO a crescer acima de 30%.

### 3. Os agentes monetizam *(25%)*

**A história.** A tese do Satya funciona: o Copilot passa de posto a consumo ("o novo OS do trabalho"), o Foundry torna-se a camada de agentes empresariais e a GitHub prova o modelo (agentes abrem mais de um terço dos PRs). A receita cresce 3 pp acima do consenso durante seis anos, com o mesmo capex do base — a eficiência da frota (+50% de throughput no Copilot num trimestre) deixa cada GPU servir mais receita. O opex melhora 1 pp por alavanca.

| Pressuposto | Valor | Porquê |
|---|---|---|
| Crescimento | 21,5% · 22,9% · 23,5% · 18,5% · 17,0% · 15,0% → 6,0% *(CAGR 15,18%)* | +3 pp no Y1-Y6 a convergir até ao Y10: Azure ≥ 50% e consumo de Copilot fora do coding |
| Capex / receita | como no base | A eficiência compra receita, não poupa capex |
| Cash opex / receita | 37,5% → 36,0% | −1 pp de alavanca |
| Resultado | margem EBIT mínima 40,8% (Y4), 45,8% no Y10; FCFF/receita Y10 34,9% | |
| **Valor** | **$ 491,35** @WACC · $ 420,85 @required | IRR ao preço de hoje: 9,85% |

**Sinais de que estamos aqui:** Azure ≥ 50% durante o FY27 *com* M365 commercial cloud a acelerar acima de 20%; receita de Copilot divulgada; seats a acelerar de novo acima de 7%.

*Variante do lado do custo — "A frota rende mais": receita do base, capex −5 pp do Y2 em diante, opex −1 pp → $ 440,65 @WACC, $ 380,06 @required. Escolhi a variante da receita como favorável porque é a que o preço desconta: o motor B pede crescimento, não capex mais baixo.*

### Leitura conjunta

| | Infraestrutura comoditizada | **O ciclo paga com atraso** | Os agentes monetizam | Ponderado |
|---|---|---|---|---|
| Probabilidade | 25% | 50% | 25% | — |
| Valor @WACC | $ 308,45 | **$ 404,02** | $ 491,35 | $ 401,96 |
| Valor @required | $ 265,09 | $ 346,38 | $ 420,85 | $ 344,67 |
| IRR ao preço de hoje | 7,50% | 8,78% | 9,85% | — |

A $ 545 o preço fica **acima dos três cenários** ao WACC. O mercado não está só a dar 100% de probabilidade ao cenário favorável (é o que o `07` mostra por interpolação): está a pagar mais do que ele vale a 10,47%. Ou desconta a uma taxa mais baixa, ou espera mais crescimento do que o consenso.

**Matriz cenário × taxa de desconto** — separa negócio de taxa:

| Cenário ＼ taxa | WACC anterior 9,12% | WACC −100 bp 9,47% | **WACC actual 10,47%** | Required 11,47% |
|---|---|---|---|---|
| Infraestrutura comoditizada | 389 | 365 | 308 | 265 |
| **O ciclo paga com atraso** | 511 | 479 | **404** | 346 |
| Os agentes monetizam | **623** | **583** | 491 | 421 |

*(A negrito, células acima do preço actual.)* Só o cenário favorável, a uma taxa de 9,5% ou menos, chega ao preço de hoje.

---

## SUMÁRIO EXECUTIVO

**Recomendação: esperar.** Fair value de **$ 404,02** ao WACC de 10,47% e de $ 346,38 ao required return de 11,47%, contra $ 545,00 — **−25,9%** e −36,4%. Não é *evitar*: o negócio fez neste trimestre tudo o que a tese pedia, e o capital novo continua a render acima do custo (ROIC marginal de 14,8%). Não é *entrada faseada*: nenhum dos três cenários nomeados vale o preço ao WACC, e o retorno oferecido (8,78%) está 269 bp abaixo do exigido.

### A tese numa frase

A Microsoft está a converter um negócio de software com ROIC de 26% num negócio de infraestrutura que agora tem um cliente a 11% da receita. A $ 545 o mercado paga a versão em que o capex compra crescimento acima do consenso durante uma década — e isso só é visível a uma taxa de desconto abaixo do meu custo de capital.

### Os financials, em vinte segundos

O FY27-Q1 teve receita de $ 92.279 M, **+18,8%** (consenso $ 90,69 mM), com o Agents and Infra a +24,5% ($ 76.795 M, 83% da receita) e o Devices and Consumer a −3,2%. O **Azure cresceu 48%** e foi divulgado em dólares pela primeira vez: $ 33.165 M, 36% da receita. O Microsoft Cloud fez $ 63,9 mM (+30%), com margem bruta de 66% (65% no Q4-26). A margem operacional GAAP subiu de 48,9% para **49,8%**: o opex cresceu 6% com o headcount a −2%. O net income GAAP subiu 32%, mas **+18% sem a OpenAI**, porque o Q1-26 tinha uma perda de $ 4,1 mM nessa participação: o crescimento real do lucro é o da receita. O único ajuste non-GAAP é esse, de −0,6% do lucro deste trimestre, e o SBC é 3,4% da receita. O que mudou de natureza está no cash flow e no balanço. O CFO subiu 29% para $ 58,0 mM, mas o capex cash dobrou (+103%, $ 39,4 mM) e o FCF caiu 27% para $ 18,6 mM. A caixa desceu $ 12,3 mM num trimestre, para $ 64,5 mM. A OpenAI passou a 10,8% da receita. Há $ 364,6 mM de leases por iniciar. E a CFO anunciou pela primeira vez que vai a mercado buscar financiamento. A reclassificação de finance para operating leases já se vê: $ 6,5 mM de ROU de operating leases no trimestre, contra $ 1,4 mM no homólogo, fora do capex reportado.

### O DCF — pressupostos e resultado

| Pressuposto | Y1 → Y10 | Âncora histórica |
|---|---|---|
| Crescimento da receita | 18,5% · 19,9% · 20,5% · 15,5% · 14,0% → 6,0% (CAGR 13,08%) | Q1-27 +18,8%; guidance Q2 +18–19%; consenso FY27-31; FY22-26 13,74% |
| Cash opex ex-D&A *(SBC dentro)* | 38,5% → 37,0% | LTM 40,6%; Q1-27 37,5%; guidance Q2 ~39,7% |
| Capex / receita *(definição da gestão)* | 55,8% → 19,5% | LTM 44,9%; Q1-27 49,0%; consenso cash × 1,12 |
| D&A | endógeno, por classe: 14,5% → 24,6% (Y4) → 18,9% | Servidores 75% a 6 anos, edifícios 25% a 25 anos, meio ano; carteira em três tranches |
| Imposto · NWC | 20% → 21% · 0% | Guidance ~20%; média FY24-26 do NWC = fonte de 9,1% |
| WACC · g perpétuo | 10,47% · 2,5% | Ke 10,64%; peso da dívida 2,6% |
| SOTP | OpenAI: $ 102.240 M na ponte ($ 13,73/acção) | 24% × $ 852 mM (ronda de Abr-2026, Bloomberg Law) × 50% |

**Resultado:** EV de $ 2.948.068 M (`DCF!B15`) contra $ 3.997.775 M de mercado; **$ 404,02 por acção**. No reverse DCF, o preço oferece **8,78%** (motor A). Para render 11,47%, a receita teria de crescer **19,23% ao ano durante dez anos** (motor B), e para render o WACC, 17,08%. Pelo lado do capex não há solução: o motor D pede capex de 8,28% da receita no Y10, abaixo do D&A.

**Três honestidades obrigatórias.** *Primeira:* o terminal pesa **68,7%** do EV (`DCF!B16`), com saída a 7,0x EV/EBITDA — baixo porque o terminal ainda carrega capex de 19,5%. Em EV/FCFF é 12,9x, e no ano 5 o `06` lê 8,3x EV/EBITDA, 15,8x EV/(EBITDA−capex) e 20,8x EV/FCFF. *Segunda:* a margem EBIT cai de 47% para 38,4% no Y4 com o D&A a 24,6% da receita, enquanto o consenso a mantém nos 46%. O D&A só pesa no FCFF pelo escudo fiscal, mas é a razão pela qual o meu EBIT de FY28-30 fica 5–8 pp abaixo do da rua. *Terceira:* a amplitude por driver.

| Driver | Cenário adverso | Valor/ação | Δ vs base |
|---|---|---|---|
| **Crescimento da receita** | −3 pp/ano | $ 322,17 | −$ 81,85 |
| WACC *(não é eixo)* | +100 bp | $ 346,36 | −$ 57,66 |
| **Capex / receita** | +5 pp | $ 341,18 | −$ 62,84 |
| g perpétuo *(não é eixo)* | 1,5% | $ 371,32 | −$ 32,70 |
| Cash opex / receita | +3 pp | $ 370,12 | −$ 33,90 |
| Taxa de imposto | +5 pp | $ 373,45 | −$ 30,57 |

**G15, frase obrigatória.** Contra os factos o base inclina-se para o lado **favorável** em 7,55%: o cash opex terminal (37,0%) está 2,7 pp abaixo do implícito no guidance do Q2 (39,7%), e repô-lo leva o base a $ 373,51. Do lado cauteloso, o imposto e o NWC valem +4,14%. A âncora estrutural foi dispensada (sem comparáveis, decisão escrita do Hugo), por isso o opex terminal só tem o facto e o consenso como travão.

**G20, frase obrigatória.** O base implica um ROIC marginal de 17,3% até ao Y5 e de 35,0% no Y10, e $ 0,33 de receita nova por dólar de capex contra $ 0,47 no histórico (70%). O `02` sinaliza atenção porque o Y10 fica acima de 1,5x os 14,35% de referência. Esses 14,35% são um marginal de um ano, medido a meio da construção, antes de a capacidade nova facturar. O ROIC médio é 25,6% — a leitura honesta é que o base não é optimista nos retornos, mas fica a escrita.

### Os múltiplos — e se contradizem o DCF

*Contra a mediana própria* (seis trimestres do CapIQ, Jun-25 a Set-26 — não há três anos no export): EV/EBITDA LTM de 19,5x contra 19,5x e NTM de 15,6x contra 16,6x. O múltiplo voltou ao nível de 2025, depois de ter descido a 14,2x em Junho. *Contra peers:* não actualizado e, por decisão do Hugo, sem peer set. *Contra o trimestre corrente anualizado:* o Q1-27 × 4 dá EV/EBITDA de 17,3x, EV/EBIT de 21,8x e EV/receita de 10,8x, contra 19,5x, 24,5x e 11,5x LTM. O múltiplo desce quando se anualiza o trimestre, portanto o lucro está a crescer. Os múltiplos não contradizem o DCF: dizem que a acção está no nível de 2025, quando o capex era metade do de hoje.

### Qual das fontes é mais credível aqui

**Governa o DCF**, por três razões específicas. *Primeira:* a mediana de seis trimestres apanha um de-rating e um re-rating completos (24,7x → 14,2x → 19,5x), e é uma série curta sobre um activo que mudou de intensidade de capital. *Segunda:* o EBITDA forward do consenso tem D&A de 14–15% com capex de 50% — inconsistente com servidores a seis anos —, pelo que os múltiplos de EBIT forward estão inflacionados. *Terceira:* o DCF projecta capex e não depreciação reportada, e não é afectado pela extensão da vida útil para 25 anos nem pela reclassificação de leases. Contra o DCF pesa o terminal de 68,7% e a amplitude de $ 183,84 no crescimento. O cross-check independente é o reverse DCF: 17,1% de CAGR para render o WACC é uma afirmação falsificável, e está acima do que a empresa entregou.

### Se comprar a X, ganho quanto por ano?

*(Saída do `06_retorno.py --md`, colada.)*

| Preço | EV/EBITDA NTM à entrada | Retorno total 5a | **Anualizado, com re-rating** | Sem re-rating | Re-rating |
|---|---|---|---|---|---|
| $ 545,00 *(preço actual)* | 15,8x | +21,95% | **4,05%** | 8,78% | −4,74% |
| $ 404,02 *(fair value @WACC)* | 11,7x | +64,50% | **10,47%** | 10,47% | +0,00% |
| $ 346,38 *(1ª tranche)* | 10,0x | +91,88% | **13,92%** | 11,47% | +2,45% |
| $ 344,67 *(2ª tranche)* | 9,9x | +92,83% | **14,03%** | 11,50% | +2,53% |
| $ 277,19 *(posição cheia)* | 7,9x | +139,77% | **19,11%** | 13,09% | +6,02% |

**Heatmap — IRR a 5 anos ao preço de hoje ($ 545,00)**, por crescimento da receita × EV/(EBITDA−capex) de saída. O `06` escolheu esta base porque o capex do Y6 é 48% do EBITDA.

| Crescimento da receita ＼ EV/(EBITDA−capex) de saída | 11,0x *(= 5,8x EBITDA)* | 13,4x *(= 7,0x)* | 15,8x *(DCF; = 8,3x)* | 18,1x *(= 9,5x)* | 20,5x *(= 10,7x)* |
|---|---|---|---|---|---|
| −2 pp | −4,42% | −0,98% | 2,03% | 4,62% | 7,07% |
| −1 pp | −3,48% | −0,00% | 3,05% | 5,67% | 8,15% |
| base | −2,54% | 0,98% | **4,07%** | 6,72% | 9,23% |
| +1 pp | −1,59% | 1,97% | 5,10% | 7,78% | 10,32% |
| +2 pp | −0,65% | 2,96% | 6,13% | 8,84% | 11,41% |

A coluna "hoje" foi omitida: o EV/(EBITDA−capex) NTM de hoje é 170,8x, sem significado nesta base. A $ 545, **8,78% é negócio** (o retorno sem re-rating) e **−4,74 pp é de-rating** até ao fair value. O retorno com re-rating é 4,05%. Só com saída acima de ~20x EBITDA−capex (≈10,7x EBITDA) e crescimento +2 pp a IRR chega a 11%.

### Porque não é a recomendação adjacente, e o que a mudaria

**Probabilidades declaradas antes de ver os valores:** Infraestrutura comoditizada 25% · O ciclo paga com atraso 50% · Os agentes monetizam 25% *(default)*.

| Banda | Preço | Racional | Assimetria favorável:adverso @WACC | Peso máx. |
|---|---|---|---|---|
| Preço actual | $ 545,00 | IRR esperada 8,79% · IRR base 8,78% | −0,23x (nenhum cenário acima do preço) | 3,89% |
| **1ª tranche** | **$ 346,38** | **Valor base** ao required return | 3,82x | — |
| **2ª tranche** | $ 344,67 | **Valor ponderado** ao required return | 4,05x | — |
| **Posição cheia** | $ 277,19 | Base com o driver dominante adverso (crescimento −3 pp) ao required return | sem downside até ao adverso | — |

**A escada trocou os dois primeiros degraus:** o ponderado ($ 344,67) saiu abaixo do base ($ 346,38) porque o adverso perde mais do que o favorável ganha. Abaixo de $ 369,42 a assimetria passa 2,0x. A $ 545 o retorno oferecido está 269 bp abaixo do exigido, e mesmo o favorável rende 9,85%. Mudam a recomendação os invalidadores do bloco A: contra a tese, capex/receita LTM acima de 50% (#1, hoje 44,9%), Microsoft Cloud GM abaixo de 63% (#2) ou receita da OpenAI acima de 15% (#8). A favor, o que o cenário 3 pede: Azure ≥ 50% durante o FY27 com o M365 a acelerar. Nenhum destes muda o valor o suficiente para chegar a $ 545 ao WACC de hoje. O que muda a decisão a curto prazo é o preço ou a taxa.

**Prémios aplicados** — nenhum risco cobrado duas vezes.

| Prémio | Aplicado? | Valor | Risco que cobre | Sobrepõe-se a outro? |
|---|---|---|---|---|
| CRP *(Damodaran ctryprem)* | Não | 0 | — (receita quase toda em mercados desenvolvidos; 54% nos EUA) | — |
| Hurdle *(nível 2 — WACC + 100 bp, decisão do Hugo 29-10-2026)* | Sim | +100 bp | Alocação de capital num capex de ~$ 220 mM/ano com financiamento externo anunciado, e concentração na OpenAI (10,8%) | Não — o beta mede covariância com o mercado, não a concentração num cliente nem o retorno do capex |
| ERP acima do implícito *(5,0% vs 4,20% Damodaran Out-26)* | **Sim — implícito** | +80 bp no ERP, ≈ −$ 65/acção | Nenhum risco específico: é uma escolha de mercado para toda a carteira | **Ver nota** |
| Fade terminal abaixo da âncora estrutural | n/a | — | Sem âncora (dispensada) | — |

**Nota sobre o ERP.** O G19 (método A) pede Rf do dia mais ERP implícito do Damodaran do mesmo mês. Segundo a ficha GOOGL, esse ERP é **4,20%** (Damodaran, 1-Out-2026), e é o que a GOOGL usa. A META e esta ficha usam 5,0% por decisão do Hugo. São duas convenções na mesma carteira, e as três mega-caps deixaram de ser comparáveis entre si. A 4,20% o base vale **$ 469,12** ($ 396,38 ao required). **Decisão pendente do Hugo:** uniformizar o ERP nas três fichas.

**Próximo catalisador:** FY27-Q2 a 28-01-2027. Antes disso, as revisões do sell-side depois do Q1, que ainda não estão no export, e os termos do financiamento externo anunciado.

---

## 1. Negócio — o que vende

A Microsoft vende três coisas economicamente distintas sob uma marca. **Assinaturas de produtividade e segurança** a quase todas as organizações do mundo ocidental, por posto e cada vez mais por consumo (GitHub Copilot, créditos de Copilot). **Capacidade de computação e serviços de plataforma** através do Azure e do Foundry, cobrados por consumo, onde o custo escala com o uso e exige capital à frente da receita. E **software e hardware de consumo** — Windows OEM, Xbox, publicidade — maduro, a encolher, que financia o resto.

A tensão estrutural mantém-se e agravou-se: o primeiro negócio não consome capital, o terceiro decresce (Windows OEM −22% no Q1-27), e o segundo — Azure, 36% da receita, +48% — concentra o crescimento, o capital e agora um cliente a 10,8%.

**Segmentos** *(FY27-Q1, nova estrutura anunciada em Set-2026 e recast pela empresa — G6)*

| Segmento | % receita | Receita Q1-27 | Margem operacional | O que é | Cliente-tipo |
|---|---|---|---|---|---|
| Agents and Infra | 83,2% | $ 76.795 M (+24,5%) | 52,8% *(53,1% no Q1-26)* | Azure, M365 cloud, licenciamento de produtividade e servidores, Industry solutions (Dynamics, LinkedIn Talent), Frontier and support | Empresas e developers |
| Devices and Consumer | 16,8% | $ 15.484 M (−3,2%) | 34,6% *(32,8%)* | Windows OEM e dispositivos, Xbox, Search e publicidade, M365 consumer | OEMs, consumidores, anunciantes |

**Linhas de produto** *(Q1-27, 10-Q Nota 16)*

| Linha | Receita | % | YoY |
|---|---|---|---|
| Azure | $ 33.165 M | 35,9% | +48% |
| Microsoft 365 cloud | $ 27.778 M | 30,1% | +17% |
| Productivity and server licensing | $ 8.407 M | 9,1% | −3% |
| Search and advertising | $ 6.554 M | 7,1% | +10% |
| XBOX | $ 5.379 M | 5,8% | −2% |
| Industry solutions | $ 5.337 M | 5,8% | +9% |
| Windows OEM and devices | $ 3.551 M | 3,8% | −22% |
| Frontier and support services | $ 2.108 M | 2,3% | +4% |

**Métricas de escala** *(FY27-Q1, deck e 10-Q)*

- **Microsoft Cloud: $ 63,9 mM**, +30% (+31% cc); gross margin 66% (68% no Q1-26, 65% no Q4-26). Guidance Q2: ~65%.
- **RPO comercial: $ 677 mM**, +73% YoY e plano QoQ (678); duração média de 2,3 anos; ~30% em 12 meses (+29%), o resto +98%.
- **Commercial bookings: −12%** (−11% cc), contra +112% no homólogo.
- **Azure +48%**; guidance Q2 49–50% cc. **M365 commercial cloud +17%** (+18% ajustado); **seats +5%** (7% no Q4-26) com "weaker sales execution" no E3. **M365 consumer +17%**. **Industry solutions cloud +10%**, com bookings a moderar.
- **Windows OEM −27%**, com inventário de canal elevado; Q2 guiado em "mid-thirties" negativos.
- Capex da gestão de $ 45,2 mM (+30%), cash $ 39,4 mM (+103%); PP&E líquido $ 346.844 M (era $ 313.076 M em Jun-26).

**Exposição geográfica.** EUA $ 49.459 M (53,6%), resto do mundo $ 42.820 M. O 10-Q diz que nenhum país fora dos EUA passa os 10%.

**Concentração de clientes — CORRIGIDO face a Julho.** A ficha de Julho citava o 10-K FY26: "no sales to an individual customer or country other than the United States accounted for more than 10%". O 10-Q do Q1-27 **já só fala de países**. Pela divulgação de related party (Nota 3), a receita de acordos comerciais com a OpenAI, incluindo revenue-sharing, foi **$ 10,0 mM no trimestre, 10,8% da receita**, com $ 7,2 mM em contas a receber (11,6% do AR; eram $ 6,0 mM em Junho). A OpenAI é ao mesmo tempo cliente do Azure, investida a ~24% e fornecedora de modelos — a única relação individual cuja deterioração teria efeito material, e agora acima do limiar. *Erro de Julho registado no changelog: a ficha afirmava ausência de concentração sem ler a nota de related party.*

---

## 2. Vantagem competitiva — porquê esta e não a rival

**Rival de referência: Amazon Web Services** *(mantido de Julho)*. É o único concorrente com escala instalada superior em infraestrutura e a mesma dependência de capex, e a disputa decide-se em cargas empresariais — onde a Microsoft tem a relação de licenciamento que a Amazon não tem.

| Dimensão | Microsoft | AWS (Amazon) | Quem ganha, e porquê |
|---|---|---|---|
| Produto / tecnologia | Stack completo: OS, produtividade, identidade, dados, cloud, modelos próprios (MAI) e de terceiros | Infraestrutura mais profunda, catálogo maior, chips próprios (Trainium) | **AWS** em infraestrutura pura; **MSFT** em cargas empresariais integradas |
| Distribuição e go-to-market | Contrato de licenciamento já assinado com quase todas as grandes empresas | Vendas directas e canal | **MSFT**, por margem larga |
| Pricing power | Alto no M365 (ARPU a subir com E5/E7/Copilot), mas seats a abrandar (+5%); moderado no Azure, com o token pricing a variar trimestre a trimestre | Compete em preço | **MSFT** — no software, não na cloud |
| Escala | PP&E $ 346.844 M; capex ~$ 170 mM em CY26 | Capex superior em valor absoluto | Empate |
| Custo de mudança | **Muito alto**: Entra, dados no M365 (Work IQ), Agent 365 | Alto, confinado à infraestrutura | **MSFT** |
| Economia unitária | Margem operacional 49,8% no Q1-27; Agents and Infra 52,8% | Margem do segmento AWS estruturalmente inferior | **MSFT**, pelo mix |

**Onde aparece o diferencial.** Na margem operacional de 49,8% com o Azure a crescer 48% sobre uma base de $ 133 mM anualizados. No RPO de $ 677 mM. E, neste trimestre, na eficiência: a gestão monetizou capacidade de CPU subutilizada e realocou GPUs para o Foundry sem capex adicional — o Azure bateu as expectativas *apesar* dos atrasos de capacidade de terceiros.

**Onde NÃO aparece.** No FCF, que caiu 27% num trimestre de receita +19%. Na margem bruta do Microsoft Cloud, a cair de 68% para 66% YoY pelo mix de Azure. Na concentração: a OpenAI a 10,8% da receita, quando o próprio CEO diz na call que "quatro clientes que compram muita capacidade" não são um negócio. **A assimetria mantém-se:** o moat está intacto no software; no negócio de infraestrutura que absorve o capital há vantagem de distribuição e, agora, dependência de um cliente.

---

## 3. Monetização — de onde vem exactamente o dinheiro

| Fluxo | % receita *(Q1-27)* | Unidade cobrada | Quem paga | Recorrente? |
|---|---|---|---|---|
| Azure (inclui Foundry e GPU IaaS) | 35,9% | Consumo (compute-hora, GB, tokens) | Empresas, developers, labs de AI (OpenAI) | Sim, variável com o uso |
| Microsoft 365 cloud (comercial + consumo; inclui GitHub Copilot e segurança) | 30,1% | Posto/mês + consumo (créditos) | Empresas e consumidores | **Sim** |
| Licenciamento de produtividade e servidores | 9,1% | Licença + suporte | Empresas | Parcialmente |
| Industry solutions (Dynamics, LinkedIn Talent/Sales) | 5,8% | Posto, subscrição | Empresas | Sim |
| Search e publicidade | 7,1% | CPC, impressão | Anunciantes | Misto |
| XBOX | 5,8% | Conteúdo, Game Pass | Consumidores | Misto |
| Windows OEM e dispositivos | 3,8% | Por licença/dispositivo | OEMs | **Não** |
| Frontier and support | 2,3% | Contrato | Empresas | Sim |

**Mecânica do fluxo principal.** Mantém-se a de Julho: o Enterprise Agreement plurianual cobre M365 e compromissos de Azure, e o compromisso não consumido fica no RPO. A Microsoft é paga antes de servir: o unearned revenue era $ 69.563 M em Set-26 (−$ 6.149 M no trimestre, sazonal; o padrão do Q1 é a facturação anual de Julho a ser reconhecida).

**Alavanca nova — do posto ao consumo.** A gestão descreve a passagem de "per-seat subscriptions" para "consumption, expanding our TAM and ARPU": os clientes de Copilot com consumo de créditos cresceram 75% no trimestre, e o consumo agêntico no GitHub "mais do que duplicou" desde a faturação por uso. **Isto inverte parcialmente a assimetria de Julho** (posto fixo com custo por token): no consumo o preço acompanha o custo. Ainda sem número de receita de Copilot divulgado ("did not disclose").

**Qualidade da receita.** Alta, mas mais concentrada do que a ficha assumia: 10,8% vem de um cliente que é também investida. O RPO de $ 677 mM inclui "large Azure commitments", e o 10-Q não diz quanto é OpenAI. Sem NRR nem duração por cliente — não estimo.

**Assimetria de monetização vs custo.** A margem bruta do Microsoft Cloud caiu de 68% para 66% YoY e é guiada a ~65% no Q2, "as continued improvement in product-level margins is more than offset by sales mix shift to Azure". É exactamente a linha que o invalidador #2 vigia, e está a 2–3 pp do threshold.

---

## 4. Moat — porque é que isto não é replicável

| Tipo de moat | Presente? | Evidência quantitativa | Força |
|---|---|---|---|
| Network effects | Parcial | GitHub (agentes abrem mais de 1/3 dos PRs); LinkedIn (1,4 mil M de membros) | Moderado |
| **Switching costs** | **Sim** | RPO comercial $ 677 mM; Entra, Work IQ, Agent 365 (50 M de agentes no registo, +30% QoQ) | **Muito forte** |
| Economias de escala | Sim | 24 datacenters novos num trimestre; PP&E $ 346.844 M | Forte, partilhado com AWS e Google |
| Intangíveis | Sim | Direitos sobre a IP da OpenAI (modelos e infraestrutura); MAI próprio | Forte, com dependência de terceiro |
| Vantagem de custo estrutural | **A emergir** | Maia 200 (1,7x tokens por watt), throughput de Copilot +50% QoQ, dock-to-live −20% | Por provar em margem: MS Cloud GM a cair |
| **Eficiência de distribuição** | **Sim** | Azure vendido dentro do EA; E7 com "milhões de postos pagos" | **Muito forte** |

**Teste do capital ilimitado** *(mantido de Julho)*. O dinheiro compra datacenters, GPUs e engenheiros. Não compra o contrato de licenciamento assinado com 400 mil organizações, nem a identidade e os documentos dos utilizadores já no Entra e no SharePoint. E $ 10 mM não chegam: a Microsoft gastou 4,5x isso só no Q1-27.

**O que erode o moat, e a que velocidade.** (i) Comoditização de modelos — **já observável**: o Satya descreve clientes a passar da fronteira para open weights e para modelos próprios treinados nos seus traces. É bom para o Foundry como orquestrador e mau para quem vende acesso preferencial a um modelo. Horizonte 1–3 anos. (ii) Concentração na OpenAI, que pode deslocar consumo para outras clouds — o 10-Q diz que "strategic partners... may adjust their purchasing decisions". (iii) Fadiga de preço no M365, onde os seats abrandaram para +5%. **Trajectória: a alargar na distribuição, a estreitar na economia.** RPO +73%, ROIC marginal a 14,8%.

### O moat converte-se em economia? O teste do ROIC

| | FY2025 | FY2026 | **LTM Set-26** |
|---|---|---|---|
| EBIT | 128.528 | 155.237 | 163.191 |
| Taxa efectiva | 17,63% | 19,40% | 19,68% |
| NOPAT | 105.869 | 125.127 | 131.069 |
| Capital investido *(equity + dívida + finance leases − cash e ST)* | 338.237 | 472.432 | 512.454 |
| **ROIC** *(capital fim de período)* | **31,30%** | **26,49%** | **25,58%** |
| Spread vs WACC de 10,47% | +2.083 bp | +1.602 bp | **+1.511 bp** |

Bases de Julho mantidas: capital médio FY26 30,87%; NOPAT normalizado da amortização de aquisições sem diferença material (intangíveis de $ 18.609 M para $ 17.751 M, sem aquisições relevantes).

| | FY25 → FY26 | **Jun-26 → Set-26 (LTM)** |
|---|---|---|
| Capital investido acrescentado | +134.195 | +40.022 |
| Δ NOPAT normalizado | +19.258 | +5.942 |
| **ROIC marginal** | **14,35%** | **14,8%** |
| WACC | 10,47% | 10,47% |
| **Spread** | +388 bp | +438 bp |

O marginal **estabilizou** em ~14–15%, acima do WACC corrigido de 10,47% mas com metade da folga de Julho (era +523 bp contra o WACC de então, de 9,12%). O capital novo continua a criar valor, e a margem para erro é menor do que parecia. *Cruzamento com o Return on Capital % da folha Ratios do CapIQ: pendente — lacuna mantida.*

---

## 5. SWOT

**Forças** *(internas, presentes)*
- Margem operacional de **49,8%** no Q1-27 com receita +18,8%; Agents and Infra a 52,8%.
- **RPO comercial de $ 677 mM** (+73%), 2,3 anos de duração média.
- Azure a **+48%** e guidance de 49–50% com a capacidade de terceiros atrasada: a eficiência da frota está a libertar oferta.
- SBC a **3,4% da receita**: o lucro GAAP é economicamente real.
- Dívida financeira de $ 35.481 M (reembolsou $ 4.850 M no trimestre), rating que a CFO descreve como acesso aberto ao mercado de dívida.

**Fraquezas** *(internas, presentes — as reais)*
- **Cliente a 10,8% da receita** (OpenAI), também investida e fornecedora.
- **FCF de $ 18,6 mM, −27%**, com capex cash +103%; a caixa caiu $ 12,3 mM num trimestre.
- ~3/4 do capex em activos de vida curta: obrigação de reinvestimento permanente.
- **Seats M365 a +5%** e "weaker sales execution" no E3 — o motor de software abranda na base.
- Commercial bookings −12% e Industry solutions com bookings a moderar.

**Oportunidades** *(externas, com dimensão)*
- Consumo de Copilot fora do coding: a gestão diz que o M365 commercial cloud acelera ao longo do ano (~19% cc no Q2). Cada +1 pp de crescimento do grupo durante 10 anos vale ~$ 30/acção (G13).
- Foundry como camada multi-modelo: 120 mil clientes, receita a triplicar.
- OpenAI cotada ou numa nova ronda: a participação de ~24% está no SOTP a 50% de uma marcação de Abril ($ 13,73/acção). A 100% vale $ 27,46.

**Ameaças** *(externas, com probabilidade e horizonte)*
- **Sobrecapacidade de compute:** $ 364,6 mM de leases contratadas até FY34 — probabilidade média, horizonte 2–3 anos. É o cenário 1.
- **Comoditização dos modelos de fronteira** — alta, 1–3 anos, já descrita pela própria gestão.
- **Deslocação do consumo da OpenAI para outras clouds** — média, 1–2 anos; o 10-Q (Item 1A) passou a falar de "strategic partners... significant customers of Azure" que "may adjust their purchasing decisions".
- **Custo de capital:** com o UST 10Y a 4,99%, cada +100 bp no WACC vale −$ 57,66/acção.
- Antitrust na UE e escrutínio à parceria OpenAI — média, 2–4 anos, não quantificável.

---

## 6. Legal, regulatório e fiscal

| Matéria | Tipo | Estado | Exposição máx. | % market cap | Timeline |
|---|---|---|---|---|---|
| Impostos — exames do IRS e jurisdições estrangeiras | Fiscal | Em curso | Long-term income taxes $ 29.235 M | ~0,7% | Plurianual |
| Irish Data Protection Commission — LinkedIn | Privacidade | Em curso (desde 2018; 10-Q Nota 13) | Não quantificado | n/d | Em curso |
| Escrutínio a licenciamento cloud (UE) | Antitrust | Em curso | Não quantificado | n/d | 2–4 anos |
| Parceria OpenAI — escrutínio concorrencial | Antitrust | Em curso | Não quantificado | n/d | 2–4 anos |

**Risco fiscal.** ETR de 20,3% no Q1-27, guidance de ~20%. **Antitrust.** Sem novidade material no trimestre.

**Factores de risco — o que o 10-Q do Q1-27 diz agora** *(Item 1A; comparação com o 10-K FY25 continua por fazer)*. Três passagens com linguagem que não estava na ficha de Julho: (i) os investimentos de AI "require substantial and increasing capital expenditures and **continued access to capital**", e alterações de taxas, crédito ou rating "could increase our cost of capital or limit our ability to execute our infrastructure strategy"; (ii) "overestimation of demand... may result in underutilization of infrastructure and may lead to **impairment of assets**"; (iii) os parceiros estratégicos "in some cases... are **significant customers of Azure**" e "expected consumption... may not materialize, may be delayed or reduced". *Não consigo dizer se são novas sem o 10-K FY25 — a lacuna #1 de Julho mantém-se, agora com estas três frases como ponto de partida.*

---

## 7. Enquadramento de valuation

### Que métricas são as certas

| Múltiplo | Usar? | Porquê / porque não |
|---|---|---|
| P/E GAAP | Referência | 28,5x LTM. O lucro inclui ganhos e perdas da OpenAI (o Q1-26 teve −$ 4,1 mM) |
| P/E ajustado (ex-OpenAI) | Sim, para crescimento | É a definição da empresa e afasta o ruído do equity method; o fosso GAAP/non-GAAP é só esse |
| EV/EBITDA | Âncora secundária | 19,5x LTM. Não vê o capex de 49% da receita |
| EV/Receita | Cross-check | 11,5x LTM, 10,8x no Q1 anualizado |
| P / NTM EPS | Sim | 26,0x — sobre um consenso cujo D&A está abaixo do que o capex implica |
| **EV/FCF** | **Sim — o que decide** | 66,7x cash, **99,3x** na definição da gestão |
| Específico | RPO, Azure cc, receita OpenAI / receita | Os três números que movem a acção e a tese |

**Métrica âncora: DCF de FCFF**, com EV/FCF da gestão como alarme. **Peers:** nenhum, por decisão do Hugo (29-10-2026) — os múltiplos comparam-se só com a própria história, como na GOOGL. O peer set saneado de Julho (ORCL, NVDA, GOOGL, AMZN, CRM, ADBE; NTM EV/EBITDA mediano 11,03x) fica como registo, não actualizado. **Armadilhas conhecidas:** (i) o **TEV do CapIQ mudou de definição entre Junho e Setembro**: em Jun-26 tinha dívida de 128.813 (com finance leases e op. leases); em Set-26 tem 57.200 = dívida 35.481 + op. leases LT 21.719, sem os $ 70.973 M de finance leases (G18); (ii) o D&A do Q1-26 no CapIQ (13.061) não é a série recast do 10-Q (8.147); (iii) a vida útil de 25 anos e a passagem para operating leases reduzem o D&A e o capex reportados sem mudar a economia.

### O múltiplo é barato porque o preço caiu, ou porque o lucro caiu?

| | LTM Set-26 | Mediana própria *(6 trim.)* | **Q1-27 anualizado** |
|---|---|---|---|
| EV / Receita | 11,54x | n/d | **10,83x** |
| EV / EBITDA | 19,47x | 19,5x | **17,33x** |
| EV / EBIT | 24,50x | 21,9x | **21,77x** |

*(EV a $ 545 com finance leases e sem a OpenAI = `Inputs!B15`. Folha `Crosscheck`.)* O múltiplo **não está barato**: está na mediana própria em EBITDA e 12% acima em EBIT, e só desce quando se anualiza o trimestre, porque o lucro cresce. Ao contrário de Julho, a acção já não está em de-rating — recuperou-o todo.

### Decomposição de qualquer colapso de margem

**Não há colapso.** A margem operacional GAAP subiu de 48,9% (Q1-26) para 49,8% (Q1-27) contra o homólogo (G11). A margem bruta caiu 1,2 pp (69,0% → 67,8%), mais do que compensada pela alavanca no opex (20,2% → 18,0% da receita). O único item non-GAAP está fora do EBIT (OpenAI em other income). No Devices and Consumer a margem sobe de 32,8% para 34,6% pela amortização da Activision a correr off (G5) — não é operação.

**Coerência obrigatória.** A compressão que o modelo projecta (EBIT de 47% para 38,4% no Y4) é depreciação de infraestrutura, permanente e operacional, e não amortização que corre off. O invalidador de margem (#2) continua definido sobre a **margem bruta do Microsoft Cloud** e não sobre a margem operacional consolidada.

### Três lentes, três veredictos

| Lente | Veredicto |
|---|---|
| vs história própria de múltiplos | **Neutro** — EV/EBITDA LTM na mediana de seis trimestres; EBIT 12% acima |
| vs peers | n/a — decisão do Hugo |
| DCF | **Caro** — $ 404,02, −25,9%; o preço só fecha com o cenário favorável a uma taxa ≤ 9,5% |

As lentes discordam, e a discordância é a mesma da GOOGL: o múltiplo mede o lucro de hoje e o DCF mede o caixa depois do capex. Governa o DCF.

### Os drivers dominantes — por sensibilidade, não por intuição (G13)

Bandas definidas antes de olhar para o resultado: crescimento ±3 pp, WACC ±100 bp, capex ±5 pp, g ±1 pp, cash opex ±3 pp, imposto ±5 pp, NWC −2/+4 pp, vida do capex novo +2,7/−1,8 anos (`03_sensibilidade.py`, folha `Cenarios`).

| Driver | Banda | Favorável | Adverso | Amplitude |
|---|---|---|---|---|
| **1. Crescimento da receita** | ±3 pp | $ 506,01 | $ 322,17 | **$ 183,84** |
| 2. WACC *(não é eixo)* | ∓100 bp | $ 479,23 | $ 346,36 | $ 132,87 |
| **3. Capex / receita** | ∓5 pp | $ 466,86 | $ 341,18 | **$ 125,68** |
| 4. g perpétuo *(não é eixo)* | ±1 pp | $ 446,11 | $ 371,32 | $ 74,79 |
| 5. Cash opex / receita | ∓3 pp | $ 437,93 | $ 370,12 | $ 67,81 |
| 6. Taxa de imposto | ∓5 pp | $ 434,60 | $ 373,45 | $ 61,15 |
| 7. NWC / Δ receita | −2 / +4 pp | $ 406,35 | $ 399,37 | $ 6,99 |
| 8. Vida do capex novo | +2,7 / −1,8 anos | $ 400,12 | $ 406,41 | $ 6,29 |

**Grelha — capex (linhas) × crescimento (colunas)**, valor por acção ao WACC de 10,47% (motor local, folha `Cenarios`):

| Capex ＼ crescimento | −3 pp | −1,5 pp | **base** | +1,5 pp | +3 pp |
|---|---|---|---|---|---|
| +5 pp | $ 272 | $ 305 | $ 341 | $ 382 | $ 428 |
| +2,5 pp | $ 297 | $ 333 | $ 373 | $ 417 | $ 467 |
| **base** | $ 322 | $ 361 | **$ 404** | $ 452 | $ 506 |
| −2,5 pp | $ 347 | $ 389 | $ 435 | $ 487 | **$ 545** |
| −5 pp | $ 373 | $ 417 | $ 467 | $ 522 | $ 584 |

O preço de hoje está na célula **capex −2,5 pp e crescimento +3 pp**: o mercado paga as duas coisas ao mesmo tempo.

**Coerência interna, nos dois sentidos.**

- **Alavanca operacional coerente com a receita.** O cash opex melhora 1,5 pp em cinco anos com a receita a crescer 14–20%, e estabiliza com o fade.
- **G14 — o capex está modelado a descer** quando o Q1-27 foi 49,0% (56% com op. leases). É eixo de cenário e tem o invalidador #1 ligado.
- **G15 — Tabela 1** *(04_reversao.py)*:

| Driver | Tipo | No modelo | Referência | Fonte | Direcção | Efeito no valor/acção |
|---|---|---|---|---|---|---|
| Crescimento | facto | Y1 18,5% | 18,5% | Q1-27 +18,8%; guidance Q2 +18–19% (trailing no Y1, mesmo fade) | em linha | $ 0,00 |
| Cash opex | facto | Y10 37,0% | 39,7% | Implícito no guidance do Q2-27 | **favorável** | −$ 30,51 |
| Capex | facto | Y10 19,5% | 19,5% | Condição de estado estacionário (armadilha 1: não é driver favorável) | em linha | $ 0,00 |
| Imposto | facto | Y10 21,0% | 20,0% | Guidance FY27 ~20% | conservador | +$ 6,12 |
| NWC | facto | 0% | −9,1% | Média FY24-26 das linhas do CF (fonte de caixa) | conservador | +$ 10,60 |

**Tabela 2 — reversão cumulativa**

| Passo | Driver reposto | Valor/acção | Delta acumulado |
|---|---|---|---|
| 0 | base publicado | $ 404,02 | — |
| *Conservadores vs factos* | | | |
| 1 | imposto | $ 410,14 | +1,51% |
| 2 | + NWC | $ 420,74 | +4,14% |
| *Favoráveis vs factos (simetria)* | | | |
| 1 | cash opex | $ 373,51 | **−7,55%** → frase obrigatória (sumário) |

**Âncora estrutural: dispensada** — "Hugo, 29-10-2026: sem comparáveis limpos em mega-caps multi-negócio (mesma decisão da GOOGL)". O cash opex terminal só tem o facto e o consenso como travão.

**G15 vs consenso — decomposição do gap de $ 201,10 face ao PT ($ 605,12).** (i) **Base contabilística / D&A: +$ 22,06.** Com a margem EBIT do consenso (~46% até ao Y5, opex derivado), o meu modelo daria $ 426,08: a diferença é o consenso ter D&A de 14–15% com capex de 50%. (ii) **Taxa de desconto: ~$ 179.** Com a operação do consenso, o PT só se obtém a uma taxa de **8,47%** (8,27% com o meu base), contra o meu WACC de 10,47%. ~89% do gap é custo de capital, não pressupostos operacionais. O crescimento do base **é** o consenso de receita FY27-31, e o LT growth de 15,95% (n=6) é de EPS, não de receita.

**G20.** ROIC marginal implícito de 17,3% no Y5 e de 35,0% no Y10; receita nova por dólar de capex 0,33 contra 0,47 histórico (70%, acima do limiar de 60%). Atenção do `02` pelo Y10 acima de 1,5x a referência — frase no sumário. A receita do consenso foi importada junto com o capex do consenso (regra v1.6), e o cenário "ciclo paga" é o próprio base.

**G16.** Nenhum driver "aproximado a meio".

### Calibração entre nomes *(gatilho: FV/PT < 0,70 em 3+ fichas — disparado)*

| Ficha | FV / PT consenso | IRR implícita (motor A) | ERP usado |
|---|---|---|---|
| ADYEN | 1,00 | 12,31% | 4,20% (implícito) |
| **MSFT** | **0,67** | **8,78%** | **5,0% (Hugo)** |
| META | 0,60 | 9,15% | 5,0% (Hugo) |
| GOOGL | 0,57 | 8,52% | 4,20% (implícito) |
| NOW | 0,60 *(Set-26)* | 8,84% | — |
| NU | 0,49 *(Set-26)* | 11,5% | — |

**Leitura.** As três mega-caps de AI (MSFT, META, GOOGL) dão retornos implícitos de 8,52% a 9,15% — **63 bp de intervalo** — contra WACCs de 9,4% a 10,5%. É o padrão que o G15 descreve: a classe de activos limpa a ~8,5–9%, abaixo do meu custo de capital. Não é três achados independentes sobre três empresas caras: é informação sobre o meu custo de capital. Somam-se duas convenções de ERP na mesma classe (4,20% na GOOGL e 5,0% na META e na MSFT). **Não ajusto parâmetros para acertar o resultado.** Registo a decisão pendente: uniformizar o ERP. A 4,20% o base da MSFT vale $ 469,12 (FV/PT 0,78).

<!-- G12: todos os números de valuation desta ficha lêem-se de células identificadas do MSFT_DCF.xlsx (Inputs, DCF,
     Reverse, Cenarios, Crosscheck) ou das saídas dos scripts 02-07 de 29-10-2026. Ficheiro recalculado headless:
     798 fórmulas, 0 erros. Detectores: motor A 0,00000000%, B 0,00000002%, D 0,00000001% — verdes. -->

---

## A. Invalidadores da tese

**Regras:** número legível numa fonte pública **sem estimar**; threshold que a série já quase tocou; frequência compatível com a fonte.

| # | Afirmação (secção) | Invalidador — condição observável | Onde verifico | Definido | Estado | Revisto |
|---|---|---|---|---|---|---|
| 1 | O capex normaliza a partir do FY28 (Ciclo, DCF) | Capex na definição da gestão **acima de 50% da receita** em base LTM de 4 trimestres | Deck, slide de capex ÷ receita LTM | 30-07-2026 | **Vigiar** — LTM 44,9% (era 43,8%); Q1-27 isolado 49,0%. *Nota: a reclassificação para operating leases tira ROU do capex reportado ($ 6,5 mM no Q1); o threshold mantém-se na definição da gestão, e os ROU de op. leases (10-Q, Nota 12) leem-se como indicador ao lado* | 29-10-2026 |
| 2 | O AI é monetizado sem destruir margem (§3) | **Microsoft Cloud gross margin abaixo de 63%** num trimestre | Deck, Trended Investor Metrics | 30-07-2026 | **Vigiar** — 66% (65% no Q4-26); Q2 guiado a ~65%. *Definição recast (inclui Industry solutions cloud); a série recast começa nos 68% do Q1-26* | 29-10-2026 |
| 3 | O crescimento contratado sustenta Y1-Y3 (§1) | **RPO comercial a decrescer** face ao trimestre homólogo | Deck / 10-Q, Nota 10 | 30-07-2026 | OK — $ 677 mM, +73% YoY (plano QoQ) | 29-10-2026 |
| 4 | O Azure é o motor (§1) | **Azure growth abaixo de 25%** num trimestre | ER / deck | 30-07-2026 | OK — +48%; guidance 49–50% cc. *Definição recast* | 29-10-2026 |
| 5 | O capital novo cria valor (§4) | **Distribuição (buyback + dividendo) acima de 1,5x o FCF** da gestão, em base FY | Cash flow vs deck | 30-07-2026 | OK — Q1-27: $ 10,2 mM vs FCF da gestão $ 12,8 mM (0,80x); FY26 1,29x | 29-10-2026 |
| 6 | O balanço suporta o buildout (§5) | **Caixa + ST investments abaixo de $ 50 mM** | Balanço trimestral | 30-07-2026 | **Vigiar** — $ 64,5 mM, −$ 12,3 mM no trimestre. *Desenho a rever: com financiamento externo anunciado, a caixa pode ser reposta por dívida. Proposta para o Q2-27: dívida líquida com finance leases / EBITDA LTM > 1,0x (hoje 0,20x)* | 29-10-2026 |
| 7 | O SBC não é o lucro (§7) | **SBC acima de 6% da receita** em base FY | Cash flow | 30-07-2026 | OK — 3,4% no Q1-27 | 29-10-2026 |
| **8** | Não há dependência de um cliente (§1) — **novo** | **Receita de acordos com a OpenAI acima de 15% da receita** num trimestre | 10-Q, Nota 3 (related party) | 29-10-2026 | OK — 10,8% ($ 10,0 mM / $ 92,3 mM) | 29-10-2026 |

**Nota de calibração.** Os #1, #2 e #6 estão em vigilância porque a série já está perto do threshold. O #8 é novo e está calibrado a ~4 pp do valor actual. O #4 (Azure < 25%) continua folgado de propósito: seria uma mudança de regime. **Contagem: 0 disparados de 8, 3 em vigilância — bate com o ESTADO.**

**Disparados — o que fiz a seguir**

| # | Data | O que disparou | Decisão tomada |
|---|---|---|---|
| — | — | Nenhum | — |

**Regra de saída.** Para o caso de estar certo: preço abaixo de $ 346,38 → 1ª tranche; Azure ≥ 50% durante o FY27 *com* M365 commercial cloud > 20% → rever as probabilidades a favor de "Os agentes monetizam". Para o caso de estar errado: #1 *e* #8 no mesmo trimestre → reescrever o base para "Infraestrutura comoditizada". Gate de *trim* (quando houver posição): acima de $ 491,35 (o favorável ao WACC).

---

## B. Log de fair value e decisões

| Data | Quarter | Preço | FV DCF | IRR impl. | Growth impl. | Decisão | Racional (1 linha) |
|---|---|---|---|---|---|---|---|
| 30-07-2026 | FY26-Q4 | $ 390,54 | $ 402,51 *(ver nota)* | 9,28% | 11,83% *(@10%)* | Esperar | Assimetria de 1,59:1 não pagava o risco de execução; 1ª tranche a $ 345,28 |
| **29-10-2026** | **FY27-Q1** | **$ 545,00** | **$ 404,02** | **8,78%** | **19,23%** *(@11,47%)* | **Esperar** | O negócio acelerou e o base subiu para o consenso, mas a acção subiu 40% e o custo de capital foi corrigido; nenhum cenário vale o preço ao WACC |

*Nota ao registo de 30-07-2026 — erro identificado a 29-10-2026:* o Rf usado (4,25%, herdado do modelo NOW) não era o do dia; o UST 10Y a 29-07 estava em 4,67% (mesmo erro registado na ficha META). Com o Rf correcto, o FV de Julho teria sido **$ 374,42**, não $ 402,51 (−$ 28,08), e a 1ª tranche estaria mais baixa. O registo não se apaga: fica como estava, com esta nota.

**Ponte do fair value face à revisão anterior** *(passo a passo; passos 1–5 na mecânica de Julho, passo 6 na mecânica v1.7; fecha ao cêntimo em $ 404,02)*

| Grupo | Passo | WACC | Valor/acção | Δ |
|---|---|---|---|---|
| — | FV publicado a 30-07 (rev.1) | 9,12% | $ 402,51 | — |
| Erros / método | Rf 4,25% → 4,67% (10Y a 29-07) | 9,52% | $ 374,42 | −$ 28,08 |
| Mercado e balanço | Preço $ 545, dívida + FL, caixa e shares a Set-26 | 9,59% | $ 368,92 | −$ 5,50 |
| Mercado e balanço | SOTP OpenAI (24% × $ 852 mM × 50%) | 9,59% | $ 382,66 | +$ 13,73 |
| Ano-base | FY26 → LTM Set-26 (receita $ 331.839 M → $ 346.445 M) | 9,59% | $ 399,14 | +$ 16,49 |
| **Taxa de desconto** | Rf 4,67% → 4,99%; ERP 4,5% → 5,0%; Kd 4,0% → 4,8% | 10,47% | $ 347,00 | **−$ 52,14** |
| **Business plan e método** | Receita e capex do consenso; cash opex; D&A por classe (vs % da receita) | 10,47% | **$ 404,02** | **+$ 57,02** |

**Atribuição:** taxa de desconto −$ 80,22 (−$ 52,14 de mercado mais −$ 28,08 de erro) · business plan e método +$ 57,02 · ano-base +$ 16,49 · mercado, balanço e SOTP +$ 8,23. **Mais de metade do movimento bruto vem da taxa.** Ao WACC de Julho o base valeria **$ 511**: a recomendação não mudou, mas a razão mudou — em Julho era o preço que estava no fair value, hoje o preço está 35% acima dele. *O passo 6 junta business plan e mudança de mecânica (D&A por classe, cadeia de cash opex) porque as duas mecânicas não têm o mesmo motor; não se separam sem um terceiro modelo.*

*(A matriz cenário × taxa vive na secção CENÁRIOS.)*

**Verificação retrospectiva** — primeira revisão prevista para Jan-2027 (após o FY27-Q2). A pergunta já tem uma resposta parcial: o FV mexeu-se por taxa e por fundamentais em sentidos opostos; o preço mexeu-se +40%.

---

## D. Sentimento e posicionamento

**Insider** — **não verificado nesta revisão** (sem export de Insider Transactions nem Forms 4). A empresa recomprou 6,5 M de acções no trimestre por $ 2.925 M, a $ 393,77 em Julho, $ 494,12 em Agosto e $ 499,62 em Setembro (10-Q, Parte II, Item 2). Restam $ 37,7 mM do programa de $ 60 mM. O ritmo de recompra caiu de $ 3.955 M no Q1-26 para $ 2.925 M.

**Short interest** — sem export novo. Último registo (29-07-2026): **1,244%** das acções, contra mediana de 5 anos de 0,657% e máximo de 1,281%. Por actualizar com o export de 5 anos: a pergunta é se os shorts de Julho cobriram na subida de +40%.

**Sell-side** *(CapIQ Estimates, 28-10-2026 — antes da reacção aos resultados)*

| | Valor |
|---|---|
| PT médio / mediano | $ 605,12 / $ 600,00 *(era $ 555,77 em Julho)* |
| Intervalo | $ 440,00 – $ 870,00 · desvio-padrão $ 65,32 |
| Nº de estimativas | 52 |
| Distribuição | 41 Buy · 13 Outperform · 3 Hold · 0 Underperform · 0 Sell |
| **LT growth do consenso** | **15,95%** (mediana 16,82%; 12,30%–19,00%; **n=6**) — EPS |
| Receita de consenso FY27-31 | $ 391,6 / 468,6 / 570,1 / 644,3 / 738,1 mM (n = 52 / 52 / 27 / 8 / 6) |
| Upside implícito no PT | +11,0% vs $ 545 |

| Base | Fair value | Governa a decisão? |
|---|---|---|
| **DCF, SBC como custo real, capex da gestão, D&A por classe** | **$ 404,02** | **Sim** |
| Meu DCF com a margem EBIT do consenso | $ 426,08 | Não — decomposição |
| Meu base a ERP 4,20% (implícito Damodaran Out-26) | $ 469,12 | Não — sensibilidade, decisão pendente |
| Consenso sell-side | $ 605,12 | Não — referência |
| Mínimo do intervalo sell-side | $ 440,00 | Não — 19% abaixo do preço, 9% acima do meu base |

**Decomposição do gap de $ 201,10:** +$ 22,06 de base contabilística (D&A do consenso inconsistente com o capex do consenso) e ~$ 179 de taxa de desconto (a operação do consenso chega ao PT a 8,47%). Não é diferença de crescimento: o base usa a receita do consenso. *Sinal de calibração:* o LT growth continua com só 6 estimativas contra 52 no PT, e as receitas de FY30-31 com 8 e 6.

**Estrutura accionista** — não verificada nesta revisão. Sem activistas conhecidos; free float essencialmente total.

---

## C. Changelog

| Data | Quarter | O que mudou | Secções |
|---|---|---|---|
| 29-10-2026 | FY27-Q1 | **Rev.2: FY27-Q1 processado** (10-Q, deck, transcript, CapIQ Financials e Estimates de 28-10). **Migração para o template v3.3 / plugin v1.7:** RESUMO, Tópicos-chave, Ciclo de capex, três cenários nomeados, escada por valor esperado, prémios aplicados, ponte do FV. **Modelo reconstruído no pipeline `dcf-reverso`:** cadeia de cash opex, D&A por classe (75% a 6 anos, 25% a 25, meio ano, carteira em 3 tranches), SOTP da OpenAI ($ 102.240 M), motores A/B/C/D, G12 verde, 0 erros. **Custo de capital:** Rf 4,25% → 4,99%; ERP 4,5% → 5,0% (Hugo, como na META); Kd 4,0% → 4,8%; WACC 9,12% → 10,47%. **Hurdle:** de 10% fixo para nível 2 (WACC + 100 bp = 11,47%, Hugo). **Preço:** $ 545 (Hugo, 29-10; G17 resolvido). **Base:** receita e capex do consenso FY27-31 (era 16% no Y1 e capex sem a receita coerente — G20 de Julho). FV $ 402,51 → $ 404,02; 1ª tranche $ 345,28 → $ 346,38. **Erros registados:** (1) Rf de Julho 4,25% com o 10Y a 4,67% (FV correcto de Julho $ 374,42); (2) §1 afirmava ausência de concentração de clientes — a OpenAI é 10,8% da receita (related party). **Novo invalidador #8** (OpenAI > 15%). #6 passa a Vigiar e o seu desenho fica a rever. **G15:** âncora estrutural dispensada (Hugo); reversão vs factos −7,55% do lado favorável (opex terminal), frase no sumário. **G18:** o TEV do CapIQ mudou de definição (omite as FL em Set-26). **Decisão pendente:** uniformizar o ERP nas três mega-caps (4,20% na GOOGL vs 5,0% na META e MSFT). | Todas |
| 30-07-2026 | FY26-Q4 | **Ficha criada.** DCF de 9 folhas, 3 motores de reverse, grelha de 2 eixos. Recomendação: esperar, 1ª tranche a $ 345,28. Achados: ROIC marginal de 14,35% contra 26,5% médio; $ 66.594 M de finance leases omitidas pelo CapIQ; capex da gestão a 43,8% da receita; distribuição a 1,29x o FCF; short interest a duplicar desde 2022. G13: o driver dominante é o crescimento, não o capex. | Todas |

**Lacunas abertas, a fechar no próximo ciclo** *(registadas em vez de estimadas — G16)*

1. **Item 1A do 10-K FY26 vs FY25** — continua por fazer. As três frases do 10-Q do Q1-27 (§6) são o ponto de partida.
2. **Insider e 10b5-1** — sem dados.
3. **Short interest** — export de 5 anos por actualizar desde 29-07.
4. **Estrutura accionista** — sem dados.
5. **Parte da OpenAI no RPO** — não divulgada. Perguntar no próximo call ou ler o 10-K.
6. **`Return on Capital %`** da folha Ratios do CapIQ — verificação independente do ROIC pendente.
7. **ERP** — uniformizar nas fichas GOOGL, META e MSFT (decisão do Hugo).
8. **Marcação da OpenAI** — $ 852 mM é de Abril-2026; ronda posterior não verificada em fonte séria.
9. **Revisões do consenso pós-Q1** — o export é de 28-10, antes da reacção.

---

*Template v3.3 — Outubro 2026 (plugin v1.7). Camada 1 de três: ficha estrutural · análise trimestral em chat · `MSFT_DCF.xlsx`.*
*Modelo recalculado headless a 29-10-2026 — 798 fórmulas, 0 erros, detectores G12 verdes. Preço de ancoragem $ 545,00 (`Inputs!B6`); memo $ 531,01 (`Inputs!B7`). Todos os múltiplos e upsides recalculam-se mudando `Inputs!B6`.*
