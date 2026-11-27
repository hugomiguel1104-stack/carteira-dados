# Ficha de Empresa — Amazon.com (AMZN · NasdaqGS)

<!-- dados {"preco": 246.82, "fv": 206.05, "bear": 118, "bull": 309, "t1": 211, "cheia": 157, "upside": -0.1652, "data": "20-11-2026", "decisao": "Esperar / manter — não reforçar", "quarter": "Q3-26", "invalidadores": "0 de 6 · 2 em vigilância", "moeda": "USD", "par": {"rf": 0.049100000000000005, "erp": 0.05, "rf_metodo": "A", "erp_fonte": "Kroll"}} -->

`Q3-2026` · `revista 23-11-2026` · `criada 23-11-2026` · `plugin v2.1 · template v5.0` · **RASCUNHO v0**

> **Estado do modelo:** v0, calculado com o motor `modelo_calc.py` do plugin (o mesmo do Excel) a partir de `config_AMZN.json`. Ainda **não há Excel** (o `01_build_modelo.py` não correu) nem a verificação G12 do `02`. Os números servem para decidir o sentido; antes de os citar como definitivos, corre-se o pipeline no PC.
> **Fontes:** releases trimestrais da Amazon (Q1, Q2 e Q3-26, IR) e o S-1/A da Anthropic (participação). Sem Capital IQ: o consenso, os múltiplos históricos, o short interest e os insiders estão **n/d**.

**Preço do modelo:** $ 246,82 *(fecho de 20-11-2026)* · **Market cap:** $ 2.697 mM *(10.929 M acções diluídas, Q3-26)* · **Par Rf/ERP:** UST 10Y 4,91% · ERP 5,0%

---

## Questões-chave

