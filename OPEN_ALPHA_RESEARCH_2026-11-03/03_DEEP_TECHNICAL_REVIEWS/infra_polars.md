# Polars: transformaciones y límites explícitos de antigüedad

Recurso: [polars](https://github.com/pola-rs/polars). Commit observado: `f07718c97e3d06eee3babaa6fb7c0b4b5cc054df`. Verificación: 2026-11-04; nivel V3, análisis estático.

**Decisión:** Adoptar biblioteca cuando haya transformaciones tabulares; evitar añadirla si SQL y pandas ya resuelven el alcance. Puntuación editorial: **88/100**; riesgo bloqueante: ninguno identificado en esta ruta; no equivale a certificación.

## Arquitectura e implementación observada

DataFrame.join_asof expone dirección, grupos, tolerancia, coincidencias exactas y comprobación de orden. El wrapper delega en el plan lazy y el motor nativo. Se inspeccionó esta interfaz, su manifiesto y tests; no el motor Rust completo.

## Qué aprovechar

La tolerancia permite declarar que un funding o dato de profundidad es demasiado viejo para usarse, aunque exista una observación anterior. La dirección backward es apropiada para joins de información disponible; nearest o forward pueden incorporar el futuro. Separar uniones de investigación histórica de interpolación descriptiva.

## Qué no asumir

Exigir orden dentro de cada grupo, tipos temporales homogéneos y un criterio explícito para empates. La misma fecha puede contener revisiones con distinto conocimiento: join_asof no sustituye ese modelo. La tolerancia debe reflejar la frecuencia de la fuente, no optimizarse sobre rentabilidad. Un cambio de runtime puede afectar resultados y APIs.

## Dependencias, pruebas y requisitos

El manifiesto observado declara polars-runtime-32 ==2.1.0 y Python >=3.11; extras opcionales añaden pyarrow, pandas o GPU. La máquina del trabajo usa Python 3.10 para scripts propios: no se instaló ni se probó Polars en ella.

El archivo test_join_asof.py contiene pruebas de tolerancia, claves nulas, orden, tipos y allow_exact_matches. Se leyó el caso de trades/quotes que excluye coincidencias exactas; no se ejecutó ni se midió cobertura.

CPU y 8–16 GB RAM como supuesto de un prototipo diario; no requiere GPU para la capacidad propuesta.

## Licencia y acceso

MIT. Clasificación: **REUTILIZACIÓN POTENCIALMENTE COMPATIBLE**. El permiso del código no se extiende a los datos ni a servicios alojados. No se investigó exhaustivamente cada dependencia o incidencia de seguridad.

## Alternativa y experimento mínimo propuesto

DuckDB ofrece SQL y lectura directa de Parquet; pandas reduce fricción con librerías quant. Elegir un motor principal y convertir únicamente en las fronteras necesarias.

Replay de series desordenadas, publicación tardía y cambios de zona horaria. Comprobar una unión manual de 30 filas y rechazar datos fuera de tolerancia, sin rellenar automáticamente el hueco. Este experimento es un diseño, no una prueba realizada.

## Evidencias trazables

- [LICENSE](https://raw.githubusercontent.com/pola-rs/polars/f07718c97e3d06eee3babaa6fb7c0b4b5cc054df/LICENSE) — HTTP 200; SHA-256 `8296022372dc83cc8ef234b3d4889ef8f8b1779754a78bebf13d2c5178a6b4c4`.
- [README.md](https://raw.githubusercontent.com/pola-rs/polars/f07718c97e3d06eee3babaa6fb7c0b4b5cc054df/README.md) — HTTP 200; SHA-256 `771ed4b6d939071a415160838c21f0388aab166284b573cbe5d7b0f155073fbb`.
- [py-polars/src/polars/dataframe/frame.py](https://raw.githubusercontent.com/pola-rs/polars/f07718c97e3d06eee3babaa6fb7c0b4b5cc054df/py-polars/src/polars/dataframe/frame.py) — fuente `infra-S0011`; inspección parcial de rutas descritas.
- [py-polars/tests/unit/operations/test_join_asof.py](https://raw.githubusercontent.com/pola-rs/polars/f07718c97e3d06eee3babaa6fb7c0b4b5cc054df/py-polars/tests/unit/operations/test_join_asof.py) — fuente `infra-S0012`; inspección parcial de rutas descritas.
- [py-polars/pyproject.toml](https://raw.githubusercontent.com/pola-rs/polars/f07718c97e3d06eee3babaa6fb7c0b4b5cc054df/py-polars/pyproject.toml) — fuente `infra-S0013`; inspección parcial de rutas descritas.

Puntuación por criterio (máximos 25/15/15/12/10/8/8/7): utility=23, evidence=13, data=14, ease=10, license=10, maintenance=5, usability=7, differentiation=6. La disponibilidad y utilidad reciben peso alto; mantenimiento no obtiene puntuación máxima porque no se auditó su sostenibilidad.
