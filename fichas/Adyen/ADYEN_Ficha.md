# Ficha de Empresa — Adyen N.V. (ADYEN · Euronext Amsterdam)

> **Documento único e vivo.** Não se cria cópia por trimestre — actualiza-se este.
> **Secções 1–7:** estrutura. Escritas uma vez, revistas anualmente ou quando um invalidador dispara.
> **Blocos A–D:** infraestrutura. Actualizados a cada análise trimestral.

`Criada:` 28-10-2026 · `Última revisão estrutural:` 28-10-2026 · `Último quarter processado:` Q3-26 (business update, 28-10-2026)

> **Preliminar.** Preço de ancoragem € 842,00 às 09:49 CET (Bloomberg, nota da equipa BlueCrow), posterior ao update mas intraday — G17 aceite, trocar pelo fecho de 28-10 em `Inputs!B6` e regerar. Drivers do base ainda não validados pelo Hugo (passo 4 da `dcf-reverso`).

---

> **Revisão de 30-10-2026 — regra de custo de capital da carteira** (Rf soberana a 10 anos à data do preço, ERP do estudo Kroll mais recente — zona euro 5,0–5,5%, usado 5,0% —, CRP só se relevante: aqui sai). Actualizados o ESTADO, o capítulo REVERSE DCF (novo), o log e o changelog. **O sumário executivo, as tabelas "Se comprar a X" e a §7 continuam ao Ke de 8,55%** (versão de 28-10 em `_arquivo\ADYEN_Ficha_20261028.md`). O config do pipeline foi reconstruído do `ADYEN_DCF.xlsx` (`00_extrair_config.py`; reproduz € 1.358,95 ao cêntimo) e grava agora a escada.

## ESTADO

| | | | |
|---|---|---|---|
| **Preço** | € 842,00 | **Data** | 28-10-2026 (09:49 CET, intraday) |
| **Market cap** | € 26.759 M *(31,78 M acções diluídas)* | **EV** | € 22.084 M *(mkt cap + leases 409 − cash próprio disponível 3.067 − 50% capital regulatório 600 − float 1.418)* |
| **Valor DCF** *(base: cresc. 21%→5%, EBITDA 50%→53,5%)* | € 1.280,35 @WACC 8,84% | **Upside** | +52,1% |
| **Valor ponderado** *(p bull/base/bear 25/50/25 — declaradas antes)* | € 1.100,36 @required *(25/50/25)* · € 1.268,52 @WACC | **IRR esperada** | 12,22% vs required 9,84% |
| **Ke** *(regra da carteira: Bund 10Y 3,37% + ERP Kroll zona euro 5,0%; CRP 0 — o 0,51% era spread de desenvolvidos, não risco emergente; beta unlev 1,10 Damodaran US)* | 8,93% | **Ke ±100 bp** | valor/acção € 1.511,06 / € 1.112,61 |
| **Amplitude bull–bear** *(2 eixos)* | € 873,43 – € 1.307,22 @required | **Drivers dominantes** | Crescimento da receita (543,67) · Capex/receita (279,75) |
| **IRR implícita** *(reverse DCF)* | 12,31% | **vs required return** | spread +247 bp |
| **Growth implícito** *(@ required return)* | CAGR 10a 8,81% | **vs CAGR histórico** | net revenue FY23–LTM +20,2%/ano; base do modelo 13,4% |
| **Decisão** | entrada faseada | **Gates** | 1ª tranche < € 1.110,40 (base — troca, ponderado < base) · 2ª < € 1.100,36 (ponderado) · cheia < € 924,21 (bear eixo único) |
| **Peso máximo da posição** | 13,2% *(a 28-10; por refazer)* | **Bear conjunto** | **por refazer** — a definição de 28-10 não ficou gravada; o valor antigo (€ 714,79) era ao ERP de 4,20% |
| **Invalidadores disparados** | 0 de 6 · 2 em vigilância | **Último report** | Q3-26 business update, 28-10-2026 |
| **ROIC marginal** *(sobre o capital deployado)* | 151% ex-M&A · ~45% com M&A *(FY23 → LTM Jun-26)* | **vs WACC** | ROIC médio LTM 137% ex-M&A / 68% com M&A |
| **Próximo catalisador** | Resultados H2-26 e objectivos 2027 — 11-02-2027 | **O que decide** | Margem EBITDA guiada para 2027 (≥ 50%) e trajectória do take rate |
| **Consenso sell-side** | PT médio € 1.362 (n=35, mín. € 887) — pré-corte | **vs o meu DCF** | € 1.280,35 · rácio FV/PT 0,94 |
| **Peers** *(múltiplo âncora)* | Visa NTM P/E 26,7x · EV/EBITDA NTM 21,0x | **vs pares maduros** | Adyen ~19,6x NTM P/E (EPS consenso pré-corte) — desconto de ~27% à Visa |
| **Short interest** | n/d *(sem export)* | **vs mediana 5 anos** | n/d |
| **Posição actual** | detida (quantidade e custo não registados) | **% da carteira** | n/d |

**Múltiplos-chave** — os que decidem nesta empresa. Justificação na §7. EV sobre **cash próprio** (€ 22.568 M = mkt cap 26.759 + leases 409 − 4.600); o TEV do CapIQ mete ~€ 8 mM de fundos de merchants no cash e não se usa.

