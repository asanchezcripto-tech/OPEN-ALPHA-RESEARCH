# DuckDB: uniones temporales sin confundir fecha con conocimiento

Recurso: [duckdb](https://github.com/duckdb/duckdb). Commit observado: `6bb57d29dbc1f9032005816e6bb08763bd1a8fb2`. Verificación: 2026-11-04; nivel V3, análisis estático.

**Decisión:** Adoptar biblioteca para consultas locales; fijar una versión compatible con los conectores. Puntuación editorial: **90/100**; riesgo bloqueante: ninguno identificado en esta ruta; no equivale a certificación.

## Arquitectura e implementación observada

El operador PhysicalAsOfJoin separa claves de partición y ordenación, asigna orden ascendente o descendente según la desigualdad y trata de forma distinta igualdad ordinaria y equivalencia con nulos. La biblioteca consulta tablas y Parquet en el mismo proceso. La ruta examinada prueba que ASOF es una operación implementada; no verifica todas las optimizaciones, extensiones o conectores.

## Qué aprovechar

Para un panel macro permite asociar una decisión con la última observación publicada antes de ella. Conservar explícitamente los timestamps de ambos lados: una proyección que solo devuelve el tiempo izquierdo oculta la edad del dato. La unidad y el identificador del activo deben formar parte del contrato, pues SQL no detecta que se mezclan OI en contratos y OI en dólares.

## Qué no asumir

Un ASOF no resuelve por sí solo la bitemporalidad de datos revisables. Filtrar por tiempo de conocimiento y resolver revisiones por periodo antes de buscar el dato pertinente; si hay dos desigualdades independientes, usar una consulta por ventanas. Igualdades con nulos pueden unir identidades desconocidas: en un catálogo financiero se debe rechazar una identidad nula. No se midió rendimiento ni memoria.

## Dependencias, pruebas y requisitos

Motor C++/CMake; bindings y extensiones tienen superficie propia. dlt inspeccionado limita DuckDB a <2 en sus destinos: no recomendar latest sin resolver versiones.

Se inspeccionó test_asof_join_nulls.test: diferencia claves de partición con IS NOT DISTINCT FROM, igualdad ordinaria y nulos en el campo temporal. No se ejecutaron tests; la ruta inicial asof_join.test devolvió 404 y fue sustituida por la ruta real.

Estimación de diseño: CPU corriente, 8–16 GB RAM para tablas diarias pequeñas; almacenamiento depende de snapshots. No es un benchmark ni un requisito mínimo oficial.

## Licencia y acceso

MIT. Clasificación: **REUTILIZACIÓN POTENCIALMENTE COMPATIBLE**. El permiso del código no se extiende a los datos ni a servicios alojados. No se investigó exhaustivamente cada dependencia o incidencia de seguridad.

## Alternativa y experimento mínimo propuesto

SQLite para registro de tesis y metadatos; Polars para transformaciones por expresiones. XTDB solo si el coste de mantener bitemporalidad propia supera claramente operar otro servidor.

Preparar 20 casos con publicación tardía, revisión, timestamp duplicado, unidad distinta y dato ausente. Exigir cero lecturas con knowledge_time posterior a la decisión y mostrar cuándo no hay dato válido. Este experimento es un diseño, no una prueba realizada.

## Evidencias trazables

- [LICENSE](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/LICENSE) — HTTP 200; SHA-256 `075c33400ffcb0c586dd106a029d3e733e9da3693f8fcb9cebfc651c8a2f14e3`.
- [README.md](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/README.md) — HTTP 200; SHA-256 `d9c2afdbd78821e5cd28731bdefa22760374c7670ef2100cd4c44e2d8ced8a8a`.
- [src/execution/operator/join/physical_asof_join.cpp](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/src/execution/operator/join/physical_asof_join.cpp) — fuente `infra-S0004`; inspección parcial de rutas descritas.
- [CMakeLists.txt](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/CMakeLists.txt) — fuente `infra-S0006`; inspección parcial de rutas descritas.
- [test/sql/join/asof/test_asof_join_nulls.test](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/test/sql/join/asof/test_asof_join_nulls.test) — fuente `infra-S0007`; inspección parcial de rutas descritas.

Puntuación por criterio (máximos 25/15/15/12/10/8/8/7): utility=24, evidence=13, data=14, ease=11, license=10, maintenance=5, usability=7, differentiation=6. La disponibilidad y utilidad reciben peso alto; mantenimiento no obtiene puntuación máxima porque no se auditó su sostenibilidad.
