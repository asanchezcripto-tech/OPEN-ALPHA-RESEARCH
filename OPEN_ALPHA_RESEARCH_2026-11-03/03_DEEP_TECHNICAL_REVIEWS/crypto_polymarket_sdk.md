# Polymarket unified Python SDK — revisión técnica estática

Observado: 2026-11-04. Referencia del mandato: 2026-11-03. Commit examinado: `aa94ec431e3d4946576fb7c0d079fe1c14fcf676`. La fecha de este commit no se obtuvo; la instantánea observada el día 4 no se presenta como reconstrucción certificada del día 3. Nivel V3: inspección de rutas concretas; no se ejecutó, instaló ni importó software externo.

La conclusión más útil es de compatibilidad: el sucesor de `py-clob-client` ya no es simplemente `py-clob-client-v2`. Los READMEs oficiales de ambos remiten al SDK unificado. La [release v1.2.1 de V2](https://github.com/Polymarket/py-clob-client-v2/releases/tag/v1.2.1) publica la deprecación. Para investigación personal conviene empezar por `PublicClient` y no por los ejemplos de firma/órdenes.

## Evidencia inspeccionada

| Archivo | Alcance |
|---|---|
| [src/polymarket/clients/public.py](https://github.com/Polymarket/py-sdk/blob/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/src/polymarket/clients/public.py) | Métodos públicos, referencias de activos, mercado y precios. |
| [src/polymarket/clients/_transport.py](https://github.com/Polymarket/py-sdk/blob/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/src/polymarket/clients/_transport.py) | Errores HTTP, rate limits y análisis de Retry-After. |
| [src/polymarket/pagination.py](https://github.com/Polymarket/py-sdk/blob/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/src/polymarket/pagination.py) | Página, cursores, truncamiento y conversión a dataframes. |
| [tests/unit/test_date_field_contract.py](https://github.com/Polymarket/py-sdk/blob/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/tests/unit/test_date_field_contract.py) | Contrato de fechas y casos inválidos. |
| [tests/unit/test_public_calls_surface.py](https://github.com/Polymarket/py-sdk/blob/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/tests/unit/test_public_calls_surface.py) | Superficie de llamadas públicas. |
| [tests/unit/test_data_retry.py](https://github.com/Polymarket/py-sdk/blob/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/tests/unit/test_data_retry.py) | Casos de reintentos de datos. |

El [pyproject.toml](https://github.com/Polymarket/py-sdk/blob/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/pyproject.toml) declara `polymarket-client`0.16.0 en el commit observado y Python>=3.11. Es una versión de manifest, no una afirmación de que esa sea la última release publicada. Se comprobaron `httpx`, Pydantic, websockets y extras opcionales Arrow/pandas/Polars. Licencia [MIT](https://github.com/Polymarket/py-sdk/blob/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/LICENSE).

## Diseño y capacidades transferibles

La API pública separa acciones de transporte y parsing. Devuelve objetos del SDK y utiliza `Decimal` para precios monetarios concretos. Se puede consultar el mercado por identificador, slug o URL. Las peticiones de referencias de activos validan selectores y explicitan metadatos nulos; algunas observaciones pueden ir retrasadas.

La clase `Page` diferencia `has_more`, `next_cursor` y `limit_reached`: alcanzar un tope de profundidad impide comprobar otra página, pero no demuestra que existan más registros. La conversión a pandas conserva banderas de truncamiento. Esta es una técnica aprovechable por cualquier laboratorio: una tabla grande no debe presentarse como exhaustiva sin señal de cobertura.

El transporte interpreta `Retry-After` numérico y como fecha HTTP, y expone errores tipados. Esa implementación no autoriza a ignorar límites ni garantiza que cualquier endpoint se reintente de la misma manera. Se inspeccionaron tests de fechas, llamadas y retry; no se ejecutaron ni se dedujo cobertura porcentual.

## Valor financiero y límites

Polymarket puede aportar escenarios y fechas de resolución a un Thesis Tracker, pero el precio refleja también spread, liquidez, costes, diseño de contrato y participantes. Dos mercados con títulos parecidos pueden resolver con criterios distintos. El análisis debe guardar texto de resolución y versión observada, no sólo ticker y probabilidad.

Un backtest de acontecimientos necesita mercados cerrados y fallidos, no sólo los listados hoy; conservar actualizaciones de resolución evita conocer retrospectivamente información no disponible. Los volúmenes y posiciones no dan automáticamente una medida de convicción independiente: una entidad puede operar muchos mercados y wallets.

## Coste, alternativa y experimento

Para una cesta curada de 20 mercados, CPU y unos pocos GB de RAM deberían bastar —estimación, no medición—. El coste principal sería mantenimiento del contrato de API y adquisición prospectiva. No se descargaron históricos completos ni se verificaron derechos de redistribución; éstos son distintos de la licencia MIT.

Comparar durante cuatro semanas SDK público frente a HTTP directo en 10 mercados: 100% de fechas UTC y unidades explícitas; ninguna fila truncada silenciosamente; todas las resoluciones vinculadas a su regla; estados inválidos generan abstención. Medir tiempo de revisión y número de contradicciones detectadas frente a leer manualmente las páginas. Evitar perps, wallets, órdenes y relayer en este primer uso: añaden funciones ajenas al objetivo autorizado.


## Decisión y puntuación

Incorporar mercados predictivos como evidencia contextual. Adoptar biblioteca. Puntuación editorial: **80/100**; utility 20, evidence 13, data 10, ease 10, license 10, maintenance 5, usability 6, differentiation 6. Los puntos expresan encaje para este inversor y fuerza de la evidencia estática, no fiabilidad absoluta ni rentabilidad.

Condiciones pendientes: validación operacional y permisos de datos; las obligaciones de licencia dependen del modo de integración y distribución.
