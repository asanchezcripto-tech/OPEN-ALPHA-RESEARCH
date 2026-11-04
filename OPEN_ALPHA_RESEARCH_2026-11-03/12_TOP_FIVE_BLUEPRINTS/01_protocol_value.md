# OP-01 — Protocol Value & Dilution Analyzer

Diseño preliminar, no implementado. Prioridad estratégica 1. Horizonte: 3–18 meses. La selección responde al interés principal del mandato en actividad económica, captura de valor y dilución; el score no es una estimación de rentabilidad.

## Problema y primera capacidad útil

Un protocolo puede cobrar más, pagar más incentivos y dejar menos valor atribuible al token. El producto debe explicar ese puente, no ofrecer un múltiplo único que mezcle denominadores. Primera entrega futura: una ficha semanal de HYPE con tres cifras reconciliadas y una tabla de qué falta; después UNI y RAY. PUMP se incorpora cuando las fuentes se puedan reconciliar. Polymarket se estudia como negocio/mercado, sin atribuir derechos a un token no comprobado.

Casos: comprobar si crecen ingresos netos de subsidios; distinguir una recompra anunciada de una ejecutada; explicar una caída del múltiplo por precio, ingresos, emisiones o revisión metodológica. El analista debe poder abrir la transacción o definición que sostiene cada conclusión.

## Flujo y arquitectura mínima

```mermaid
flowchart LR
  A[Fuentes y eventos] --> B[Snapshot fechado y hash]
  B --> C[Identidad, unidades y cobertura]
  C --> D[Puente económico por mecanismo]
  D --> E[Supply y escenarios]
  E --> F[Ficha semanal con evidencia]
  C --> G[Cuarentena y abstención]
```

Un recolector batch, ficheros Parquet inmutables, DuckDB y un informe marimo o HTML. Tablas mínimas: observaciones, versiones de mecanismos, movimientos de supply, fuentes y controles. No hace falta backend multiusuario, indexar todas las cadenas ni desplegar contratos. Cada herramienta conserva su propio almacenamiento y puede exportar el contrato ligero de [datos](../06_DATA_AND_INFRASTRUCTURE.md).

Bibliotecas candidatas: DuckDB, Pandera y DataComPy. SDK oficial para leer el ámbito de un protocolo; adaptadores DefiLlama como referencia revisable, con permiso de código por resolver donde proceda. No copiar por defecto un adaptador sin licencia verificada.

## Fuentes, permisos y alternativa gratuita

