import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
OUT=ROOT.parent.parent/'03_DEEP_TECHNICAL_REVIEWS'
repos={x['repo']:x for x in json.loads((ROOT/'inspection_sources.json').read_text(encoding='utf8'))}
candidates={x['original_url'].removeprefix('https://github.com/'):x for x in json.loads((ROOT/'candidates.json').read_text(encoding='utf8'))}
def link(repo,path,label=None):
 return '['+(label or path)+'](https://github.com/'+repo+'/blob/'+repos[repo]['sha']+'/'+path+')'
def render(repo,slug,body):
 c=candidates[repo]
 header=f"# {c['name']} — revisión técnica estática\n\nObservado: 2026-11-04. Referencia del mandato: 2026-11-03. Commit examinado: `{repos[repo]['sha']}`. La fecha de este commit no se obtuvo; la instantánea observada el día4 no se presenta como reconstrucción certificada del día3. Nivel V3: inspección de rutas concretas; no se ejecutó, instaló ni importó software externo.\n\n"
 footer='\n\n## Decisión y puntuación\n\n'+c['practical_use']+'. '+c['adoption_mode']+'. Puntuación editorial: **'+str(c['total_score'])+'/100**; '+', '.join(k+' '+str(v) for k,v in c['scores'].items())+'. Los puntos expresan encaje para este inversor y fuerza de la evidencia estática, no fiabilidad absoluta ni rentabilidad.\n\nBloqueantes: '+(' '.join(c['blockers']) if c['blockers'] else 'No se identificó un bloqueo de licencia del código examinado; siguen pendientes validación operacional y permisos de datos.')+'\n'
 (OUT/('crypto_'+slug+'.md')).write_text(header+body+footer,encoding='utf8')

repo='DefiLlama/dimension-adapters'
render(repo,'defillama_dimensions',f'''El valor principal es aprender cómo se construye una cifra de actividad económica. La existencia de un adaptador no garantiza que otra persona pueda reconstruir sus históricos ni que todas las cifras estén disponibles con el conocimiento de cada fecha.

## Evidencia examinada

| Ruta | Qué se comprobó |
|---|---|
| {link(repo,'adapters/types.ts')} | Contratos de adaptadores y resultados dimensionales. |
| {link(repo,'fees/hyperliquid-hlp.ts')} | Ingresos atribuidos a proveedores HLP; ramificación por fecha y origen del dato. |
| {link(repo,'helpers/hyperliquid.ts')} | Repartos fechados, dependencia del indexador, snapshots y fallback a estado actual. |
| {link(repo,'package.json')} | Dependencias y comando de prueba de adaptadores; no hay declaración de licencia. |

La [guía oficial](https://docs.llama.fi/list-your-project/other-dashboards) describe entradas temporales, llamadas RPC, logs y balances. Es una especificación; las rutas anteriores permiten contrastar parte de su implementación.

## Arquitectura y semántica

Un `fetch` recibe ventana temporal y utilidades; el adaptador obtiene datos, agrupa importes por token y devuelve dimensiones. La infraestructura puede después valorar esos balances en dólares. La ruta HLP usa un proveedor previo al umbral de cobertura del indexador y otra ruta a partir de ese momento. Devuelve las fees de HLP como ingresos de los proveedores y revenue propio cero: sumar HLP como negocio independiente al total Hyperliquid duplicaría una distribución interna. El adaptador se marca `doublecounted`.

El helper contiene `getRevenueRatioShares(timestamp)`: antes/después del umbral2025-08-30 utiliza repartos97/3 y99/1. Son proporciones sobre la base definida por esa implementación, no prueba de que99% de cualquier fee bruta termine en HYPE. En ramas HIP-3 hay descuentos, fee de deployer y cambios fechados. Un indicador debe conservar nombre del denominador, programa/mercado y versión del método.

## Hallazgos de calidad temporal

`LLAMA_HL_INDEXER_FROM_TIME` fija cobertura inicial en2025-08-01; otras familias de snapshots empiezan después. Algunas consultas requieren la variable `LLAMA_HL_INDEXER` y fallan si no existe. La disponibilidad del código no convierte ese servicio en público.

En la obtención de `metaAndAssetCtxs`, si falla el snapshot histórico y la fecha solicitada está en los últimos dos días, la ruta consulta el estado actual de Hyperliquid. Esto es útil operativamente para un dashboard, pero **no debe etiquetarse como observación histórica point-in-time**. Una aplicación propia debe guardar `requested_at`, `observed_at`, origen del fallback y bandera de reconstrucción. La misma cifra diaria puede cambiar al repetirse la consulta.

Estos hechos son estáticos. No se llamó al indexador ni se evaluó la magnitud real del sesgo. Tampoco se auditó toda la familia de adaptadores o cada balance. El comando `test` ejecuta un adaptador; su presencia no constituye cobertura de tests automatizados ni validación contable independiente.

## Licencia, coste y alternativa

No se localizó LICENSE raíz en las variantes examinadas y el manifest no declara licencia. Clasificación: **LICENCIA NO VERIFICADA**. El repositorio puede consultarse como evidencia metodológica; copiar/adaptar código exige aclarar el permiso. Los datos hospedados, RPC y endpoints internos requieren revisión separada.

Para un particular, el primer caso útil sería una comparación semanal de tres protocolos con10–20 series por protocolo. CPU doméstica y almacenamiento de snapshots pequeños deberían bastar para esa escala —estimación de diseño, no benchmark—; reconstruir todo el indexador aumentaría drásticamente operación y coste de datos. Alternativa: leer resultados públicos permitidos y contrastar una muestra contra eventos originales.

## Experimento previo a adopción

Seleccionar30 días de un protocolo, incluidos un cambio de reparto y un día de dato faltante. Reconciliar fees, pagos a proveedores, protocolo y holders con definiciones explícitas; permitir partidas no cubiertas, nunca completar con cero. Conservar la primera observación y una revisión posterior.

Criterios propuestos:100% de las cifras con fuente/ventana/versión; diferencias entre sumas explicadas; ningún fallback actual usado como pasado sin marca; error de reconciliación dentro de tolerancia definida según redondeos y cobertura. Beneficio a medir: cuántas divergencias de valoración desaparecen tras corregir metodología. No se ejecutó este experimento.
''')