| Múltiplo | Actual | Mediana 3 anos | vs mediana | Leitura |
|---|---|---|---|---|
| EV/EBITDA LTM Jun-26 | 16,8x | n/d | n/d | Mediana própria não comparável: o CapIQ calcula o TEV com o float no cash |
| EV/EBITDA FY26E (guidance 50%) | 15,7x | n/d | n/d | Forward sobre guidance da empresa, não consenso (consenso ainda pré-corte) |
| P/E LTM | 23,7x | n/d | n/d | EPS LTM € 35,57 (H2-25 18,39 + H1-26 17,18). Inclui ~€ 300 M/ano de finance income |
| EV/net revenue LTM *(o que contraria a tese)* | 8,8x | TEV/receita CapIQ 7,5x (2024) → 6,5x (2026) | de-rating contínuo | A mediana é a média da queda, não um nível de reversão |

<!-- SIGLAS: take rate = net revenue / volume processado, em pontos base (16,36 bp = € 16,36 por cada € 100.000 processados). cc = constant currency. Net revenue = receita após interchange e scheme fees (pass-through). -->

---

## REVERSE DCF — o que o preço exige *(30-10-2026, ERP 5,0%, CRP 0)*

*Calculado sobre o `modelo_calc` do `config_ADYEN.json` (Excel regerado e verificado a 30-10). Preço € 842,00.*

**0. A grelha simples — valor por acção ao WACC (8,84%)** *(crescimento × margem EBITDA do Y10; todas acima do preço)*

| CAGR 10a ＼ Margem EBITDA Y10 | 47,5% | 50,5% | **53,5% (base)** | 56,5% | 58,5% |
|---|---|---|---|---|---|
| 10,4% *(base −3 pp)* | € 937,4 | € 996,6 | € 1.055,9 | € 1.115,1 | € 1.154,6 |
| 11,9% | € 1.029,5 | € 1.095,8 | € 1.162,0 | € 1.228,2 | € 1.272,3 |
| **13,4% (base)** | € 1.132,4 | € 1.206,4 | **€ 1.280,4** | € 1.354,3 | € 1.403,7 |
| 14,9% | € 1.247,0 | € 1.329,7 | € 1.412,3 | € 1.495,0 | € 1.550,1 |
| 16,4% *(base +3 pp)* | € 1.374,6 | € 1.467,0 | € 1.559,3 | € 1.651,6 | € 1.713,2 |

Capex (2.º driver do G13) na linha do base: −0,5 pp → € 1.293,5 · +1 pp → € 1.254,1 · +2 pp → € 1.227,9. **Para valer € 842 ao WACC**, com a margem do base o CAGR teria de ser **6,7%**; com o crescimento do base, a margem EBITDA do Y10 teria de ser **35,7%**.

**1. Retorno que o preço oferece (motor A)** — inalterado pelo ERP

| | IRR |
|---|---|
| **Base** · ponderado (25/50/25) | **12,31%** · 12,22% |
| Base com crescimento −3 pp / cash opex +3 pp / g −1 pp | 10,65% / 11,74% / 11,84% |

**2. Crescimento exigido (motor B) — CAGR a 10 anos, por retorno exigido × margem EBITDA do Y10**

| Retorno exigido ＼ Margem Y10 | 47,5% | 50,5% | **53,5% (base)** | 56,5% |
|---|---|---|---|---|
| WACC + 25 bp (9,09%) | 9,18% | 8,19% | 7,27% | 6,40% |
| **Required 9,84% (nível 2)** | 10,77% | 9,76% | **8,81%** | 7,93% |
| 11% | 13,06% | 12,01% | 11,04% | 10,12% |
| 12% | 14,92% | 13,84% | 12,84% | 11,90% |

Âncoras: CAGR do base 13,38% · net revenue FY23–LTM +20,2%/ano.

**3. Em números falsificáveis** — Y4 com Y1–Y2 no base: o preço exige net revenue de **€ 4.610 M** (base € 5.116 M), EBITDA **€ 2.374 M** (base € 2.635 M), NOPAT/acção **€ 47,23** (base € 53,18) — crescimento de 12% no Y3 a cair para ~0% no Y10.

**Leitura:** o preço pede 8,8% de crescimento durante dez anos para render o required, contra 20% realizado. A tese continua a ser o take rate e a margem guiada para 2027 (H2-26 a 11-02-2027).

---

## TÓPICOS-CHAVE

- **O preço exige pouco.** A € 842 o reverse DCF pede um CAGR de receita de 8,05% a 10 anos ao required return de 9,47%, contra +22% cc no Q3-26 e +20,2%/ano de FY23 ao LTM.
- **O valor ao required return está acima do preço nos três degraus.** Ponderado € 1.157,55, base € 1.168,21, bear de eixo único € 969,02; só o bear conjunto (€ 714,79, −15,1%) perde, e limita o peso a 13,2%.
- **O EV publicado está errado.** O CapIQ conta € 12,4 mM de cash, dos quais € 8,1 mM são de merchants; o EV correcto sobre cash próprio é ~€ 22,6 mM, não € 17,8 mM — os múltiplos EV "baratos" que circulam estão subavaliados ~25%.
- **A margem perdeu a âncora.** FY26 guiado a 50% (era ~51,7% em Agosto e "em linha com 2025" em Fevereiro); o objectivo de >55% em 2028 foi retirado e só há novos objectivos a 11-02-2027.
- **O que contraria a tese: o preço por transacção cai.** Take rate do Digital −9,7% YoY no Q3-26 (receita +15,6% com volume +28%), mais fundo que os −3,7% do H1; sem as aquisições, o take rate do grupo caiu face ao Q2.

---

## SUMÁRIO EXECUTIVO

**Recomendação: entrada faseada.** Fair value € 1.358,95 ao WACC (€ 1.168,21 ao required return de 9,47%) contra preço de € 842,00 — **+61,4%**. Não é "compra cheia" porque o driver dominante é o crescimento, a empresa acabou de retirar a única âncora de margem que tinha, e a informação que resolve isso chega numa data conhecida (11-02-2027); não é "esperar" porque, ao preço de hoje, até o bear de eixo único rende o required return.

