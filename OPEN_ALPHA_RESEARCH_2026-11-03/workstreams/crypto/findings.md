# Hallazgos crypto/DeFi

Referencia del mandato: 2026-11-03. Fuentes observadas: 2026-11-04. Investigación documental y estática; ninguna operación, instalación, importación de software externo, API autenticada ni contratación. Las revisiones no prueban rentabilidad ni certifican despliegues. Los commits fijan el contenido leído, pero no se recuperó sistemáticamente su fecha: no se presentan como reconstrucción exacta de lo disponible el día 3.

## Resultado y alcance

El catálogo contiene **63 candidatos: 10 V3, 47 V2, 5 V1 y 1 D0**. Hay 288 referencias de fuente: 198 consultadas y 90 intentos inaccesibles o redirigidos sin el contenido buscado. Son referencias, no 288 proyectos. Las 196 evidencias combinan constancia de archivos examinados con afirmaciones específicas. Cinco URLs iniciales rechazadas/corregidas quedan fuera del catálogo cualificado. Los 8 datasets, 4 proveedores, 2 líneas de investigación, 5 métodos y 4 comparaciones complementan el catálogo; no deben sumarse sin deduplicar como proyectos nuevos.

V1 confirma fuente y función declarada; V2 añade licencia o archivo técnico; V3 inspecciona rutas críticas, interfaces y tests seleccionados. Ningún nivel equivale a ejecución. El único D0 es la pista `DefiLlama/emissions-adapters`: la documentación la menciona, pero no se verificó directamente su repositorio, código ni licencia.

La búsqueda fue especialmente fuerte en GitHub, documentación de operadores y bibliotecas EVM/Solana. Los intentos en chino y Codeberg no produjeron nuevos candidatos suficientemente verificados. La cobertura internacional y de repositorios alternativos es limitada. No se inventan resultados para completar cuotas.

## Tesis principal

La oportunidad más defendible consiste en reconciliar actividad económica y oferta del token con fuentes fechadas. La diferenciación no procede de añadir otro dashboard de fees, sino de explicar cambios de definición, destinatario, inventario y dilución que un agregado oculta. Para un horizonte de 3–18 meses, un monitor semanal acotado puede aportar más utilidad que infraestructura de ejecución o una reconstrucción global de todas las cadenas.

El núcleo debe separar tres capas: declaración del mecanismo, código/configuración que podría ejecutarlo y movimientos efectivamente observados. La evidencia de una capa no completa automáticamente las otras. Una documentación oficial también puede estar incompleta: el panel de Pump reconoce problemas de cobertura después de introducir custom pairs; sus importes visibles no se validaron aquí.

## Hallazgos que cambian una decisión

1. **El sucesor de Polymarket no es el cliente V2.** `py-clob-client` está archivado y declara no ser funcional; el cliente de transición `py-clob-client-v2` también remite al SDK unificado. Se revisó `Polymarket/py-sdk`, cuyo manifest observado declara `polymarket-client` 0.16.0. Para lectura pública ofrece `PublicClient` y paginación que hace visibles cursores y truncamiento. Los clientes legados quedan como referencia de migración.

2. **DefiLlama puede tener fórmulas abiertas y upstream no reproducible.** El helper Hyperliquid depende de `LLAMA_HL_INDEXER`, tiene coberturas por fecha y contempla fallback a contexto actual ante fallo de snapshots recientes. Una fecha histórica en la salida no garantiza que el dato conserve lo conocido entonces. La revisión localiza además cambios de reparto y la marca `doublecounted` de HLP. No se reconstruyeron cifras del proveedor ni se accedió al indexador.

3. **Recompra, burn y distribución tienen efectos diferentes.** RAY recomprado figura como mantenido por el protocolo; UNI enviado a una dirección irrecuperable no demuestra por sí solo que baje el `totalSupply` de ERC20. HYPE tiene componentes de ejecución propios de HyperCore, de modo que un monitor limitado a eventos ERC20 de HyperEVM sería insuficiente.

4. **Normalizar el SDK no normaliza el contrato económico.** En CCXT se inspeccionaron contratos lineales/inversos, `contractSize`, unidades de OI e intervalos de funding posiblemente nulos. Cryptofeed tiene reglas específicas para interpretar el lado de una liquidación reportada. Usar valores homogenizados sin conservar el payload original puede invertir el sentido de una señal.

5. **Las licencias cambiaron o difieren entre piezas de una misma marca.** El SDK Polymarket es MIT, mientras que `ctf-exchange-v2` es BUSL-1.1 con cambio a MIT en 2030 según el texto examinado. Raydium SDK es GPL y sus programas examinados Apache-2.0. Orca Whirlpools tiene licencia propia restrictiva desde 2025; Cryptofeed es AGPL con atribución adicional. No inferir permisos por fama, organización o licencia de una versión antigua.

