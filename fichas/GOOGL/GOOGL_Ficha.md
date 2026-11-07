# Ficha de Empresa — Alphabet (GOOGL · NasdaqGS)

> **Documento único e vivo.** Não se cria cópia por trimestre — actualiza-se este.
> **Secções 1–7:** estrutura. Escritas uma vez, revistas anualmente ou quando um invalidador dispara.
> **Blocos A–D:** infraestrutura. Actualizados a cada análise trimestral.
> Todo o número de valuation lê-se de uma célula do `GOOGL_DCF.xlsx` ou da saída dos scripts `02`–`06` (G12). Recalculado a 29-Out-2026 com o plugin v1.5: 583 fórmulas, zero erros, detectores do G12 verdes.
> **Sem comparáveis, por decisão do Hugo (26-Out-2026):** uma mega-cap com n negócios não tem peer limpo. Os múltiplos comparam-se só com a própria história.
> **Mecânica v1.5 (ciclo de capex):** D&A por classe de activo (servidores e rede a 6 anos, edifícios a 25), Waymo valorizada à parte (SOTP), G20 de coerência capex–crescimento e saída do `06` em EV/(EBITDA−capex).

`Criada:` 26-Out-2026 · `Última revisão estrutural:` 26-Out-2026 · `Último quarter processado:` Q3-2026

---

> **Revisão de 30-10-2026 — regra de custo de capital da carteira** (Rf UST 10Y à data do preço, ERP do estudo Kroll mais recente, CRP só se relevante). Actualizados o ESTADO, o capítulo REVERSE DCF (novo), o log e o changelog. **O sumário executivo, as tabelas "Se comprar a X" e a §7 continuam a ERP 4,20%** (versão de 29-10 em `_arquivo\GOOGL_Ficha_20261029.md`). O `config_GOOGL.json` em disco era o de 26-10; o de 29-10 foi reconstruído do `GOOGL_DCF.xlsx` (`00_extrair_config.py`, reproduz $ 245,54 ao cêntimo).

## ESTADO

| | | | |
|---|---|---|---|
| **Preço** | $ 292,50 | **Data** | 28-10-2026, after-hours das 19h59 ET *(FinanceFeeds; fecho de 324,89 na Alpha Vantage, −9,97%)*. Aproximado: refazer com o fecho de 29-Out |
| **Market cap** | $ 3.628.755 M *(12.406 M acções diluídas)* | **EV** | $ 3.400.167 M *(mkt cap + dívida e preferenciais $ 148.525 M − caixa, títulos e cotadas $ 257.048 M − 50% das não cotadas − Waymo $ 53.550 M + minoritários)* |
| **Valor DCF** *(base, ao WACC de 10,28%)* | **$ 209,17** | **Upside** | −28,5% |
| **Fair value ao required return de 11,28%** | $ 177,57 *(−39,3%)* | **Valor esperado ponderado** *(25/50/25, declaradas antes)* | $ 213,57 @WACC · $ 181,26 @required |
| **Ke** *(regra da carteira: Rf 5,05% UST 10Y 28-Out + ERP Kroll 5,0%; β 1,094; CRP 0)* | 10,52% | **Ke ±100 bp** | valor/acção $ 248,94 / $ 178,67 |
| **Amplitude bull–bear** *(2 eixos)* | $ 154,04 a $ 281,89 | **Drivers dominantes** | Capex/receita · crescimento da receita |
| **IRR implícita** *(reverse DCF, motor A)* | **8,52%** | **vs required return** | spread **−277 bp** vs 11,28%; −177 bp vs WACC |
| **Growth implícito** *(@ required return)* | CAGR receita **19,10%** a 10 anos | **vs CAGR histórico** | 17,2% FY20-25 · LTM +22,2% · base 12,05% a 10 anos · consenso FY25-30 20,0% (pré-Q3) |
| **Decisão** | **Esperar — reforço só abaixo de $ 181; peso máx. 2,9%** | **Gates** | 1ª tranche < $ 181,26 · 2ª tranche < $ 177,57 · cheia < $ 133,86 |
| **Peso máximo da posição** | 2,9% ao preço de hoje *(perda máx. 2% da carteira no bear conjunto)* | **Bear conjunto** | $ 89,08 (−69,5% vs preço) |
| **IRR esperada** *(ponderada, ao preço de hoje)* | 8,62% | **vs required** | −266 bp |
| **Invalidadores disparados** | 0 de 7 · 3 em vigilância (1, 2, 3) | **Último report** | Q3-2026 (28-Out-2026) |
| **ROIC marginal** *(sobre o capital deployado)* | 23,3% FY23→LTM · 17,3% nos últimos 12 meses | **vs WACC** | 2,5x e 1,8x; ROIC médio 31,6–38,7% conforme a base |
| **ROIC marginal implícito no base** *(G20, v1.5)* | 7,9% no Y5 · 21,7% no Y10 | **Receita nova por $ de capex** | 0,35 no base contra 0,62 no histórico → ATENÇÃO |
| **Próximo catalisador** | 10-Q do Q3-26 (próximos dias) · IPO da Anthropic (reportado: marketing a partir de ~9-Nov, primeira negociação antes de 26-Nov) · guidance de capex FY27 no call do Q4-26 (início de Fev-2027) | **O que decide** | Se o capex de 2027 vem com receita Cloud a acompanhar — backlog e crescimento — ou sem ela |
| **Consenso sell-side** | PT médio $ 429,12 (n=54, 22-Out — **pré-Q3**, revisões por incorporar) | **vs o meu DCF** | rácio FV/PT **0,49** → calibração corrida (§7) |
| **Peers** *(múltiplo âncora)* | n/a — decisão do Hugo | **vs pares maduros** | n/a |
| **Short interest** | n/d — sem export | **vs mediana 5 anos** | n/d |
| **Posição actual** | GOOG + GOOGL; trim de 15% a 13-Out-2026 | **% da carteira** | ~9% do investido depois da queda (9,7% a ~$ 325); a maior posição individual, mais exposição via ETFs. **~3x o peso máximo da ficha** |

**Múltiplos-chave** — os três que decidem *nesta* empresa. Justificação na §7.

| Múltiplo | Actual | Mediana 3 anos | vs mediana | Leitura |
|---|---|---|---|---|
| TEV/LTM EBITDA *(âncora, LTM)* | 18,9x | 16,8x | +12% | Sobre EBITDA GAAP (SBC dentro). O Q3 anualizado dá 17,9x |
| P/NTM EPS normalizado *(forward — o que contraria a tese)* | 19,7x | 21,5x | −8% | Abaixo da mediana, mas sobre o consenso de 22-Out: o EPS ajustado do Q3 ficou 12% abaixo, e a revisão vai subir o múltiplo |
| Market cap / FCF LTM | 182x | 45,3x | n/s | FCF LTM de $ 19,7 mM; o FCF do Q3 foi −$ 9,1 mM. O múltiplo deixou de ter significado até 2028 |

<!-- TEV na definição CapIQ, para comparar com a série própria: mkt cap 12.294 M acções básicas x 292,50 + dívida ~149.100 (book + finance leases, estimado) + pref. 18.023 − caixa e ST 265.098 = 3.498.020. -->

---

## TÓPICOS-CHAVE

- **A queda tirou o preço do canto bull, mas não o pôs na banda.** A $ 292,50 o mercado oferece 8,52% ao ano (motor A), 187 bp abaixo do required — contra 7,39% e −301 bp a $ 320,21. O fair value subiu para $ 245,54 (de $ 205,66): $ 12,56 do roll-forward com a mecânica v1.5 e $ 27,32 de dois drivers que o G15 obrigou a reescrever.
- **O capex continua a ser o driver dominante.** Capex/receita ±5 pp move o valor em $ 113,07, mais do que o crescimento ±3 pp ($ 108,48) ou o WACC ±100 bp ($ 95,21). O Q3 gastou $ 51,4 mM (40% da receita), o guidance de 2026 implica $ 63–73 mM no Q4, e 2027 "aumenta significativamente", sem número.
- **O motor de caixa abrandou.** Search & other cresceu 12,0% (16,8% no Q2) com as queries a crescer ao ritmo mais alto em cinco anos: mais pesquisas, menos receita por pesquisa. YouTube +9,2% (12,9% no Q2). São os $ 96 mM de Services que pagam o capex — o Cloud ainda não.
- **O Cloud é real.** +103% para $ 30,7 mM com margem de 36,2%, e o backlog subiu $ 47 mM no trimestre, para $ 561 mM. É o melhor dado da tese; o G20 mostra o que falta: o base compra $ 0,35 de receita nova por $ de capex, contra $ 0,62 no histórico.
- **O que contraria a tese.** O P/E forward está abaixo da mediana (19,7x contra 21,5x) e, se o EV/EBITDA de hoje se mantiver até ao ano 5, a IRR é 15,5%. Mas esse P/E assenta num consenso anterior ao Q3, e o múltiplo que o DCF implica no ano 5 é 9,1x EV/EBITDA: a diferença entre as duas leituras é toda a aposta.