repo='hyperliquid-dex/hyperliquid-python-sdk'
render(repo,'hyperliquid_sdk',f'''Es una pieza proporcionada para investigar HYPE, BTC y ETH con lecturas públicas. Su utilidad diferencial es exponer posición, funding y estructura de mercado con semántica del protocolo; no proporciona por sí solo un archivo histórico completo ni identifica entidades económicas.

## Rutas críticas

Se inspeccionaron {link(repo,'hyperliquid/info.py')}, {link(repo,'hyperliquid/websocket_manager.py')}, {link(repo,'tests/info_test.py')} y {link(repo,'pyproject.toml')}. El manifest examinado declara versión0.24.0 y Python compatible con3.9+, con `requests`, `websocket-client`, `msgpack`, `eth-account` y `eth-utils`. La [licencia MIT]({ 'https://github.com/'+repo+'/blob/'+repos[repo]['sha']+'/LICENSE.md' }) cubre el repositorio examinado; no se extendió a datos ni binarios del nodo.

## Arquitectura y datos

La clase `Info` encapsula llamadas a `/info`. `user_state` pide `clearinghouseState`; `funding_history` usa milisegundos; `l2_snapshot` y `candles_snapshot` construyen peticiones por instrumento. Los estados monetarios llegan frecuentemente como cadenas y varios retornos se tipan `Any`: debe añadirse validación local de unidades, campos faltantes y números exactos.

`Info` inicia un gestor WebSocket por defecto. Para un proceso diario de lectura REST resulta relevante `skip_ws=True`; evita iniciar un hilo que la tarea no necesita. El gestor envía pings y despacha mensajes a suscripciones. No se verificó que cubra todos los casos de reconexión ni que reconstruya huecos después de una caída.

La [documentación del endpoint Info](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint) distingue identificadores spot/perp, remapeos y paginación de consultas temporales. El wrapper de funding inspeccionado realiza una petición; el consumidor debe demostrar completitud de las páginas. El conjunto de wallets que consulta un usuario sigue siendo una muestra: estado público de una cuenta no equivale al censo de participantes.

## Qué prueba la evidencia

`tests/info_test.py` usa cassettes VCR para user state, fills, funding, libro y velas; comprueba ciertos campos, tipos y recuentos. Esto respalda la existencia de un contrato de respuesta y ejemplos reproducibles del SDK. No se ejecutaron tests, no se midió cobertura, y fixtures antiguos no garantizan compatibilidad de la API actual.

Los precios de liquidación de cuentas son estados contingentes: depósitos, retiradas, posiciones correlacionadas y cambios de margen los desplazan. Un mapa de precios posibles debe separarse de fills confirmados. Para interpretación fundamental, la [página oficial de fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees) documenta asistencia a HYPE y quema; demostrar importes históricos exige reconciliación adicional, no sólo repetir esa descripción.

## Uso proporcional y costes

Flujo mínimo propuesto: tres activos→snapshot de metadatos/OI/funding→validación→tabla diaria con cambios y cobertura. Un portátil CPU sin GPU es suficiente como hipótesis para unas pocas peticiones; el espacio depende de conservar payloads. No se midió consumo. El nodo completo es otra categoría: el README de [hyperliquid-dex/node](https://github.com/hyperliquid-dex/node) prescribe128GB RAM y grandes volúmenes de logs; queda fuera de la primera capacidad útil.

Alternativas: HTTP directo si se requieren pocos campos; CCXT si interesa normalizar varios exchanges. El SDK oficial es preferible cuando los campos Hyperliquid son la pregunta de investigación; CCXT evita duplicar parsers de mercado general.

## Experimento y aceptación

Registrar prospectivamente14 días para BTC/ETH/HYPE y verificar una muestra manual de snapshots. Criterios: identidad de activo y DEX explícita; funding con intervalo conocido; datos fuera de plazo visibles; páginas sin huecos detectables; cambios de universo versionados. Comparar señal de estrés con un baseline de volatilidad realizada, sin afirmar causalidad ni previsión de precios. No se accedió a cuentas privadas ni se crearon órdenes.
''')

