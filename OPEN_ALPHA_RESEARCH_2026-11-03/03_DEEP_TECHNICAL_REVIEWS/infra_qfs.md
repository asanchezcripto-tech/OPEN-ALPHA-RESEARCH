# Quant Feature Store: un ejemplo útil que no debe adoptarse sin licencia

Recurso: [quant-feature-store](https://github.com/sophie-nguyenthuthuy/quant-feature-store). Commit observado: `61b8fb9b58a6d9ea0d783112e075ede0be79a65b`. Verificación: 2026-11-04; nivel V3, análisis estático.

**Decisión:** Extraer la técnica conceptual; bloquear copia/adaptación de código mientras la licencia siga sin verificar. Puntuación editorial: **60/100**; riesgo bloqueante: No copiar/adaptar código hasta verificar licencia aplicable..

## Arquitectura e implementación observada

El prototipo guarda versiones de features en Parquet y usa DuckDB/Polars. La ruta rápida depende de unicidad por evento, publicación estrictamente creciente y ausencia de timestamps predictivos. Si no se cumplen, el join usa las dos restricciones temporales y ordena por event_time y knowledge_time.

## Qué aprovechar

Hace visible una diferencia fácil de perder: conocer hoy un valor referido a enero no significa haberlo conocido en enero. La estrategia de escoger camino rápido solo bajo invariantes verificables es transferible a otros sistemas.

## Qué no asumir

No se encontró licencia en la raíz ni en el manifiesto inspeccionados: público no equivale a reutilizable. Es un prototipo, sin prueba de operación sostenida. El requisito event_time<=as_of es adecuado para hechos observados, pero no para un calendario de unlocks futuros ya anunciados: ese dominio necesita scheduled_event_time y announced_at separados. Nombres e identificadores interpolados en SQL necesitarían revisión de confianza antes de exponerlos a un agente.

## Dependencias, pruebas y requisitos

Manifiesto 0.1.0, Python>=3.10, DuckDB, Polars, pandas, NumPy, PyArrow y yfinance sin fijación estrecha. Las condiciones del proveedor de datos son independientes.

Se leyó test_no_lookahead_on_knowledge_time: una revisión publicada después queda excluida y se incorpora al avanzar la fecha de consulta. Los tests son fixtures sintéticos; no certifican que los históricos de yfinance tengan vintages reales.

Estimación del patrón: un portátil basta para fixtures y series diarias pequeñas. No se evaluó escalabilidad del proyecto.

## Licencia y acceso

LICENCIA NO VERIFICADA. Clasificación: **LICENCIA NO VERIFICADA**. El permiso del código no se extiende a los datos ni a servicios alojados. No se investigó exhaustivamente cada dependencia o incidencia de seguridad.

## Alternativa y experimento mínimo propuesto

Diseñar un contrato propio y consultas SQL pequeñas basadas en principios generales; XTDB aporta bitemporalidad nativa a costa de otra base y más operación.

Reproducir el comportamiento requerido con fixtures redactados independientemente: dos revisiones, llegada fuera de orden, publicación simultánea, forecast y evento futuro anunciado. No copiar tests mientras no haya permiso. Este experimento es un diseño, no una prueba realizada.

## Evidencias trazables

- [README.md](https://raw.githubusercontent.com/sophie-nguyenthuthuy/quant-feature-store/61b8fb9b58a6d9ea0d783112e075ede0be79a65b/README.md) — HTTP 200; SHA-256 `5b4c5fbb01bf09761c4529585b2029449cc294c3d1674eace2dda35db754dab8`.
- [qfs/store.py](https://raw.githubusercontent.com/sophie-nguyenthuthuy/quant-feature-store/61b8fb9b58a6d9ea0d783112e075ede0be79a65b/qfs/store.py) — fuente `infra-S0234`; inspección parcial de rutas descritas.
- [tests/test_point_in_time.py](https://raw.githubusercontent.com/sophie-nguyenthuthuy/quant-feature-store/61b8fb9b58a6d9ea0d783112e075ede0be79a65b/tests/test_point_in_time.py) — fuente `infra-S0235`; inspección parcial de rutas descritas.
- [pyproject.toml](https://raw.githubusercontent.com/sophie-nguyenthuthuy/quant-feature-store/61b8fb9b58a6d9ea0d783112e075ede0be79a65b/pyproject.toml) — fuente `infra-S0236`; inspección parcial de rutas descritas.

Puntuación por criterio (máximos 25/15/15/12/10/8/8/7): utility=20, evidence=10, data=9, ease=7, license=0, maintenance=2, usability=5, differentiation=7. La disponibilidad y utilidad reciben peso alto; mantenimiento no obtiene puntuación máxima porque no se auditó su sostenibilidad.