### A tese numa frase

O mercado está a pagar a Adyen como se o lucro crescesse ~8% ao ano durante uma década, numa empresa cujo volume cresce 30% e cuja receita cresce 20% orgânico — a tensão é se a queda do preço por transacção e o reinvestimento sem data de retorno transformam esse crescimento de volume num crescimento de lucro de um dígito.

### Os financials, em vinte segundos

A net revenue do Q3-26 foi € 738,1 M, +23,3% reportado e +22% cc, com ~2 pp das aquisições (Talon.One e Orb, fechadas a 1-Jul): o orgânico está em ~20%, sem aceleração face ao Q2. O volume processado subiu 30% para € 451,1 mM, mas o take rate caiu de 17,25 bp para 16,36 bp (−5,2% YoY), e no Digital — metade da receita — o preço por euro processado caiu ~10%. A Adyen reporta em IFRS; o EBITDA é uma APM, mas inclui o SBC (€ 29,6 M no H1-26, +48% YoY), pelo que não há add-back a desmontar. A margem EBITDA foi 52,7% em FY25 (55,3% no H2) e 49,2% no H1-26; a guidance de FY26 passou a 50%, o que implica ~50,6% no H2 contra 55,3% um ano antes. A conversão em caixa é alta: FCF da empresa € 1.160 M no LTM (86% do EBITDA), capex 5% da receita a subir para 7% em 2026 (data centers). O balanço não tem dívida financeira; dos € 12,4 mM de cash, € 4,9 mM são próprios, ~€ 4,6 mM depois das aquisições. O que mudou de natureza neste trimestre foi a política, não o negócio: a gestão passou de prometer alavanca operacional com data para reinvestir sem data.

### O DCF — pressupostos e resultado

| Pressuposto | Y1 → Y10 | Âncora histórica |
|---|---|---|
| Crescimento da net revenue | 21% → 5% (CAGR 13,4%) | Guidance FY26 21–23% cc; FY23→LTM +20,2%/ano; LT growth consenso 18,7% (n=3) |
| Cash opex ex-D&A / receita | 50% → 46,5% (EBITDA 50% → 53,5%) | FY25 47,3% (EBITDA 52,7%); H2-25 44,7%; quartil superior dos pares ~51% |
| SBC / receita | dentro do cash opex | ~2,3% (H1-26 € 29,6 M / € 1.302,9 M) |
| Capex + leases / receita | 8,7% → 6,5% | FY25 6,95%; guidance FY26 7% + ~1,7% leases |
| WACC · g perpétuo | 8,47% · 2,5% | Ke 8,55% (método A); g ≤ PIB nominal da zona euro |

**Resultado:** enterprise value operacional € 38.512 M, valor por acção **€ 1.358,95**. Reverse DCF na mesma respiração: o preço oferece **12,31%** de retorno implícito (motor A), e ao required return de 9,47% exige um **CAGR de receita de 8,05%** durante dez anos (motor B).

**Três honestidades obrigatórias.** O terminal value pesa **65,5%** do EV, e o Gordon implica uma saída de **11,3x EV/EBITDA** no Y10 — abaixo dos 14,2x NTM de hoje, portanto não heróico. Nenhum movimento de margem é compensado por outro: o D&A sobe com o capex e a margem EBITDA sobe por alavanca sobre pessoal, não por runoff de amortização. A amplitude por driver:

| Driver | Cenário adverso | Valor/ação | Δ vs base |
|---|---|---|---|
| Crescimento da receita | −3 pp/ano | € 1.116,65 | −17,8% |
| WACC | +100 bp | € 1.168,21 | −14,0% |
| g perpétuo | 1,5% | € 1.238,44 | −8,9% |
| Capex / receita | +5 pp | € 1.219,07 | −10,3% |
| Taxa de imposto | +5 pp | € 1.276,56 | −6,1% |
| Cash opex / receita | +3 pp | € 1.279,89 | −5,8% |
| NWC / Δ receita | 4% | € 1.349,06 | −0,7% |
| Vida do capex novo | −1,8 anos | € 1.363,61 | +0,3% |

### Os múltiplos — e se contradizem o DCF

Contra a **própria história**, o múltiplo comprimiu sem interrupção — TEV/receita do CapIQ de 19,3x (2022) para 6,5x (2026) — e "estar no mínimo" é tautológico, porque o mínimo é hoje. Contra **os pares**, a Adyen a ~19,6x P/E NTM (EPS consenso pré-corte) negoceia ~27% abaixo da Visa (26,7x), com o dobro do crescimento e sem a posição de rede; o resto do peer set do CapIQ (Worldline, StoneCo, Edenred) são processadores em declínio ou noutro negócio, a 3–11x. Contra o **trimestre corrente anualizado**, o EBITDA implícito do H2-26 (€ 801 M × 2) dá 14,1x EV/EBITDA, contra 16,8x LTM: o múltiplo cai quando se olha para a frente, porque a receita cresce mais do que a margem desce. Os múltiplos não contradizem o DCF; contradizem a leitura de que a Adyen ficou cara depois da queda.

### Qual das fontes é mais credível aqui

A mediana histórica não serve: foi calculada sobre um de-rating contínuo e com um TEV contaminado pelo float de merchants. O peer set do CapIQ também não, porque metade são cartões de frota e benefícios. O DCF tem 65,5% no terminal, e a amplitude do crescimento é de € 543,67 por acção. **Governa o reverse DCF**, porque não depende dos meus pressupostos: um CAGR de 8% para quem cresce 20% é uma barra baixa. O DCF base serve de **cross-check**, e é ele que mostra onde está o risco — no crescimento, não na margem.

### Se comprar a X, ganho quanto por ano?

