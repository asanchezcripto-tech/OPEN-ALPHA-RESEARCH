# Comparaciones tecnológicas por escenario

Son decisiones de ingeniería apoyadas en revisión estática, no benchmarks propios. No comparar un framework general y una función pequeña como si resolvieran el mismo alcance. Las preferencias se limitan al analista individual, horizonte de 3–18 meses y ausencia de ejecución automática.

La regla de adopción es: resolver primero la pregunta, después el contrato de datos y finalmente elegir el componente más pequeño suficiente. Un riesgo bloqueante de licencia o de histórico prevalece sobre el score.

## Almacén local frente a servidor

**Alternativas:** [duckdb](https://github.com/duckdb/duckdb), [sqlite](https://github.com/sqlite/sqlite), [polars](https://github.com/pola-rs/polars), [ClickHouse](https://github.com/ClickHouse/ClickHouse), [questdb](https://github.com/questdb/questdb), [timescaledb](https://github.com/timescale/timescaledb).

**Elección por escenario:** DuckDB/Parquet para análisis local; SQLite para tesis/metadatos; servidor solo ante escala medida.

**Coste y límites:** Ficheros simples requieren disciplina de versiones; servidor añade operación.

**Evidencia:** [duckdb — repositorio](https://github.com/duckdb/duckdb), [duckdb/LICENSE](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/LICENSE), [duckdb/README.md](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/README.md). Fuentes restantes y versiones en el inventario.

## Validación estructural

**Alternativas:** [pandera](https://github.com/unionai-oss/pandera), [patito](https://github.com/JakobGM/patito), [pydantic](https://github.com/pydantic/pydantic), [great_expectations](https://github.com/great-expectations/great_expectations), [soda-core](https://github.com/sodadata/soda-core).

**Elección por escenario:** Pandera para varios backends, Patito para Polars; Pydantic para objetos.

**Coste y límites:** No duplicar validadores; ninguna biblioteca conoce por sí sola la semántica económica. Soda actual tiene restricciones.

**Evidencia:** [pandera — repositorio](https://github.com/unionai-oss/pandera), [pandera/LICENSE.txt](https://raw.githubusercontent.com/unionai-oss/pandera/7ad5f3948d9d1810217d5a25070e6b65e9154059/LICENSE.txt), [pandera/README.md](https://raw.githubusercontent.com/unionai-oss/pandera/7ad5f3948d9d1810217d5a25070e6b65e9154059/README.md). Fuentes restantes y versiones en el inventario.

## Interfaz de investigación

**Alternativas:** [marimo](https://github.com/marimo-team/marimo), [streamlit](https://github.com/streamlit/streamlit), [datasette](https://github.com/simonw/datasette), [panel](https://github.com/holoviz/panel), [perspective](https://github.com/finos/perspective).

**Elección por escenario:** marimo para explorar supuestos; Streamlit/Panel para panel; Datasette para tablas; Perspective para pivotes.

**Coste y límites:** Exportar solo lo necesario; reactividad no garantiza frescura; hosting separado.

**Evidencia:** [marimo — repositorio](https://github.com/marimo-team/marimo), [marimo/LICENSE](https://raw.githubusercontent.com/marimo-team/marimo/54552ec3137df83992ac29aa73d1adf73eb252b1/LICENSE), [marimo/README.md](https://raw.githubusercontent.com/marimo-team/marimo/54552ec3137df83992ac29aa73d1adf73eb252b1/README.md). Fuentes restantes y versiones en el inventario.

## Ingesta y caché

**Alternativas:** [dlt](https://github.com/dlt-hub/dlt), [requests-cache](https://github.com/requests-cache/requests-cache), [hishel](https://github.com/karpetrosyan/hishel), [httpx](https://github.com/encode/httpx), [ingestr](https://github.com/bruin-data/ingestr).

**Elección por escenario:** HTTPX/requests y snapshots para pocos endpoints; dlt al crecer conectores.

**Coste y límites:** Caché no es archivo; cursor puede perder revisiones; ingestr FSL.

**Evidencia:** [dlt — repositorio](https://github.com/dlt-hub/dlt), [dlt/LICENSE.txt](https://raw.githubusercontent.com/dlt-hub/dlt/75ea7f33e24dbf3e46a42e4b9739404ea4d9631e/LICENSE.txt), [dlt/README.md](https://raw.githubusercontent.com/dlt-hub/dlt/75ea7f33e24dbf3e46a42e4b9739404ea4d9631e/README.md). Fuentes restantes y versiones en el inventario.

## Conocimiento temporal

**Alternativas:** [quant-feature-store](https://github.com/sophie-nguyenthuthuy/quant-feature-store), [xtdb](https://github.com/xtdb/xtdb), [sirix](https://github.com/sirixdb/sirix), [alpha-lake](https://github.com/mblaauw/alpha-lake), [point-in-time-datawarehouse](https://github.com/winstongarth/point-in-time-datawarehouse).

**Elección por escenario:** Extraer invariantes y usar tabla append-only antes de operar otro sistema.

**Coste y límites:** QFS y warehouse sin licencia verificada; no copiar. XTDB/otros añaden coste de operación.

**Evidencia:** [quant-feature-store — repositorio](https://github.com/sophie-nguyenthuthuy/quant-feature-store), [quant-feature-store/README.md](https://raw.githubusercontent.com/sophie-nguyenthuthuy/quant-feature-store/61b8fb9b58a6d9ea0d783112e075ede0be79a65b/README.md), [quant-feature-store/qfs/store.py](https://raw.githubusercontent.com/sophie-nguyenthuthuy/quant-feature-store/61b8fb9b58a6d9ea0d783112e075ede0be79a65b/qfs/store.py). Fuentes restantes y versiones en el inventario.

## Reconciliación de fuentes

**Alternativas:** [datacompy](https://github.com/capitalone/datacompy), [data-diff](https://github.com/datafold/data-diff), [sqlglot](https://github.com/tobymao/sqlglot).

**Elección por escenario:** DataComPy o SQL pequeño para cambios entre snapshots.

**Coste y límites:** data-diff archivado; linaje SQL no implica procedencia económica por fila.

**Evidencia:** [datacompy — repositorio](https://github.com/capitalone/datacompy), [datacompy/LICENSE](https://raw.githubusercontent.com/capitalone/datacompy/5a7a1eac257c2efdfa9a6f162647233c4ee7de9f/LICENSE), [datacompy/README.md](https://raw.githubusercontent.com/capitalone/datacompy/5a7a1eac257c2efdfa9a6f162647233c4ee7de9f/README.md). Fuentes restantes y versiones en el inventario.

## Exploración vs secuencia de ejecución

**Alternativas:** [vectorbt](https://github.com/polakowo/vectorbt), [bt](https://github.com/pmorissette/bt), [Backtesting.py](https://github.com/kernc/backtesting.py), [NautilusTrader](https://github.com/nautechsystems/nautilus_trader), [LEAN](https://github.com/QuantConnect/Lean).

**Elección por escenario:** barridos y sensibilidad: vectorbt condicionado por licencia y registro de ensayos; asignación mensual: bt o cálculo de ledger simple; orden de eventos/funding/latencia material: Nautilus o LEAN tras verificar instrumento y datos

**Coste y límites:** Mayor fidelidad de motor no compensa datos malos ni hace útil un problema de HFT fuera de alcance.

**Evidencia:** [NautilusTrader](https://github.com/nautechsystems/nautilus_trader), [bt](https://github.com/pmorissette/bt), [vectorbt](https://github.com/polakowo/vectorbt). Fuentes restantes y versiones en el inventario.

## Optimización y validación de cartera

**Alternativas:** [PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt), [skfolio](https://github.com/skfolio/skfolio), [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib), [cvxportfolio](https://github.com/cvxgrp/cvxportfolio).

**Elección por escenario:** covarianza y escenarios fáciles de inspeccionar: PyPortfolioOpt; validación y selección integradas: skfolio; catálogo amplio de medidas de riesgo: Riskfolio-Lib; costes de negociación en asignación: cvxportfolio

**Coste y límites:** Más objetivos amplían el espacio de búsqueda; exigir equal-weight/BTC-ETH de referencia y sensibilidad.

**Evidencia:** [PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt), [skfolio](https://github.com/skfolio/skfolio), [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib). Fuentes restantes y versiones en el inventario.

## Conector macro ligero vs plataforma

**Alternativas:** [fredapi](https://github.com/mortada/fredapi), [OpenBB / OpenBQ](https://github.com/openbq-org/OpenBB), [sdmx1](https://github.com/khaeru/sdmx), [pandaSDMX](https://github.com/dr-leo/pandaSDMX).

**Elección por escenario:** FRED/ALFRED y trazabilidad estrecha: fredapi con selección correcta de vintages o HTTP oficial; muchos proveedores: OpenBB con snapshot original independiente; agencias SDMX: sdmx1, revisar capacidades por organismo

**Coste y límites:** La normalización puede eliminar campos de conocimiento; retener respuesta bruta y derechos.

**Evidencia:** [sdmx1](https://github.com/khaeru/sdmx), [OpenBB / OpenBQ](https://github.com/openbq-org/OpenBB), [fredapi](https://github.com/mortada/fredapi). Fuentes restantes y versiones en el inventario.

## Cambio estructural vs estado latente

**Alternativas:** [ruptures](https://github.com/deepcharles/ruptures), [strucchange (mirror CRAN)](https://github.com/cran/strucchange), [hmmlearn](https://github.com/hmmlearn/hmmlearn), [statsmodels](https://github.com/statsmodels/statsmodels).

**Elección por escenario:** explorar retrospectivamente: ruptures; monitorizar residuo con umbral: strucchange/CUSUM; estados probabilísticos con supuestos: MarkovRegression/HMM

**Coste y límites:** Offline, filtrado y suavizado responden preguntas distintas; replay obligatorio para alertas.

**Evidencia:** [statsmodels](https://github.com/statsmodels/statsmodels), [hmmlearn](https://github.com/hmmlearn/hmmlearn), [ruptures](https://github.com/deepcharles/ruptures). Fuentes restantes y versiones en el inventario.

## Pruebas estadísticas de selección

**Alternativas:** [arch](https://github.com/bashtage/arch), [skepsis](https://github.com/abhinay/skepsis), [The Deflated Sharpe Ratio](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf), [The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf).

**Elección por escenario:** comparación múltiple de pérdidas: arch SPA/StepM/MCS; diagnóstico DSR/PBO: papers y candidato skepsis para revisión adicional

**Coste y límites:** Ningún test estadístico certifica ausencia de leakage; skepsis alpha no auditado integralmente.

**Evidencia:** [skepsis](https://github.com/abhinay/skepsis), [The Deflated Sharpe Ratio](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf), [arch](https://github.com/bashtage/arch). Fuentes restantes y versiones en el inventario.

## Asociación de evento vs identificación causal

**Alternativas:** [eventstudy](https://github.com/LemaireJean-Baptiste/eventstudy), [PyFixest](https://github.com/py-econometrics/pyfixest), [DoWhy](https://github.com/py-why/dowhy), [Inferring causal impact using Bayesian structural time-series models](https://arxiv.org/abs/1506.00356).

**Elección por escenario:** reacción descriptiva: event study con benchmark; cambio comparativo con controles plausibles: DiD/contrafactual; explicitar supuestos y refutaciones: DoWhy

**Coste y límites:** Elegir diseño identificable antes que biblioteca; contagio entre protocolos compromete controles.

**Evidencia:** [DoWhy](https://github.com/py-why/dowhy), [Inferring causal impact using Bayesian structural time-series models](https://arxiv.org/abs/1506.00356), [PyFixest](https://github.com/py-econometrics/pyfixest). Fuentes restantes y versiones en el inventario.

## exchange-clients

**Alternativas:** [CCXT](https://github.com/ccxt/ccxt), [Cryptofeed](https://github.com/bmoscon/cryptofeed), [Hummingbot](https://github.com/hummingbot/hummingbot).

**Elección por escenario:** CCXT para snapshots REST de lectura; Cryptofeed si hace falta streaming y se acepta AGPL+atribución; Hummingbot sólo referencia

**Coste y límites:** Horizonte inversor y coste operativo no justifican motor de ejecución

**No medido:** Latencia, cobertura real de endpoints y mantenimiento futuro

**Evidencia:** [ccxt/ccxt / README.md](https://raw.githubusercontent.com/ccxt/ccxt/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/README.md), [ccxt/ccxt / LICENSE](https://raw.githubusercontent.com/ccxt/ccxt/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/LICENSE), [ccxt/ccxt / LICENSE.md](https://raw.githubusercontent.com/ccxt/ccxt/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/LICENSE.md). Fuentes restantes y versiones en el inventario.

## indexers

**Alternativas:** [Cryo](https://github.com/paradigmxyz/cryo), [Ponder](https://github.com/ponder-sh/ponder), [Graph Node](https://github.com/graphprotocol/graph-node), [SQD Squid SDK](https://github.com/subsquid/squid-sdk).

**Elección por escenario:** Cryo para extracción batch acotada; Ponder para índice continuo con reorgs; Graph Node/Subsquid cuando exista necesidad de servicio/archivo más amplio

**Coste y límites:** Elegir alcance de datos antes de infraestructura

**No medido:** Rendimiento, costes RPC y disponibilidad de historial

**Evidencia:** [paradigmxyz/cryo / README.md](https://raw.githubusercontent.com/paradigmxyz/cryo/80eedf5355ca7b141d48123126515e6c9dd7d290/README.md), [paradigmxyz/cryo / LICENSE](https://raw.githubusercontent.com/paradigmxyz/cryo/80eedf5355ca7b141d48123126515e6c9dd7d290/LICENSE), [paradigmxyz/cryo / LICENSE.md](https://raw.githubusercontent.com/paradigmxyz/cryo/80eedf5355ca7b141d48123126515e6c9dd7d290/LICENSE.md). Fuentes restantes y versiones en el inventario.

## prediction-sdk

**Alternativas:** [Polymarket unified Python SDK](https://github.com/Polymarket/py-sdk), [Polymarket legacy Python CLOB](https://github.com/Polymarket/py-clob-client), [Polymarket Python CLOB v2](https://github.com/Polymarket/py-clob-client-v2).

**Elección por escenario:** SDK unificado actual; repos legados sólo migración y referencia

**Coste y límites:** Fuentes oficiales documentan ambas deprecaciones

**No medido:** Compatibilidad local y estabilidad futura de API 0.x

**Evidencia:** [Polymarket/py-sdk / README.md](https://raw.githubusercontent.com/Polymarket/py-sdk/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/README.md), [Polymarket/py-sdk / LICENSE](https://raw.githubusercontent.com/Polymarket/py-sdk/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/LICENSE), [Polymarket/py-sdk / pyproject.toml](https://raw.githubusercontent.com/Polymarket/py-sdk/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/pyproject.toml). Fuentes restantes y versiones en el inventario.

## fundamentals

**Alternativas:** [DefiLlama dimension adapters](https://github.com/DefiLlama/dimension-adapters), [Dune Spellbook](https://github.com/duneanalytics/spellbook).

**Elección por escenario:** Fórmulas y eventos versionados para núcleo; proveedores como contraste de definiciones

**Coste y límites:** Adaptador público no garantiza upstream abierto; dashboard cerrado no prueba replicabilidad

**No medido:** Exactitud de importes e historial de revisiones de cada proveedor

**Evidencia:** [DefiLlama/dimension-adapters / README.md](https://raw.githubusercontent.com/DefiLlama/dimension-adapters/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/README.md), [DefiLlama/dimension-adapters / LICENSE](https://raw.githubusercontent.com/DefiLlama/dimension-adapters/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/LICENSE), [DefiLlama/dimension-adapters / LICENSE.md](https://raw.githubusercontent.com/DefiLlama/dimension-adapters/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/LICENSE.md). Fuentes restantes y versiones en el inventario.

## Forecasting de magnitudes económicas

**Alternativas:** [StatsForecast](https://github.com/Nixtla/statsforecast), [MLForecast](https://github.com/Nixtla/mlforecast), [Chronos forecasting library](https://github.com/amazon-science/chronos-forecasting), [TimesFM library](https://github.com/google-research/timesfm), [Uni2TS / Moirai](https://github.com/SalesforceAIResearch/uni2ts).

**Elección por escenario:** StatsForecast/MLForecast baseline; Chronos2 comparador

**Coste y límites:** No benchmark crypto reproducido; preferencia de ingeniería provisional.

**Evidencia:** [Chronos forecasting library repositorio](https://github.com/amazon-science/chronos-forecasting), [Chronos forecasting library readme](https://raw.githubusercontent.com/amazon-science/chronos-forecasting/1224fafa91e1ecd6674f5204066b159e40b5e4a1/README.md), [Chronos forecasting library license](https://raw.githubusercontent.com/amazon-science/chronos-forecasting/1224fafa91e1ecd6674f5204066b159e40b5e4a1/LICENSE). Fuentes restantes y versiones en el inventario.

## Evaluación de foundation models

**Alternativas:** [Forecast Evaluation (fev)](https://github.com/autogluon/fev), [GIFT-Eval](https://github.com/SalesforceAIResearch/gift-eval).

**Elección por escenario:** fev para tareas propias; GIFT como referencia

**Coste y límites:** Ambos relacionados con proveedores de modelos; FinVerse solo abstract consultado.

**Evidencia:** [GIFT-Eval repositorio](https://github.com/SalesforceAIResearch/gift-eval), [GIFT-Eval readme](https://raw.githubusercontent.com/SalesforceAIResearch/gift-eval/82f89c3a2de1e7cd98e35dbcb6917cb4ebb6fd18/README.md), [GIFT-Eval license](https://raw.githubusercontent.com/SalesforceAIResearch/gift-eval/82f89c3a2de1e7cd98e35dbcb6917cb4ebb6fd18/LICENSE.txt). Fuentes restantes y versiones en el inventario.

## Extracción documental

**Alternativas:** [Docling](https://github.com/docling-project/docling), [Trafilatura](https://github.com/adbar/trafilatura), [Unstructured library](https://github.com/Unstructured-IO/unstructured), [Marker](https://github.com/datalab-to/marker).

**Elección por escenario:** Trafilatura HTML; Docling tablas/PDF

**Coste y límites:** No corpus local convertido; exactitud aún pendiente.

**Evidencia:** [Docling repositorio](https://github.com/docling-project/docling), [Docling readme](https://raw.githubusercontent.com/docling-project/docling/0634e2f74561e5950d69b2cace67ef95400506ad/README.md), [Docling license](https://raw.githubusercontent.com/docling-project/docling/0634e2f74561e5950d69b2cace67ef95400506ad/LICENSE). Fuentes restantes y versiones en el inventario.

## Investigación asistida por agentes

**Alternativas:** [TradingAgents](https://github.com/TauricResearch/TradingAgents), [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT), [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot), [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund).

**Elección por escenario:** Extraer controles temporales y comparar contra flujo determinista

**Coste y límites:** No coste ni calidad de salida medidos; no rentabilidad demostrada.

**Evidencia:** [FinGPT repositorio](https://github.com/AI4Finance-Foundation/FinGPT), [FinGPT readme](https://raw.githubusercontent.com/AI4Finance-Foundation/FinGPT/ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8/README.md), [FinGPT license](https://raw.githubusercontent.com/AI4Finance-Foundation/FinGPT/ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8/LICENSE). Fuentes restantes y versiones en el inventario.

## Drift/anomalías ligeras

**Alternativas:** [River](https://github.com/online-ml/river), [PyOD](https://github.com/yzhao062/pyod), [ADTK](https://github.com/arundo/adtk), [Alibi Detect](https://github.com/SeldonIO/alibi-detect), [Merlion](https://github.com/salesforce/Merlion).

**Elección por escenario:** River para online; PyOD para comparación multivariable

**Coste y límites:** Sensibilidad a autocorrelación y falsos positivos debe medirse.

**Evidencia:** [River repositorio](https://github.com/online-ml/river), [River readme](https://raw.githubusercontent.com/online-ml/river/4768de0579f977315e65cd23ee658534c1d62c26/README.md), [River license](https://raw.githubusercontent.com/online-ml/river/4768de0579f977315e65cd23ee658534c1d62c26/LICENSE). Fuentes restantes y versiones en el inventario.

## Benchmarks de QA financiero

**Alternativas:** [FinQA code / benchmark repository](https://github.com/czyssrs/FinQA), [TAT-QA](https://github.com/NExTplusplus/TAT-QA), [FinanceBench repository](https://github.com/patronus-ai/financebench), [ConvFinQA](https://github.com/czyssrs/ConvFinQA), [Tencent finLLM-Eval](https://github.com/Tencent/finLLM-Eval).

**Elección por escenario:** Gold set propio de protocolos apoyado en tareas FinQA/TAT-QA

**Coste y límites:** Licencias y contaminación de benchmarks limitan reproducción.

**Evidencia:** [FinQA code / benchmark repository repositorio](https://github.com/czyssrs/FinQA), [FinQA code / benchmark repository readme](https://raw.githubusercontent.com/czyssrs/FinQA/0f16e2867befa6840783e58be38c9efb9229d742/README.md), [FinQA code / benchmark repository license](https://raw.githubusercontent.com/czyssrs/FinQA/0f16e2867befa6840783e58be38c9efb9229d742/LICENSE). Fuentes restantes y versiones en el inventario.

## Qué usar directamente y qué requiere adaptación

Los paneles públicos de DefiLlama y las páginas oficiales de protocolos permiten comenzar una ficha manual, conservando sus límites. Dune/Token Terminal sirven como referencia funcional y contraste de definiciones; son servicios con condiciones propias. marimo, Datasette, VisiData u OpenBB/OpenBQ son candidatos de uso directo tras instalación/permiso y verificación de fuentes, no instalaciones realizadas aquí.

Bibliotecas como DuckDB, arch o Pandera exigen pequeñas integraciones; su licencia no entrega datos. SDKs actuales permiten lectura, pero también contienen superficies de ejecución que deben quedar fuera del producto propuesto. Los prototipos sin licencia y los agentes financieros completos son referencias o experimentos, no recomendaciones de despliegue inmediato.

No se recomienda construir desde cero un motor SQL, parser documental, cliente de exchange completo, motor genérico de backtesting ni un foundation model. Sí diseñar explícitamente el pequeño contrato temporal, las definiciones financieras, los criterios de abstención y los experimentos de utilidad que ninguna biblioteca decide por el usuario.
