# dlt: ingesta incremental que no garantiza un archivo de revisiones

Recurso: [dlt](https://github.com/dlt-hub/dlt). Commit observado: `75ea7f33e24dbf3e46a42e4b9739404ea4d9631e`. Verificación: 2026-11-04; nivel V3, análisis estático.

**Decisión:** Adoptar biblioteca si hay varias fuentes incrementales; un recolector pequeño puede bastar al principio. Puntuación editorial: **81/100**; riesgo bloqueante: ninguno identificado en esta ruta; no equivale a certificación.

## Arquitectura e implementación observada

Incremental mantiene estado por recurso y cursor. get_state crea un estado transitorio si existe end_value; en uso normal conserva el avance. bind resuelve contexto del planificador y rango. Faltas de cursor producen errores por defecto. Se inspeccionaron código, manifiesto y pruebas, sin ejecutar un pipeline.

## Qué aprovechar

Reduce trabajo repetido en paginación temporal y recuperación de rangos solapados. Una ventana lag permite volver a consultar observaciones recientes que la fuente corrige. Esto es útil para métricas de protocolos cuyos adaptadores se actualizan después del día al que atribuyen el dato.

## Qué no asumir

Un cursor de fecha del evento no detecta una revisión tardía de un evento antiguo si la API no expone updated_at ni se relee ese intervalo. La deduplicación de frontera no equivale a merge global; con lag no deben presumirse las mismas garantías. Un destino con merge puede borrar el estado previo si no se añade una capa append-only de snapshots. El planificador externo también puede cambiar el intervalo efectivo.

## Dependencias, pruebas y requisitos

Python >=3.10,<3.15. El manifiesto limita varios extras DuckDB a <2. Este es un bloqueo de compatibilidad para una receta que combine indiscriminadamente las versiones más nuevas.

Se leyó test_missing_cursor_field y su expectativa de IncrementalCursorPathMissing/PipelineStepFailed. El archivo contiene pruebas de solapamientos, nulos, claves compuestas y lag. No se ejecutaron.

Estimación: CPU y 8–16 GB RAM; el coste dominante puede ser el proveedor y el historial, no la biblioteca.

## Licencia y acceso

Apache-2.0. Clasificación: **REUTILIZACIÓN POTENCIALMENTE COMPATIBLE**. El permiso del código no se extiende a los datos ni a servicios alojados. No se investigó exhaustivamente cada dependencia o incidencia de seguridad.

## Alternativa y experimento mínimo propuesto

HTTPX/requests, un cursor persistido y snapshots Parquet para 2–3 endpoints. Prefect/Dagster solo cuando se necesite operación más compleja.

Simular una revisión fuera del lag, fallo después de descarga y reintento. Exigir que no haya pérdida, que repetir sea idempotente y que ambas versiones históricas permanezcan consultables. Este experimento es un diseño, no una prueba realizada.

## Evidencias trazables

- [LICENSE.txt](https://raw.githubusercontent.com/dlt-hub/dlt/75ea7f33e24dbf3e46a42e4b9739404ea4d9631e/LICENSE.txt) — HTTP 200; SHA-256 `3bd68ce12f57c10e265b3d19b3251efa5aa40f780f590bc8bb7b1c83f85854ca`.
- [README.md](https://raw.githubusercontent.com/dlt-hub/dlt/75ea7f33e24dbf3e46a42e4b9739404ea4d9631e/README.md) — HTTP 200; SHA-256 `7230060b84ef30cfcf5106e3121a42e04cf77b8fb0be6dc06782274a0f07a461`.
- [dlt/extract/incremental/__init__.py](https://raw.githubusercontent.com/dlt-hub/dlt/75ea7f33e24dbf3e46a42e4b9739404ea4d9631e/dlt/extract/incremental/__init__.py) — fuente `infra-S0032`; inspección parcial de rutas descritas.
- [tests/extract/test_incremental.py](https://raw.githubusercontent.com/dlt-hub/dlt/75ea7f33e24dbf3e46a42e4b9739404ea4d9631e/tests/extract/test_incremental.py) — fuente `infra-S0033`; inspección parcial de rutas descritas.
- [pyproject.toml](https://raw.githubusercontent.com/dlt-hub/dlt/75ea7f33e24dbf3e46a42e4b9739404ea4d9631e/pyproject.toml) — fuente `infra-S0034`; inspección parcial de rutas descritas.

Puntuación por criterio (máximos 25/15/15/12/10/8/8/7): utility=22, evidence=13, data=12, ease=8, license=10, maintenance=5, usability=6, differentiation=5. La disponibilidad y utilidad reciben peso alto; mantenimiento no obtiene puntuación máxima porque no se auditó su sostenibilidad.
