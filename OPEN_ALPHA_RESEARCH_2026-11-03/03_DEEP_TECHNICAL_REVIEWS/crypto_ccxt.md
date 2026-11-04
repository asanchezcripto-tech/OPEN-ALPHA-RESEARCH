# CCXT — revisión técnica estática

Observado: 2026-11-04. Referencia del mandato: 2026-11-03. Commit examinado: `28d9b2ca6e06173ce00f020cfd5bfac3275604d4`. La fecha de este commit no se obtuvo; la instantánea observada el día 4 no se presenta como reconstrucción certificada del día 3. Nivel V3: inspección de rutas concretas; no se ejecutó, instaló ni importó software externo.

CCXT aporta normalización reutilizable; el error sería confundir nombres de campos uniformes con equivalencia económica entre exchanges. Es una buena primera biblioteca para frecuencia diaria u horaria, siempre acompañada por metadatos y payload original.

## Evidencia y arquitectura

Se inspeccionaron [python/ccxt/base/exchange.py](https://github.com/ccxt/ccxt/blob/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/python/ccxt/base/exchange.py), rutas concretas de [python/ccxt/binance.py](https://github.com/ccxt/ccxt/blob/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/python/ccxt/binance.py), [python/ccxt/test/base/test_parse_precision.py](https://github.com/ccxt/ccxt/blob/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/python/ccxt/test/base/test_parse_precision.py) y [package.json](https://github.com/ccxt/ccxt/blob/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/package.json). El manifest registra4.5.91 en la instantánea observada. Licencia [MIT](https://github.com/ccxt/ccxt/blob/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/LICENSE.txt). La amplitud del repo no se auditó: la revisión técnica se concentra en OHLCV, funding, identidad contractual y open interest de Binance.

La clase base proporciona interfaz y utilidades; cada exchange implementa métodos específicos y parsing. `fetch_ohlcv` deriva su endpoint de producto/mercado. Los símbolos contractuales incluyen activo de liquidación y metadatos `linear`, `inverse`, `contractSize`; `info` preserva respuesta original en muchas estructuras.

En Binance, el parser de funding toma por separado `lastFundingRate`, `nextFundingTime` y, cuando está disponible en la respuesta correspondiente, `fundingIntervalHours`. El intervalo puede quedar vacío; no es correcto multiplicar toda tasa por 3×365 suponiendo ocho horas. La señal que se usa debe declarar si representa último pago, estimación próxima o promedio histórico.

El parser de open interest distingue instrumentos inversos y deja `baseVolume` sin valor para esos casos. `openInterestAmount` puede ser contratos, mientras que valores en moneda base o dólares requieren conversiones distintas. La normalización conserva información útil, pero no elimina la necesidad de comprobar denominadores.

## Control temporal y pruebas

`fetch_funding_rate_history` expone `since` en milisegundos y paginación opcional. La disponibilidad de historia depende del endpoint; solicitar una ventana no prueba que se recibió completa. La última vela puede estar abierta; universo actual excluye delistings. Guardar `instrument_id`, mercado, ventana cerrada, event_time, acquisition_time y respuesta raw evita buena parte de errores evitables.

El test de precisión examinado valida conversiones de precisión; **no constituye un test del histórico de funding ni del open interest**. Una ruta de test adicional buscada para funding no fue accesible con el nombre supuesto y se registró el fallo. No se ejecutaron tests, llamadas de mercado ni benchmarks de latencia.

## Encaje, coste y alternativa

Una lectura diaria de 20 activos en 2–3 venues es proporcionada a CPU doméstica y almacenamiento columnar pequeño; es una estimación de diseño. Cada exchange impone cuotas, condiciones y retención. La licencia MIT del cliente no cubre la comercialización de datos. La amplitud del paquete también exige pinning y revisión de dependencias antes de cualquier ejecución futura.

Cryptofeed sería preferible si la pregunta requiere mensajes WebSocket y reconstrucción de libro. Pybit o conectores oficiales de Binance son útiles cuando CCXT no expone un campo o una actualización concreta. No construir un wrapper universal adicional antes de conocer esa necesidad.

## Experimento mínimo

Elegir BTC spot, BTC perp lineal y un contrato inverso; cotejar30 puntos horarios contra datos originales. Criterios: conversiones de notional trazables; funding con intervalo explícito o abstención; velas incompletas apartadas; detección de huecos y delistings; mismos resultados al reejecutar sobre snapshots fijados. La comparación debe medir errores de normalización y tiempo de mantenimiento, no rentabilidad de una estrategia inventada.


## Decisión y puntuación

Comparar fuerza relativa y estrés entre venues. Adoptar biblioteca. Puntuación editorial: **83/100**; utility 24, evidence 13, data 11, ease 10, license 10, maintenance 5, usability 6, differentiation 4. Los puntos expresan encaje para este inversor y fuerza de la evidencia estática, no fiabilidad absoluta ni rentabilidad.

Condiciones pendientes: validación operacional y permisos de datos; las obligaciones de licencia dependen del modo de integración y distribución.
