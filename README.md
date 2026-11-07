# carteira-dados

Dados para o Terminal do artefacto **Carteira Hugo e Je**. Corre no GitHub Actions; nada depende do PC.

| Script | Fonte | Saída (`out/` no ramo `data`) |
|---|---|---|
| `pipeline/precos.py` | Yahoo Finance | `precos.json`: empresas, índices, setores EUA e Europa; ATH, RSI 14, 1d/1s/1m/3m/YTD/12m |
| `pipeline/sec.py` | SEC EDGAR | `sec.json`: 10 anos de financials (anual e trimestral) e links dos filings |
| `pipeline/calendario.py` | Nasdaq | `calendario.json`: datas de resultados e EPS vs consenso |
| `pipeline/econ.py` | BLS, BEA, ECB/Eurostat, Michigan | `mk_econ.json` (script do kit Stocks dashboard) |
| `pipeline/fichas.py` | `fichas/` (cópia da pasta Análise Ações) | `fichas.json`: números da ficha (parser do `tracker.py`), versões e comparador |

- Empresas acompanhadas: `cfg/universo.json`. Índices e setores: `cfg/mercado.json`.
- Corre nos dias úteis às 21:20 UTC, ao sábado de manhã, a cada push em `fichas/`, `cfg/` ou `pipeline/`, e a pedido.
- `fichas/` é só cópia: os originais vivem na pasta Análise Ações e nunca se editam aqui.
- Estado de cada fonte: `out/estado.json`.