| Preço | EV/EBITDA NTM à entrada | Retorno total 5a | **Anualizado, com re-rating** | Sem re-rating | Re-rating |
|---|---|---|---|---|---|
| € 842,00 *(preço actual)* | 14,2x | +142,35% | **19,37%** | 12,31% | +7,05% |
| € 1.358,95 *(fair value @WACC)* | 24,7x | +50,16% | **8,47%** | 8,47% | +0,00% |
| € 1.157,55 *(ponderado)* | 20,6x | +76,28% | **12,01%** | 9,54% | +2,47% |
| € 1.168,21 *(base)* | 20,8x | +74,68% | **11,80%** | 9,47% | +2,33% |
| € 969,02 *(posição cheia)* | 16,8x | +110,58% | **16,06%** | 10,96% | +5,10% |

**Heatmap — IRR a 5 anos ao preço de hoje**, por crescimento da receita × EV/EBITDA de saída.

| Crescimento da receita ＼ EV/EBITDA de saída | 9,8x | 11,3x | 12,0x | 14,1x *(DCF)* | 14,2x *(hoje)* | 16,2x | 17,0x | 18,3x |
|---|---|---|---|---|---|---|---|---|
| -2 pp | 11,52% | 13,71% | 14,68% | 17,40% | 17,53% | 19,90% | 20,79% | 22,20% |
| -1 pp | 12,40% | 14,64% | 15,63% | 18,40% | 18,53% | 20,94% | 21,85% | 23,28% |
| base | 13,30% | 15,58% | 16,58% | **19,41%** | 19,54% | 21,99% | 22,92% | 24,37% |
| +1 pp | 14,20% | 16,52% | 17,55% | 20,42% | 20,55% | 23,05% | 23,99% | 25,46% |
| +2 pp | 15,11% | 17,47% | 18,52% | 21,44% | 21,57% | 24,11% | 25,07% | 26,57% |

Ao preço de hoje, **12,31% vem do negócio** (o retorno sem re-rating) e **~7 pp do re-rating** até ao fair value. As colunas "DCF" e "hoje" quase coincidem (14,1x vs 14,2x), pelo que a leitura do heatmap não depende de escolher entre elas. Mesmo com saída a 9,8x e crescimento −2 pp, a IRR fica em 11,5%, acima do required.

### Porque não é a recomendação adjacente, e o que a mudaria

**Probabilidades declaradas antes de ver os valores:** bull 25% · base 50% · bear 25% *(default)*

| Banda | Preço | Racional | Assimetria bull:bear | Peso máx. |
|---|---|---|---|---|
| Preço actual | € 842,00 | IRR esperada 12,22% · IRR base 12,31% | +64% : +9% (o bear não perde) | 13,2% |
| **1ª tranche** | € 1.168,21 | **Valor base** ao required return | +18% : −22% (0,8:1) | 5,2% |
| **2ª tranche** | € 1.157,55 | **Valor ponderado** ao required return | +19% : −21% (0,9:1) | 5,2% |
| **Posição cheia** | € 969,02 | **Bear de eixo único** (crescimento −3 pp) ao required return | +42% : −6% (7,6:1) | 7,6% |

**A escada trocou os dois primeiros degraus:** o ponderado (€ 1.157,55) saiu abaixo do base (€ 1.168,21) porque o bear pesa mais do que o bull (cenários côncavos), e a escada desce sempre. Os três degraus estão acima do preço, pelo que o framework autoriza a posição cheia, limitada pelo peso. **A minha leitura não é mecânica:** o driver dominante é o crescimento, e o take rate do Digital mostra que parte do crescimento de volume não chega à receita. Por isso proponho a 1ª e a 2ª tranche agora e a cheia depois do 11-02-2027, se os invalidadores 1 e 2 passarem. O que mudaria a recomendação são exactamente os invalidadores do bloco A: margem FY26 abaixo de 49,5%, margem FY27 guiada abaixo de 50%, crescimento cc trimestral abaixo de 18%, take rate LTM abaixo de 15,8 bp, crescimento do Digital abaixo de 10% ou capex de 2027 acima de 7%.

**Prémios aplicados** — nenhum risco cobrado duas vezes.

| Prémio | Aplicado? | Valor | Risco que cobre | Sobrepõe-se a outro? |
|---|---|---|---|---|
| CRP *(Damodaran ctryprem)* | Sim | 0,51% | Exposição LatAm (5,7%), APAC (10%), UK/FR | Não |
| Hurdle *(nível 2, WACC + 100 bp)* | Sim | 9,47% | Execução das aquisições e reinvestimento sem objectivo de margem | Não — o CRP aqui é sobretudo spread de mercados desenvolvidos, não risco emergente; mantém-se no nível 2 em vez de descer para 1, e fica escrito |
| Fade terminal abaixo da âncora estrutural | Não | EBITDA terminal 53,5% vs âncora ~49% | — | Não — está acima da âncora (desvio −8,73% no valor, dentro dos 15%) |

**Próximo catalisador:** H2-26 e objectivos 2027 a 11-02-2027, com o primeiro letter do novo CFO (Niclas Neglen, desde 01-02-2027) e a contabilização das aquisições.

---

## 1. Negócio — o que vende

A Adyen é um processador e acquirer de pagamentos enterprise, com licença bancária europeia (DNB/BCE) e uma única plataforma própria que faz gateway, risco, acquiring, settlement e reconciliação para grandes merchants, online e em loja. Desde Julho de 2026 junta software à volta do pagamento: loyalty e promoções (Talon.One, € 750 M) e billing por consumo (Orb, $ 335 M). Cobra uma margem por transacção sobre o volume processado — interchange e scheme fees passam ao lado e não entram na net revenue.

**Segmentos / linhas de produto** *(Q3-26)*

