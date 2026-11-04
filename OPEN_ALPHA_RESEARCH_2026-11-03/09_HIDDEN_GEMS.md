# Hallazgos menos obvios

«Menos obvio» se refiere a la capacidad aprovechable para este mandato, no a un ranking de popularidad. No se usaron estrellas como prueba de calidad. Algunos candidatos sirven para aprender un patrón y no para copiar su código.

| Recurso/capacidad | Qué se encontró | Oportunidad | Condición o límite |
|---|---|---|---|
| [arch: comparación múltiple](03_DEEP_TECHNICAL_REVIEWS/quant_arch.md) | SPA, StepM y Model Confidence Set además de volatilidad | Auditor de experimentos que compara todos los candidatos con la misma pérdida | Registrar también variantes fallidas; bloques y supuestos importan |
| [fredapi: selección de vintage](03_DEEP_TECHNICAL_REVIEWS/quant_fredapi.md) | El método as-of no reduce por sí solo a una observación final por periodo | Una capa pequeña de selección correcta puede aportar más que otro índice macro | Conservar fechas originales y condiciones por serie |
| [DataComPy](03_DEEP_TECHNICAL_REVIEWS/infra_datacompy.md) | Diff tabular con tolerancias explícitas | Detectar que cambió la historia de revenue y no el protocolo | Normalizar definiciones y unidades antes del diff |
| [Patito](03_DEEP_TECHNICAL_REVIEWS/infra_patito.md) | Esquema Pydantic aplicado a Polars | Contrato legible para un analista individual | Una tabla vacía puede superar unicidad; añadir completitud |
| [Quant Feature Store](03_DEEP_TECHNICAL_REVIEWS/infra_qfs.md) | Ruta rápida temporal solo cuando se cumplen invariantes; fallback por ventanas | Modelo conceptual compacto para evitar joins incorrectos | Licencia no verificada: no adoptar/copiar; distinguir hechos de eventos futuros anunciados |
| [River/ADWIN](03_DEEP_TECHNICAL_REVIEWS/ai_river.md) | Detección incremental de cambios en una secuencia | Vigilar errores, retrasos o discrepancias entre fuentes | Cambio detectado no identifica causa ni dirección de precio |
| [fev](03_DEEP_TECHNICAL_REVIEWS/ai_fev.md) | Contrato de tarea y evaluación de forecasts | Probar volumen/fees/volatilidad con cortes comunes y baselines | Datasets y contaminación de pretraining se evalúan aparte |
| [GraphSense lib](03_DEEP_TECHNICAL_REVIEWS/crypto_graphsense.md) | Herramientas de etiquetas y continuidad frente a componente archivado | Mostrar procedencia y confianza de etiquetas en flujos | No garantiza identidad económica; operación pesada para universo global |
| [Ponder](03_DEEP_TECHNICAL_REVIEWS/crypto_ponder.md) | Indexación selectiva dirigida a contratos/eventos | Reconciliar un mecanismo de fees sin indexar toda una red | RPC, reorg, esquema y backfill siguen siendo trabajo real |
| [Cryo](03_DEEP_TECHNICAL_REVIEWS/crypto_cryo.md) | Extracción de datos EVM hacia formatos analíticos | Muestras verificables para estudios de eventos | Datos archive y coste/permiso del RPC no vienen con la licencia del extractor |
| [TradingAgents: controles temporales](03_DEEP_TECHNICAL_REVIEWS/ai_tradingagents.md) | Fecha as-of, retención de datos live-only y tests específicos | Reutilizar el principio de abstención temporal en un investigador sencillo | Un LLM puede recordar el futuro aunque la herramienta esté filtrada |
| [strucchange](https://cran.r-project.org/package=strucchange) / [gingado](https://github.com/bis-med-it/gingado) | Monitorización econométrica y ML macro fuera del circuito cripto habitual | Contrastar segmentación offline con monitorización y bases macro | Revisión de selección; falta ensayo y adaptación de datos cripto |

También es valioso un hallazgo negativo: Tencent finLLM-Eval describe comprobación de números, pero parte de esa capacidad depende de una base interna no publicada. No se debe recomendar como verificador completo por su descripción. Ver [hallazgos IA](workstreams/ai/findings.md).

El criterio común es concreto: reducir un error identificable, un coste de revisión o una dependencia innecesaria. Una técnica pequeña con licencia clara y un experimento falsable puede ser preferible a una plataforma más conocida. Ninguna selección implica ventaja de mercado demostrada.