1. **O que é que o preço exige?** Um CAGR de receita de **12,1% durante 10 anos** (o base dá 9,9%), ou capex terminal de **8,1%** da receita (o base usa 10,5%). → [Reverse DCF](#reverse-dcf)
2. **O capex de ~$ 220 mM rende?** A AWS acelerou para +39% e a gestão projecta >40% em 2027 e 2028. Mas o FCF LTM é −$ 42,4 mM e a dívida de longo prazo passou de $ 65,6 mM para $ 173,1 mM em 9 meses. → [Cenários](#cenários)
3. **Quanto vale a Anthropic?** Cerca de **$ 14,9 por acção** reconhecidos (6% do preço), com descontos. → [Valuation](#valuation)
4. **O que contraria a tese?** O capex ficar estrutural: com capex terminal +3 pp o valor cai para ~$ 157. → [Invalidadores](#invalidadores)

---

## Resumo

| | |
|---|---|
| **Preço** | $ 246,82 *(20-11-2026)* |
| **Fair value DCF (base)** | **$ 206,05 @WACC 10,04% → −16,5%** · $ 207,43 @required 10% |
| **Cenários @required** | Capex estrutural $ 118 · **Ciclo paga com atraso $ 207** · O capex rende $ 309 |
| **Ponderado** | $ 210,6 *(25/50/25, proposta)* · $ 220,1 *(30/50/20, Hugo)* |
| **Retorno que o preço oferece** | **9,04%** ao ano (motor A), contra 10% exigido |
| **Decisão** | **ESPERAR / manter** — não reforçar; a posição (8,8% da carteira) já está acima do que o retorno justifica |
| **O que decide** | Guidance de capex de 2027 e o crescimento da AWS no Q4-26 (início de Fev-2027) |

| Invalidadores | Consenso sell-side | Ciclo de capex | Posição |
|---|---|---|---|
| 0 de 6 · 2 em vigilância (FCF, dívida) | n/d (sem CapIQ) | **Pico transitório, com nível estrutural mais alto** | 8,8% da carteira (+~1% via ETFs) |

### Sumário executivo

- **Recomendação.** Esperar e manter. Ao preço de 20-11 o negócio rende ~9%, abaixo da barreira de 10%. Mudava se a AWS sustentasse >40% e o capex de 2027 estabilizasse em % da receita.
- **Tese.** A Amazon troca hoje FCF por capacidade de IA na AWS. A tese vale se a AWS converter o capex em receita a ~$ 0,5 por cada dólar investido e se a intensidade de capex voltar a ~10% até 2030.
- **Financials.** Receita LTM de $ 797 mM (+15%). Margem EBIT LTM de 13,1%, um máximo histórico. EBITDA LTM de $ 184 mM (23,1%). Capex líquido LTM de $ 210,7 mM (26,4% da receita). FCF LTM de **−$ 42,4 mM**.
- **DCF.** $ 206 por acção. Os dois pressupostos que o fazem são o capex a cair de 27% para 10,5% da receita e a margem EBITDA a subir de 23,5% para 28% com o mix AWS. O TV pesa 72,9%.
- **Reverse DCF.** O preço exige mais 2,2 pp de crescimento por ano sobre o base (CAGR de 12,1%), ou capex terminal de 8,1%, abaixo do pré-IA (8,4% em 2023). Exequível no cenário favorável, não no base.
- **Múltiplos.** EV/EBITDA LTM ~14,2x, já sem a Anthropic. EV/(EBITDA − capex) é negativo: os múltiplos de caixa não funcionam neste ponto do ciclo.
- **Risco principal.** O capex ficar estrutural. Com +3 pp de capex em todos os anos, o valor desce para ~$ 157 (−36% face ao preço).

---

## Sentimento e narrativa

**A narrativa de hoje.** O mercado vê a Amazon como ganhadora da IA (AWS a acelerar, Trainium, parceria com a Anthropic), mas castiga o FCF negativo e o financiamento com dívida. A acção caiu menos do que o Nasdaq na correcção de Novembro.

| Indicador | Valor | Leitura |
|---|---|---|
| Consenso sell-side | n/d | Sem CapIQ |
| Revisões de estimativas *(3 meses)* | n/d | |
| Short interest | n/d | |
| Insiders *(6 meses)* | Bezos vende por planos 10b5-1 (ficha de gestão na app) | Sem sinal novo |
| Múltiplo-âncora vs mediana 3 anos | n/d | |

| Base | Fair value | Governa a decisão? |
|---|---|---|
| DCF, SBC como custo real | $ 206,05 | **Sim** |
| Consenso sell-side | n/d | — |

---

## Reverse DCF

| Motor | Resultado | Leitura |
|---|---|---|
| **A** — retorno ao preço | **9,04%** | 96 bp abaixo do required (10%) |
| **B** — crescimento exigido @10% | **+2,19 pp/ano → CAGR 12,1%** | O base dá 9,9%. A Amazon cresceu ~11–13% ao ano em 2021–25 |
| **D** — capex terminal exigido @10% | **8,1% da receita** no Y10 | O base usa 10,5%. 2023: 8,4%; 2024: ~13% |

**As estimativas — exequíveis, bullish ou bearish?**

| Estimativa | Valor | Contra o quê | Veredicto |
|---|---|---|---|
| Guidance da gestão | Q4-26: receita +12–16%, EBIT $ 28,5–33,5 mM; capex 2026 ~$ 220 mM; AWS >40% em 2027 e 2028 | AWS ~20% da receita → +8 pp ao grupo | Base alinhado (15% em Y1 e Y2) |
| Consenso FY+1 · FY+2 | n/d | | |
| O que o preço implica | CAGR de 12,1% **ou** capex terminal de 8,1% | Histórico e guidance | **Exigente**: pede o crescimento do cenário favorável ou capex abaixo do pré-IA |

**Veredicto.** O preço já desconta mais do que o base: exige ou crescimento de dois dígitos durante 10 anos, ou que a intensidade de capex volte abaixo de 2023. É possível, mas é o cenário favorável, não o central.

---

## Cenários

| Cenário | p *(proposta)* | A história | Crescimento | Margem EBITDA Y10 | Capex Y10 | Valor @10% | Sinal de que estamos aqui |
|---|---|---|---|---|---|---|---|
| Capex estrutural | 25% | A IA exige reinvestimento permanente; a AWS cresce, mas com retorno marginal baixo | base −2 pp | 26,5% | 14,0% | **$ 118** | Capex de 2027 acima de 30% da receita sem a AWS acima de 40% |
| **Ciclo paga com atraso** | **50%** | AWS a 40% em 2027-28, capex a normalizar a partir de 2028 | 15% → 5% *(CAGR 9,9%)* | 28,0% | 10,5% | **$ 207** | AWS 35–45% e capex/receita a cair a partir de 2028 |
| O capex rende | 25% | A Trainium e a Anthropic dão retorno alto; o capex normaliza mais depressa | base +2 pp | 30,0% | 8,5% | **$ 309** | AWS acima de 40% com a margem operacional da AWS acima de 38% |

O preço ($ 246,82) fica entre o base e o favorável: paga ~38% do caminho até ao favorável.

**Probabilidades.** O Hugo propôs **30/50/20** (favorável/base/adverso). Proponho **25/50/25**: a aceleração da AWS é evidência a favor, mas o FCF negativo, a dívida financiada para capex e o histórico de outras grandes de IA (a ficha da Meta mostra um retorno do capital novo de 3,6% até Y5) são evidência contra, de força parecida. **A diferença não muda a decisão:** ponderado $ 220 vs $ 211, ambos abaixo do preço.

---

## Negócio

| Segmento (Q3-26) | Receita | Cresc. homólogo | Margem op. | O que é · quem paga |
|---|---|---|---|---|
| North America | $ 112,9 mM | +6% *(Prime Day no Q2)* | 7,7% | Retalho 1P/3P, publicidade, assinaturas |
| International | $ 43,1 mM | +5% | 3,7% | Idem, fora dos EUA |
| AWS | $ 46,0 mM | **+39,3%** | **38,7%** | Cloud, IA (Bedrock, Trainium), computação |
| **Total** | **$ 201,9 mM** | +12% | 13,9% | |

**Do lucro ao FCF (LTM Set-26).** OCF $ 168,3 mM − capex líquido $ 210,7 mM = **FCF −$ 42,4 mM**. D&A LTM $ 79,4 mM. SBC LTM $ 19,9 mM, tratado como custo (está dentro do EBIT).

**Ciclo de capex.** Transitório no pico, estrutural no nível: o terminal fica em 10,5%, acima do pré-IA.

| | 2023 | LTM Set-26 | Guidance 2026 | Y1 (modelo) | Y3 | Y5 | Y10 |
|---|---|---|---|---|---|---|---|
| Capex / receita | 8,4% | 26,4% | ~26,5% | 27,0% | 22,0% | 16,0% | 10,5% |

**O modelo, da receita ao FCF (base, $ mM).**

| | Y1 | Y2 | Y3 | Y4 | Y5 | Y10 |
|---|---|---|---|---|---|---|
| Receita | 917 | 1.055 | 1.192 | 1.329 | 1.462 | 2.049 |
| Capex | 248 | 264 | 262 | 252 | 234 | 215 |
| D&A | 95 | 131 | 167 | 203 | 175 | 202 |
| Margem EBIT | 13,2% | 11,6% | 10,5% | 9,7% | 13,5% | 18,1% |
| FCFF | −49 | −28 | 11 | 60 | 105 | 287 |

*(Valores arredondados do `modelo_calc`; o D&A tem um degrau no Y5, quando a tranche de 4,5 anos da carteira acaba. Rever no Excel.)*

---

## Moat e ROIC

| Moat | Presente? | Evidência | Força |
|---|---|---|---|
| Escala logística (NA) | Sim | Margem NA de 4,8% para 7,7% num ano | Forte |
| Escala e ecossistema cloud | Sim | AWS a 38,7% de margem e +39% | Forte |
| Custo de chips próprio (Trainium/Graviton) | Em formação | Negócio de chips a >$ 25 mM de run rate (Q2-26) | Por provar |

**ROIC marginal (G20, base):** 15,6% até Y5 e 38,8% até Y10. Cada dólar de capex compra ~$ 0,53 de receita nova. O retorno até Y5 está próximo do WACC (10%): o valor depende da segunda metade da década.

---

## Valuation

### Pressupostos do DCF

| Pressuposto | Y1 → Y10 | Âncora |
|---|---|---|
| Crescimento da receita | 15% · 15% · 13% · 11,5% · 10% → 5% *(CAGR 9,9%)* | Q4 guidance +12–16%; AWS >40% em 2027-28 (gestão) |
| Margem EBITDA *(SBC dentro)* | 23,5% → 28,0% | LTM 23,1%; mix AWS (38,7% de margem op.) |
| Capex / receita | 27% → 10,5% | LTM 26,4%; 2023: 8,4% |
| D&A | Por classe: 55% a 5 anos, 20% a 10, 25% a 25; carteira $ 509 mM em duas tranches | Servidores a 5 anos (política Amazon) |
| Imposto · NWC | 17% → 20% · −3% da Δreceita | ETR recente; working capital negativo histórico |
| WACC · g · peso do TV | **10,04%** · 2,5% · 72,9% *(saída 6,8x EBITDA)* | Rf 4,91% · ERP 5% · β unlev 1,05 (Damodaran Jan-26, ponderado) · Kd 5,2% |

**Ponte.** Dívida $ 183,1 mM (dívida LP de $ 173,1 mM + ~$ 10 mM estimados de finance leases; os operating leases ficam no opex) − caixa e títulos $ 114,2 mM − Anthropic $ 162,6 mM reconhecidos (14,7% a $ 88,5 com 80% reconhecido, mais os convertíveis, 9,1% com 40% reconhecido). **Sem a Anthropic, o fair value seria $ 191.**

### Drivers dominantes (G13)

| Driver | Choque | Valor/acção | Δ vs base |
|---|---|---|---|
| **Capex / receita** | ±3 pp | $ 255 / $ 157 | **+$ 49 / −$ 49** |
| Crescimento | −3 pp/ano | $ 162 | −$ 44 |
| Cash opex | +3 pp | $ 161 | −$ 45 |
| WACC | +1 pp | $ 175 | −$ 31 |

**O capex é o eixo dominante**, como na Meta e na Alphabet.

### Escada de entrada *(hoje sem compras: posição já de 8,8%)*

| Degrau | Preço | Regra |
|---|---|---|
| 1.ª tranche | **~$ 211** | Valor ponderado @10% (25/50/25) |
| 2.ª tranche | **~$ 207** | Base @10% |
| Posição cheia | **~$ 157** | Adverso de eixo único (capex +3 pp) |
| Pensar em reduzir | **acima de ~$ 300** | Perto do valor do cenário favorável: já paga o melhor caso |

---

## Invalidadores

| # | Afirmação | Invalidador — condição observável | Onde verifico | Estado |
|---|---|---|---|---|
| 1 | A AWS converte o capex em receita | AWS abaixo de 30% durante dois trimestres | Release trimestral | OK (39,3%) |
| 2 | O capex normaliza a partir de 2028 | Guidance de capex de 2027 acima de ~$ 280 mM sem a AWS acima de 40% | Call do Q4-26 | Por saber |
| 3 | O FCF volta | FCF LTM ainda negativo no Q4-27 | Release | **Em vigilância** (−$ 42,4 mM) |
| 4 | Balanço sólido | Dívida líquida (sem a Anthropic) acima de 1,0x EBITDA | Balanço | **Em vigilância** (~0,4x, com a dívida LP a subir $ 107 mM em 2026) |
| 5 | O retalho financia a transição | Margem NA abaixo de 6% durante dois trimestres | Segmentos | OK (7,7%) |
| 6 | A Anthropic é um activo | ANT abaixo de $ 45 (−50%) | Preço | OK — custa ~$ 7/acção, não parte a tese |

**Regra de saída.** Os invalidadores #2 e #3 juntos reescrevem o base para "Capex estrutural". Nesse caso, pensar em reduzir a posição para ≤ 5%.

---

## Legal e regulatório

| Matéria | Estado | Leitura |
|---|---|---|
| FTC v. Amazon (antitrust, retalho) | **A verificar**: não consultado nesta versão | Pendente |

---

## Log

| Data | Quarter | Preço | FV | IRR impl. | Par Rf/ERP | Decisão | Racional |
|---|---|---|---|---|---|---|---|
| 23-11-2026 | Q3-26 | $ 246,82 | $ 206,05 | 9,04% | 4,91% / 5,0% | Esperar · manter | O preço exige mais 2,2 pp de crescimento por ano do que o base, ou capex abaixo do pré-IA |

---

## Changelog

| Data | Quarter | O que mudou |
|---|---|---|
| 23-11-2026 | Q3-26 | Criação (rascunho v0) com dados públicos e o motor `modelo_calc`, sem Excel |

---

## Notas de método

| | |
|---|---|
| Custo de capital | Rf 4,91% (UST 10Y, 20-11) · ERP 5,0% · β desalavancado 1,05 = 58% Software (System & Application) 1,25 + 42% Retail (General) 0,78 (Damodaran Jan-2026, ponderado pelo EBIT LTM) · Kd 5,2% · CRP 0 |
| Fontes | Releases da Amazon Q1, Q2 e Q3-26 (ir.aboutamazon.com); S-1/A da Anthropic (participação de 14,7%, 23,8% se convertida). Receita do Q4-25 derivada do guidance do Q4-26 (~$ 213,4 mM): confirmar com o 10-K |
| Limites | Sem consenso, múltiplos históricos, short interest nem insiders. Finance leases estimadas. Sem o 10-Q completo (só o release). D&A com um degrau no Y5 |
| Gates | G12 e G15 não corridos (falta o Excel). G17 OK (preço de 20-11, posterior ao 10-Q de 30-10). G19 OK no par; beta a confirmar pelo Hugo |