| Segmento | % receita | O que é | Cliente-tipo |
|---|---|---|---|
| Digital | 52,5% | E-commerce e in-app | Grandes marcas: travel, subscrições, retail |
| Unified Commerce | 33,9% | Online e loja física no mesmo contrato, terminais POS | Retalho omnicanal |
| Platforms | 13,6% | Pagamentos embebidos em plataformas SaaS e marketplaces | Plataformas e os seus sub-merchants |

**Métricas de escala:** volume processado € 451,1 mM no Q3-26 (+30% YoY); net revenue LTM Set-26 € 2.713 M; take rate 16,36 bp; 838 mil terminais transaccionais (H1-26, +27%); volume em loja 22% do total; 46 plataformas acima de € 1 mM/ano; ~5.020 FTE (Jun-26, ~5.800 esperados no fim de 2026).

**Exposição geográfica:** EMEA 57,4%, América do Norte 26,9%, APAC 10,0%, LatAm 5,7%. **Concentração de clientes:** não quantificada. O AR 2025 diz apenas que a concentração "remained within risk appetite" e que os grandes enterprise trabalham com vários PSPs e podem mudar volume — o risco existe e não é medível com o que é divulgado.

---

## 2. Vantagem competitiva — porquê esta e não a rival

**Rival de referência:** Stripe — é o único concorrente com stack próprio de ponta a ponta à mesma escala e disputa os mesmos clientes enterprise e plataformas. Privada, com dados limitados.

| Dimensão | Adyen | Stripe | Quem ganha, e porquê |
|---|---|---|---|
| Produto / tecnologia | Uma plataforma, licenças de acquiring próprias, forte em loja (Unified Commerce) | Developer-first, ecossistema de produtos (Billing, Connect) mais largo | Empate. Adyen no omnicanal enterprise, Stripe no long tail e nas plataformas |
| Distribuição e go-to-market | Venda directa a enterprise | Self-serve + enterprise | Stripe em amplitude; Adyen em contas grandes |
| Pricing power | Em queda: take rate −5,2% YoY, Digital −9,7% | Desconhecido | Nenhum: tiered pricing é a moeda de troca por share of wallet |
| Escala | € 1,65 bi de volume LTM | Maior em volume total *(conhecimento geral, não verificado)* | Stripe |
| Custo de mudança para o cliente | Médio-alto em loja (terminais, reconciliação); baixo no online (multi-PSP) | Alto nas plataformas (Connect) | Depende do canal |
| Economia unitária | EBITDA 52,7% FY25 sobre net revenue, FCF 86% do EBITDA | Desconhecida | Adyen é a referência pública |

**Se o diferencial for real, aparece nos números.** Aparece na quota de wallet: a carteira de 2024 ou anteriores produz dois terços do crescimento, e a quota típica sobe de <20% para >40% numa década (carta H1-26). **E onde NÃO aparece?** No preço. Cada ganho de quota num grande merchant chega com um escalão de preço mais baixo, e o take rate do Digital caiu ~10% num ano. O diferencial converte-se em volume, não em preço — é a assimetria que define a tese.

---

## 3. Monetização — de onde vem exactamente o dinheiro

| Fluxo | % receita | Unidade cobrada | Quem paga | Recorrente? | Preço/unidade |
|---|---|---|---|---|---|
| Processing fee + markup | maioria (não desagregado) | Fixo por transacção + % do volume | Merchant | Sim, por volume | ~16 bp médio |
| Métodos locais e FX | n/d | Por transacção / spread | Merchant | Sim | n/d |
| Terminais POS | n/d | Venda/aluguer + transacção | Merchant em loja | Parcial | n/d |
| Produtos financeiros (issuing, capital, contas) | n/d | Interchange partilhada, juros | Plataformas e merchants | Sim | n/d |
| Software (Talon.One, Orb) | ~1,6% (~€ 12 M/trimestre, estimado) | Subscrição/uso | Enterprise | Sim | n/d |
| Juros sobre saldos (finance income) | fora da net revenue | — | — | Depende de taxas | ~2,5% sobre cash médio |

**Mecânica do fluxo principal:** autorização em segundos, clearing e settlement em 1–2 dias; a Adyen recebe da rede, retém a margem e paga ao merchant no calendário acordado. Fica com o risco do merchant nesse intervalo. **Alavancas de preço:** mix de métodos de pagamento, valor acrescentado (risco, tokenização, reconciliação) e venda cruzada de software. **Onde o dinheiro NÃO vem:** de interchange (pass-through) nem de crédito ao consumidor. **Qualidade da receita:** transaccional mas altamente recorrente — não há RPO nem contratos plurianuais divulgados.

**Assimetria de monetização vs custo:** a receita é por euro processado e o custo é sobretudo pessoal e data centers. O tiered pricing faz a receita por euro cair à medida que a escala sobe, e isso só se nota porque a margem deixou de expandir.

---

## 4. Moat — porque é que isto não é replicável

| Tipo de moat | Presente? | Evidência quantitativa | Força |
|---|---|---|---|
| Network effects | Fraco | Dados de risco agregados entre merchants; sem efeito de rede de dois lados | Baixa |
| Switching costs | Sim, em loja | 838 mil terminais; reconciliação unificada online + loja; UC take rate +5,4% YoY | Média |
| Economias de escala | Sim | EBITDA 52,7% com 4.771 FTE para € 1,4 bi de volume (FY25) | Média-alta |
| Intangíveis (licenças) | Sim | Licença bancária UE, licença de branch nos EUA, acquiring directo em vários países | Média-alta |
| Vantagem de custo estrutural | Sim | Stack único, sem legacy de fusões até 2026 | Média |
| Eficiência de distribuição | Não | Venda enterprise directa, cara | Baixa |

**Teste do capital ilimitado**

