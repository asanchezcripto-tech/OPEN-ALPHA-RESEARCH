# OPEN ALPHA — Investigación independiente

**Conclusión:** la mejora más defendible para un inversor particular es comprobar fundamentos, cambios y fechas de conocimiento con herramientas pequeñas y evidencia trazable. El valor de los modelos y agentes debe demostrarse frente a una base simple.

Entrega en español: **288 recursos**, **39 revisiones técnicas estáticas**, **22 componentes seleccionados**, **16 conceptos** y **5 diseños**. 285 recursos tienen consulta original suficiente para su nivel; no son herramientas instaladas ni estrategias rentables demostradas. [Resumen ejecutivo](00_EXECUTIVE_BRIEF.md).

Referencia: 3-nov-2026. Observación de fuentes: 4-nov-2026. No se garantiza reconstrucción exacta de todos los repositorios al cierre del 3. No se ejecutó software de terceros, no se modificó CIE y no se creó/modificó repositorio remoto.

## Lectura recomendada

1. [Informe ejecutivo](00_EXECUTIVE_BRIEF.md), 5–10 minutos.
2. [Dictamen estratégico](14_FINAL_STRATEGIC_VERDICT.md) y [cartera de herramientas](11_PRODUCT_OPPORTUNITIES.md).
3. [Cinco diseños preliminares](12_TOP_FIVE_BLUEPRINTS/README.md).
4. [Catálogo](02_PROJECT_CATALOG.md), [comparaciones](08_TECHNOLOGY_COMPARISONS.md) y revisión de cada candidato.

## Contenido

| Archivo | Para qué sirve |
|---|---|
|[00 — Executive brief](00_EXECUTIVE_BRIEF.md)|Conclusiones y selección inicial|
|[01 — Search coverage](01_SEARCH_COVERAGE.md)|Método, consultas, cobertura real y lagunas|
|[02 — Project catalog](02_PROJECT_CATALOG.md)|Recursos por categoría y acceso a fichas|
|[03 — Deep technical reviews](03_DEEP_TECHNICAL_REVIEWS/README.md)|39 revisiones con rutas/commits y límites|
|[04 — Algorithms and methods](04_ALGORITHMS_AND_METHODS.md)|32 técnicas y criterios de validación|
|[05 — Models and datasets](05_MODELS_AND_DATASETS.md)|Capacidades, benchmarks, licencias y recursos|
|[06 — Data and infrastructure](06_DATA_AND_INFRASTRUCTURE.md)|Fuentes y contrato temporal ligero|
|[07 — License and risk matrix](07_LICENSE_AND_RISK_MATRIX.md)|Permisos por capa y riesgos bloqueantes|
|[08 — Technology comparisons](08_TECHNOLOGY_COMPARISONS.md)|Alternativas por escenario|
|[09 — Hidden gems](09_HIDDEN_GEMS.md)|Capacidades menos obvias|
|[10 — Novel combinations](10_NOVEL_COMBINATIONS.md)|Hipótesis comprobables y grafo de relaciones|
|[11 — Product opportunities](11_PRODUCT_OPPORTUNITIES.md)|16 herramientas personales autónomas|
|[12 — Top five blueprints](12_TOP_FIVE_BLUEPRINTS/README.md)|Diseños, experimentos y aceptación|
|[13 — Research backlog](13_RESEARCH_BACKLOG.md)|Continuidad priorizada|
|[14 — Final strategic verdict](14_FINAL_STRATEGIC_VERDICT.md)|Decisión estratégica del investigador|
|[Revisión de calidad](QUALITY_REVIEW.md)|Comprobación cruzada y límites de QA|

Categorías cubiertas: macro; mercado cripto; derivados; on-chain; fundamentales; oportunidades; validación; IA; agentes; noticias/eventos; cartera/riesgo; visualización; infraestructura; fuentes alternativas. La cobertura es desigual: ver la tabla por categoría antes de interpretar amplitud como profundidad uniforme.

## Componentes seleccionados

La lista incluye bibliotecas, referencias y técnicas; no es una instalación conjunta. Los bloqueantes prevalecen sobre puntos.