- [DefiLlama: metodología y dimensiones](https://docs.llama.fi/list-your-project/other-dashboards): localizar la fórmula y fuente de cada serie. La revisión del helper Hyperliquid identifica un fallback a contexto actual; no toda fecha pasada certifica un vintage.
- [Hyperliquid: fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees): mecanismo documentado del assistance fund; contrastar alcance, periodo y movimientos antes de convertirlo en ratio.
- [Uniswap: protocol-fees](https://github.com/Uniswap/protocol-fees): contratos y pruebas; existencia de código no prueba activación en toda red/pool. Distinguir propuesta, despliegue y ejecución.
- [Pump: panel del token](https://pump.fun/pump-token): advierte de incorrecciones de cobertura tras custom pairs. Las cifras visibles no pasan automáticamente la reconciliación.

Alternativa sin API de pago: ficha manual de un protocolo con fuentes oficiales y muestras de eventos públicos. Reduce automatización, universo e historial; mantiene la pregunta útil. Si se necesita archive RPC, API premium o datos de unlocks, documentar cobertura y cotizar después. No se ha contratado nada ni se presupone permiso de redistribución.

## Entradas, cálculos y salidas

Cada observación lleva asset/protocol/chain/contract, unidad, intervalo, event_at, available_at, acquired_at, versión de método, fuente y calidad. Cada mecanismo añade fecha de propuesta, activación, alcance, beneficiario y posibilidad de modificación. Un unlock futuro conocido lleva announced_at y scheduled_at; no se elimina por ser posterior a hoy.

Presentar por separado fees brutas, pagos a proveedores/LP/creadores, revenue del protocolo, incentivos, recompra ejecutada, burn ejecutado y emisión. **No restar dos veces** pagos ya excluidos por el proveedor. Emitir un puente con residual de reconciliación. Una recompra que permanece en tesorería no es automáticamente burn ni flujo recibido por el tenedor.

Un unlock aumenta oferta circulante disponible pero no necesariamente supply total; mint y burn sí pueden modificar totalSupply según el contrato. Un envío a una dirección supuestamente irrecuperable no se etiqueta como burn contable sin comprobar el mecanismo. El puente debe admitir inventario retenido, cambio de divisa, precio de conversión y desfase entre devengo, barrido, recompra y quema; no tratar todo residual como error o fuga de valor.

Guardar por separado minted, burned, locked, treasury, circulating y bridged_representation. Reconciliar primero cantidades por activo y después valorar bajo una convención explícita. Una ruta Jar→bridge→destino no crea tres ingresos. Definir product_scope, mechanism_version, valid_from/to y coverage_status: los logs ERC20 de HyperEVM por sí solos no cubren fees de HyperCore. Incentivos de tesorería, tokens recién emitidos y costes externos son magnitudes distintas; evitar doble sustracción. Identificar además elegibilidad de pagos —staking/bloqueo/voto— y no repartirlos imaginariamente entre todos los tokens.

Ratios opcionales: market cap / ingresos comparables de 12 meses; valor destinado a recompra / capitalización media; emisión neta / supply inicial. Indicar moneda, ventana y definición. No sumar un porcentaje de burn al rendimiento de caja del tenedor. Supply efectivo bajo escenarios de unlock/vesting y flujo atribuible por token son análisis de sensibilidad, no derechos contractuales ni valor intrínseco certificado.

Salida: waterfall de magnitudes, tres escenarios, cambios desde la última revisión y una tabla de contradicciones. Mostrar «no comparable» cuando cambie cobertura o no se conozca el destinatario económico.

## Incertidumbre, experimentos y aceptación

Piloto propuesto: tres protocolos, 90 días de snapshots prospectivos o históricos con disponibilidad verificable. Un analista reconcilia diez días y cinco eventos por protocolo. Incluir una revisión de adaptador, un cambio de mecanismo y un hueco de fuente.

Aceptar si ≥95% de importes materiales tienen fuente/definición/periodo, todos los cambios de método quedan visibles y ninguna cifra marcada como desconocida se convierte en cero. Fijar antes del piloto qué es material —por ejemplo, 1% del total o la magnitud capaz de cambiar una conclusión— y publicar diferencias residuales. Medir tiempo ahorrado frente a la ficha manual y correcciones detectadas; no exigir rentabilidad para probar utilidad informativa.

El denominador del 95% es el universo de productos/cadenas explícitamente delimitado, no una totalidad desconocida. Exigir trazabilidad del 100% de eventos materiales de la muestra auditada y residual por activo dentro de tolerancia predefinida; separar residual explicado del no resuelto. Si no puede medirse cobertura, retirar el porcentaje y declarar la laguna. Guardar fechas de anuncio, efectividad, primera observación y adquisición; una reconstrucción ex post se etiqueta como tal.

Riesgos: volumen circular, subsidios en tokens volátiles, cambios de supply, dobles conteos entre redes y datos adquiridos hoy tratados como información histórica. Abstenerse de un ranking si el puente económico no cierra. Una fuente oficial puede ser incompleta o interesada.

## Incrementos y coste estimado

1. Ficha manual y contrato de métricas de un protocolo.
2. Snapshots, diff y comparación de tres protocolos.
3. Escenarios de dilución y reconciliación de recompras.
4. Avisos de cambios de mecanismo con revisión humana.

Estimación editorial: 6–12 jornadas para un primer protocolo acotado; tres protocolos e históricos completos requieren nueva estimación tras conocer las fuentes. Prever 1–2 horas semanales de mantenimiento al principio. Un piloto prospectivo de 90 días requiere 90 días naturales aunque prepararlo lleve menos jornadas. CPU y 8–16 GB RAM como supuesto, no benchmark. Evitar un token valuation model universal, un agente que cambie definiciones solo y cualquier ejecución de operaciones.