> Se um competidor com € 10 mil milhões e cinco anos copiasse isto amanhã, **o que é que o dinheiro não compra?**

As licenças de acquiring em dezenas de mercados, a confiança dos departamentos de tesouraria dos maiores retalhistas do mundo e 15 anos de dados de risco. O código compra-se; a aprovação regulatória e as integrações em loja demoram. A Stripe prova que é replicável com uma década e capital ilimitado — e é por isso que o moat é médio, não largo.

**O que erode o moat, e a que velocidade:** o pricing por escalões, que é escolha da própria Adyen, e os multi-PSP no online. **Trajectória:** estável em quota (volume +30%), a estreitar em preço (take rate −5,2% YoY).

### O moat converte-se em economia? O teste do ROIC

Capital investido operacional = PP&E + ROU + intangíveis + NWC operacional (receivables, inventário e impostos menos payables), **sem** cash nem saldos de merchants. Com M&A, soma-se o prepaid acquisition consideration (€ 655 M em Jun-26).

| | FY23 | FY24 | FY25 | LTM Jun-26 |
|---|---|---|---|---|
| NOPAT normalizado (EBIT × 75,5%) | 485 *(base CapIQ)* | 670 | 838 | 900 |
| Capital investido (fim de período, ex-M&A) | 384 | 392 | 434 | 659 |
| **ROIC** *(capital fim de período)* | 126% | 171% | 193% | 137% |
| Spread vs WACC (8,47%) | +118 pp | +162 pp | +185 pp | +128 pp |

Capital médio dá números maiores. Incluindo os € 655 M das aquisições, o ROIC LTM cai para ~68%. As três bases dizem a mesma coisa: o negócio core quase não precisa de capital.

| | |
|---|---|
| Capital investido acrescentado (FY23 → LTM Jun-26) | 275 ex-M&A · ~930 com M&A |
| Δ NOPAT normalizado | 415 |
| **ROIC marginal** | **151% ex-M&A · ~45% com M&A** |
| WACC | 8,47% |

O capital deployado rende muito acima do custo de capital, mesmo com as aquisições. A questão não é o capital, é o opex: o reinvestimento está a ser feito em pessoas, que passam pela P&L e não pelo balanço. O *Return on Capital %* do CapIQ (folha Ratios) usa outra definição de capital e não foi reconciliado.

---

## 5. SWOT

**Forças:** fundadores ainda na gestão (Pieter van der Does, co-CEO); stack único e licenças próprias; ROIC core >100%; FCF de € 1,16 mM LTM, 86% do EBITDA; sem dívida financeira e € 4,6 mM de cash próprio.
**Fraquezas:** take rate a cair em todos os pilares menos UC (Digital −9,7% YoY); duas revisões de margem em 11 semanas; objectivo de 2028 retirado; CFO interino até 01-02-2027; concentração de clientes não divulgada.
**Oportunidades:** Platforms +46% (13,6% da receita); software sobre o pagamento (loyalty, billing) para os mesmos clientes enterprise; loja física (22% do volume, a subir).
**Ameaças:** Stripe no enterprise e nas plataformas (alta probabilidade, contínua); descida das taxas BCE retira finance income (~€ 300 M/ano, ~22% do resultado líquido); um terceiro corte de margem a 11-02-2027.

---

## 6. Legal, regulatório e fiscal

| Matéria | Tipo | Estado | Exposição máx. | % market cap | Timeline |
|---|---|---|---|---|---|
| Capital regulatório CRR/CRD IV | Supervisão (DNB, "less significant institution") | Own funds € 5,3 mM, só CET1 | Requisito não divulgado no AR (Pillar 3) | n/d | Contínua |
| Restricted cash (licença de branch nos EUA, etc.) | Regulatório | € 331 M | € 331 M | 1,2% | Contínua |

**Regime regulatório:** banco da UE pelo método standard; o risco operacional (Basic Indicator Approach) é o requisito mais pesado. **Risco fiscal:** ETR 24,4% (H1-26); Pillar 2 sem impacto material referido. **Antitrust:** nada material. **Histórico de condenações:** nada identificado no AR 2025. **Factores de risco novos face ao ano anterior:** não comparados nesta sessão — a fazer na revisão anual.

---

## 7. Enquadramento de valuation

### Que métricas são as certas

| Múltiplo | Usar? | Porquê / porque não |
|---|---|---|
| P/E GAAP | Sim, com cuidado | Inclui ~€ 300 M de finance income sensível a taxas |
| P/E ajustado | Não | Não há ajustamentos materiais |
| EV/EBITDA | Sim | **Só com EV sobre cash próprio**; o EBITDA da empresa inclui SBC |
| EV/Receita *(LTM e forward)* | Cross-check | A margem está em transição |
| P / NTM EPS *(forward)* | Sim | Âncora contra a Visa |
| EV/FCF | Sim | FCF de 86% do EBITDA |
| P/TBV e ROE *(financeiras)* | Não | Banco por licença, não por modelo de negócio |
| Específico do sector | Take rate e volume | É a decomposição da receita |

**Métrica âncora:** reverse DCF, com EV/EBITDA forward sobre cash próprio. **Peers nomeados:** Visa (rede madura, tecto de qualidade) e Stripe (rival directo, privado). O peer set do CapIQ, que não se pode editar, mistura processadores em declínio e cartões de frota. **Armadilhas conhecidas:** o TEV do CapIQ inclui o float de merchants (subavalia o EV em ~€ 8 mM); o finance income sobre o float inflaciona o P/E e não está no EBITDA; Q2 e Q4 são derivados.

### O múltiplo é barato porque o preço caiu, ou porque o lucro caiu?

