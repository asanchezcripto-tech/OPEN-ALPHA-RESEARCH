# Pandera: calidad estructural con cuarentena de datos

Recurso: [pandera](https://github.com/unionai-oss/pandera). Commit observado: `7ad5f3948d9d1810217d5a25070e6b65e9154059`. Verificación: 2026-11-04; nivel V3, análisis estático.

**Decisión:** Adoptar biblioteca para controles de calidad explícitos y pequeños. Puntuación editorial: **84/100**; riesgo bloqueante: ninguno identificado en esta ruta; no equivale a certificación.

## Arquitectura e implementación observada

La API DataFrameSchema.validate recibe head, tail, sample, lazy e inplace. El backend ejecuta parsers, comprobaciones de columnas, coacción de tipos y validadores. La inspección muestra que validar puede transformar los datos; no debe confundirse con comprobar una copia inmutable.

## Qué aprovechar

Un contrato puede exigir unidad conocida, claves únicas, magnitudes finitas y consistencia entre fecha de publicación y adquisición. Las reglas económicas, por ejemplo revenue no equivalente a fees o cambios permitidos de suministro, siguen siendo responsabilidad del analista.

## Qué no asumir

head/tail/sample comprueban subconjuntos: una validación correcta de muestra no certifica toda la tabla. drop_invalid_rows exige lazy=True y puede ocultar observaciones si no se guarda un registro de rechazos. Coerce y defaults pueden transformar un fallo de proveedor en un valor aparentemente limpio. Preferir cuarentena con razón antes de descartar silenciosamente.

## Dependencias, pruebas y requisitos

Python >=3.10; extras pandas>=2.1.1 y polars>=1.20.0 observados. Elegir un solo backend para el primer alcance.

Se inspeccionó el árbol real de tests/pandas y el caso test_drop_invalid_rows_failure_limit.py; el antiguo tests/core/test_schemas.py no existía. No se calculó porcentaje de cobertura ni se ejecutó código.

Estimación: CPU, memoria proporcional a la tabla y copia de validación; 8–16 GB para un universo diario pequeño.

## Licencia y acceso

MIT. Clasificación: **REUTILIZACIÓN POTENCIALMENTE COMPATIBLE**. El permiso del código no se extiende a los datos ni a servicios alojados. No se investigó exhaustivamente cada dependencia o incidencia de seguridad.

## Alternativa y experimento mínimo propuesto

Pydantic para cada objeto de entrada, Patito si el proyecto es exclusivamente Polars. Great Expectations añade contexto y operación que puede no compensar para un usuario.

Inyectar 12 errores conocidos: unidades mezcladas, timestamps sin zona, duplicados, nulos, infinito, negativo imposible y cambio de esquema. El informe debe identificar todos y conservar la entrada original. Este experimento es un diseño, no una prueba realizada.

## Evidencias trazables

- [LICENSE.txt](https://raw.githubusercontent.com/unionai-oss/pandera/7ad5f3948d9d1810217d5a25070e6b65e9154059/LICENSE.txt) — HTTP 200; SHA-256 `142d0a4e2b2ade63e1d3f85d8289865f729397aafeec9afced01877826c54640`.
- [README.md](https://raw.githubusercontent.com/unionai-oss/pandera/7ad5f3948d9d1810217d5a25070e6b65e9154059/README.md) — HTTP 200; SHA-256 `cbe2f43b6dba825ebf0bfee73e12d48f490b103da9c346c005d90e1010c53847`.
- [pandera/api/pandas/container.py](https://raw.githubusercontent.com/unionai-oss/pandera/7ad5f3948d9d1810217d5a25070e6b65e9154059/pandera/api/pandas/container.py) — fuente `infra-S0073`; inspección parcial de rutas descritas.
- [pandera/backends/pandas/container.py](https://raw.githubusercontent.com/unionai-oss/pandera/7ad5f3948d9d1810217d5a25070e6b65e9154059/pandera/backends/pandas/container.py) — fuente `infra-S0074`; inspección parcial de rutas descritas.
- [pyproject.toml](https://raw.githubusercontent.com/unionai-oss/pandera/7ad5f3948d9d1810217d5a25070e6b65e9154059/pyproject.toml) — fuente `infra-S0076`; inspección parcial de rutas descritas.
- [tests/pandas/test_drop_invalid_rows_failure_limit.py](https://raw.githubusercontent.com/unionai-oss/pandera/7ad5f3948d9d1810217d5a25070e6b65e9154059/tests/pandas/test_drop_invalid_rows_failure_limit.py) — fuente `infra-S0077`; inspección parcial de rutas descritas.

Puntuación por criterio (máximos 25/15/15/12/10/8/8/7): utility=22, evidence=12, data=13, ease=10, license=10, maintenance=5, usability=6, differentiation=6. La disponibilidad y utilidad reciben peso alto; mantenimiento no obtiene puntuación máxima porque no se auditó su sostenibilidad.