6. **Una etiqueta on-chain no equivale a una entidad observada.** GraphSense aporta campos de fuente, red y confianza; esa confianza es una categoría del sistema, no una probabilidad calibrada. Los flujos hacia un exchange pueden contener movimientos internos, custodios o wallets mal clasificadas. La incorporación retrospectiva de etiquetas crea fuga de información si se usa en un backtest como si fueran conocidas desde siempre.

## Captura de valor: qué puede y qué no puede sostenerse

| Caso | Evidencia observada | Comprobación pendiente para una ficha financiera |
|---|---|---|
| Hyperliquid/HYPE | Documentación del assistance fund, SDK público y fórmula de agregador inspeccionados | Alcance por producto, periodos, fees netas, conversión y oferta reconciliados; no aplicar un porcentaje universal a todo el volumen |
| Uniswap/UNI | Contratos TokenJar/Releaser/Firepit y tests; anuncio TJAR de octubre de 2026 | Pool/red/configuración activos y eventos, lag de conversión, costes/excedentes y destino final; no convertir código en prueba de activación general |
| Raydium/RAY | Ruta actual de fees y buybacks consultada; layouts/configuración en SDK | Lectura de cuentas por slot, trazabilidad hasta holding de RAY y tratamiento del inventario; no etiquetar holding como burn |
| Pump/PUMP | Panel anuncia asignación a recompra/quema y declara limitaciones | Reconciliar custom pairs, fuente de revenue, transacciones y oferta antes de usar múltiplos; abstenerse sobre cifras del panel |
| Polymarket | SDK público y reglas de datos/mercados | Negocio, mercados y producto estudiables; no se verificó token ni derecho económico atribuible, y no se infiere del SDK |

El cociente market cap/revenue del protocolo puede ser descriptivo, pero no es automáticamente P/E del token. Un ingreso del protocolo no constituye un derecho de caja del poseedor. Los incentivos distribuidos desde tesorería, nuevos tokens emitidos y unlocks preexistentes requieren tratamiento separado para evitar restar un coste dos veces o llamar emisión a un simple cambio de circulante.

## Priorización concreta

| Recurso revisado | Score editorial /100 | Decisión inicial |
|---|---:|---|
| Hyperliquid Python SDK | 87 | Lectura pública acotada; registrar cobertura y evitar WebSocket por defecto si basta REST |
| CCXT | 83 | Base de snapshots de mercados, manteniendo especificaciones y respuestas nativas |
| Polymarket SDK unificado | 80 | Cesta curada de eventos como evidencia contextual de tesis |
| Cryo | 77 | Extracción batch de contratos/bloques seleccionados, con límites RPC explícitos |
| Uniswap protocol-fees | 75 | Extraer esquema contable y lectura de eventos; no desplegar contratos |
| Ponder | 74 | Evaluar sólo cuando haga falta índice continuo con manejo de reorgs |
| GraphSense lib | 73 | Extraer esquema de atribución y trazabilidad; plataforma completa sólo si el alcance lo justifica |
| DefiLlama dimension adapters | 70 | Referencia de fórmulas y descubrimiento; copia bloqueada mientras no se aclare licencia |
| Raydium SDK V2 | 68 | Interpretación de pools y configuración; revisar obligaciones GPL antes de integración/distribución |
| Cryptofeed | 68 | Streaming sólo si su utilidad compensa operación y obligaciones AGPL/atribución |

Las puntuaciones favorecen utilidad para el inversor, evidencia, datos y facilidad; no miden alpha. Mantenimiento no se puntuó con estrellas: faltó una auditoría cronológica sistemática y se penalizó esa incertidumbre. Los bloqueantes de licencia, datos o deprecación prevalecen sobre el total. Hummingbot, nodo Hyperliquid, Graph Node y Geyser global no son la primera elección para un monitor personal semanal.

## Datos y límites que deben entrar en los diseños

**Oferta y stablecoins.** Registrar activos nativos, wrappers, bridges y custodios con una identidad común y representaciones separadas. CCTP documenta burn-and-mint intercadena: inferimos que un mint local puede ser migración, no entrada fiat. Unlock aumenta disponibilidad circulante, no necesariamente total emitido. Guardar cantidades nativas, decimales, precio usado, fecha de anuncio y revisiones del calendario. No sustituir reservas del emisor por balances de contratos.