---

## REVERSE DCF — o que o preço exige *(30-10-2026, ERP 5,0%)*

*Calculado sobre o `modelo_calc` do `config_GOOGL.json` (Excel regerado e verificado a 30-10). Preço $ 292,50.*

**0. A grelha simples — valor por acção ao WACC (10,28%)** *(crescimento × margem EBITDA do Y10)*

| CAGR 10a ＼ Margem EBITDA Y10 | 41% | 44% | **47% (base)** | 50% | 52% |
|---|---|---|---|---|---|
| 9,0% *(base −3 pp)* | $ 124,9 | $ 146,8 | $ 168,6 | $ 190,5 | $ 205,0 |
| 10,5% | $ 139,2 | $ 163,5 | $ 187,8 | $ 212,1 | $ 228,3 |
| **12,0% (base)** | $ 155,2 | $ 182,2 | **$ 209,2** | $ 236,2 | $ 254,2 |
| 13,5% | $ 173,0 | $ 203,0 | $ 233,0 | $ 263,1 | $ 283,1 |
| 15,0% *(base +3 pp)* | $ 192,8 | $ 226,2 | $ 259,6 | **$ 293,0** | **$ 315,3** |

*A negrito, células acima do preço.* O capex é o driver dominante (G13): na linha do base, −0,5 pp → $ 214,1 · +1 pp → $ 199,2 · +2 pp → $ 189,3. **Para valer $ 292,50 ao WACC**, com a margem do base o CAGR teria de ser **16,7%**; com o crescimento do base, a margem EBITDA do Y10 teria de ser **56,3%**.

**1. Retorno que o preço oferece (motor A)** — inalterado pelo ERP

| | IRR |
|---|---|
| **Base** · ponderado | **8,52%** · 8,62% |
| Base com crescimento −3 pp / cash opex +3 pp / g −1 pp | 7,52% / 7,94% / 7,88% |

**2. Crescimento exigido (motor B) — CAGR a 10 anos, por retorno exigido × margem EBITDA do Y10**

| Retorno exigido ＼ Margem Y10 | 41% | 44% | **47% (base)** | 50% |
|---|---|---|---|---|
| WACC + 25 bp (10,53%) | 21,52% | 19,26% | 17,32% | 15,62% |
| **Required 11,28% (nível 2)** | 23,44% | 21,10% | **19,10%** | 17,34% |
| 11% | 22,73% | 20,43% | 18,45% | 16,71% |
| 12% | 25,21% | 22,81% | 20,74% | 18,94% |

Âncoras: CAGR do base 12,05% · histórico FY20-25 17,2% · LTM +22,2% · consenso FY25-30 20,0% (pré-Q3).

**3. Em números falsificáveis** — Y4 com Y1–Y2 no base: o preço exige receita de **$ 1.052 mil M** (base $ 906 mil M), EBITDA **$ 447 mil M** (base $ 385 mil M), NOPAT/acção **$ 18,03** (base $ 14,30) — crescimento de ~25% no Y3 a cair para 14% no Y10.

**Leitura:** com o ERP de 5%, o preço pede ~19% de crescimento durante dez anos com a margem do base para render o required — acima do histórico próprio e no limite do consenso pré-Q3. O retorno que oferece (8,5%) não mudou; o que subiu foi a barra.

---

## SUMÁRIO EXECUTIVO

**Recomendação: esperar — não reforçar acima de $ 209,53; na posição detida, o tecto de peso ao preço de hoje é 3,1% da carteira, e a posição está em ~9%.** Fair value de $ 245,54 ao WACC de 9,39% e de $ 205,22 ao required return de 10,39%, contra $ 292,50 — −16% e −30%. Não é "evitar" porque o negócio continua a melhorar onde a tese precisa: o Cloud dobrou com margem de 36% e o backlog cresceu $ 47 mM num trimestre. Não é "entrada faseada" porque nem o valor ponderado ao required return ($ 209,53) nem o bull ($ 276,53) chegam ao preço.

### A tese numa frase

A Alphabet está a trocar um negócio de pesquisa com capex de 11% da receita por uma plataforma de IA com capex de 40% a 49%, financiada agora com acções novas e dívida; a $ 292 o mercado já não paga o consenso inteiro, mas ainda paga mais crescimento (17% ao ano durante dez anos) do que o base assume (12%) — e a tensão passou do Cloud para a pesquisa: as queries aceleram e a receita por query não.

### Os financials, em vinte segundos

Receita LTM de $ 471.097 M (+22,2%), +24,7% no Q3-26 ($ 127,6 mM, ligeiramente abaixo dos $ 128,2 mM do consenso LSEG): Search & other +12,0% (49,7% da receita), YouTube +9,2%, Network +1,4%, subscrições e devices +11,0%, Cloud +102,6% (24,1%). Só há GAAP: margem operacional de 31,8% no Q3 (34,0% no Q2; 30,5% no Q3-25, com a coima da CE), 33,3% LTM, com o SBC dentro. EPS GAAP de $ 2,12; sem a perda de $ 8,7 mM em participações (SpaceX), $ 2,67 contra $ 3,02 esperados. O que mudou de natureza continua a mudar: capex de $ 51,4 mM (+114%), FCF de −$ 9,1 mM, recompras a zero, $ 12,4 mM de acções emitidas pelo programa ATM (36 M acções a ~$ 344) e $ 28,7 mM de obrigações novas. O inventário subiu $ 3,2 mM no trimestre (sistemas TPU). Caixa e títulos de ~$ 187 mM contra $ 148,5 mM de dívida e preferenciais, mais ~$ 222 mM de participações.

### O DCF — pressupostos e resultado

| Pressuposto | Y1 → Y10 | Âncora histórica |
|---|---|---|
| Crescimento da receita | 22,2% · 19% · 16% · 14% · 12% → 5% (CAGR 5a 16,6%; 10a 12,05%) | LTM +22,2%; Q3 +24,7%; FY20-25 17,2%; consenso FY25-30 20,0% (pré-Q3); backlog Cloud $ 561 mM, >55% em 24 meses |
| Cash opex ex-D&A *(SBC dentro)* | 60,5% → 53,0% | LTM 60,7%; Q3-26 61,6%; Q3-25 64,0% (60,6% sem a coima); consenso 2030 50,9% |
| Capex / receita | 49% · 48% · 42% · 35% · 30% → 16,5% | Guidance FY26 $ 195–205 mM (Q4 implícito $ 63–73 mM) e "aumento significativo" em 2027; Q3-26 40,3%; pré-IA 10–11% |
| D&A | endógeno, por classe: 9,0% → 20,9% (Y6) → 16,5% | Servidores e rede a 6 anos (70% do capex), edifícios a 25 (30%), meio ano; carteira calibrada na depreciação do Q3 × 4 |
| Imposto · NWC | 18% → 19,5% · 10% da Δ receita | ETR LTM 18,1% · média FY22-25 10,8% |
| WACC · g perpétuo | 9,39% · 2,5% | Ke 9,59% (método A; β 1,094 com D/E de 4,1% a $ 292,50); peso da dívida 3,9% |
| SOTP *(v1.5)* | Waymo: $ 53.550 M na ponte | Ronda de Fev-2026 a $ 126 mM × 85% (hipótese) × 50%; perdas do Other Bets (~$ 8 mM/ano) retiradas do cash opex |

**Resultado:** EV de $ 2.817.571 M contra $ 3.400.167 M de mercado; **$ 245,54** por acção. O reverse DCF: o preço oferece **8,52%** (motor A); para render 10,39% a receita teria de crescer **16,98% ao ano durante dez anos** (motor B), ou o capex cair para **12,35%** da receita no Y10 (motor D).

**Três honestidades obrigatórias.** O terminal pesa **81,1%** do EV, com EV/EBITDA de saída de 7,7x — baixo porque o terminal ainda carrega capex de 16,5%. A margem EBIT cai de 31,9% no Y1 para ~24% entre o Y4 e o Y6, com o D&A a chegar a 20,9% da receita, que no FCFF só actua pelo escudo fiscal. E a regra capex ≥ D&A passa no Y10 à justa (1,00x): o artefacto da vida única da v1.4 desapareceu com o D&A por classe, e o capex terminal está exactamente no piso da regra. A amplitude por driver:

| Driver | Cenário adverso | Valor/ação | Δ vs base |
|---|---|---|---|
| **Capex / receita** | +5 pp | $ 189,00 | −23,0% |
| **Crescimento da receita** | −3 pp/ano | $ 197,20 | −19,7% |
| WACC *(não é eixo)* | +100 bp | $ 205,22 | −16,4% |
| Cash opex / receita | +3 pp | $ 214,76 | −12,5% |
| g perpétuo *(não é eixo)* | 1,5% | $ 220,61 | −10,2% |