repo='Polymarket/py-sdk'
render(repo,'polymarket_sdk',f'''La conclusión más útil es de compatibilidad: el sucesor de `py-clob-client` ya no es simplemente `py-clob-client-v2`. Los READMEs oficiales de ambos remiten al SDK unificado. La [release v1.2.1 de V2](https://github.com/Polymarket/py-clob-client-v2/releases/tag/v1.2.1) publica la deprecación. Para investigación personal conviene empezar por `PublicClient` y no por los ejemplos de firma/órdenes.

## Evidencia inspeccionada

| Archivo | Alcance |
|---|---|
| {link(repo,'src/polymarket/clients/public.py')} | Métodos públicos, referencias de activos, mercado y precios. |
| {link(repo,'src/polymarket/clients/_transport.py')} | Errores HTTP, rate limits y análisis de Retry-After. |
| {link(repo,'src/polymarket/pagination.py')} | Página, cursores, truncamiento y conversión a dataframes. |
| {link(repo,'tests/unit/test_date_field_contract.py')} | Contrato de fechas y casos inválidos. |
| {link(repo,'tests/unit/test_public_calls_surface.py')} | Superficie de llamadas públicas. |
| {link(repo,'tests/unit/test_data_retry.py')} | Casos de reintentos de datos. |

El {link(repo,'pyproject.toml')} declara `polymarket-client`0.16.0 en el commit observado y Python>=3.11. Es una versión de manifest, no una afirmación de que esa sea la última release publicada. Se comprobaron `httpx`, Pydantic, websockets y extras opcionales Arrow/pandas/Polars. Licencia {link(repo,'LICENSE','MIT')}.

## Diseño y capacidades transferibles

La API pública separa acciones de transporte y parsing. Devuelve objetos del SDK y utiliza `Decimal` para precios monetarios concretos. Se puede consultar el mercado por identificador, slug o URL. Las peticiones de referencias de activos validan selectores y explicitan metadatos nulos; algunas observaciones pueden ir retrasadas.

La clase `Page` diferencia `has_more`, `next_cursor` y `limit_reached`: alcanzar un tope de profundidad impide comprobar otra página, pero no demuestra que existan más registros. La conversión a pandas conserva banderas de truncamiento. Esta es una técnica aprovechable por cualquier laboratorio: una tabla grande no debe presentarse como exhaustiva sin señal de cobertura.

El transporte interpreta `Retry-After` numérico y como fecha HTTP, y expone errores tipados. Esa implementación no autoriza a ignorar límites ni garantiza que cualquier endpoint se reintente de la misma manera. Se inspeccionaron tests de fechas, llamadas y retry; no se ejecutaron ni se dedujo cobertura porcentual.

## Valor financiero y límites

Polymarket puede aportar escenarios y fechas de resolución a un Thesis Tracker, pero el precio refleja también spread, liquidez, costes, diseño de contrato y participantes. Dos mercados con títulos parecidos pueden resolver con criterios distintos. El análisis debe guardar texto de resolución y versión observada, no sólo ticker y probabilidad.

Un backtest de acontecimientos necesita mercados cerrados y fallidos, no sólo los listados hoy; conservar actualizaciones de resolución evita conocer retrospectivamente información no disponible. Los volúmenes y posiciones no dan automáticamente una medida de convicción independiente: una entidad puede operar muchos mercados y wallets.

## Coste, alternativa y experimento

Para una cesta curada de20 mercados, CPU y unos pocos GB de RAM deberían bastar —estimación, no medición—. El coste principal sería mantenimiento del contrato de API y adquisición prospectiva. No se descargaron históricos completos ni se verificaron derechos de redistribución; éstos son distintos de la licencia MIT.

Comparar durante cuatro semanas SDK público frente a HTTP directo en10 mercados:100% de fechas UTC y unidades explícitas; ninguna fila truncada silenciosamente; todas las resoluciones vinculadas a su regla; estados inválidos generan abstención. Medir tiempo de revisión y número de contradicciones detectadas frente a leer manualmente las páginas. Evitar perps, wallets, órdenes y relayer en este primer uso: añaden funciones ajenas al objetivo autorizado.
''')

