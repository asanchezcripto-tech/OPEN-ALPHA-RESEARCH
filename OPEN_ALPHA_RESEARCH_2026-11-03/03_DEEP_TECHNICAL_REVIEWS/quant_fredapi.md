# fredapi + ALFRED: distinguir todas las vintages de la última conocida

Candidato `quant-fredapi` · observación 2026-11-04 · nivel V3 (estático). Commit `d0a0ba3001ebbbceafdcbdd3eb23828f0537cdff`.

La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.

## Capacidad y alcance

Cliente pequeño con transporte XML y conversión pandas. get_series_all_releases recupera vintages; get_series_first_release agrupa por periodo y toma la primera fila. Se pueden mantener datos de observación y conocimiento por separado sin instalar un terminal financiero completo.

**Entradas:** Identificador FRED, fecha de consulta, rango temporal y clave pública de desarrollador emitida por el proveedor.

**Salidas:** Series actuales o filas con date, realtime_start y value para publicaciones y revisiones.

## Evidencia técnica y límites

get_series_as_of_date convierte la fecha y filtra realtime_start<=as_of_date, pero retorna ese DataFrame completo: puede contener varias revisiones para el mismo periodo, pese a que el docstring describe último dato conocido. El consumidor debe ordenar por fecha de conocimiento y seleccionar última fila por date, sin eliminar el historial original. Los tests leídos usan urlopen simulado y validan consultas/errores, no se ejecutaron.

ALFRED incorpora revisiones tras su publicación y puede utilizar primera disponibilidad en FRED si no se conoce la fecha original. Su granularidad de fecha no garantiza el instante intradía de llegada al mercado. Un análisis diario debe aplicar una convención conservadora y guardar acquired_at propio. Primera revisión de un periodo no equivale al último dato conocido en una fecha posterior.

## Adopción proporcional

Pequeño, legible y útil para Market Regime Navigator. Requiere lógica de normalización propia y vigilancia del API; ni Apache ni la disponibilidad de un endpoint autorizan redistribuir todas las series de terceros. API FRED requiere clave; este mandato no la solicitó ni realizó descargas autenticadas.

**Dependencias observadas:** pandas, urllib/XML de biblioteca estándar.

CPU y 4–8 GB RAM para decenas de series macro, estimación editorial. Coste operativo relativo bajo, sin precio externo contratado. No GPU. Los metadatos de setup.py contienen clasificadores antiguos; no son evidencia de mantenimiento reciente ni de compatibilidad de versiones.

**Licencia del código:** Apache-2.0. Clasificación: REUTILIZACIÓN POTENCIALMENTE COMPATIBLE. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.

## Experimento de aceptación propuesto, no ejecutado

Fixture manual de un trimestre con tres publicaciones. Exigir tres vistas diferentes: first-release, todas las vintages antes de t y última vintage por periodo a t. La tercera debe cambiar solo cuando cruza una fecha de disponibilidad, y conservar la fuente/versionado.

## Veredicto

Adoptar biblioteca ligera con wrapper de semántica temporal, o llamar directamente a API oficial. Apache-2.0 del código revisada; derechos por serie pendientes. Esta comprobación de cinco líneas tiene más valor para evitar sesgo que añadir un modelo predictivo complejo.

Puntuación editorial 85/100: utilidad 24/25; evidencia 12/15; datos 13/15; facilidad 11/12; licencia 10/10; mantenimiento 3/8; uso diario 7/8; diferenciación 5/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.

## Fuentes exactas

- [fredapi/fred.py](https://github.com/mortada/fredapi/blob/d0a0ba3001ebbbceafdcbdd3eb23828f0537cdff/fredapi/fred.py)
- [fredapi/tests/test_fred.py](https://github.com/mortada/fredapi/blob/d0a0ba3001ebbbceafdcbdd3eb23828f0537cdff/fredapi/tests/test_fred.py)
- [setup.py](https://github.com/mortada/fredapi/blob/d0a0ba3001ebbbceafdcbdd3eb23828f0537cdff/setup.py)
- [LICENSE](https://github.com/mortada/fredapi/blob/d0a0ba3001ebbbceafdcbdd3eb23828f0537cdff/LICENSE)
- [ALFRED: ayuda y determinación de vintages](https://alfred.stlouisfed.org/help)
- [API: observaciones y parámetros realtime](https://fred.stlouisfed.org/docs/api/fred/series_observations.html)
