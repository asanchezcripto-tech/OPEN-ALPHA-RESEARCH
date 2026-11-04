# OpenBB/OpenBQ: transición real en 2026 y pérdida de vintages en una ruta concreta

Candidato `quant-openbb` · observación 2026-11-04 · nivel V3 (estático). Commit `2a392e890f6eb1f0f4e3a71742720af8f056333a`.

La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.

## Capacidad y alcance

Fetcher define etapas transform_query, extract/aextract_data y transform_data, además de una ruta de streaming. El proveedor FRED implementa consultas y transporte específicos; no existe una licencia universal para los datos que circulan por el framework.

**Entradas:** Consulta tipada, identificadores de series, fechas y credenciales del proveedor cuando se exijan.

**Salidas:** Objetos normalizados con datos y metadata para terminales, APIs o análisis.

## Evidencia técnica y límites

En models/series.py se llama a series/observations y series para valores y metadata; se usa fred_get con caché/rate limiter. Antes de formar la serie se eliminan realtime_start y realtime_end, se convierten valores a float y se descartan faltantes. Esta ruta concreta devuelve una serie útil para lectura actual pero destruye columnas necesarias para auditar vintages; otras rutas FRED no se juzgan aquí. Tests del proveedor están presentes y sus casos fueron inspeccionados.

La publicación oficial del 1-oct-2026 sitúa la continuidad en OpenBQ. La release v5 del 30-sep anuncia Apache-2.0 y eliminación de proveedores; el LICENSE actual confirma Apache. No combinar instrucciones de v4/AGPL y capacidades de v5. Guardar respuestas brutas de proveedor fuera de transformaciones que eliminen fechas de revisión.

## Adopción proporcional

Puede ahorrar conectores cuando se usan varias fuentes. Para solo ALFRED, un cliente mínimo que preserve vintages es más claro. La continuidad institucional y compatibilidad de extensiones son riesgos a revisar tras el traspaso; actividad de repositorio no demuestra que todos los endpoints funcionen.

**Dependencias observadas:** openbb-core, extensiones por proveedor, Pydantic, pandas, diskcache, lxml; Python>=3.11 en proveedor FRED.

CPU y 8–16 GB RAM estimados para consultas pequeñas; costes variables de proveedores, sin tarifas verificadas. No se probaron endpoints con clave ni el escritorio. El proveedor FRED pyproject declara 2.0.0 y Python>=3.11.

**Licencia del código:** Apache-2.0. Clasificación: REUTILIZACIÓN POTENCIALMENTE COMPATIBLE. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.

## Experimento de aceptación propuesto, no ejecutado

Comparar respuesta original FRED con objeto normalizado para una serie revisada, con un dato faltante y dos vintages. Exigir preservación de campos en el almacén propio y documentar qué transformación pierde información. Probar tres endpoints gratuitos antes de elegirlo como base de una herramienta.

## Veredicto

Investigar más/adoptar conectores seleccionados con versionado. Apache-2.0 del código actual no cubre cada proveedor. Evitar una dependencia global del terminal cuando bastan dos clientes ligeros.

Puntuación editorial 79/100: utilidad 22/25; evidencia 13/15; datos 11/15; facilidad 7/12; licencia 10/10; mantenimiento 4/8; uso diario 8/8; diferenciación 4/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.

## Fuentes exactas

- [openbb_platform/core/openbb_core/provider/abstract/fetcher.py](https://github.com/openbq-org/OpenBB/blob/2a392e890f6eb1f0f4e3a71742720af8f056333a/openbb_platform/core/openbb_core/provider/abstract/fetcher.py)
- [openbb_platform/providers/fred/openbb_fred/models/series.py](https://github.com/openbq-org/OpenBB/blob/2a392e890f6eb1f0f4e3a71742720af8f056333a/openbb_platform/providers/fred/openbb_fred/models/series.py)
- [openbb_platform/providers/fred/tests/test_fred_fetchers.py](https://github.com/openbq-org/OpenBB/blob/2a392e890f6eb1f0f4e3a71742720af8f056333a/openbb_platform/providers/fred/tests/test_fred_fetchers.py)
- [openbb_platform/providers/fred/pyproject.toml](https://github.com/openbq-org/OpenBB/blob/2a392e890f6eb1f0f4e3a71742720af8f056333a/openbb_platform/providers/fred/pyproject.toml)
- [LICENSE](https://github.com/openbq-org/OpenBB/blob/2a392e890f6eb1f0f4e3a71742720af8f056333a/LICENSE)
- [Anuncio oficial de continuidad en OpenBQ](https://openbb.co/)
- [Release v5 y cambio de licencia](https://github.com/openbq-org/OpenBB/releases)
