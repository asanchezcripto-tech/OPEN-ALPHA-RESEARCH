# arch: una biblioteca de inferencia que vale más que otro optimizador

Candidato `quant-arch` · observación 2026-11-04 · nivel V3 (estático). Commit `8f0f8f214852071245d4d8bf310110a0a781e493`.

La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.

## Capacidad y alcance

bootstrap/base implementa remuestreo temporal; multiple_comparison aplica pérdidas diferenciales, varianzas de largo plazo y remuestreo para comparación múltiple. El código admite stationary, circular y moving block bootstrap; la inferencia queda separada del motor que produjo resultados.

**Entradas:** Pérdidas de un benchmark y de todas las variantes sobre las mismas fechas; o retornos para modelos de volatilidad.

**Salidas:** Pruebas SPA/StepM, conjuntos de confianza MCS, intervalos bootstrap y distribuciones condicionadas.

## Evidencia técnica y límites

SPA exige benchmark unidimensional y alternativas T×K, pérdidas finitas y muestras compatibles. La longitud de bloque por defecto depende de sqrt(T), pero el propio contrato recomienda elegirla para los datos. nested=True con studentize requiere aproximadamente reps² remuestreos, por lo que es una opción cara. Los tests leídos comprueban kernels, studentización dentro del bootstrap, pérdidas idénticas, errores y reproducibilidad de semillas.

Los bloques conservan dependencia local mejor que barajar retornos sueltos, pero no crean observaciones independientes ni arreglan series con look-ahead. Si cambia el régimen, la estacionariedad aproximada necesaria para extrapolar se debilita. La longitud de bloque debe probarse en un rango predefinido.

## Adopción proporcional

Permite rechazar una colección de señales que no supera un baseline bajo búsqueda múltiple. Evitar interpretar p-value como probabilidad de que una estrategia sea rentable. MCS devuelve alternativas indistinguibles a un nivel dado, no una orden de comprar la mejor.

**Dependencias observadas:** NumPy, pandas, SciPy, statsmodels, packaging; Cython/Meson para compilación.

CPU y 8 GB RAM estimados para pocas decenas de señales diarias; RAM/tiempo crecen con T,K,reps. El método MCS revisado forma tensores de comparaciones por pares; un catálogo inmenso no es gratis. No se ejecutó benchmark.

**Licencia del código:** NCSA. Clasificación: REUTILIZACIÓN POTENCIALMENTE COMPATIBLE. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.

## Experimento de aceptación propuesto, no ejecutado

Registrar primero 20 reglas y benchmark, producir pérdidas netas homogéneas y aplicar SPA con tres longitudes de bloque justificadas. Añadir un control deliberadamente sin señal y un caso con fuga temporal para comprobar que la auditoría de datos, separada, lo rechaza. Exigir un resultado estable o abstenerse.

## Veredicto

Adoptar biblioteca. Licencia NCSA verificada en pyproject y texto, no etiquetarla MIT por parecido. Prioridad alta para un Evidence/Backtest Auditor independiente; reutiliza técnicas de estadística antes de incorporar agentes generadores de estrategias.

Puntuación editorial 89/100: utilidad 24/25; evidencia 14/15; datos 13/15; facilidad 10/12; licencia 10/10; mantenimiento 5/8; uso diario 7/8; diferenciación 6/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.

## Fuentes exactas

- [arch/bootstrap/multiple_comparison.py](https://github.com/bashtage/arch/blob/8f0f8f214852071245d4d8bf310110a0a781e493/arch/bootstrap/multiple_comparison.py)
- [arch/bootstrap/base.py](https://github.com/bashtage/arch/blob/8f0f8f214852071245d4d8bf310110a0a781e493/arch/bootstrap/base.py)
- [arch/tests/bootstrap/test_multiple_comparison.py](https://github.com/bashtage/arch/blob/8f0f8f214852071245d4d8bf310110a0a781e493/arch/tests/bootstrap/test_multiple_comparison.py)
- [pyproject.toml](https://github.com/bashtage/arch/blob/8f0f8f214852071245d4d8bf310110a0a781e493/pyproject.toml)
- [LICENSE.md](https://github.com/bashtage/arch/blob/8f0f8f214852071245d4d8bf310110a0a781e493/LICENSE.md)
