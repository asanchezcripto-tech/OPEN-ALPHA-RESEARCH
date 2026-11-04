# Datos e infraestructura proporcional

El cuello de botella principal es la definición y disponibilidad histórica del dato. Una API pública, un SDK abierto y un dataset redistribuible son tres cosas distintas. La propuesta mínima es un recolector de lectura, snapshots, validación, consultas locales y un informe. No se ha instalado ningún componente ni se ha construido una herramienta financiera.

## Contrato ligero de observación

| Campo | Significado y regla |
|---|---|
| observation_id / source_record_id | Identidad propia y nativa; no deduplicar únicamente por valor |
| asset_id / protocol_id / instrument_id | Identidad estable: cadena, contrato/venue, base/quote, vencimiento y versión cuando corresponda |
| metric / unit / currency / scale | Qué se mide; USD, token, contrato, porcentaje y fracción no son intercambiables |
| period_start / period_end / event_at | Periodo económico y momento del evento; indicar precisión temporal |
| available_at | Primer momento verificable en que esa versión fue pública/conocida; puede ser desconocido |
| acquired_at | Momento de adquisición por la herramienta; no sustituye automáticamente a available_at |
| source_updated_at / vintage | Revisión declarada por la fuente; conservar versiones previas |
| scheduled_at / announced_at | Para catalizadores futuros: un evento aún no ocurrido puede ser conocido hoy |
| source_url / source_hash / method_version | Procedencia y definición exactas; fuente y adaptador pueden cambiar independientemente |
| quality / uncertainty / coverage | Observado, reconstruido, inferido, faltante, caducado, parcial; incertidumbre no siempre numérica |
| restrictions / retention / attribution | Condiciones verificadas o pendientes; no usar una licencia de código para autorizar datos |
| value / abstention_reason | Resultado o abstención; null no se transforma en cero |

`available_at` puede preceder a `acquired_at` si se acredita publicación anterior. Si no se sabe cuándo fue público, guardar la primera adquisición como cota conservadora y etiquetarla. El sistema necesita distinguir lo que era público de lo que el propio investigador había adquirido. Las consultas de backtest deben declarar qué interpretación usan.

Para hechos revisados, seleccionar versiones conocidas en el corte, resolver revisiones por periodo y después unir series. Un ASOF sobre la fecha económica no basta. Las pruebas propuestas incluyen revisión tardía, backfill, simultaneidad, calendario futuro, zona horaria, delisting y ausencia de observación. [DuckDB: revisión](03_DEEP_TECHNICAL_REVIEWS/infra_duckdb.md), [fredapi: revisión](03_DEEP_TECHNICAL_REVIEWS/quant_fredapi.md).

## Almacenamiento y operación

Parquet conserva tablas compactas; DuckDB permite SQL local sobre ellas. SQLite es suficiente para tesis, fuentes y revisiones cortas. Empezar con un único motor principal. Mantener datos adquiridos sin sobrescritura y una vista derivada que se pueda regenerar; la caché HTTP solo reduce llamadas y no constituye archivo histórico.

Los lotes deben escribir primero el snapshot, luego validar y finalmente actualizar la vista aceptada. Si falla un paso, la versión anterior sigue visible con indicador de frescura. Un registro de ejecución guarda fuente, rango, resultado, hash y error. Reintentos con espera y límites de proveedor; nunca eludir cuotas. No hace falta Kafka, Kubernetes, un catálogo empresarial ni un feature store distribuido.

La revisión de [dlt](03_DEEP_TECHNICAL_REVIEWS/infra_dlt.md) muestra por qué cursor/merge no preservan automáticamente revisiones antiguas. La de [requests-cache](03_DEEP_TECHNICAL_REVIEWS/infra_requests-cache.md) muestra que un 200 de caché puede estar caducado. [DataComPy](03_DEEP_TECHNICAL_REVIEWS/infra_datacompy.md) ayuda a detectar cambios; [Pandera](03_DEEP_TECHNICAL_REVIEWS/infra_pandera.md) valida estructura y reglas explícitas. Ninguna prueba que la explicación económica sea correcta.

## Fuentes por necesidad

