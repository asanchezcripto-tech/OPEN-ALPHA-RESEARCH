# OPEN ALPHA — Informe ejecutivo

**La oportunidad principal es construir capacidad de comprobación:** saber qué cambió, cuándo pudo conocerse, quién recibe el valor económico y qué datos podrían invalidar una tesis. Hay suficiente software reutilizable para hacerlo en herramientas pequeñas. Esta investigación no encontró una base para prometer rentabilidad extraordinaria ni para priorizar un gran sistema de agentes de trading.

El catálogo reúne **288 recursos diferenciados**, de los cuales **285 tienen comprobación directa al nivel declarado**: 39 revisiones de rutas técnicas, 208 revisiones de documentación más licencia/archivo técnico y 38 verificaciones de alcance más limitado. Tres pistas siguen sin comprobar suficientemente. Se documentan 32 métodos, 22 comparaciones, 16 conceptos de herramientas y 5 diseños preliminares. Los recursos incluyen bibliotecas, pesos, datasets, servicios y papers; no son 288 aplicaciones listas para usar. [Cobertura y límites](01_SEARCH_COVERAGE.md).

Fecha estratégica de referencia: 3-nov-2026. Fuentes consultadas el 4-nov-2026; los commits fijados no reconstruyen en todos los casos el cierre del día 3. No se instalaron ni ejecutaron proyectos, modelos o tests de terceros. No se construyó ninguna herramienta financiera, no se operó ni se modificó CIE.

## Qué merece atención

**Fundamentales con un puente económico verificable.** Comparar fees, ingresos del protocolo, incentivos, recompras, quema y oferta exige definiciones por mecanismo y fecha. HYPE, UNI, RAY y PUMP no se pueden evaluar aplicando el mismo porcentaje de captura. La documentación de Raydium, por ejemplo, distingue recompras mantenidas por el protocolo de una quema; código desplegable y movimientos efectivamente observados son capas distintas. [Análisis crypto](workstreams/crypto/findings.md).

**Temporalidad y revisiones como parte del análisis.** El código inspeccionado de fredapi puede devolver varias revisiones anteriores al corte; el consumidor debe escoger la última por periodo. Una ruta de OpenBB elimina campos de vintage. El helper Hyperliquid de DefiLlama contempla un fallback a contexto actual. Estos comportamientos pueden producir históricos engañosos si la herramienta no conserva la procedencia. [fredapi](03_DEEP_TECHNICAL_REVIEWS/quant_fredapi.md), [DefiLlama](03_DEEP_TECHNICAL_REVIEWS/crypto_defillama_dimensions.md).

**IA para tareas comprobables.** Extracción documental con citas, baselines de forecasting de actividad y detección de cambios tienen un camino de evaluación más claro que pedir a un agente un precio objetivo. MLForecast/StatsForecast, fev, River, Docling y un experimento limitado con Chronos2 son candidatos útiles. La mejora debe medirse en exactitud, calibración, tiempo o errores evitados. [Modelos y datasets](05_MODELS_AND_DATASETS.md).

**Herramientas pequeñas de control.** DuckDB/Parquet, Pandera, DataComPy y marimo permiten consultar, validar, comparar revisiones y explorar escenarios localmente. El beneficio está en reducir errores específicos, no en añadir componentes. Un portátil puede bastar para pilotos diarios acotados; no se midió rendimiento ni se recomienda comprar hardware. [Infraestructura](06_DATA_AND_INFRASTRUCTURE.md).

## Cambios que una lista antigua pasaría por alto

- Polymarket sustituyó tanto `py-clob-client` como el cliente V2 de transición; el candidato actual es el SDK unificado `py-sdk` / `polymarket-client`. [Revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_polymarket_sdk.md).
- TimesFM3 y los pesos FinBERT tienen condiciones diferentes del código de sus bibliotecas. Vectorbt incorpora Commons Clause. Un permiso de un SDK no se hereda a contratos o datasets de la misma marca. [Matriz](07_LICENSE_AND_RISK_MATRIX.md).
- Una clase de validación «purged» puede traer purga/embargo en cero. PELT identifica cambios retrospectivos si recibe toda la serie. Nombres y gráficos no garantizan validación temporal. [skfolio](03_DEEP_TECHNICAL_REVIEWS/quant_skfolio.md), [ruptures](03_DEEP_TECHNICAL_REVIEWS/quant_ruptures.md).
- La propia página de Pump advierte problemas en las cifras del dashboard tras introducir custom pairs. Una fuente oficial tampoco se acepta sin reconciliar alcance y método. [Fuente primaria](https://pump.fun/pump-token).

## Cinco oportunidades de desarrollo

| Prioridad | Herramienta | Primera capacidad útil |
|---|---|---|
|1|[Protocol Value & Dilution Analyzer](12_TOP_FIVE_BLUEPRINTS/01_protocol_value.md)|Una ficha de protocolo que reconcilie actividad, destinatarios y oferta|
|2|[Thesis Tracker](12_TOP_FIVE_BLUEPRINTS/02_thesis_tracker.md)|Tres tesis con evidencia, contradicciones y criterios de invalidación|
|3|[Market Regime & Liquidity Navigator](12_TOP_FIVE_BLUEPRINTS/03_regime_navigator.md)|BTC/ETH y pocos indicadores con fecha conocida y antigüedad visible|
|4|[Derivatives Stress Monitor](12_TOP_FIVE_BLUEPRINTS/04_derivatives_stress.md)|Funding/OI de dos venues con unidades y cobertura verificadas|
|5|[Event Impact Research Lab](12_TOP_FIVE_BLUEPRINTS/05_event_lab.md)|Una familia de eventos con cronología, controles y resultados negativos conservados|

El monitor de revisiones de datos es una capacidad transversal de prioridad alta: se incorpora desde el primer piloto, aunque no se convierte en una sexta plataforma. La cartera de riesgo puede empezar con bibliotecas existentes y posiciones introducidas localmente. [Los 16 conceptos y sus métricas de utilidad](11_PRODUCT_OPPORTUNITIES.md).

## Qué puede aprovecharse ya y qué aplazar

Ya se puede elaborar una ficha manual con documentos oficiales, paneles públicos y el catálogo de esta investigación. DefiLlama, Dune o Token Terminal ayudan a consultar/contrastar, con sus condiciones y limitaciones; sus servicios no se clasifican como código abierto por tener documentación o clientes públicos. Las herramientas locales candidatas siguen pendientes de instalación y piloto autorizado.

Aplazar un superagente de inversión, un índice global de todas las cadenas, entrenamiento de modelos enormes y motores de ejecución. No construir de cero SQL, parsers documentales, SDKs completos ni backtesting general. Sí diseñar el contrato de datos, las definiciones financieras y los criterios de abstención propios.

El siguiente paso más eficiente sería una ficha manual de un protocolo y una tesis falsable, seguida de snapshots y detección de revisiones. Solo automatizar lo que demuestre ahorro de tiempo o reducción de errores. La investigación deja preparados esos experimentos; **no los presenta como resultados obtenidos**. [Dictamen estratégico](14_FINAL_STRATEGIC_VERDICT.md).