repo='ccxt/ccxt'
render(repo,'ccxt',f'''CCXT aporta normalización reutilizable; el error sería confundir nombres de campos uniformes con equivalencia económica entre exchanges. Es una buena primera biblioteca para frecuencia diaria u horaria, siempre acompañada por metadatos y payload original.

## Evidencia y arquitectura

Se inspeccionaron {link(repo,'python/ccxt/base/exchange.py')}, rutas concretas de {link(repo,'python/ccxt/binance.py')}, {link(repo,'python/ccxt/test/base/test_parse_precision.py')} y {link(repo,'package.json')}. El manifest registra4.5.91 en la instantánea observada. Licencia {link(repo,'LICENSE.txt','MIT')}. La amplitud del repo no se auditó: la revisión técnica se concentra en OHLCV, funding, identidad contractual y open interest de Binance.

La clase base proporciona interfaz y utilidades; cada exchange implementa métodos específicos y parsing. `fetch_ohlcv` deriva su endpoint de producto/mercado. Los símbolos contractuales incluyen activo de liquidación y metadatos `linear`, `inverse`, `contractSize`; `info` preserva respuesta original en muchas estructuras.

En Binance, el parser de funding toma por separado `lastFundingRate`, `nextFundingTime` y, cuando está disponible en la respuesta correspondiente, `fundingIntervalHours`. El intervalo puede quedar vacío; no es correcto multiplicar toda tasa por3×365 suponiendo ocho horas. La señal que se usa debe declarar si representa último pago, estimación próxima o promedio histórico.

El parser de open interest distingue instrumentos inversos y deja `baseVolume` sin valor para esos casos. `openInterestAmount` puede ser contratos, mientras que valores en moneda base o dólares requieren conversiones distintas. La normalización conserva información útil, pero no elimina la necesidad de comprobar denominadores.

## Control temporal y pruebas

`fetch_funding_rate_history` expone `since` en milisegundos y paginación opcional. La disponibilidad de historia depende del endpoint; solicitar una ventana no prueba que se recibió completa. La última vela puede estar abierta; universo actual excluye delistings. Guardar `instrument_id`, mercado, ventana cerrada, event_time, acquisition_time y respuesta raw evita buena parte de errores evitables.

El test de precisión examinado valida conversiones de precisión; **no constituye un test del histórico de funding ni del open interest**. Una ruta de test adicional buscada para funding no fue accesible con el nombre supuesto y se registró el fallo. No se ejecutaron tests, llamadas de mercado ni benchmarks de latencia.

## Encaje, coste y alternativa

Una lectura diaria de20 activos en2–3 venues es proporcionada a CPU doméstica y almacenamiento columnar pequeño; es una estimación de diseño. Cada exchange impone cuotas, condiciones y retención. La licencia MIT del cliente no cubre la comercialización de datos. La amplitud del paquete también exige pinning y revisión de dependencias antes de cualquier ejecución futura.

Cryptofeed sería preferible si la pregunta requiere mensajes WebSocket y reconstrucción de libro. Pybit o conectores oficiales de Binance son útiles cuando CCXT no expone un campo o una actualización concreta. No construir un wrapper universal adicional antes de conocer esa necesidad.

## Experimento mínimo

Elegir BTC spot, BTC perp lineal y un contrato inverso; cotejar30 puntos horarios contra datos originales. Criterios: conversiones de notional trazables; funding con intervalo explícito o abstención; velas incompletas apartadas; detección de huecos y delistings; mismos resultados al reejecutar sobre snapshots fijados. La comparación debe medir errores de normalización y tiempo de mantenimiento, no rentabilidad de una estrategia inventada.
''')

repo='Uniswap/protocol-fees'
render(repo,'uniswap_protocol_fees',f'''Este repositorio permite pasar de la etiqueta genérica “revenue de Uniswap” a una cadena verificable de derechos, conversiones y destinos. Es particularmente valioso para separar fees de LP, importes recolectados y tokens enviados a quema. No se verificaron transacciones o parámetros desplegados durante esta revisión.

## Implementación comprobada

| Ruta | Hallazgo estático |
|---|---|
| {link(repo,'src/TokenJar.sol')} | Sólo el releaser puede extraer; el owner puede cambiar el releaser. |
| {link(repo,'src/releasers/ExchangeReleaser.sol')} | Intercambia recursos por activos del Jar, controla nonce y limita número de activos. |
| {link(repo,'src/releasers/Firepit.sol')} | Fija destinatario del recurso en `0xdead`. |
| {link(repo,'test/Firepit.t.sol')} | Casos ERC20/nativo, saldo insuficiente y nonce inválido. |
| {link(repo,'foundry.toml')} | Configuración de compilación y pruebas; no ejecutada. |

Los archivos examinados contienen SPDX `AGPL-3.0-only`. El README declara esa licencia para el proyecto, pero las dependencias —incluido material de v4-core y Solmate— deben revisarse por archivo si se copia código. Para un monitor de lectura bastaría interpretar contratos/ABI; no es necesario desplegar ni bifurcar el protocolo.

## Flujo económico

Los adaptadores de fees alimentan un TokenJar. Un agente externo entrega el umbral del recurso elegido y recibe activos del Jar. `ExchangeReleaser` usa `safeTransferFrom` hacia el destinatario del recurso y emite `Released`. Firepit concreta la dirección de quema.

El código también comenta límites económicos: polvo que nunca resulta rentable retirar, costes de gas, cambios bruscos de precio y excedente para quien ejecuta la conversión. Por ello, valorar todos los activos acumulados como una recompra inmediata de UNI exageraría lo realizado. Hay que separar devengo de fee, transferencia al Jar, liberación y destino final.

Un envío a `0xdead` es evidencia de tokens retirados económicamente del uso; no debe afirmarse que el contrato ERC20 reduce `totalSupply` sin verificar su implementación. Y que el contrato exista en GitHub no prueba que cada pool lo utilice. El {link(repo,'README.md','README')} enumera despliegues, pero no se contrastó bytecode ni estado de cada uno.

El [artículo oficial de TJAR del30-10-2026](https://blog.uniswap.org/how-tjar-works-uniswaps-onchain-fee-conversion-system) describe despliegue y generalización del sistema. Es anuncio/documentación del operador; ofrece evidencia más reciente que una propuesta de2025, pero no sustituye recibos y parámetros on-chain.

## Pruebas, riesgos y uso

Los tests inspeccionados cubren mecánica de transferencia y nonces. No prueban que el mecanismo maximice captura de valor, que un threshold sea adecuado o que no existan vulnerabilidades en el conjunto. Tampoco se revisaron informes de auditoría completos.

La capacidad útil para3–18 meses sería un ledger semanal de fees cobradas, pendientes de conversión, UNI transferido a destino y cambios de política. Debe registrar chain_id, contrato, bloque, tx/log y etapa contable para evitar sumar L2→bridge→L1 como tres ingresos. Un watcher acotado no necesita GPU ni nodo propio; coste incierto del proveedor RPC y amplitud de historia. Es una estimación, sin benchmark.

## Experimento de valor añadido

Seleccionar un Jar y30 días; reconciliar balances inicial/final, entradas y releases. Comparar una métrica ingenua de revenue con captura realizada y lag de conversión. Aceptación: cada release atribuible a evento; ninguna transferencia interna duplicada; diferencias contables explicadas; parámetros observados fechados; ausencia de actividad se representa como desconocida si falla la fuente. Resultado buscado: detectar falsas divergencias de valoración por desfases de conversión, sin afirmar que capturen retornos futuros.
''')