| Componente | Puntos editoriales | Qué aprovechar |
|---|---:|---|
| [duckdb](03_DEEP_TECHNICAL_REVIEWS/infra_duckdb.md) | 90 | Consultas locales y joins explícitos; fijar compatibilidad. |
| [pandera](03_DEEP_TECHNICAL_REVIEWS/infra_pandera.md) | 84 | Contratos de tablas y cuarentena, sin ocultar rechazos. |
| [datacompy](03_DEEP_TECHNICAL_REVIEWS/infra_datacompy.md) | 84 | Revisiones de datos y reconciliación. |
| [marimo](03_DEEP_TECHNICAL_REVIEWS/infra_marimo.md) | 87 | Exploración reproducible y lectura de escenarios. |
| [CCXT](03_DEEP_TECHNICAL_REVIEWS/crypto_ccxt.md) | 83 | Lectura de mercados manteniendo contrato/unidad nativos. |
| [Hyperliquid Python SDK](03_DEEP_TECHNICAL_REVIEWS/crypto_hyperliquid_sdk.md) | 87 | Lectura pública acotada de Hyperliquid. |
| [Polymarket unified Python SDK](03_DEEP_TECHNICAL_REVIEWS/crypto_polymarket_sdk.md) | 80 | SDK vigente para datos y reglas de mercados. |
| [DefiLlama dimension adapters](03_DEEP_TECHNICAL_REVIEWS/crypto_defillama_dimensions.md) | 70 | Referencia de fórmulas; no copiar sin licencia verificada. |
| [Uniswap protocol fees](03_DEEP_TECHNICAL_REVIEWS/crypto_uniswap_protocol_fees.md) | 75 | Estudiar mecanismos y eventos; no desplegar contratos. |
| [Cryo](03_DEEP_TECHNICAL_REVIEWS/crypto_cryo.md) | 77 | Extracción batch EVM selectiva; RPC y permisos separados. |
| [fredapi](03_DEEP_TECHNICAL_REVIEWS/quant_fredapi.md) | 85 | Vintages con selección correcta en el consumidor. |
| [statsmodels](https://github.com/statsmodels/statsmodels) | 63 | Bases econométricas antes de modelos complejos. |
| [arch](03_DEEP_TECHNICAL_REVIEWS/quant_arch.md) | 89 | Bootstrap y comparación múltiple de experimentos. |
| [ruptures](03_DEEP_TECHNICAL_REVIEWS/quant_ruptures.md) | 88 | Segmentación y replay de detección, sin anticipación ficticia. |
| [skfolio](03_DEEP_TECHNICAL_REVIEWS/quant_skfolio.md) | 85 | Walk-forward y cartera con purga configurada. |
| [PyPortfolioOpt](03_DEEP_TECHNICAL_REVIEWS/quant_pyportfolioopt.md) | 83 | Riesgo/covarianza y escenarios de concentración. |
| [StatsForecast](https://github.com/Nixtla/statsforecast) | 81 | Baselines estadísticos de magnitudes económicas. |
| [MLForecast](03_DEEP_TECHNICAL_REVIEWS/ai_mlforecast.md) | 84 | Forecast con features y boosting controlables. |
| [Forecast Evaluation (fev)](03_DEEP_TECHNICAL_REVIEWS/ai_fev.md) | 86 | Contrato común de tareas y evaluación. |
| [River](03_DEEP_TECHNICAL_REVIEWS/ai_river.md) | 84 | Cambios en errores/fuentes, no señal automática de compra. |
| [Docling](03_DEEP_TECHNICAL_REVIEWS/ai_docling.md) | 83 | Extracción con estructura y evidencia localizable. |
| [Chronos forecasting library](03_DEEP_TECHNICAL_REVIEWS/ai_chronos.md) | 78 | Comparador probabilístico opcional contra base simple. |

## Cómo consultar el inventario

`inventories/` contiene CSV y JSON para proyectos, bibliotecas, modelos, datasets, papers, algoritmos, licencias, proveedores, oportunidades, comparaciones, fuentes y evidencias; además relaciones, búsquedas, deduplicación y control de etapas. JSON conserva listas/objetos; CSV los serializa como JSON en celdas. Codificación UTF-8 y CSV con escapado estándar.

Empezar por `projects.json`: localizar ID, nivel, bloqueantes y `deep_review_path`. Seguir `evidence_ids` a `evidence.json`, y `source_id` a `sources.json`. Leer URL/commit, tipo de evidencia y limitación, no solo el score. Las fichas de área en `workstreams/` conservan decisiones y revisión crítica; sus inventarios originales explican deduplicaciones del coordinador.

Los puntos suman 25 utilidad+ 15 evidencia+ 15 datos+ 12 facilidad+ 10 licencia+ 8 mantenimiento+ 8 uso+ 7 diferenciación. Son juicio editorial con confianza aparte. No expresan alpha ni calidad medida en producción. V1/V2 verifican alcance limitado; V3 es lectura técnica, nunca ejecución. Diferencias pequeñas no justifican preferencias firmes.

## Limitaciones y continuación

Sesgo GitHub/Python/Hugging Face/inglés y macro occidental. No hubo auditoría completa de issues/releases, seguridad transitiva, derechos por dataset, despliegues ni precisión de modelos. Algunas fuentes son inaccesibles o tienen cobertura parcial; varios papers se leyeron solo por abstract. No se cotizaron servicios ni se conocen todos los recursos del ordenador del usuario.

Los scripts `research_tools/` y de cada área son auxiliares propios de investigación documental; no son los productos financieros propuestos. Un nuevo agente debe leer el protocolo, cobertura y backlog, escoger un ID y añadir una observación sin sobrescribir la anterior. No repetir el barrido por defecto. El archivo `FILE_MANIFEST.json` registra hashes de la entrega; el ZIP excluye cachés y código externo.

Mandato recibido identificado por SHA-256 `B73F8C03294031AAD581EA0D4BBEFB29A4968AEE0A9253962B7C0BBADC8BEE50`; los dos adjuntos recibidos eran idénticos. No se incluyó una ruta privada del equipo en las fuentes de investigación.