**G15, frase obrigatória:** contra os factos o base inclina-se agora para o lado *cauteloso* — repor o capex terminal na âncora factual (15,4%) e o imposto no ETR LTM acrescenta 7,24% ao valor; o crescimento do Y1 está no facto (22,2%). Por trás disto há duas mudanças, ambas escritas na §7: a âncora de capex foi recalculada com as classes da v1.5 (era 18,5% com a vida única de 7,8 anos — a vida que acerta o D&A não é a que acerta o stock de PP&E), e com os drivers aprovados a 26-Out o G15 bloqueava (+25,5% contra os factos), por isso o base foi reescrito (G16) em vez de "aproximado a meio".

### Os múltiplos — e se contradizem o DCF

Contra a própria história, o múltiplo de lucro está barato e os de caixa não: TEV/EBITDA LTM 18,9x contra 16,8x (+12%), P/NTM EPS 19,7x contra 21,5x (−8%), market cap/FCF 182x. A queda tirou quase dois terços ao prémio do EV/EBITDA (era +31%). A contradição explica-se como em Outubro: o EPS de consenso tem D&A de $ 52 mM em 2027 e $ 120 mM em 2030, e o DCF paga o capex quando ele sai de caixa. Com uma ressalva nova: o P/E de 19,7x assenta num EPS que vai ser revisto em baixa — o ajustado do Q3 ficou 12% abaixo.

### Qual das fontes é mais credível aqui

Governa o DCF; a mediana do P/E é cross-check. Formou-se com capex de 10% a 30% da receita — outra empresa, em intensidade de capital. Contra o DCF pesam o terminal de 81% e a amplitude de $ 113 no capex, mas o capex é guidance, não escolha minha. E o consenso não fecha consigo próprio: o FCF de 2030 ($ 214 mM) não bate com o seu EBIT e capex, que dão ~$ 80–110 mM.

### Se comprar a X, ganho quanto por ano?

| Preço | EV/EBITDA NTM à entrada | Retorno total 5a | **Anualizado, com re-rating** | Sem re-rating | Re-rating |
|---|---|---|---|---|---|
| $ 292,50 *(preço actual)* | 14,4x | +31,49% | **5,63%** | 8,51% | −2,89% |
| $ 245,54 *(fair value @WACC)* | 12,0x | +56,63% | **9,39%** | 9,39% | +0,00% |
| $ 209,53 *(1ª tranche)* | 10,1x | +83,55% | **12,92%** | 10,27% | +2,65% |
| $ 205,22 *(2ª tranche)* | 9,8x | +87,41% | **13,39%** | 10,39% | +3,00% |
| $ 156,25 *(posição cheia)* | 7,3x | +146,14% | **19,74%** | 12,13% | +7,61% |

**Heatmap — IRR a 5 anos ao preço de hoje**, por crescimento da receita × EV/(EBITDA−capex) de saída. A v1.5 lê a saída nesta base porque o capex do Y6 é 57% do EBITDA.

| Crescimento da receita ＼ EV/(EBITDA−capex) de saída | 16,8x *(= 7,3x EBITDA)* | 21,0x *(DCF; = 9,1x)* | 27,1x *(= 11,8x)* | 33,3x *(hoje; = 14,5x)* | 39,9x *(= 17,3x)* |
|---|---|---|---|---|---|
| −2 pp | −0,77% | 3,55% | 8,77% | 13,21% | 17,28% |
| −1 pp | 0,20% | 4,58% | 9,86% | 14,36% | 18,48% |
| base | 1,17% | **5,61%** | 10,96% | 15,52% | 19,68% |
| +1 pp | 2,15% | 6,65% | 12,07% | 16,68% | 20,89% |
| +2 pp | 3,14% | 7,69% | 13,18% | 17,84% | 22,10% |

A $ 292,50 o retorno continua a ser aposta no múltiplo: 8,51% se o mercado mantiver a taxa de hoje, 5,63% ao ano se convergir para o fair value. Um EV/EBITDA de saída de 15–18x — o intervalo do S&P 500 — corresponde às duas últimas colunas e dá 15,5–19,7%; mas, com o capex ainda a 25% da receita no Y6, isso equivale a pagar 33–40x o EBITDA−capex. Lê-se a coluna DCF (21,0x), não a "hoje": manter o múltiplo de hoje é apostar que o mercado continua a não descontar o capex. Entre linhas a IRR mexe ~1 pp por cada ponto de crescimento — menos do que um ponto de múltiplo.

### Porque não é a recomendação adjacente, e o que a mudaria

**Probabilidades declaradas antes de ver os valores:** bull 25% · base 50% · bear 25% *(default)*. Bull = crescimento +3 pp e cash opex −2 pp; bear = −3 pp e +2 pp; bear de eixo único = capex +5 pp; bear conjunto = crescimento −3 pp, opex +3 pp, capex +5 pp.

| Banda | Preço | Racional | Assimetria bull:bear | Peso máx. |
|---|---|---|---|---|
| Preço actual | $ 292,50 | IRR esperada 8,62% · IRR base 8,52% | −5% : −48% | 3,1% |
| **1ª tranche** | $ 209,53 | **Valor ponderado** ao required return | +32% : −28% (1,1:1) | 4,0% |
| **2ª tranche** | $ 205,22 | **Valor base** ao required return | +35% : −26% (1,3:1) | 4,1% |
| **Posição cheia** | $ 156,25 | **Bear de eixo único** (capex +5 pp) ao required return | +77% : −3% | 6,0% |

A escada desce sempre (ponderado de $ 209,53 acima do base de $ 205,22). O retorno oferecido está 187 bp abaixo do exigido. Na posição detida (~9% do investido), o peso máximo de 3,1% vem da cauda conjunta: no bear conjunto a posição de hoje custaria ~5,8% da carteira (9% × 64%), quase o triplo da perda máxima de 2%. O gate de trim da ficha está disparado desde Outubro; reduzir pesa impostos (FIFO, art. 43.º CIRS) e é decisão do Hugo.

Mudam a recomendação os invalidadores do bloco A. A favor: receita LTM ≥ 25% (INV-1, hoje 22,2%) ou margem LTM ≥ 32% no Q2-27 com o capex cumprido (INV-5). Contra: capex FY27 acima de $ 350 mM sem o Cloud a acompanhar (INV-2), ou Search & other abaixo de 9% num trimestre (INV-3, hoje 12,0%).

**Prémios aplicados** — nenhum risco cobrado duas vezes.

| Prémio | Aplicado? | Valor | Risco que cobre | Sobrepõe-se a outro? |
|---|---|---|---|---|
| CRP *(Damodaran ctryprem)* | Não | 0 | — (o ERP do S&P 500 já embute ~40% de receita externa; a Alphabet tem 49% fora dos EUA, quase toda em mercados desenvolvidos) | — |
| Hurdle *(nível 2 — WACC + 100 bp)* | Sim | +100 bp | Alocação de capital: capex de $ 200–300 mM/ano, FCF negativo em 2026, acções emitidas em Jun-26 e pelo ATM no Q3 ($ 12,4 mM) | Não — o beta mede covariância com o mercado, não a qualidade da alocação |
| Fade terminal abaixo da âncora estrutural | n/a | — | Sem âncora (sem comps). Cash opex Y10 de 53% fica 2,1 pp acima do consenso de 2030 e 8 pp abaixo de hoje | Não — a diferença face ao consenso vem de capacidade de terceiros e energia, não do risco de alocação |

**Próximo catalisador:** o 10-Q do Q3-26, nos próximos dias — paid clicks e CPC, activos por entrar ao serviço, backlog por cliente e o detalhe do ATM. O IPO da Anthropic (reportado para antes de 26-Nov, a ~$ 1,8–2,0 bi): a participação (~13%, não divulgada) passa de não cotada a 50% para cotada a 100% menos imposto — ~+$ 10 por acção na ponte, e a contraparte de >40% do backlog passa a ter preço diário. Depois, as revisões do sell-side e o call do Q4-26 (início de Fev-2027), com o guidance de capex de 2027 — o número que decide o INV-2. **O modelo fica obsoleto com o fecho de 29-Out (preço aproximado) e com o 10-Q (ponte com estimativas marcadas) — G17.**

---

## 1. Negócio — o que vende

A Alphabet vende atenção e computação. A atenção — pesquisa, YouTube, Android, Chrome — monetiza-se em leilões de publicidade cobrados por clique ou impressão; é onde está ~64% da receita (Q3-26) e quase todo o resultado. A computação vende-se através do Google Cloud, por consumo e por compromissos plurianuais, e desde o Q2-26 também como venda de sistemas TPU instalados nos data centers dos clientes. A transição em curso é usar a mesma infraestrutura de IA (modelos Gemini, chips TPU próprios) para as duas metades: respostas na pesquisa (AI Overviews, AI Mode) e capacidade vendida a terceiros — incluindo concorrentes nos modelos, como a Anthropic.