repo='raydium-io/raydium-sdk-V2'
render(repo,'raydium_sdk',f'''El SDK sirve para leer la estructura real de pools Solana y calcular con enteros grandes. Su mejor uso inicial es interpretar cuentas y cotizaciones, con cuidado de distinguir CLMM, CPMM y AMMv4. No se necesita firmar swaps para analizar fundamentales.

## Rutas examinadas

{link(repo,'src/raydium/clmm/layout.ts')} expone layouts con `protocolFeeRate`, `tradeFeeRate`, `fundFeeRate`, acumuladores de fees, rewards y campos de fee dinámica. Se inspeccionaron también rutas de {link(repo,'src/raydium/clmm/clmm.ts')}, {link(repo,'src/raydium/cpmm/cpmm.ts')} y el test {link(repo,'test/cpmmSwapQuote.test.js')}. El {link(repo,'package.json')} declara0.2.81-alpha en el commit observado, y dependencias Solana web3/SPL, BN, decimal.js y axios. Licencia raíz {link(repo,'LICENSE','GPL3')}.

## Arquitectura y precisión

El SDK organiza módulos por producto: cuenta, token, CLMM, CPMM y rutas, entre otros. Los layouts convierten datos binarios de cuentas en campos financieros. Los acumuladores de fees y liquidez deben interpretarse con decimales y escalas de punto fijo; convertir directamente a float puede perder precisión.

Una cuota de reparto documentada no identifica por sí sola los pagos efectivos a tokenholders. Los campos de configuración proporcionan la base técnica para preguntar qué fee se aplicó a qué pool y cuándo. Es necesario unir instrucciones/events, configuración y transferencia final para comprobar buybacks. Las fees de LP no deben atribuirse a RAY.

La ruta antigua de protocol fees devolvió 404. Se localizó y abrió la [ruta canónica actual](https://docs.raydium.io/ray/protocol-fees): documenta reparto LP/buyback/tesorería de 84/12/4 para CLMM y CPMM, y 88/12 para AMM v4. Son porcentajes de la fee, no del volumen. Las escalas de configuración difieren: 10.000 para AMM v4 y 1.000.000 para CLMM/CPMM. Esta es evidencia documental, sin lectura independiente del estado desplegado.

La página de [buybacks](https://docs.raydium.io/ray/ray-buybacks) indica que el RAY recomprado permanece en una dirección del protocolo. Acumulación en esa cuenta no equivale a burn ni a distribución de caja a tenedores. La [comparación de fees](https://docs.raydium.io/reference/fee-comparison) describe configuraciones y cambios de septiembre de 2026, incluidos campos de creator fee. Un monitor debe fijar pool, programa, slot y versión de configuración; los datos agregados no bastan para certificar el destino de cada importe.

## Qué se comprobó en tests

`cpmmSwapQuote.test.js` construye fixtures que sustituyen peticiones de cuenta, reutiliza una cotización y comprueba que construir dos transacciones no muta la cotización ni altera límites. Incluye variantes exact-in/exact-out y financiación máxima de SOL nativo. Es una prueba significativa del contrato de cálculo/construcción, aunque no cubre todo el mercado. Se leyó, no se ejecutó; no hay porcentaje de cobertura medido ni prueba de rentabilidad de LP.

## Riesgos de interpretación

Token2022 puede añadir fees de transferencia; la cantidad enviada, recibida y contabilizada no tiene por qué coincidir. Liquidez concentrada fuera de rango no equivale a profundidad ejecutable. Un evento de swap puede ser una pierna de una ruta más larga; sumar todas las piernas como usuarios nuevos o capital nuevo sobreestima actividad.

Los datos agregados de API y el estado RPC deben guardar timestamps/slots y consistencia. Los porcentajes de crecimiento sin corrección de bots, incentivos y composición de pools no demuestran actividad orgánica. Este SDK no resuelve por sí solo esa identificación causal.

## Adopción y experimento

GPL exige evaluar obligaciones al combinar o distribuir; programas Raydium CLMM/CPMM poseen licencias propias que se comprobaron por separado. Para un análisis privado acotado, estudiar layouts o usar una lectura RPC mínima puede reducir superficie de dependencias. La biblioteca completa aporta comodidad cuando se necesitan varios productos.

Muestra propuesta: cinco pools por tipo, siete días, lecturas de configuración y10 swaps contrastados por pool. Aceptación: importes exactos reconciliados; fees separadas por destino; programa/slot/versiones guardados; sin extrapolar porcentajes globales no verificados. CPU doméstica y pocos GB deberían bastar para esta muestra —estimación—; un archivo completo de Solana requiere infraestructura muy diferente. Valor añadido esperado: detectar crecimiento aparente explicado por mix de pools o cambios de fees.
''')