**CEX/DEX y derivados.** Los depósitos/retiros etiquetados no revelan compras/ventas dentro de CEX. Un swap puede ser una pierna de un router; volumen bruto no cuenta usuarios únicos ni capital nuevo. OI USD cambia por cantidad y precio, y la exposición agregada de venues puede incluir coberturas duplicadas económicamente. Distinguir funding estimado del realizado y conservar el signo, moneda, duración y referencia temporal. Mark IV es una magnitud modelada del venue, no volatilidad futura observada.

**Liquidaciones y profundidad.** Ninguna fuente se comprobó como censo universal. La antigua URL Binance de streams redirigió sin confirmar la regla histórica de muestreo; no repetirla como estado actual. Al añadir profundidad se necesitan snapshots y secuencias completas; un corte invalida reconstrucciones hasta resincronizar. Las estimaciones de liquidación deben permanecer separadas de eventos reportados.

**Acceso e historia.** El SDK Hyperliquid no aporta archivo ilimitado; Polymarket puede retrasar peticiones bajo throttling. Los archivos Spot de Binance cambian escala temporal a microsegundos desde enero de 2025 según su README. Una respuesta grande no prueba universo completo, y disponer hoy de un histórico revisado no reconstruye el vintage original.

**Servicios cerrados.** Dune puede ahorrar extracción y Token Terminal facilitar comparación, pero sus productos hospedados no se transforman en abiertos por tener clientes o páginas públicas. La metodología textual de tokenholder revenue de Token Terminal declara generación automática; sirve como definición del proveedor, con validación de implementación pendiente. No se cotizaron planes ni se obtuvieron claves. La alternativa gratuita es reducir universo e historial y conservar observaciones propias autorizadas.

## Combinaciones propuestas y prueba de valor añadido

- **Fundamentales + oferta + cambios documentales:** snapshots de mecanismo, eventos de captura y calendario de supply. Buscar divergencias explicadas por cambios de definición o dilución antes de convertirlas en tesis de valoración. Piloto de un protocolo, con residual visible y abstención cuando falte una etapa.
- **Estrés de derivados + flujos etiquetados:** comparar presión por venue con transferencias de colateral, manteniendo incertidumbre de entidad. Una coincidencia temporal es indicio para investigación, no identificación causal de “whales” ni predicción de liquidación.
- **Polymarket + tesis de inversión:** enlazar eventos a reglas de resolución y a evidencia documental fechada. Guardar contradicciones entre mercados aparentemente equivalentes. Medir tiempo de revisión y errores detectados antes de estudiar retornos.
- **Índice de eventos + versiones de adaptador:** comparar serie publicada con reconstrucción pequeña y reproducible. Un cambio metodológico debería generar una explicación de revisión, no una alerta financiera falsa.

Ninguna combinación fue implementada o probada. El primer experimento futuro debe comparar con una ficha manual y una regla simple, fijar tolerancias de reconciliación y evaluar utilidad, errores y fatiga de avisos. Una extracción local acotada puede funcionar en CPU y memoria domésticas; historia granular o un nodo completo cambia radicalmente el coste. Son estimaciones, no benchmarks.

## Ocho fuentes primarias para la síntesis

1. [Polymarket SDK actual, README fijado](https://github.com/Polymarket/py-sdk/blob/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/README.md): cliente unificado y ámbito público.
2. [DefiLlama helper Hyperliquid fijado](https://github.com/DefiLlama/dimension-adapters/blob/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/helpers/hyperliquid.ts): fórmulas, upstream y temporalidad.
3. [Hyperliquid fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees): mecanismos y ámbitos de fee documentados.
4. [Uniswap TokenJar fijado](https://github.com/Uniswap/protocol-fees/blob/00066e1cad8b5e78f768860e4169b39baf4b300c/src/TokenJar.sol): permisos y etapas contractuales.
5. [Raydium buybacks](https://docs.raydium.io/ray/ray-buybacks): destino documentado de las recompras.
6. [Pump token dashboard](https://pump.fun/pump-token): declaración del mecanismo y advertencia de cobertura.
7. [Circle CCTP](https://developers.circle.com/cctp): contraejemplo de mint local frente a entrada de capital nuevo.
8. [Token Terminal tokenholder revenue](https://tokenterminal.com/explorer/metrics/tokenholder_revenue): definición de proveedor y límites de metodología publicada.

Las revisiones completas están en `03_DEEP_TECHNICAL_REVIEWS/crypto_*.md`. `critical_review.md` contiene correcciones propuestas a los blueprints OP-01 y OP-04. `REPRODUCIBILITY.md` explica qué se conserva y qué no se ejecutó.