**Segmentos / linhas de produto** *(Q3-26, ER; YoY entre parênteses)*

| Segmento | % receita | O que é | Cliente-tipo |
|---|---|---|---|
| Google Search & other | 49,7% *(+12,0%)* | Anúncios na pesquisa, Maps, Gmail, AI Mode | Anunciantes de performance (retalho, finanças) |
| YouTube ads | 8,8% *(+9,2%)* | Vídeo, brand e direct response, Shorts, TV | Marcas e agências |
| Google Network | 5,8% *(+1,4%)* | AdMob, AdSense, Ad Manager em sites de terceiros | Editores e anunciantes |
| Subscriptions, platforms & devices | 11,2% *(+11,0%)* | YouTube Premium/Music, Google One (planos de IA), Play, Pixel | Consumidor |
| Google Cloud | 24,1% *(+102,6%)* | GCP, IA (Vertex, Gemini Enterprise), Workspace, sistemas TPU | Empresas, laboratórios de IA |
| Other Bets | 0,3% | Waymo e outros | Consumidor (robotáxi) |

**Métricas de escala:** receita LTM $ 471,1 mM ("half-trillion run rate"); Gemini app acima de 1.000 M utilizadores mensais; ~32 mM de tokens por minuto nos modelos próprios, 4x há um ano; queries de pesquisa a crescer ao ritmo mais alto em cinco anos (ER do Q3-26, sem número); backlog do Cloud de $ 561 mM, mais de 55% em 24 meses (Reuters); PP&E líquido de $ 372,8 mM, dos quais $ 122,8 mM por entrar ao serviço em Jun-26 (10-Q); capex LTM de $ 159,8 mM; 204.757 empregados (+7,7%). *Paid clicks e CPC do Q3 por confirmar no 10-Q.*

**Exposição geográfica** *(Q2-26):* EUA 51%, EMEA 27%, APAC 16%, outras Américas 6%. **Concentração de clientes:** o 10-K diz que nenhum cliente passou de 10% da receita em 2023-25 — mas a nota fala de receita, não de backlog, e é no backlog que está a concentração (Anthropic, >40% segundo a The Information).

---

## 2. Vantagem competitiva — porquê esta e não a rival

**Rival de referência:** Microsoft — é a única empresa que ataca as duas metades da tese ao mesmo tempo: IA de consumo e pesquisa (Copilot, Bing, participação na OpenAI) e cloud de IA (Azure, +43% no último trimestre fiscal, segundo a ficha MSFT). A Amazon (AWS, Trainium) é a rival no Cloud; a OpenAI é a rival na pesquisa.

| Dimensão | Alphabet | Microsoft | Quem ganha, e porquê |
|---|---|---|---|
| Produto / tecnologia | Modelos próprios (Gemini) + chips próprios (TPU) + cloud própria | Modelos da OpenAI + GPUs Nvidia + chips Maia | **Alphabet** — integração vertical baixa o custo por token; a TPU já se vende a terceiros |
| Distribuição e go-to-market | Pesquisa, Android, Chrome, YouTube — milhares de milhões de utilizadores | Base de postos Windows/Office nas empresas | **Empate** — Alphabet no consumidor, Microsoft na empresa |
| Pricing power | CPC +3% com cliques +13% (Q2); Search +12% no Q3 com queries a acelerar | Preços por posto (Copilot) e consumo (Azure) | **Microsoft** — o posto empresarial sobe preço; o CPC está a crescer devagar |
| Escala | Capex 2026 $ 195–205 mM | Capex a 44–48% da receita | **Empate** — os dois compram a mesma escala com o mesmo dinheiro |
| Custo de mudança para o cliente | Pesquisa: um clique (ChatGPT está ao lado) | Office, Entra, Teams: anos | **Microsoft** — é a fraqueza estrutural da Alphabet |
| Economia unitária | Margem Cloud 36,2%; Services 40,7% (Q3-26) | Margem operacional 46,8% | **Microsoft** — mais software, menos publicidade |

**Se o diferencial for real, aparece nos números. Onde?** No Cloud: margem de 23,7% para 36,2% em doze meses, a crescer 103% — a TPU própria aparece na margem. E na pesquisa até ao Q2: com o ChatGPT a vender anúncios desde 2026, Search acelerou de +9,8% (Q1-25) para +19,1% (Q1-26) e +16,8% (Q2-26). *No Q3-26 desceu para +12,0%, com as queries a acelerar — a primeira vez que a receita por query aparece a fazer o trabalho contrário.*

**E onde NÃO aparece?** No FCF: −$ 5,9 mM no Q2 e −$ 9,1 mM no Q3, recompras a zero e acções emitidas a ~$ 355 (Jun) e ~$ 344 (ATM, Q3). E no ROIC, de 43,9% (FY24) para 31,6% (LTM), porque o capital cresce mais depressa do que o lucro. O diferencial tecnológico existe, mas ainda não se vê em caixa.

**Riscos dos competidores — o que a pesquisa encontrou** *(fontes sérias, Out-2026)*

| Competidor | Movimento | Canal de transmissão | Sinal a seguir |
|---|---|---|---|
| OpenAI | Anúncios no ChatGPT acima de $ 1 mM de run-rate anualizado (Adweek, 31-Ago-26); objectivo de $ 2,5 mM em 2026 e $ 100 mM em 2030 (Axios, via MarketScreener) | Queries comerciais e CPC da pesquisa | Paid clicks e CPC no 10-Q; Search & other YoY |
| Anthropic | Compromisso de $ 200 mM em 5 anos com o Google Cloud (The Information, via Reuters, 5-Mai-26) | Concentração do backlog; contraparte é também participada (até $ 40 mM investidos) | Nota de concentração do 10-K; marcações das não cotadas |
| Microsoft / AWS | Capex ao mesmo ritmo; Azure +43% | Preço da capacidade de IA → margem Cloud | Margem Cloud por trimestre |
| Apple | Gemini a alimentar a nova Siri (reportado em Jan-26); acordo de pesquisa por defeito sob os remédios do DOJ | TAC e quota de queries no iOS | Recurso do DOJ; TAC no 10-Q |
| Fornecedores de capacidade (neoclouds) | A Alphabet vai usar capacidade de terceiros no Q3 como "ponte" (call do Q2) | Margem de curto prazo: capacidade de terceiros é opex, não capex | Cash opex do Q3-26 |

---

## 3. Monetização — de onde vem exactamente o dinheiro

| Fluxo | % receita | Unidade cobrada | Quem paga | Recorrente? | Preço/unidade |
|---|---|---|---|---|---|
| Anúncios na pesquisa | 49,7% | Clique (CPC) | Anunciante | Repetido, sem contrato | CPC +3% YoY (Q2; Q3 no 10-Q) |
| Anúncios YouTube | 8,8% | Impressão / visualização | Anunciante | Repetido | n/d |
| Anúncios Network | 5,8% | Impressão | Anunciante (paga-se TAC ao editor) | Repetido | Impressões −12% (Q2) |
| Subscrições, plataformas, devices | 11,2% | Assinatura / comissão Play / hardware | Consumidor | Sim (assinaturas) | n/d |
| Cloud — GCP e IA | 24,1% *(Cloud total; a TPU não é separada)* | Consumo e compromissos | Empresas, labs de IA | Contratado (backlog) | n/d |
| Cloud — sistemas TPU | dentro do Cloud; "meaningful contributor" no Q3 | Venda de sistema | Clientes com data center próprio | Não — receita de hardware | "Vast majority" em 2027 |
| Other Bets | 0,3% | Viagem, licença | Consumidor | Não | n/d |

**Mecânica do fluxo principal.** O anunciante licita por palavra-chave e paga por clique. A Alphabet paga traffic acquisition costs a quem lhe traz a query — Apple, Samsung, browsers e editores da Network. Desde Set-2025 esses acordos não podem ser exclusivos (remédios do caso DOJ). **Alavancas de preço:** formatos novos de anúncio no AI Mode e Shopping ads em queries mais longas. **Onde o dinheiro NÃO vem:** do Gemini app, que monetiza por assinatura (Google One) e não por anúncios. **Qualidade da receita:** backlog de $ 561 mM no Cloud (mais de 55% em 24 meses, Reuters); deferred revenue de apenas $ 8,6 mM (Dez-25). Desde o Q1-26 o backlog inclui contratos ≤ 1 ano, e a série deixou de ser comparável (G6).