repo='paradigmxyz/cryo'
render(repo,'cryo',f'''Cryo es una opción especialmente proporcionada para conseguir muestras EVM en Parquet y comprobar una hipótesis, sin levantar una plataforma de indexación. Su README declara estado temprano y advierte que los valores por defecto pueden sobrecargar un RPC de terceros; no debe recomendarse su ejecución ciega.

## Evidencia de arquitectura

Se inspeccionaron {link(repo,'crates/freeze/src/freeze.rs')}, {link(repo,'crates/freeze/src/types/sources.rs')}, {link(repo,'crates/freeze/src/types/schemas.rs')} y {link(repo,'Cargo.toml')}. Licencia dual {link(repo,'LICENSE-MIT','MIT')} o {link(repo,'LICENSE-APACHE','Apache2')}. El workspace declara0.3.2; incluye CLI, freeze, conversión a dataframes y bindings Python.

El motor divide consultas en particiones y tipos de dataset. `freeze` prepara trabajos, comprueba dry run, omite archivos existentes cuando no se permite sobrescribir y produce resumen con completados, errores y omitidos. La colección usa semáforos de chunks y escribe dataframes; esto facilita reanudar, pero saltarse un archivo no verifica que su contenido siga siendo canónico tras una reorg o revisión de la fuente.

El manifest actual usa Alloy y Polars. Parte del README aún describe ethers.rs; esta diferencia es razón para preferir la implementación fijada al explicar arquitectura, sin concluir por ello que todo el README sea inválido.

## Control de datos y límites

`Source` contiene chain_id, RPC, control de concurrencia y campos de rate limiter. El constructor inspeccionado no activa por sí solo todos esos controles; algunos valores son etiquetas descriptivas. Por tanto no se dedujo que un número visible como100 solicitudes concurrentes pruebe limitación efectiva de tráfico en cualquier ruta. Antes de ejecutar habría que revisar el parsing CLI y configuración concreta. Esta revisión no ejecutó Cryo ni verificó tasas reales.

Para `eth_getBlockReceipts` existe fallback a recibos por transacción. Un mismo rango de bloques puede costar muchas más peticiones según las capacidades del RPC. Traces, state diffs y estados históricos requieren proveedores con métodos y retención adecuados. “Open source” no implica RPC archival gratis.

Los esquemas admiten conversiones de U256 y chain_id. Para cantidades monetarias conviene conservar integer/string/binary exacto y aplicar decimales después; float sólo para visualización o estadísticas con tolerancia declarada. Guardar hash de bloque y ventana finalizada es responsabilidad del flujo analítico; Parquet por sí solo no garantiza provenance.

## Pruebas y coste

Se inspeccionó el motor y esquema, pero no un conjunto completo de pruebas de regresión de datasets. No hay resultados de rendimiento propios. El tamaño de muestra manda: extracción de algunos contratos/días probablemente cabe en8–16GB RAM y CPU doméstica, mientras trazas de toda una cadena exigen mucho más. Son estimaciones operativas y deben sustituirse por medición futura autorizada en un entorno aislado.

Ethereum ETL es una alternativa Python simple si CSV basta. Ponder resulta preferible para servicio continuo y rollback de reorg. SQD puede reducir extracción multichain, con dependencia adicional de su red. No hace falta seleccionar una sola tecnología para todos los casos.

## Experimento propuesto

Obtener en el futuro una ventana finalizada pequeña de logs de un contrato y repetirla con otro RPC autorizado. Comparar recuentos, clave `(chain_id,block_hash,tx_hash,log_index)`, cantidades exactas y checksums del resultado. Aceptación: cero huecos sin explicación; fallos visibles en resumen; reanudación idempotente; límites de tráfico respetados; coste por mil bloques registrado. Hipótesis: una muestra bien fijada reduce tiempo de falsar métricas frente a depender sólo del dashboard agregado.
''')

