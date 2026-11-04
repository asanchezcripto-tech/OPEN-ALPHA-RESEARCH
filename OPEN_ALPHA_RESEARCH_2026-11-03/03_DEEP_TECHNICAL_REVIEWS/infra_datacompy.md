# DataComPy: un detector de revisiones y discrepancias, no un árbitro económico

Recurso: [datacompy](https://github.com/capitalone/datacompy). Commit observado: `5a7a1eac257c2efdfa9a6f162647233c4ee7de9f`. Verificación: 2026-11-04; nivel V3, análisis estático.

**Decisión:** Adoptar biblioteca para reconciliación y comparar snapshots. Puntuación editorial: **84/100**; riesgo bloqueante: ninguno identificado en esta ruta; no equivale a certificación.

## Arquitectura e implementación observada

PolarsCompare compara tablas por claves y evalúa diferencias numéricas con tolerancias absoluta y relativa. El código resuelve el nombre del parámetro de igualdad de nulos según la interfaz Polars, lo que muestra compatibilidad explícita entre ramas de API.

## Qué aprovechar

Comparar la respuesta de hoy para una fecha pasada contra el snapshot anterior permite detectar que la historia cambió. La diferencia se puede atribuir a precio, cantidad, cobertura o metodología solo si se conservan esos campos: un diff aislado no explica la causa.

## Qué no asumir

La tolerancia es relativa al segundo conjunto, por lo que el papel de referencia debe ser consistente. Una tolerancia amplia puede ocultar una corrección material. Claves duplicadas o cambios de identidad pueden crear diferencias aparentes. Reconciliar fees de distinto alcance sin armonizar definición produciría falsos positivos.

## Dependencias, pruebas y requisitos

Python>=3.10; el manifiesto observado declara pandas>=2.2,<=3.1 y polars[pandas]>=0.20.4,<=2.1. Integraciones Spark/Snowflake son opcionales e innecesarias aquí.

Se inspeccionó tests/test_polars.py y su compatibilidad con semántica de nulos en CSV; la antigua ruta test_core.py no existía. No se ejecutó la batería ni se midió precisión.

CPU y memoria proporcional al tamaño de tablas; estimación 8–16 GB para snapshots diarios de un universo pequeño.

## Licencia y acceso

Apache-2.0. Clasificación: **REUTILIZACIÓN POTENCIALMENTE COMPATIBLE**. El permiso del código no se extiende a los datos ni a servicios alojados. No se investigó exhaustivamente cada dependencia o incidencia de seguridad.

## Alternativa y experimento mínimo propuesto

EXCEPT/join SQL con diferencias de columnas puede bastar para dos tablas estables. data-diff está archivado según su propio repositorio; conservarlo como referencia.

Crear snapshots con diez revisiones conocidas y cinco diferencias de redondeo. Exigir detectar todas las materialmente relevantes, registrar cambios de esquema y explicar por qué se acepta cada tolerancia. Este experimento es un diseño, no una prueba realizada.

## Evidencias trazables

- [LICENSE](https://raw.githubusercontent.com/capitalone/datacompy/5a7a1eac257c2efdfa9a6f162647233c4ee7de9f/LICENSE) — HTTP 200; SHA-256 `58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd`.
- [README.md](https://raw.githubusercontent.com/capitalone/datacompy/5a7a1eac257c2efdfa9a6f162647233c4ee7de9f/README.md) — HTTP 200; SHA-256 `ac0bdb01880ec5dba6ad1eea3e20afd7eb1426057f217d1cf5e7d86738dd9774`.
- [datacompy/polars.py](https://raw.githubusercontent.com/capitalone/datacompy/5a7a1eac257c2efdfa9a6f162647233c4ee7de9f/datacompy/polars.py) — fuente `infra-S0219`; inspección parcial de rutas descritas.
- [pyproject.toml](https://raw.githubusercontent.com/capitalone/datacompy/5a7a1eac257c2efdfa9a6f162647233c4ee7de9f/pyproject.toml) — fuente `infra-S0221`; inspección parcial de rutas descritas.
- [tests/test_polars.py](https://raw.githubusercontent.com/capitalone/datacompy/5a7a1eac257c2efdfa9a6f162647233c4ee7de9f/tests/test_polars.py) — fuente `infra-S0222`; inspección parcial de rutas descritas.

Puntuación por criterio (máximos 25/15/15/12/10/8/8/7): utility=21, evidence=12, data=13, ease=10, license=10, maintenance=5, usability=7, differentiation=6. La disponibilidad y utilidad reciben peso alto; mantenimiento no obtiene puntuación máxima porque no se auditó su sostenibilidad.
