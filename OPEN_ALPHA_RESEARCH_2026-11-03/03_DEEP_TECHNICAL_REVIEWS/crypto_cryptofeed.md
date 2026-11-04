# Cryptofeed — revisión técnica estática

Observado: 2026-11-04. Referencia del mandato: 2026-11-03. Commit examinado: `3128a3bed0c06812751b528d35f89debb22a5202`. La fecha de este commit no se obtuvo; la instantánea observada el día 4 no se presenta como reconstrucción certificada del día 3. Nivel V3: inspección de rutas concretas; no se ejecutó, instaló ni importó software externo.

Cryptofeed aporta feeds normalizados cuando se necesita más granularidad que una consulta periódica. La inspección detecta dos cuestiones que cambian la adopción: semántica de liquidaciones y licencia actual AGPL con atribución adicional. No debe recomendarse por memoria como si conservara una licencia permisiva histórica.

## Evidencia de código

Se inspeccionaron [cryptofeed/exchanges/binance.py](https://github.com/bmoscon/cryptofeed/blob/3128a3bed0c06812751b528d35f89debb22a5202/cryptofeed/exchanges/binance.py), [cryptofeed/exchanges/bybit.py](https://github.com/bmoscon/cryptofeed/blob/3128a3bed0c06812751b528d35f89debb22a5202/cryptofeed/exchanges/bybit.py), [tests/unit/test_bybit_liquidations.py](https://github.com/bmoscon/cryptofeed/blob/3128a3bed0c06812751b528d35f89debb22a5202/tests/unit/test_bybit_liquidations.py), [tests/unit/test_binance_depth_stream.py](https://github.com/bmoscon/cryptofeed/blob/3128a3bed0c06812751b528d35f89debb22a5202/tests/unit/test_binance_depth_stream.py) y [pyproject.toml](https://github.com/bmoscon/cryptofeed/blob/3128a3bed0c06812751b528d35f89debb22a5202/pyproject.toml). La [licencia](https://github.com/bmoscon/cryptofeed/blob/3128a3bed0c06812751b528d35f89debb22a5202/LICENSE) dice AGPL3 o posterior y exige preservar/display una atribución del autor en los lugares indicados. Código cliente, derechos de datos y términos del exchange son capas distintas.

## Flujo y campos críticos

Los conectores parsean mensajes y emiten callbacks de trades, libros, funding, OI o liquidaciones. Binance construye libro desde snapshot con `lastUpdateId` y actualizaciones; expone números de secuencia. La secuencia permite detectar inconsistencias, pero una revisión del parser no acredita recuperación correcta ante todos los huecos.

Bybit usa `allLiquidation` y recibe una lista de entradas. El campo `S` describe lado de la posición liquidada; el callback normalizado usa lado de la orden de liquidación. El test examinado exige invertir Buy→SELL y Sell→BUY. Una herramienta que compare ambos campos sin esa traducción interpretaría una cascada al revés.

La cantidad y precio de una liquidación también requieren semántica: contrato lineal/inverso, multiplicador, tamaño ejecutado y precio de bancarrota no son intercambiables. La evidencia observada sólo demuestra parser y pruebas para casos concretos. El feed publicado por un exchange puede ser parcial o muestreado; el SDK no puede recuperar un evento que el servidor no envía.

## Real, inferido e incompleto

Separar tres tablas: eventos de liquidación reportados, estimaciones de vulnerabilidad derivadas de estados y grandes trades sin etiqueta de liquidación. Nunca promover el tercero a liquidación por superar un umbral de tamaño. Guardar proveedor, instrumento, timestamp de evento, recepción y método de observación permite interpretar cambios de volumen durante caídas de conexión.

El proyecto [HyperData Terminal](https://github.com/Co-Messi/HyperData-Terminal/blob/5fd1f0264391de1b65b18014049ea61161d82d51/docs/DATA_INTEGRITY.md), revisado sólo documentalmente, ofrece una referencia adicional de UX: muestra cobertura y estados parcial/stale, y reconoce que ciertos conteos son muestras. Sus afirmaciones no fueron adoptadas como benchmarks independientes ni su código crítico se auditó aquí.

## Pruebas y coste

Los tests seleccionados aíslan mensajes de Bybit y nombres de streams de profundidad Binance. No se ejecutaron, ni acreditan exactitud de todos los exchanges soportados. No se midió latencia, pérdida de mensajes, reconexión o almacenamiento.

Para3–18 meses, conservar libro completo continuamente puede añadir más coste que valor. Empezar con 3 activos y métricas horarias de cobertura/estrés reduce volumen. CPU doméstica debería bastar para una muestra reducida; mantener muchos libros requiere medición. Históricos adquiridos fuera del cliente pueden implicar suscripción; no se contrató ninguna.

## Decisión experimental

Comparar14 días de métricas de estrés obtenidas por snapshots CCXT con una captura limitada por Cryptofeed. Exigir conversión exacta de tamaños, lado de liquidación coherente y propagación de eventos faltantes/estados stale. Si la granularidad no cambia decisiones de investigación o no reduce falsos positivos, conservar la opción sencilla. Antes de reutilización distribuida o servicio accesible por red, revisar AGPL y atribución contra el diseño concreto; no emitir una conclusión jurídica basada sólo en que el uso inicial sea personal.


## Decisión y puntuación

Monitor granular de estrés con cobertura explícita. Adoptar biblioteca. Puntuación editorial: **68/100**; utility 19, evidence 12, data 10, ease 7, license 6, maintenance 4, usability 5, differentiation 5. Los puntos expresan encaje para este inversor y fuerza de la evidencia estática, no fiabilidad absoluta ni rentabilidad.

Condiciones pendientes: validación operacional y permisos de datos; las obligaciones de licencia dependen del modo de integración y distribución.