| | LTM | Mediana 3 anos | **Trimestre corrente anualizado** |
|---|---|---|---|
| EV / Receita | 8,8x | n/d (TEV CapIQ contaminado) | 7,1x (H2-26E × 2) |
| EV / EBITDA | 16,8x | n/d | 14,1x (H2-26E × 2) |
| EV / EBIT | ~18,9x | n/d | ~16,0x |

O preço caiu; o lucro não. O EBITDA do H2-26 implícito na guidance (€ 801 M) é +14% YoY, e o múltiplo desce quando se anualiza o semestre corrente.

### Decomposição de qualquer colapso de margem

Não há colapso no sentido do template: não há amortização de intangíveis adquiridos ainda (PPA a 11-02-2027) nem add-backs. Ponte da guidance (nota da equipa, consistente com a carta H1-26):

| | FY25 | FY26 guiado | Δ | Corre off? |
|---|---|---|---|---|
| Margem EBITDA | 52,7% | 50,0% | −2,7 pp | — |
| das quais: diluição Talon.One + Orb (guiada em Agosto) | | | −1,0 pp | Parcialmente, quando a receita adquirida crescer |
| das quais: reinvestimento acelerado (Outubro, não desagregado) | | | −1,7 pp | **Não sabemos** — é a pergunta para Fevereiro |
| SBC (no EBITDA) | — | +48% YoY no H1 | | **Não** — é remuneração |

**Coerência obrigatória:** o invalidador de margem usa a margem EBITDA da empresa, com SBC dentro, que é a mesma base do modelo.

### Três lentes, três veredictos

| Lente | Veredicto |
|---|---|
| vs história própria de múltiplos | Inconclusiva — de-rating contínuo e TEV contaminado |
| vs peers | Barata vs Visa (−27% em P/E NTM com o dobro do crescimento); cara vs processadores europeus em declínio, que não são comparáveis |
| DCF | Barata — FV € 1.358,95 @WACC, € 1.168,21 @required; o preço exige um CAGR de 8% |

A divergência está entre o DCF e a avaliação por múltiplos de saída da equipa BlueCrow (€ 876 ponderado; ver bloco D). Governa o reverse DCF.

### Os drivers dominantes — por sensibilidade, não por intuição (G13)

| Driver | Cenário adverso | Valor/ação | Δ vs base |
|---|---|---|---|
| Crescimento da receita | −3 pp | € 1.116,65 | −17,8% |
| Capex / receita | +5 pp | € 1.219,07 | −10,3% |
| Taxa de imposto | +5 pp | € 1.276,56 | −6,1% |
| Cash opex / receita | +3 pp | € 1.279,89 | −5,8% |

WACC (amplitude 459,74) e g (289,51) ficam na tabela WACC × g, não como eixos. **Os dois operacionais mais sensíveis — crescimento e capex — são os eixos da grelha viva da folha `Cenarios`.** A margem, que é o tema do trimestre, é só o quarto driver: o que mais mudou não é o que mais pesa.

**Porquê cada eixo, e porquê o valor do base.**

- **Crescimento:** Y1 21% bate no fundo da guidance de FY26 (21–23% cc, com M&A). O fade até 5% no Y10 dá um CAGR de 13,4%, abaixo do histórico (20,2%) e do LT growth do consenso (18,7%). Duas marcações do mesmo lado, conservadoras.
- **Capex:** 8,7% no Y1 (7% guiado + leases), a normalizar para 6,5%, abaixo do facto FY25 (6,95%). É a guidance "towards historical levels" da empresa e é o único driver favorável face a um facto (−0,93% no valor).
- **Margem:** sobe de 50% para 53,5% de EBITDA, abaixo dos 55,3% do H2-25 e do objectivo retirado. **G14:** o último trimestre mostra a margem a piorar e o modelo a melhorar. Fica com cenário explícito (o bear tem cash opex +3 pp) e com invalidadores ligados (A-1, A-2). Não se ancora no trimestre porque o desvio coincide com aquisições e um ciclo de contratação identificado, com precedente de recuperação em 2023–24 (43,3% → 52,6% em 18 meses).
- **G15:** reversão vs factos +0,49% (conservadores) e −0,93% (favoráveis), ambos abaixo de 5%. Vs âncora estrutural −8,73%, dentro de 15%; a âncora é fraca (só LTM, gross vs net revenue). Vs consenso −14,18% — **divulgar**: o meu Y1 de 21% está acima do LT growth de EPS de 18,7% (n=3); a diferença é de definição (receita vs EPS) e de amostra (3 analistas), não de pressuposto.
- **G20:** ROIC marginal implícito 771% no Y5 e 377% no Y10; receita incremental por euro de capex 2,07 e 1,55. Verde — o capex não é a restrição.
- Nenhum driver ficou "aproximado a meio" (G16).

---

## A. Invalidadores da tese

**Regras:** número legível numa fonte pública **sem estimar**, *threshold* que a série já quase tocou, frequência compatível com a fonte.

| # | Afirmação (secção) | Invalidador — condição observável | Onde verifico | Definido | Estado | Revisto |
|---|---|---|---|---|---|---|
| 1 | O reinvestimento não destrói a margem do core (§7) | Margem EBITDA FY26 reportada < 49,5% | Shareholder letter H2-26 (11-02-2027) | 28-10-2026 | Vigiar | 28-10-2026 |
| 2 | A margem volta a subir a partir de 2027 (§7, DCF base) | Margem EBITDA 2027 guiada < 50% | Objectivos 2027, letter H2-26 | 28-10-2026 | Vigiar | 28-10-2026 |
| 3 | O orgânico sustenta ~20% (DCF base Y1–Y2) | Crescimento net revenue cc < 18% YoY num trimestre | Business update / letter trimestral | 28-10-2026 | OK (22% no Q3-26) | 28-10-2026 |
| 4 | A compressão do preço é tiering, não guerra de preços (§2) | Take rate LTM (net revenue / volume, 4 trimestres) < 15,8 bp | Business updates (net revenue e volume) | 28-10-2026 | OK (16,41 bp LTM Set-26) | 28-10-2026 |
| 5 | O Digital continua a crescer em receita (§1) | Net revenue Digital < +10% YoY num trimestre | Business update | 28-10-2026 | OK (+15,6% no Q3-26) | 28-10-2026 |
| 6 | O capex normaliza depois de 2026 (DCF, eixo capex) | Capex FY27 (definição da empresa) > 7% da net revenue | Letter H2-27 (Fev-2028); guidance 2027 em Fev-2027 | 28-10-2026 | OK | 28-10-2026 |