repo='ponder-sh/ponder'
render(repo,'ponder',f'''Ponder merece atención cuando la necesidad ya es seguimiento continuo de pocos contratos EVM. Su tratamiento explícito de reorgs es una capacidad verificable; para un análisis ocasional por lotes, Cryo o una consulta ya disponible suelen ser más ligeros.

## Implementación examinada

Se leyeron rutas de {link(repo,'packages/core/src/sync-realtime/index.ts')} y {link(repo,'packages/core/src/sync-realtime/index.test.ts')}, junto al {link(repo,'packages/core/package.json')}. El {link(repo,'README.md','README')} describe TypeScript, escritura a Postgres y consultas HTTP SQL/GraphQL. Licencia {link(repo,'LICENSE','MIT')}.

El módulo de sincronización conserva una cadena de bloques no finalizados ligada por `parentHash` y emite eventos de bloque, finalización y reorg. La reconciliación busca ancestro común, enumera bloques retirados y revierte direcciones hijas descubiertas por factories. Esto es relevante: una reorg afecta también al universo de contratos a seguir, no sólo a sus transacciones.

Si la reorganización cruza el bloque que el indexador considera finalizado, el código restaura el estado local de trabajo y produce error de reorg no recuperable. No afirma resolver cualquier reorganización. Parte de la finalización depende de una ventana temporal configurable, que debe ser apropiada para la cadena; no equivale por definición a finalización económica absoluta.

## Pruebas concretas y alcance

Los tests seleccionados incluyen emisión de `finalize`, búsqueda de ancestro común, eliminación de direcciones hijas con más de un parent y error ante reorg profundo. Se inspeccionaron nombres, setup y lógica relacionada, no se ejecutaron. No se auditaron todos los módulos de RPC, base de datos, migrations o API expuesta, por lo que no se afirma seguridad integral del servicio.

La utilidad funcional está apoyada por implementación y tests específicos; la fiabilidad operativa sigue pendiente de validar sobre el RPC, red y contratos elegidos. Una interfaz GraphQL bonita no aporta por sí sola mejor evidencia económica.

## Arquitectura mínima sugerida

ABI y lista de contratos fechada→RPC autorizado→Ponder→Postgres→exportación periódica de tablas concretas. Conservar identidad de cadena/contrato/bloque/evento y estado provisional/final. Un snapshot finalizado puede alimentar otra herramienta por Parquet, sin convertir el indexador en la plataforma central de toda la investigación.

Usos: releases de TokenJar, cambios de gobernanza ejecutados y eventos de vesting. No extrapolar dirección a entidad ni transferencia a ingreso. Las llamadas derivadas deben fijar bloque para evitar unir un evento antiguo con configuración actual.

## Costes, riesgos y alternativas

Un servicio Node/Postgres requiere más operación que un notebook. Para una muestra estrecha,8–16GB RAM y CPU doméstica son una estimación inicial razonable; historiales globales pueden superar ampliamente ese presupuesto. No se midió rendimiento ni se contrató RPC. MIT del framework no cubre las condiciones del proveedor, los contratos de terceros o las fuentes de etiquetas.

Comparación: Cryo para una extracción acotada; SQD para selección multichain; Graph Node si existe un subgraph exacto que ya satisface requisitos. Evitar el coste de varios indexadores antes de demostrar falta de cobertura.

## Experimento y aceptación

En una futura prueba aislada autorizada, simular una reorg pequeña y otra que sobrepase la finalización configurada, más un factory que crea una dirección. Exigir rollback de eventos y universo, error explícito en caso profundo, reanudación sin duplicar y conteo reconciliado contra RPC finalizado. Medir tiempo dedicado al mantenimiento frente al ahorro de revisión manual. La propuesta es un diseño de prueba; ninguna simulación de terceros fue ejecutada aquí.
''')

repo='graphsense/graphsense-lib'
render(repo,'graphsense',f'''La oportunidad menos obvia es reutilizar el esquema de atribución y sus controles, no desplegar toda la plataforma forense. Una etiqueta con fuente, confianza y fecha mejora el análisis de capital mucho más que llamar “smart money” a una lista de wallets sin provenance.

## Migración y rutas inspeccionadas

El repositorio histórico [graphsense-tagpack-tool](https://github.com/graphsense/graphsense-tagpack-tool) declara migración y archivo. El código actual examinado está en GraphSense lib: {link(repo,'src/graphsenselib/tagpack/confidence.py')}, {link(repo,'src/graphsenselib/tagpack/tagpack_schema.py')}, {link(repo,'src/graphsenselib/tagpack/schema.py')} y {link(repo,'src/graphsenselib/tagpack/conf/tagpack_schema.yaml')}. Se revisaron además {link(repo,'tests/tagpack/test_tagpack_schema.py')} y {link(repo,'tests/tagpack/test_cluster_staleness.py')}. Licencia {link(repo,'LICENSE','MIT')}.

## Modelo de información

El esquema exige campos de fuente, moneda, red, etiqueta y confianza; contempla actor, dirección, tx_hash, contexto, clasificación, fecha y marcadores de clusters. La clase de confianza carga categorías definidas localmente; su `level` no es una probabilidad calibrada de identidad. Una interfaz debe mostrar la categoría y fundamento, sin convertirla artificialmente en porcentaje de certeza.

El validador usa tipos, campos obligatorios y taxonomías. La existencia de una fuente no demuestra que la atribución sea cierta, pero permite revisarla. `lastmod` opcional no resuelve por sí solo historial bitemporal: una herramienta de investigación necesita añadir cuándo se conoció la atribución y para qué periodo era válida.

Los [TagPacks públicos](https://github.com/graphsense/graphsense-tagpacks) requieren origen público y enlaces de respaldo. La licencia del contenedor no prueba todos los derechos de las fuentes originales ni su actualidad. La revisión debe dar prioridad a direcciones de protocolos/tesorerías verificables, evitando inferencias personales innecesarias.

## Pruebas y límites

Los tests de esquema comprueban propiedades y campos obligatorios. El test de stale mappings crea un TagStore y backend falsos para contrastar asignaciones de clusters guardadas con las actuales. Es un mecanismo interesante: una etiqueta no debería seguir vinculada silenciosamente a un cluster que cambió al actualizar el análisis. Se leyó código de prueba; no se ejecutó ni se auditó la totalidad del motor de clustering.

Dirección, cuenta, cluster y entidad deben permanecer separados. En UTXO, heurísticas de co-input pueden fallar con CoinJoin; en EVM, contratos, routers, multisigs y smart wallets añaden relaciones diferentes. Un grafo bonito puede hacer que una atribución débil parezca demostrada. La salida correcta puede ser un intervalo de flujo atribuible, no una cifra puntual.

## Proporcionalidad y coste

El README del servicio completo describe Cassandra para blockchain y Postgres para TagStore. Es mucho para una primera herramienta personal. Extraer el patrón de esquema —o usar una pequeña parte compatible del código— permite un CSV/JSON versionado con20–100 direcciones de interés, fuentes y revisión humana. CPU ordinaria sin GPU basta para ese diccionario; el coste de plataforma completa no se extrapola a esta pieza.

Alternativa: tabla manual de entidades y direcciones con reglas explícitas; BlockSci queda como referencia académica porque su README dice que no se mantiene activamente desde2020. No usar un fork con actividad como sustituto automático sin examinar cambios sustanciales.

## Experimento propuesto

Anotar30 direcciones públicas de tesorerías/protocolos, cada una con evidencia y nivel, y revisar10 atribuciones con una segunda fuente. Calcular flujo bajo tres supuestos: sólo confirmadas, confirmadas+probables y todas. Aceptación:100% de etiquetas trazables, conflicto explícito sin sobrescritura y diferencia entre escenarios visible. Hipótesis de valor: descartar narrativas de acumulación que dependen de una atribución frágil. No se realizó identificación de personas privadas.
''')