**Assimetria de monetização vs custo.** Uma resposta de IA custa mais a servir do que uma página de links, e a monetização por query só se diz "encorajadora" — o CPC sobe 3%. O custo já aparece: o other cost of revenues subiu 22% no Q2, por depreciação, inventário de TPU e conteúdo. A partir do Q3 entra a capacidade de terceiros, que a gestão diz criar "modest margin pressure".

---

## 4. Moat — porque é que isto não é replicável

| Tipo de moat | Presente? | Evidência quantitativa | Força |
|---|---|---|---|
| Network effects | Sim | Leilão com milhões de anunciantes; paid clicks +13% (Q2) | Forte |
| Switching costs | Fraco no consumidor, médio no Cloud | Pesquisa a um clique; Cloud com compromissos plurianuais ($ 561 mM) | Médio |
| Economias de escala | Sim | Capex de $ 200 mM/ano que só 4–5 empresas no mundo conseguem financiar | Forte, mas partilhada |
| Intangíveis (dados, marca, TPU) | Sim | 20+ anos de dados de query e clique; TPU co-desenhada há uma década, já vendida a terceiros | Forte |
| Vantagem de custo estrutural | Sim, no Cloud | Margem Cloud 36,2% a crescer 103% | A provar no ciclo |
| Distribuição / densidade | Sim | Android, Chrome, defaults pagos no iOS — agora não exclusivos | A estreitar por via regulatória |

**Teste do capital ilimitado**

> Se um competidor com € 10 mil milhões e cinco anos copiasse isto amanhã, **o que é que o dinheiro não compra?**

Não compra a liquidez do leilão — anunciantes e queries juntos, cada lado a atrair o outro. Também não compra 20 anos de dados de clique, a biblioteca do YouTube nem uma década de co-desenho do chip. Compra os modelos de fronteira: OpenAI e Anthropic chegaram lá sem nada disto. E comprou cinco anos de distribuição alternativa — o ChatGPT tem centenas de milhões de utilizadores e já vende anúncios. O moat está no leilão e na distribuição, não no modelo.

**O que erode o moat, e a que velocidade.** Os motores de resposta (ChatGPT) atacam as queries informacionais primeiro e as comerciais depois. Os remédios do DOJ obrigam a partilhar dados de índice com rivais qualificados. O DMA na UE proíbe self-preferencing. **Trajectória: estável nos números, a estreitar na estrutura.** Search abrandou para +12,0% no Q3 (16,8% no Q2) com as queries a acelerar — o primeiro sinal de que o problema é a receita por query, não o volume —, e a distribuição que protegia o leilão — defaults exclusivos e dados fechados — está a ser aberta por tribunal e regulador.

### O moat converte-se em economia? O teste do ROIC

| | FY22 | FY23 | FY24 | FY25 | LTM |
|---|---|---|---|---|---|
| NOPAT normalizado *(EBIT × (1−ETR))* | $ 62.942 M | $ 72.576 M | $ 93.958 M | $ 107.360 M | $ 128.627 M |
| Capital investido *(fim)* | $ 139.092 M | $ 165.785 M | $ 214.019 M | $ 279.026 M | $ 406.688 M |
| **ROIC** *(capital fim de período)* | 45,3% | 43,8% | 43,9% | 38,5% | 31,6% |
| Spread vs WACC (9,39%) | +35,9 pp | +34,4 pp | +34,5 pp | +29,1 pp | +22,2 pp |

*LTM = Set-26 (ETR LTM 18,1%; capital investido de 30-Set com estimativas onde o 10-Q ainda não saiu).* Nas três bases: fim de período 31,6% LTM; capital médio 38,7% LTM (47,6% FY23, 49,5% FY24, 43,5% FY25); NOPAT normalizado da amortização de aquisições igual na prática (~$ 0,4 mM/trimestre de amortização). Capital investido = activo total − caixa − títulos − não cotadas − SpaceX de longo prazo − passivos operacionais sem juros.

| | |
|---|---|
| Capital investido acrescentado (FY23 → LTM) | $ 240.903 M |
| Δ NOPAT normalizado | $ 56.051 M |
| **ROIC marginal** | **23,3%** *(17,3% só nos últimos 12 meses: Δ NOPAT ~$ 25,7 mM sobre $ 148.404 M)* |
| WACC | 9,39% |

O capital deployado rende acima do custo, mas o marginal está a descer, e o que vem é de outra ordem: ~$ 1,57 bi de capex nos cinco anos do modelo contra $ 241 mM de capital acrescentado desde FY23. **G20 (v1.5):** o base implica um ROIC marginal de 21,7% no Y10 sobre $ 1.103 mM de investimento líquido — próximo do histórico, por isso não é um bear disfarçado nos retornos —, mas de 7,9% até ao Y5, abaixo do WACC, porque o D&A chega antes do lucro. E cada dólar de capex compra $ 0,35 de receita nova, contra $ 0,62 no histórico: ou o capex do base está alto para o crescimento do base, ou o crescimento baixo para o capex (teste na §7). Cruzamento com o Return on Capital do CapIQ: não incluído no export.

---

## 5. SWOT

**Forças.** Leilão de pesquisa com as queries a crescer ao ritmo mais alto em cinco anos, em plena concorrência de IA. Cloud com margem de 36,2% e backlog de $ 561 mM. Integração vertical modelo–chip–cloud, com a TPU já vendida a terceiros. Balanço com ~$ 187 mM de caixa e títulos e ~$ 222 mM de participações (SpaceX cotada desde Jun-26).

**Fraquezas.** O capex passou de 11% para 40% da receita, com FCF negativo no Q2 e no Q3. A empresa emite acções em vez de as recomprar (Jun-26 e ATM no Q3, com $ 27,6 mM por usar). ~64% da receita é publicidade e depende do comportamento de pesquisa — e a receita por query abrandou no Q3. O resultado líquido é dominado por marcações de participações, nos dois sentidos (+$ 98 mM no Q2, −$ 8,2 mM no Q3).

**Oportunidades.** Vendas de sistemas TPU sobretudo em 2027. Anúncios no AI Mode (mais de 1.000 M de utilizadores mensais). Waymo.

**Ameaças.** OpenAI nos anúncios: probabilidade alta, horizonte 2–4 anos, $ 100 mM de objectivo em 2030 contra ~$ 250 mM de Search & other LTM. Monetização por query a ceder ao AI Mode (Search +12,0% no Q3 com as queries a acelerar). Recurso do DOJ com remédios mais duros: probabilidade baixa a média, 2027. Concentração do backlog numa contraparte que é também participada. Diluição: ATM com $ 27,6 mM por usar. Taxas: com o UST 10Y a 5%, cada +100 bp no WACC vale −$ 40 por acção.

---

## 6. Legal, regulatório e fiscal

| Matéria | Tipo | Estado | Exposição máx. | % market cap | Timeline |
|---|---|---|---|---|---|
| DOJ — pesquisa (EUA) | Antitrust | Remédios de Set-2025: sem venda do Chrome, fim da exclusividade, partilha de dados com rivais. DOJ e estados recorreram a 3-Fev-2026, a pedir remédios mais duros (Bloomberg Government) | Venda do Chrome ou proibição de pagamentos por defeito → perda de quota de queries | não quantificável | Recurso no D.C. Circuit; decisão provável em 2027 (estimativa) |
| DOJ — ad tech (EUA) | Antitrust | Remédios de 16-Set-2026 (juíza Brinkema): sem venda do AdX, regras comportamentais por 6 anos, monitor de compliance. A Google recorre da condenação; o DOJ pondera recurso (Reuters) | Network = 6,1% da receita, a −0,7% YoY | < 1% | Proposta de sentença em 30 dias; recurso |
| CE — ad tech (UE) | Coima | € 2,95 mM em Set-2025, registada no Q3-25; em recurso | Coimas da CE acrescidas no balanço: $ 10,6 mM (10-Q Q3-25) | 0,3% | Tribunal Geral da UE |
| CE — DMA (UE) | Coima + conformidade | € 890 M em Jul-2026: € 460 M por self-preferencing na pesquisa, € 430 M por anti-steering no Play; 60 dias para cumprir (Law Society Gazette, 23-Jul-26) | Sanções periódicas de até 5% do volume de negócios mundial médio diário | — | Prazo de conformidade em Set-2026 |
| Pilar 2 / ETR | Fiscal | ETR LTM 18,1% (Set-26); Pilar 2 a empurrar para cima | +1 pp de ETR ≈ −$ 2,6 por acção | — | Contínuo |

**Regime regulatório.** Gatekeeper ao abrigo do DMA na UE, e condenada por monopólio em dois processos nos EUA (pesquisa em 2024, ad tech em Abr-2025). **Risco fiscal.** ETR a subir com o Pilar 2; os ganhos não realizados em participações geram impostos diferidos (~22% sobre o ganho no Q2). **Antitrust.** O risco que move o valor não é a coima: é a perda de distribuição por defeito na pesquisa. **Histórico de condenações.** CE: € 2,4 mM (2017, Shopping), € 4,1 mM (2018, Android), € 2,95 mM (2025, ad tech); a de € 1,5 mM (2019, AdSense) foi anulada em 2024.

