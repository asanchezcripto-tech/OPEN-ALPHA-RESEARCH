# DefiLlama dimension adapters — revisión técnica estática

Observado: 2026-11-04. Referencia del mandato: 2026-11-03. Commit examinado: `c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9`. La fecha de este commit no se obtuvo; la instantánea observada el día 4 no se presenta como reconstrucción certificada del día 3. Nivel V3: inspección de rutas concretas; no se ejecutó, instaló ni importó software externo.

El valor principal es aprender cómo se construye una cifra de actividad económica. La existencia de un adaptador no garantiza que otra persona pueda reconstruir sus históricos ni que todas las cifras estén disponibles con el conocimiento de cada fecha.

## Evidencia examinada

| Ruta | Qué se comprobó |
|---|---|
| [adapters/types.ts](https://github.com/DefiLlama/dimension-adapters/blob/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/adapters/types.ts) | Contratos de adaptadores y resultados dimensionales. |
| [fees/hyperliquid-hlp.ts](https://github.com/DefiLlama/dimension-adapters/blob/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/fees/hyperliquid-hlp.ts) | Ingresos atribuidos a proveedores HLP; ramificación por fecha y origen del dato. |
| [helpers/hyperliquid.ts](https://github.com/DefiLlama/dimension-adapters/blob/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/helpers/hyperliquid.ts) | Repartos fechados, dependencia del indexador, snapshots y fallback a estado actual. |
| [package.json](https://github.com/DefiLlama/dimension-adapters/blob/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/package.json) | Dependencias y comando de prueba de adaptadores; no hay declaración de licencia. |

La [guía oficial](https://docs.llama.fi/list-your-project/other-dashboards) describe entradas temporales, llamadas RPC, logs y balances. Es una especificación; las rutas anteriores permiten contrastar parte de su implementación.

## Arquitectura y semántica

Un `fetch` recibe ventana temporal y utilidades; el adaptador obtiene datos, agrupa importes por token y devuelve dimensiones. La infraestructura puede después valorar esos balances en dólares. La ruta HLP usa un proveedor previo al umbral de cobertura del indexador y otra ruta a partir de ese momento. Devuelve las fees de HLP como ingresos de los proveedores y revenue propio cero: sumar HLP como negocio independiente al total Hyperliquid duplicaría una distribución interna. El adaptador se marca `doublecounted`.

El helper contiene `getRevenueRatioShares(timestamp)`: antes/después del umbral2025-08-30 utiliza repartos97/3 y 99/1. Son proporciones sobre la base definida por esa implementación, no prueba de que99% de cualquier fee bruta termine en HYPE. En ramas HIP-3 hay descuentos, fee de deployer y cambios fechados. Un indicador debe conservar nombre del denominador, programa/mercado y versión del método.

## Hallazgos de calidad temporal

`LLAMA_HL_INDEXER_FROM_TIME` fija cobertura inicial en 2025-08-01; otras familias de snapshots empiezan después. Algunas consultas requieren la variable `LLAMA_HL_INDEXER` y fallan si no existe. La disponibilidad del código no convierte ese servicio en público.

En la obtención de `metaAndAssetCtxs`, si falla el snapshot histórico y la fecha solicitada está en los últimos dos días, la ruta consulta el estado actual de Hyperliquid. Esto es útil operativamente para un dashboard, pero **no debe etiquetarse como observación histórica point-in-time**. Una aplicación propia debe guardar `requested_at`, `observed_at`, origen del fallback y bandera de reconstrucción. La misma cifra diaria puede cambiar al repetirse la consulta.

Estos hechos son estáticos. No se llamó al indexador ni se evaluó la magnitud real del sesgo. Tampoco se auditó toda la familia de adaptadores o cada balance. El comando `test` ejecuta un adaptador; su presencia no constituye cobertura de tests automatizados ni validación contable independiente.

## Licencia, coste y alternativa

No se localizó LICENSE raíz en las variantes examinadas y el manifest no declara licencia. Clasificación: **LICENCIA NO VERIFICADA**. El repositorio puede consultarse como evidencia metodológica; copiar/adaptar código exige aclarar el permiso. Los datos hospedados, RPC y endpoints internos requieren revisión separada.

Para un particular, el primer caso útil sería una comparación semanal de tres protocolos con 10–20 series por protocolo. CPU doméstica y almacenamiento de snapshots pequeños deberían bastar para esa escala —estimación de diseño, no benchmark—; reconstruir todo el indexador aumentaría drásticamente operación y coste de datos. Alternativa: leer resultados públicos permitidos y contrastar una muestra contra eventos originales.

## Experimento previo a adopción

Seleccionar30 días de un protocolo, incluidos un cambio de reparto y un día de dato faltante. Reconciliar fees, pagos a proveedores, protocolo y holders con definiciones explícitas; permitir partidas no cubiertas, nunca completar con cero. Conservar la primera observación y una revisión posterior.

Criterios propuestos: 100% de las cifras con fuente/ventana/versión; diferencias entre sumas explicadas; ningún fallback actual usado como pasado sin marca; error de reconciliación dentro de tolerancia definida según redondeos y cobertura. Beneficio a medir: cuántas divergencias de valoración desaparecen tras corregir metodología. No se ejecutó este experimento.


## Decisión y puntuación

Extraer contabilidad de captura de valor versionada. Extraer una técnica. Puntuación editorial: **70/100**; utility 25, evidence 12, data 10, ease 6, license 0, maintenance 4, usability 6, differentiation 7. Los puntos expresan encaje para este inversor y fuerza de la evidencia estática, no fiabilidad absoluta ni rentabilidad.

Bloqueantes: Reutilización de código bloqueada hasta aclarar licencia; lectura y estudio no equivalen a permiso de copia. Algunas rutas dependen de LLAMA_HL_INDEXER y snapshots no disponibles públicamente; históricos no uniformemente point-in-time.