repo='bmoscon/cryptofeed'
render(repo,'cryptofeed',f'''Cryptofeed aporta feeds normalizados cuando se necesita más granularidad que una consulta periódica. La inspección detecta dos cuestiones que cambian la adopción: semántica de liquidaciones y licencia actual AGPL con atribución adicional. No debe recomendarse por memoria como si conservara una licencia permisiva histórica.

## Evidencia de código

Se inspeccionaron {link(repo,'cryptofeed/exchanges/binance.py')}, {link(repo,'cryptofeed/exchanges/bybit.py')}, {link(repo,'tests/unit/test_bybit_liquidations.py')}, {link(repo,'tests/unit/test_binance_depth_stream.py')} y {link(repo,'pyproject.toml')}. La {link(repo,'LICENSE','licencia')} dice AGPL3 o posterior y exige preservar/display una atribución del autor en los lugares indicados. Código cliente, derechos de datos y términos del exchange son capas distintas.

## Flujo y campos críticos

Los conectores parsean mensajes y emiten callbacks de trades, libros, funding, OI o liquidaciones. Binance construye libro desde snapshot con `lastUpdateId` y actualizaciones; expone números de secuencia. La secuencia permite detectar inconsistencias, pero una revisión del parser no acredita recuperación correcta ante todos los huecos.

Bybit usa `allLiquidation` y recibe una lista de entradas. El campo `S` describe lado de la posición liquidada; el callback normalizado usa lado de la orden de liquidación. El test examinado exige invertir Buy→SELL y Sell→BUY. Una herramienta que compare ambos campos sin esa traducción interpretaría una cascada al revés.

La cantidad y precio de una liquidación también requieren semántica: contrato lineal/inverso, multiplicador, tamaño ejecutado y precio de bancarrota no son intercambiables. La evidencia observada sólo demuestra parser y pruebas para casos concretos. El feed publicado por un exchange puede ser parcial o muestreado; el SDK no puede recuperar un evento que el servidor no envía.

## Real, inferido e incompleto

Separar tres tablas: eventos de liquidación reportados, estimaciones de vulnerabilidad derivadas de estados y grandes trades sin etiqueta de liquidación. Nunca promover el tercero a liquidación por superar un umbral de tamaño. Guardar proveedor, instrumento, timestamp de evento, recepción y método de observación permite interpretar cambios de volumen durante caídas de conexión.

El proyecto [HyperData Terminal](https://github.com/Co-Messi/HyperData-Terminal/blob/5fd1f0264391de1b65b18014049ea61161d82d51/docs/DATA_INTEGRITY.md), revisado sólo documentalmente, ofrece una referencia adicional de UX: muestra cobertura y estados parcial/stale, y reconoce que ciertos conteos son muestras. Sus afirmaciones no fueron adoptadas como benchmarks independientes ni su código crítico se auditó aquí.

## Pruebas y coste

Los tests seleccionados aíslan mensajes de Bybit y nombres de streams de profundidad Binance. No se ejecutaron, ni acreditan exactitud de todos los exchanges soportados. No se midió latencia, pérdida de mensajes, reconexión o almacenamiento.

Para3–18 meses, conservar libro completo continuamente puede añadir más coste que valor. Empezar con3 activos y métricas horarias de cobertura/estrés reduce volumen. CPU doméstica debería bastar para una muestra reducida; mantener muchos libros requiere medición. Históricos adquiridos fuera del cliente pueden implicar suscripción; no se contrató ninguna.

## Decisión experimental

Comparar14 días de métricas de estrés obtenidas por snapshots CCXT con una captura limitada por Cryptofeed. Exigir conversión exacta de tamaños, lado de liquidación coherente y propagación de eventos faltantes/estados stale. Si la granularidad no cambia decisiones de investigación o no reduce falsos positivos, conservar la opción sencilla. Antes de reutilización distribuida o servicio accesible por red, revisar AGPL y atribución contra el diseño concreto; no emitir una conclusión jurídica basada sólo en que el uso inicial sea personal.
''')
print('Written',len(list(OUT.glob('crypto_*.md'))),'reviews')