**Factores de risco NOVOS face ao ano anterior.** Os mais informativos são três: participações de grande dimensão com restrições de venda (SpaceX até ao Q3-27), dependência de capacidade de terceiros e vendas de sistemas TPU com reconhecimento de receita irregular. *Por confirmar no 10-K FY26 — o Item 1A do 10-Q do Q2 não foi comparado linha a linha.*

---

## 7. Enquadramento de valuation

### Que métricas são as certas

| Múltiplo | Usar? | Porquê / porque não |
|---|---|---|
| P/E GAAP | Não | Mark-to-market de participações nos dois sentidos: +$ 98 mM no Q2 (71% do lucro), −$ 8,2 mM no Q3 |
| P/E ajustado | Com cuidado | O consenso normalizado ainda não carrega o D&A da vaga de capex |
| EV/EBITDA | Sim, LTM | Na base do modelo (SBC dentro). O consenso soma o SBC — não usar (G1) |
| EV/Receita *(LTM e forward)* | Referência | Mudança de mix (Cloud de 12% para 24%) distorce a série |
| P / NTM EPS *(forward)* | Sim — o que o mercado paga | Cross-check, não âncora |
| EV/FCF | Sim, como alarme | FCF negativo no Q2 e no Q3: números sem significado até 2028 |
| P/TBV e ROE | Não | Não é financeira |
| Específico do sector | Backlog / receita Cloud | 6,0x a receita Cloud LTM ($ 93,2 mM); mostra a procura, não o valor |

**Métrica âncora:** DCF por FCFF, porque a questão em aberto é o capex e só o FCFF a vê. **Peers:** nenhum, por decisão do Hugo. **Armadilhas conhecidas:** o EPS GAAP inclui ganhos de participações; o TEV do CapIQ abate como caixa ~$ 80 mM de SpaceX com restrição de venda, ignora $ 135 mM de não cotadas e não separa a Waymo (G4); o EBITDA de consenso soma o SBC; o backlog mudou de definição no Q1-26.

**Forward multiples.** P/NTM EPS de 19,7x contra a mediana de forwards de 21,5x (CapIQ, Set-23 a Jun-26), sobre o consenso de 22-Out. Esteve em 29,5x a 30-Jun, no máximo de três anos. Com o EPS de 2027 revisto em baixa no mesmo ritmo do Q3 (−12%), o múltiplo voltaria a ~22x — na mediana.

### O múltiplo é barato porque o preço caiu, ou porque o lucro caiu?

Caiu o preço, não o lucro: o TEV/EBITDA LTM desceu de 22,0x para 18,9x entre 23-Out e hoje, com o EBITDA LTM a subir. O trimestre anualizado sai *abaixo* do LTM, porque o lucro continua a crescer.

| | LTM Set-26 *(TEV a $ 292,50)* | Mediana 3 anos | **Q3-26 anualizado** |
|---|---|---|---|
| EV / Receita | 7,43x | 6,2x | 6,85x |
| EV / EBITDA | 18,86x | 16,8x | 17,87x |
| EV / EBIT | 22,28x | 20,2x | 21,55x |

### Decomposição de qualquer colapso de margem

Não há colapso contra o homólogo: a margem operacional subiu de 30,5% (Q3-25) para 31,8% (Q3-26). Contra o Q2 desceu 2,2 pp (34,0%): capacidade de terceiros, vendas de TPU com margem de hardware, I&D de IA partilhada (+71%) e depreciação (+49%). A Alphabet não publica reconciliação non-GAAP, por isso a decomposição faz-se por segmento (ER), contra o trimestre homólogo (G11).

| | Q3-25 | Q3-26 | Δ | Corre off? |
|---|---|---|---|---|
| Google Services — OI | $ 33.527 M *(38,5%)* | $ 39.157 M *(40,7%)* | +$ 5.630 M | Em parte — o Q3-25 tem a coima de ~$ 3,5 mM da CE (segmento a confirmar no 10-Q); sem ela a margem homóloga desceria |
| Google Cloud — OI | $ 3.594 M *(23,7%)* | $ 11.121 M *(36,2%)* | +$ 7.527 M | — |
| Other Bets — OI | −$ 1.426 M | −$ 2.047 M | −$ 621 M | Não — Waymo em expansão; fora do cash opex no modelo (SOTP) |
| Alphabet-level | −$ 4.467 M | −$ 7.655 M | −$ 3.188 M | Não — I&D de IA partilhada |
| SBC *(dentro de tudo acima)* | $ 6.368 M | $ 8.630 M | +$ 2.262 M | **Não** — é remuneração |
| **Operating income GAAP** | **$ 31.228 M** | **$ 40.576 M** | **+$ 9.348 M** | |

**Coerência obrigatória.** A compressão que o modelo projecta (margem EBIT para ~24% entre o Y4 e o Y6) é D&A de infraestrutura, operacional e permanente. Não é amortização que corre off, e nenhum invalidador a trata como tal.

### Três lentes, três veredictos

| Lente | Veredicto |
|---|---|
| vs história própria de múltiplos | **Neutro:** P/E forward 8% abaixo da mediana (sobre consenso pré-Q3); EV/EBITDA 12% acima; P/FCF sem significado |
| vs peers | n/a — decisão do Hugo |
| DCF | **Caro:** fair value $ 245,54, −16%; o preço só fecha com crescimento +3 pp ao ano em todo o horizonte ($ 305,67) ou a um WACC de ~8,5% |

As lentes discordam porque medem coisas diferentes: o P/E mede o lucro de hoje, o DCF o caixa depois do capex. Governa o DCF — o capex é guidance da própria empresa, não uma escolha minha —, e o P/E fica como medida do que o mercado está disposto a ignorar.

### Os drivers dominantes — por sensibilidade, não por intuição (G13)

Bandas definidas antes de olhar para o resultado: crescimento ±3 pp, capex ±5 pp, cash opex ±3 pp, WACC ±100 bp, g 1,5%/3,5%, imposto ±3 pp, NWC 5%/15%, vida dos servidores 4,2/8,2 anos (em modo classes a banda desloca a classe de 6 anos).

| Driver | Cenário adverso | Valor/ação | Δ vs base |
|---|---|---|---|
| Capex / receita | +5 pp | $ 189,00 | −23,0% |
| Crescimento da receita | −3 pp | $ 197,20 | −19,7% |
| WACC *(não é eixo)* | +100 bp | $ 205,22 | −16,4% |
| Cash opex / receita | +3 pp | $ 214,76 | −12,5% |
| g perpétuo *(não é eixo)* | 1,5% | $ 220,61 | −10,2% |
| Taxa de imposto | +3 pp | $ 234,32 | −4,6% |
| NWC / Δ receita | 15% | $ 241,03 | −1,8% |
| Vida dos servidores | 8,2 anos | $ 244,21 | −0,5% *(só escudo fiscal)* |

**Os dois mais sensíveis tornam-se os eixos da grelha** (valor por acção ao WACC; viva na folha `Cenarios`).

| Capex ＼ Crescimento | bull (+3 pp) | **base** | bear (−3 pp) |
|---|---|---|---|
| bull (−5 pp) | $ 376,46 | $ 302,08 | $ 242,34 |
| **base** | $ 305,67 | **$ 245,54** | $ 197,20 |
| bear (+5 pp) | $ 234,89 | $ 189,00 | $ 152,05 |

**Porquê cada eixo, e porquê o valor do base.** O capex é o eixo 1 porque é o mais sensível e o mais guiado: o base usa o guidance e o consenso nos três primeiros anos e, no terminal, o piso da regra capex ≥ D&A. O crescimento é o eixo 2: o Y1 está no facto (LTM +22,2%) e o fade é o aprovado a 26-Out, abaixo do consenso pré-Q3 (CAGR 16,6% contra ~19% em cinco anos). Coerência interna, nos dois sentidos:

- Não há alavanca operacional agressiva numa receita a desacelerar: o cash opex melhora 0,75 pp/ano, abaixo do ritmo de FY22-25 (~1,5 pp/ano).
- O último trimestre **não** confirma o driver de opex do Y1 (G14): Q3-26 61,6% contra 60,5% no Y1 (Q3-25 64,0%, 60,6% sem a coima). Capacidade de terceiros e TPU. LTM 60,7%. Um trimestre não muda o driver; fica em vigilância.
- Drivers do lado cauteloso ao mesmo tempo (G15): contra os factos, o capex terminal e o imposto; contra o consenso, o crescimento e o opex — quatro marcações, contadas como quatro.
- **G20 — o capex compra o crescimento que o base assume?** Não ao ritmo histórico. ROIC marginal implícito de 7,9% até ao Y5 (abaixo do WACC) e 21,7% no Y10; receita nova por dólar de capex de 0,35 contra 0,62. Teste com os dois a andar juntos: crescimento no caminho do consenso e capex −5 pp em todos os anos dá 0,44, $ 322,79 ao WACC e $ 271,40 ao required — ainda abaixo do preço. Cada um sozinho: consenso no crescimento $ 262,22; capex −5 pp $ 302,08.
- A âncora estrutural não existe nesta ficha (sem comps); o opex terminal só tem o consenso como referência externa.
- Nenhum driver ficou "aproximado a meio" (G16): com os drivers aprovados o G15 bloqueava, e o base foi reescrito.

