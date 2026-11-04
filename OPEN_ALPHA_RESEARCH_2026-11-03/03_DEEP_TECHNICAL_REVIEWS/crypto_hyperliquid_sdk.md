# Hyperliquid Python SDK — revisión técnica estática

Observado: 2026-11-04. Referencia del mandato: 2026-11-03. Commit examinado: `2fdb18f9517675ea03695a0962bd19eece9c83f0`. La fecha de este commit no se obtuvo; la instantánea observada el día 4 no se presenta como reconstrucción certificada del día 3. Nivel V3: inspección de rutas concretas; no se ejecutó, instaló ni importó software externo.

Es una pieza proporcionada para investigar HYPE, BTC y ETH con lecturas públicas. Su utilidad diferencial es exponer posición, funding y estructura de mercado con semántica del protocolo; no proporciona por sí solo un archivo histórico completo ni identifica entidades económicas.

## Rutas críticas

Se inspeccionaron [hyperliquid/info.py](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/hyperliquid/info.py), [hyperliquid/websocket_manager.py](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/hyperliquid/websocket_manager.py), [tests/info_test.py](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/tests/info_test.py) y [pyproject.toml](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/pyproject.toml). El manifest examinado declara versión 0.24.0 y Python compatible con 3.9 +, con `requests`, `websocket-client`, `msgpack`, `eth-account` y `eth-utils`. La [licencia MIT](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/LICENSE.md) cubre el repositorio examinado; no se extendió a datos ni binarios del nodo.

## Arquitectura y datos

La clase `Info` encapsula llamadas a `/info`. `user_state` pide `clearinghouseState`; `funding_history` usa milisegundos; `l2_snapshot` y `candles_snapshot` construyen peticiones por instrumento. Los estados monetarios llegan frecuentemente como cadenas y varios retornos se tipan `Any`: debe añadirse validación local de unidades, campos faltantes y números exactos.

`Info` inicia un gestor WebSocket por defecto. Para un proceso diario de lectura REST resulta relevante `skip_ws=True`; evita iniciar un hilo que la tarea no necesita. El gestor envía pings y despacha mensajes a suscripciones. No se verificó que cubra todos los casos de reconexión ni que reconstruya huecos después de una caída.

La [documentación del endpoint Info](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint) distingue identificadores spot/perp, remapeos y paginación de consultas temporales. El wrapper de funding inspeccionado realiza una petición; el consumidor debe demostrar completitud de las páginas. El conjunto de wallets que consulta un usuario sigue siendo una muestra: estado público de una cuenta no equivale al censo de participantes.

## Qué prueba la evidencia

`tests/info_test.py` usa cassettes VCR para user state, fills, funding, libro y velas; comprueba ciertos campos, tipos y recuentos. Esto respalda la existencia de un contrato de respuesta y ejemplos reproducibles del SDK. No se ejecutaron tests, no se midió cobertura, y fixtures antiguos no garantizan compatibilidad de la API actual.

Los precios de liquidación de cuentas son estados contingentes: depósitos, retiradas, posiciones correlacionadas y cambios de margen los desplazan. Un mapa de precios posibles debe separarse de fills confirmados. Para interpretación fundamental, la [página oficial de fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees) documenta asistencia a HYPE y quema; demostrar importes históricos exige reconciliación adicional, no sólo repetir esa descripción.

## Uso proporcional y costes

Flujo mínimo propuesto: tres activos→snapshot de metadatos/OI/funding→validación→tabla diaria con cambios y cobertura. Un portátil CPU sin GPU es suficiente como hipótesis para unas pocas peticiones; el espacio depende de conservar payloads. No se midió consumo. El nodo completo es otra categoría: el README de [hyperliquid-dex/node](https://github.com/hyperliquid-dex/node) prescribe 128 GB RAM y grandes volúmenes de logs; queda fuera de la primera capacidad útil.

Alternativas: HTTP directo si se requieren pocos campos; CCXT si interesa normalizar varios exchanges. El SDK oficial es preferible cuando los campos Hyperliquid son la pregunta de investigación; CCXT evita duplicar parsers de mercado general.

## Experimento y aceptación

Registrar prospectivamente14 días para BTC/ETH/HYPE y verificar una muestra manual de snapshots. Criterios: identidad de activo y DEX explícita; funding con intervalo conocido; datos fuera de plazo visibles; páginas sin huecos detectables; cambios de universo versionados. Comparar señal de estrés con un baseline de volatilidad realizada, sin afirmar causalidad ni previsión de precios. No se accedió a cuentas privadas ni se crearon órdenes.


## Decisión y puntuación

Monitor de estrés de lectura pública. Adoptar biblioteca. Puntuación editorial: **87/100**; utility 24, evidence 13, data 12, ease 10, license 10, maintenance 5, usability 7, differentiation 6. Los puntos expresan encaje para este inversor y fuerza de la evidencia estática, no fiabilidad absoluta ni rentabilidad.

Condiciones pendientes: validación operacional y permisos de datos; las obligaciones de licencia dependen del modo de integración y distribución.
