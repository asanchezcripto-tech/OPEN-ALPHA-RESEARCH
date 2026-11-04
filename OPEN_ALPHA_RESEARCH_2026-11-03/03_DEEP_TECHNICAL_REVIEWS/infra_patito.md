# Patito: contratos legibles para una herramienta basada en Polars

Recurso: [patito](https://github.com/JakobGM/patito). Commit observado: `e4590c3508a2d716733df2353d95563a2f008a6f`. Verificación: 2026-11-04; nivel V3, análisis estático.

**Decisión:** Adoptar biblioteca solo si simplifica el contrato sobre Polars; mantener Pandera como alternativa más general. Puntuación editorial: **80/100**; riesgo bloqueante: ninguno identificado en esta ruta; no equivale a certificación.

## Arquitectura e implementación observada

Los modelos Pydantic describen columnas y restricciones que se aplican sobre Polars. validators.py comprueba presencia, nulabilidad, dtype, unicidad y expresiones personalizadas. Model.validate devuelve un DataFrame ligado al modelo.

## Qué aprovechar

Un mismo esquema puede hacer explícitos asset_id, moneda, unidad, fuente y tiempos antes de calcular ratios. Una expresión de validación puede exigir que una observación tenga explicación si cambia su metodología.

## Qué no asumir

Permitir columnas ausentes o superfluas cambia la garantía: no habilitar estas opciones de manera global. Las restricciones estructurales no prueban la realidad económica ni la legitimidad de una etiqueta de wallet. Un umbral de cobertura en configuración es un objetivo del proyecto, no cobertura medida por esta investigación.

## Dependencias, pruebas y requisitos

Manifiesto 0.8.6: Python>=3.9, Pydantic>=2.7 y Polars>=1.32. No hay límite superior observado para Polars: probar compatibilidad antes de adoptar un nuevo major.

Se leyó test_uniqueness_validation: el conjunto con duplicados debe fallar, el vacío puede pasar. Por ello, un chequeo de unicidad debe acompañarse de completitud y mínimo de observaciones. También se observaron casos de fecha y expresiones personalizadas.

Estimación: CPU corriente; memoria condicionada por Polars. Sin GPU ni servicio alojado obligatorio.

## Licencia y acceso

MIT. Clasificación: **REUTILIZACIÓN POTENCIALMENTE COMPATIBLE**. El permiso del código no se extiende a los datos ni a servicios alojados. No se investigó exhaustivamente cada dependencia o incidencia de seguridad.

## Alternativa y experimento mínimo propuesto

Pandera si se necesitan varios backends; Pydantic sin otra capa para unos pocos registros. No introducir dos validadores que dupliquen reglas.

Probar esquemas vacíos, claves nulas, duplicados y unidades mezcladas. Exigir que el contrato dé errores entendibles y que no transforme silenciosamente la muestra financiera. Este experimento es un diseño, no una prueba realizada.

## Evidencias trazables

- [LICENSE](https://raw.githubusercontent.com/JakobGM/patito/e4590c3508a2d716733df2353d95563a2f008a6f/LICENSE) — HTTP 200; SHA-256 `ddb738632b85d1ee67779f44dc2b11f1033551aee9a8a7c2f430f52d505532ce`.
- [README.md](https://raw.githubusercontent.com/JakobGM/patito/e4590c3508a2d716733df2353d95563a2f008a6f/README.md) — HTTP 200; SHA-256 `b9164a0720bb0235d509137ee2a408e578c9569be47ee44f8f2e0165f5d3311e`.
- [src/patito/validators.py](https://raw.githubusercontent.com/JakobGM/patito/e4590c3508a2d716733df2353d95563a2f008a6f/src/patito/validators.py) — fuente `infra-S0090`; inspección parcial de rutas descritas.
- [src/patito/pydantic.py](https://raw.githubusercontent.com/JakobGM/patito/e4590c3508a2d716733df2353d95563a2f008a6f/src/patito/pydantic.py) — fuente `infra-S0091`; inspección parcial de rutas descritas.
- [tests/test_validators.py](https://raw.githubusercontent.com/JakobGM/patito/e4590c3508a2d716733df2353d95563a2f008a6f/tests/test_validators.py) — fuente `infra-S0092`; inspección parcial de rutas descritas.
- [pyproject.toml](https://raw.githubusercontent.com/JakobGM/patito/e4590c3508a2d716733df2353d95563a2f008a6f/pyproject.toml) — fuente `infra-S0093`; inspección parcial de rutas descritas.

Puntuación por criterio (máximos 25/15/15/12/10/8/8/7): utility=20, evidence=12, data=12, ease=10, license=10, maintenance=4, usability=6, differentiation=6. La disponibilidad y utilidad reciben peso alto; mantenimiento no obtiene puntuación máxima porque no se auditó su sostenibilidad.