### Corrida de reversão (G15)

**Correcção da âncora de capex (29-Out-2026).** Em Outubro a âncora factual era 2 × 0,72 / 7,8 = 18,5%. O 7,8 é a vida que acerta o *fluxo* de D&A — 1 / (0,7/6 + 0,3/25), uma média harmónica. Para o *stock* de PP&E líquido conta a meia-vida de cada classe: em steady state (g 2,5%, meio ano) o PP&E líquido vale 5,15x o capex anual. Com a mesma regra — manter a intensidade de PP&E de hoje, 0,79x a receita, obra em curso incluída — o capex de steady state é **15,4%**; só com o PP&E em serviço (0,445x a Jun-26) seria 8,7%. Consequência: em Outubro o base já estava do lado cauteloso no capex, e a frase G15 de então ("inclina-se para o favorável") estava errada nessa parcela.

**Tabela 1 — cada driver contra a sua referência, com o tipo** *(04_reversao.py)*

| Driver | Tipo | No modelo | Referência | Fonte | Direcção | Efeito no valor/acção |
|---|---|---|---|---|---|---|
| Crescimento | facto | Y1 22,2% | 22,2% | LTM Set-26 aplicado ao Y1, mesmo fade | em linha | $ 0,00 |
| Cash opex | consenso | Y10 53,0% | 50,9% | Consenso 2030 (EBIT 37,1% + D&A 12,0%) | conservador | +$ 21,54 |
| Capex | facto | Y10 16,5% | 15,4% | Derivado com as classes v1.5: PP&E líquido/receita (0,79x) ÷ 5,15 | conservador | +$ 12,44 |
| Imposto | facto | Y10 19,5% | 18,1% | ETR LTM Set-26 | conservador | +$ 5,24 |
| NWC | facto | 10,0% | 10,8% | Média FY22-25 | favorável | −$ 0,72 |

**Tabela 2 — reversão cumulativa**

| Passo | Driver reposto | Valor/acção | Delta acumulado |
|---|---|---|---|
| 0 | base publicado | $ 245,54 | — |
| *Conservadores vs factos* | | | |
| 1 | capex | $ 257,98 | +5,07% |
| 2 | + imposto | $ 263,32 | +7,24% |
| *Favoráveis vs factos (simetria)* | | | |
| 1 | NWC | $ 244,82 | −0,29% |
| *Conservadores vs consenso (decomposição)* | | | |
| 1 | crescimento no caminho do consenso (25,8% → 5%) | $ 262,22 | +6,8% |
| 2 | + cash opex do consenso (58,5% → 50%) | $ 300,72 | +22,5% |

**Leitura.** Contra os factos o base está do lado cauteloso por 7,24% — frase obrigatória no sumário, escrita. Duas ressalvas no capex: o `04` desloca a curva inteira (−1,1 pp em todos os anos, incluindo os de guidance) e, levado aos 15,4%, o capex ficaria abaixo do D&A do Y10 (0,95x), que a regra terminal não deixa; por isso o base fica no piso, 16,5%. Contra o consenso está do lado cauteloso por $ 55,18: $ 16,68 de crescimento e $ 38,50 de margem. O resto do fosso até ao PT ($ 183,58 no total) — ~$ 128 — não é operação: com a operação do consenso, o PT só se obtém com um WACC de 7,67% (8,11% se o PT for descontado um ano). Não há diferença de base contabilística a decompor: o EBIT de consenso já é GAAP (FY25A 129.039 = 10-K).

**Com os drivers aprovados a 26-Out** (crescimento 21% no Y1, capex terminal 18%): $ 218,22 ao WACC, $ 182,70 ao required, IRR implícita de 7,97% a $ 292,50 — e G15 bloqueante (+25,5% contra os factos: crescimento +9,1%, capex +12,7%, imposto). As duas mudanças valem $ 27,32: ~$ 14 o crescimento e ~$ 13 o capex terminal.

**Âncora estrutural: dispensada.** O `04` sai com código 1 porque nenhum driver terminal tem âncora dos pares, e é isso que a regra v1.3 exige. A âncora fica dispensada por decisão do Hugo (26-Out-2026) — sem comps em mega-caps com n negócios. Consequência a não esquecer: o cash opex terminal só tem o consenso como travão.

**Calibração entre nomes** *(gatilho: 3+ fichas com FV/PT < 0,70)*

| Ficha | FV / PT consenso | IRR implícita (motor A) |
|---|---|---|
| BKNG | 1,09 | 11,97% |
| META | 0,75 | 9,29% |
| MSFT | 0,72 | 9,28% |
| CELH | 0,71 | bloqueada (G17) |
| NOW | 0,60 | 8,84% |
| **GOOGL** | **0,57** | **8,52%** |
| FICO | 0,51 | 7,36% |
| NU | 0,49 | 11,5% |
| CRWV | 0,27 | n/a |
| MELI · SAP | sem PT na ficha | 11,20% · 12,28% |

Cinco de nove fichas com PT continuam abaixo de 0,70 — informação sobre o método, não só sobre as empresas. Os retornos implícitos não se agrupam (7,4% a 12,3%), por isso não é o caso "a classe limpa ao custo de capital". Na GOOGL ~70% do fosso face ao PT é taxa de desconto: WACC de 9,39% contra os 7,67% que o PT implica com a operação do consenso — e o PT é de antes do Q3. Não se ajusta nenhum parâmetro para acertar o resultado.

### Gates que dispararam

| Gate | Saída | Número |
|---|---|---|
| G1 GAAP vs non-GAAP | Aceite | EPS GAAP do Q3 com −$ 0,55 de mark-to-market (SpaceX); o "ajustado" de $ 2,67 é construção do consenso, não da empresa; EBITDA de consenso com SBC somado — não usado |
| G4 EV / activos líquidos | Resolvido, com estimativas | SpaceX a 145,23 (28-Out) líquida de 22% de imposto; títulos de dívida e finance leases estimados até ao 10-Q; parte da Waymo tirada dos minoritários (vai no SOTP) |
| G6 Reclassificações | Aceite | D&A do Q3 só com depreciação (amortização no 10-Q); backlog com a definição do Q1-26 |
| G15 corrida | Divulgar — +7,24% cauteloso | Com os drivers de 26-Out bloqueava (+25,5%) → base reescrito (G16): crescimento do Y1 no facto e capex terminal no piso capex = D&A |
| G15 âncora de capex | Corrigida | 18,5% → 15,4% (stock de PP&E com as classes da v1.5) |
| G15 âncora estrutural | Dispensada por decisão escrita | Sem comps |
| G16 regra terminal capex ≥ D&A | Passa | 1,00x no Y10 com D&A por classe (era 0,80x por artefacto da vida única) |
| G17 | Passa, com prazo | Preço after-hours de 28-Out; refazer com o fecho de 29-Out e a ponte com o 10-Q |
| G20 coerência capex–crescimento | ATENÇÃO (2) | ROIC marginal de 7,9% até ao Y5 < WACC; receita nova/capex 0,35 vs 0,62 |
| Calibração | Disparou — corrida | FV/PT 0,57; 5 de 9 abaixo de 0,70 |

---

## A. Invalidadores da tese

**Regras:** número legível numa fonte pública **sem estimar**; threshold que a série já quase tocou; frequência compatível com a fonte.