| Necesidad | Candidatos/fuentes | Qué comprobar antes del piloto | Alternativa limitada |
|---|---|---|---|
| Spot y derivados | CCXT y APIs oficiales | Contrato, unidad, intervalos funding, paginación, historia, límites y condiciones | Captura prospectiva de 2 venues |
| Hyperliquid | SDK/info API y documentos oficiales | Histórico frente a contexto actual, límites y estado de mecanismos | Consulta manual y snapshots diarios |
| Protocol fees/revenue | DefiLlama dimensions y eventos nativos | Definición, beneficiario, subsidios, residual y versión de adaptador | Conciliar un protocolo a mano |
| Supply/unlocks | Contratos, gobernanza y documentación | Supply bridged/canónica, fechas anunciadas/ejecutadas, permisos | Escenarios de tres tokens |
| DEX y flujos | Cryo, Ponder, Subsquid/HyperSync, GraphSense | RPC/archive, reorg, decodificación, etiquetas y cobertura | Una cadena y contratos limitados |
| Mercados predictivos | Polymarket SDK actual y reglas oficiales | Cohortes cerradas/anuladas, condiciones de resolución, historial | Categoría prospectiva pequeña |
| Macro | ALFRED/FRED, BIS, ECB/SDMX | Vintage, hora conocida, divisa/unidad, licencia por serie | Descargas manuales permitidas |
| Noticias/documentos | Fuentes oficiales, Docling/Trafilatura | Copyright, fecha inicial, edición posterior, estructura de tablas | Registro manual de eventos |
| ETF flows | Pendiente de fuente gratuita completa validada | Flujo real frente a cambio de AUM, calendario y redistribución | Omitir el bloque o marcar cobertura parcial |

La URL antigua de Raydium devolvió404; el seguimiento localizó [la documentación canónica](https://docs.raydium.io/ray/protocol-fees) y [la comparación por tipo de fee](https://docs.raydium.io/reference/fee-comparison). Documentar una regla no certifica su estado desplegado en todo pool. Pump advierte que su dashboard tiene problemas de cobertura; DefiLlama puede depender de un indexador no público aunque el adaptador sea legible. Ver [revisiones crypto](03_DEEP_TECHNICAL_REVIEWS/README.md).

## Identidad y calidad económica

Mantener un registro de cambios de ticker/contrato; símbolo no es identidad. Una dirección puede representar exchange, contrato compartido, proxy, bot o usuario múltiple; un cluster es una hipótesis con evidencia y fecha. Diferenciar transferencias internas, wrapping, bridge y entrada neta. Medir sensibilidad al retirar etiquetas poco fiables.

No anualizar una semana excepcional como caso base sin mostrar la ventana. No sumar fees, revenue y holder revenue como magnitudes independientes si están contenidas unas en otras. No contar burn como flujo de caja distribuido. Separar un efecto de valoración en USD del cambio en cantidades nativas. Un «usuario activo» requiere definición, no solo una wallet que emitió una transacción.

## Recursos y costes

Para decenas de activos y datos diarios: CPU y 8–16 GB RAM son un presupuesto inicial estimado, no un benchmark. OCR puede necesitar más; profundidad, logs completos y tick data pueden multiplicar disco y coste. Un cálculo de almacenamiento debe usar filas/día × bytes/fila × retención × versiones, midiendo compresión con una muestra futura autorizada.

Modo sin contratación: datos públicos permitidos, descargas manuales y almacenamiento local existente. Esto no garantiza cuota ilimitada, historial completo ni derecho de publicación. Precios de APIs/RPC no cotizados; las capacidades de pago se señalan como pendientes. El coste eléctrico y horas de curación no son cero.

Incompatibilidades observadas: Polars y marimo revisados requieren Python≥3.11; River también. El Python disponible para los auxiliares de esta investigación es3.10. dlt observado restringe DuckDB<2 en destinos. Son datos de commits revisados, no una receta de instalación: decidir versiones compatibles en un piloto posterior y fijarlas, sin actualizar todo indiscriminadamente.

## Seguridad y reproducibilidad

No conectar herramientas de lectura a órdenes, wallets o secretos. Tratar SQL, notebooks, extensiones y parsers como código que requiere revisión antes de ejecutar. No cargar serializaciones opacas de terceros. Los documentos externos no pueden cambiar permisos del agente. Los futuros pilotos de terceros requieren entorno desechable y autorización conforme al mandato.

Exportar el contrato y las evidencias permite interoperabilidad futura sin depender de CIE. No se inspeccionó ni reutilizó arquitectura o código de CIE. La compatibilidad propuesta consiste en nombres, tiempos, unidades y procedencia; no en una plataforma nueva.