**Disparados — o que fiz a seguir**

| # | Data | O que disparou | Decisão tomada |
|---|---|---|---|

**Regra de saída:** *trim* acima de € 1.358,95 (fair value ao WACC, onde o retorno esperado cai para o WACC), ou se dois invalidadores dispararem em simultâneo.

---

## B. Log de fair value e decisões

| Data | Quarter | Preço | FV DCF | IRR impl. | Growth impl. | Decisão | Racional (1 linha) |
|---|---|---|---|---|---|---|---|
| 30-10-2026 | Q3-26 | € 842,00 | € 1.280,35 | 12,31% | CAGR 8,81% @required | entrada faseada | Regra de custo de capital da carteira: ERP 4,20% → 5,0% (Kroll zona euro, limite inferior), CRP 0,51% → 0 (não relevante). Ponte: ERP −€ 170,30, CRP +€ 91,70. Escada € 1.110,40 / € 1.100,36 / € 924,21 |
| 28-10-2026 | Q3-26 | € 842,00 | € 1.358,95 | 12,31% | 8,05% | entrada faseada | Ficha criada após a queda de −10,8% com o corte de margem; o preço exige um CAGR de 8% contra um orgânico de 20% |

**Verificação retrospectiva:** primeira entrada.

---

## D. Sentimento e posicionamento

**Insider:** n/d nesta sessão (registos AFM não consultados).

**Short interest:** n/d (sem export de Charting).

**Sell-side:** PT médio $ 1.517,71 / mediana $ 1.423,96 (≈ € 1.362 / € 1.278 a 1,1142), intervalo $ 988,30–$ 2.005,57, n=35; 21 Buy, 7 Outperform, 6 Hold, 0 Underperform, 0 Sell. LT growth 18,7% médio (n=3). **Pré-corte** — o EBITDA FY26E do consenso (€ 1.494 M) ainda está nos ~52%.

| Base | Fair value | Governa a decisão? |
|---|---|---|
| DCF, SBC como custo real | € 1.358,95 @WACC · € 1.168,21 @required | **Sim** |
| Consenso sell-side (pré-corte) | ≈ € 1.362 | Não — referência |
| Mínimo do intervalo sell-side | ≈ € 887 | |
| Equipa BlueCrow (28-10-2026), cenários por P/E | € 876 ponderado (20/50/30) | Não — cross-check |

**Decomposição do gap face à equipa (€ 1.158 vs € 876):** a equipa valoriza por P/E de saída no fim de 2026 (20–22x FY27E no base). Esse múltiplo é o múltiplo a que a acção negociava antes do resultado, pelo que o valor herda o de-rating que pretende avaliar. O próprio reverse DCF da equipa (preço implica ~5%/ano de crescimento do resultado líquido; € 1.184 a 10%/ano) está muito mais perto deste DCF do que da sua escada de cenários. A diferença é de método, não de pressupostos operacionais: a margem FY27 de 50,5% da equipa é praticamente o Y1–Y2 deste modelo.

**Estrutura accionista:** fundadores com participação relevante (não quantificada nesta sessão).

---

## C. Changelog

| Data | Quarter | O que mudou | Secções |
|---|---|---|---|
| 30-10-2026 | Q3-26 | Regra de custo de capital da carteira (decisão do Hugo): Rf Bund 10Y (3,37%, igual), ERP Kroll 5,0% (era 4,20% Damodaran), CRP 0 (era 0,51% — spread de desenvolvidos, não risco emergente). Ke 8,55% → 8,93%. FV € 1.358,95 → € 1.280,35; motor A inalterado (12,31%); motor B 8,05% → 8,81%; escada € 1.110,40 / € 1.100,36 / € 924,21. **Bear conjunto e peso máximo por refazer** (a definição de 28-10 não ficou gravada). Config reconstruído do Excel e escada gravada no config. Excel regerado e verificado | ESTADO, REVERSE DCF (novo), B, C |
| 28-10-2026 | Q3-26 | Ficha criada. Preço € 842 intraday (G17 aceite). Correcção face à análise em chat: o corte de margem é de ~1,7 pp face a Agosto (não ~3 pp), e o take rate caiu −5,2% YoY (não −2%, como dizia o agregador). | Todas |

---

### Perguntas em aberto para o Hugo (§2 e §4 — não se inventam)

1. Tens dados da Stripe (volume, take rate, quota no enterprise europeu) de fonte que possamos citar?
2. Qual é a tua posição actual (acções, custo médio) para fechar a linha do ESTADO?
3. Concordas com o beta unlevered de 1,10 (entre Computer Services 0,96 e Software 1,25)? É a escolha com mais peso no Ke.
4. O valor do float de merchants entra a 75% (€ 1.418 M, ~€ 45/acção). Preferes 0% (conservador) ou 100%?

---

*Template v3.3 — Outubro 2026. Camada 1 de três: ficha estrutural · análise trimestral em chat · DCF em Excel (`ADYEN_DCF.xlsx`, G12 verde a 28-10-2026).*