| # | Afirmação (secção) | Invalidador — condição observável | Onde verifico | Definido | Estado | Revisto |
|---|---|---|---|---|---|---|
| 1 | O crescimento do base (22,2% no Y1, a desacelerar) é o cenário modal (§7) | Receita LTM YoY ≥ 25% | ER trimestral | 26-10-2026 | **Vigiar** — LTM +22,2% (era 20,1%); Q3 +24,7% | 29-10-2026 |
| 2 | O capex normaliza a partir de 2028 (§7) | Guidance de capex FY27 > $ 350 mM *sem* receita Cloud do trimestre ≥ +50% YoY | Call do Q4-26 e ER | 26-10-2026 | **Vigiar** — FY27 "aumenta significativamente", sem número; Cloud +102,6% | 29-10-2026 |
| 3 | A pesquisa resiste aos motores de resposta (§2, §4) | Google Search & other YoY < 9% num trimestre | 10-Q, Note 2 | 26-10-2026 | **Vigiar** — +12,0% (16,8% no Q2), com as queries a acelerar; a gestão avisou de comparações mais duras no Q4 | 29-10-2026 |
| 4 | A procura no Cloud é real e diversificada (§3) | Backlog do Cloud cai face ao trimestre anterior | 10-Q, Revenue Backlog | 26-10-2026 | OK — $ 561 mM, +$ 47 mM no Q3 (Reuters; confirmar no 10-Q) | 29-10-2026 |
| 5 | O D&A comprime a margem como o modelo projecta (§7) | Margem operacional LTM ≥ 32% no Q2-27 *com* capex LTM ≥ $ 250 mM (o modelo tem 31,9% no Y1 e 28,4% no Y2) | ER do Q2-27 | 26-10-2026 | OK — por testar; LTM 33,3%, Q3 31,8%; capex LTM $ 159,8 mM | 29-10-2026 |
| 6 | Os remédios na pesquisa ficam comportamentais (§6) | Decisão de recurso que imponha a venda do Chrome ou proíba pagamentos por defeito | D.C. Circuit; 8-K | 26-10-2026 | OK — recurso pendente | 29-10-2026 |
| 7 | Sem concentração material de clientes (§1) | O 10-K divulga um cliente > 10% da receita, ou a Alphabet quantifica um cliente no backlog | 10-K, Note 2; 10-Q | 26-10-2026 | OK — "nenhum > 10%" em FY23-25; 10-Q do Q3 por ler | 29-10-2026 |

Os invalidadores 1 e 5 jogam contra a tese de preço: se dispararem, o base está demasiado baixo. Os 2, 3, 4, 6 e 7 jogam contra a tese do negócio.

**Disparados — o que fiz a seguir**

| # | Data | O que disparou | Decisão tomada |
|---|---|---|---|
| — | — | Nenhum | — |

**Regra de saída.** Para o caso de estar errado: INV-3 *e* INV-4 no mesmo trimestre → rever a ficha de raiz e reduzir a posição para metade do peso máximo. Para o caso de estar certo: preço abaixo de $ 209,53 → 1ª tranche. Gate de trim: peso acima de 3,1% da carteira ao preço de hoje (sobe para 4,0% a $ 209,53). **Estado a 29-Out: disparado — a posição está em ~9%.**

---

## B. Log de fair value e decisões

| Data | Quarter | Preço | FV DCF | IRR impl. | Growth impl. | Decisão | Racional (1 linha) |
|---|---|---|---|---|---|---|---|
| 30-10-2026 | Q3-26 | $ 292,50 | $ 209,17 | 8,52% | CAGR 19,10% @required | Esperar | Regra de custo de capital da carteira: Rf 10Y 5,05% (28-10) + ERP Kroll 5,0%. Ponte: Rf −$ 2,22, ERP −$ 34,15. Escada desce para $ 181,26 / $ 177,57 / $ 133,86 |
| 26-10-2026 | Q2-26 | $ 320,21 | $ 205,66 | 7,39% | 20,05% | Esperar · peso máx. 2,7% | Negócio a acelerar, mas o preço exige capex a normalizar e crescimento ao ritmo do consenso ao mesmo tempo |
| 29-10-2026 | Q3-26 | $ 292,50 | $ 245,54 | 8,52% | 16,98% | Esperar · peso máx. 3,1% | Cloud a dobrar e Search a abrandar; a queda e a revisão do base (G15) fecharam metade do fosso, não o todo — e a posição está ~3x acima do tecto |

**Verificação retrospectiva** — de seis em seis meses: Abr-2027.

---

## D. Sentimento e posicionamento

**Insider** *(Alpha Vantage, Abr–Set 2026; sem actualização a 29-Out)*. Sem compras em mercado aberto. Vendas em mercado aberto de ~$ 5,0 M (J. K. Walker, J. Hennessy, F. Arnold, M. Saraci, A. O'Toole); ~$ 49,5 M são retenção fiscal no vesting de RSU. Excluídos ~$ 15 M que o feed atribui ao GV, o veículo de capital de risco da própria Alphabet. Planos 10b5-1 não verificados. Sem sinal.

**Short interest** — n/d (sem export Charting).

**Sell-side** *(CapIQ, 22-Out — antes do Q3; revisões por incorporar)* — PT médio $ 429,12, mediana $ 430, intervalo $ 340–500, desvio-padrão $ 31,31, n=54; 43 Buy e 0 Sell. LT growth do EPS no consenso 13,27%. Receita de consenso FY26-30: 500 / 627 / 755 / 880 / 1.001 mM; EPS normalizado 11,9 / 15,4 / 18,2 / 22,7 / 26,7.

| Base | Fair value | Governa a decisão? |
|---|---|---|
| DCF, SBC como custo real | $ 245,54 | **Sim** |
| Meu DCF com a operação do consenso | $ 300,72 | Não — decomposição |
| Consenso sell-side (PT médio, pré-Q3) | $ 429,12 | Não — referência |
| Mínimo do intervalo sell-side (pré-Q3) | $ 340,00 | Não — 16% acima do preço |

O fosso de $ 183,58 face ao PT: $ 16,68 de crescimento, $ 38,50 de margem e ~$ 128 de taxa de desconto e horizonte. O PT é a 12 meses; a operação do consenso descontada a 7,67% chega lá (8,11% descontando o PT um ano). Não há diferença de base contabilística: o consenso usa EBIT GAAP. "Estar abaixo do PT" diz pouco: o PT é anterior ao Q3 e embute um WACC ~170 bp abaixo do meu.

**Estrutura accionista.** Os fundadores controlam a maioria dos votos pelas acções classe B. Na emissão de Jun-26 entrou um veículo da Berkshire Hathaway com $ 10 mM a ~$ 355 — um comprador de valor que pagou 21% acima do preço de hoje. No Q3 o ATM vendeu 36 M acções a ~$ 344 em média ($ 12,4 mM líquidos), com $ 27,6 mM por usar: a empresa é vendedora líquida das próprias acções a preços acima do de hoje, e o programa pesa sobre o preço enquanto durar. As acções básicas passaram de 12.086 M para 12.256 M em doze meses (+1,4%).

---

## C. Changelog

| Data | Quarter | O que mudou | Secções |
|---|---|---|---|
| 30-10-2026 | Q3-26 | Regra de custo de capital da carteira (decisão do Hugo): Rf UST 10Y à data do preço (5,05%; era 5,00% de 27-10), ERP Kroll 5,0% (era 4,20% Damodaran), CRP 0. Ke 9,59% → 10,52%. FV $ 245,54 → $ 209,17; motor A inalterado (8,52%); motor B 16,98% → 19,10%; escada $ 181,26 / $ 177,57 / $ 133,86; peso máx. 2,9%. O config do pipeline estava desactualizado (26-10): reconstruído do Excel de 29-10 com o `00_extrair_config.py` + a escada do config antigo; reproduz o publicado ao cêntimo. Excel regerado e verificado. **O preço continua a ser o after-hours de 28-10 (aproximado) — por refazer com um fecho** | ESTADO, REVERSE DCF (novo), B, C |
| 29-10-2026 | Q3-26 | Q3-26 processado (ER e deck de 28-Out; 10-Q por sair). Modelo refeito com o plugin v1.5: D&A por classe (70% a 6 anos, 30% a 25, meio ano; carteira calibrada na depreciação do Q3), Waymo no SOTP ($ 53.550 M; 85% de participação é hipótese), G20 e saída do `06` em EV/(EBITDA−capex). Âncora factual do capex corrigida (18,5% → 15,4%). Com os drivers de 26-Out o G15 bloqueava (+25,5%) → base reescrito (G16): crescimento Y1 21% → 22,2% (facto LTM) e capex terminal 18% → 16,5% (piso capex = D&A). FV $ 205,66 → $ 245,54 ($ 12,56 do roll-forward e da mecânica, $ 27,32 dos dois drivers). Preço after-hours $ 292,50. INV-3 passa a Vigiar. | ESTADO, tópicos, sumário, §1, §2, §4, §5, §6, §7, A, B, D |
| 26-10-2026 | Q2-26 | Ficha criada (template v3.2, plugin v1.4). Sem comps e sem âncora estrutural, por decisão do Hugo. ERP: método A (implícito Damodaran 4,20%) com 5–6% como sensibilidade (ERP 5,5% → $ 160,94). Hurdle nível 2. Não cotadas a 50%. SpaceX marcada a 23-Out. Pasta `Google/` legada substituída por `GOOGL/` canónica. | Todas |

---

*Template v3.3 — Outubro 2026 (plugin v1.5). Camada 1 de três: ficha estrutural · análise trimestral em chat · DCF em Excel.*
