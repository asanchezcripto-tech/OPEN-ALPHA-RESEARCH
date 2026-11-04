# skfolio: validación de carteras; la purga no viene activada por el nombre

Candidato `quant-skfolio` · observación 2026-11-04 · nivel V3 (estático). Commit `0db206ed812622088cbd33af2e34a0f4762fa71e`.

La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.

## Capacidad y alcance

Estimadores compatibles con scikit-learn, optimizadores convexos y splitters específicos. WalkForward soporta tamaños por observación y calendario. CombinatorialPurgedCV construye combinaciones de folds y recompone trayectorias; introduce un máximo de combinaciones para impedir configuraciones explosivas.

**Entradas:** Matriz temporal de retornos, reglas de entrenamiento/prueba, horizonte de etiquetas, costes y restricciones.

**Salidas:** Carteras por ventana y poblaciones de trayectorias comparables, en lugar de un único backtest elegido.

## Evidencia técnica y límites

El constructor verificado fija n_folds=10, n_test_folds=8, purged_size=0 y embargo_size=0. split usa índices de filas y elimina posiciones alrededor de fronteras. Los tests incluyen folds desiguales, límites de purga/embargo, errores de configuración y regresión de índices concatenados. No se midió cobertura porcentual ni se ejecutaron.

CPCV puede entrenar con bloques posteriores al bloque evaluado: ayuda a estimar dispersión de selección bajo supuestos, pero no sustituye una simulación prospectiva walk-forward. Una purga en filas requiere traducir el horizonte real y tratar calendarios irregulares. Etiquetas de 90–540 días dejan muy pocas observaciones efectivamente independientes.

## Adopción proporcional

La integración reduce trabajo de validación de carteras y obliga a comparar trayectorias. Para un screener fundamental simple puede bastar walk-forward con embargo explícito. No usar KFold barajado ni elegir a posteriori el mejor camino CPCV como evidencia de desempeño futuro.

**Dependencias observadas:** scikit-learn>=1.6, CVXPY-base>=1.5, Clarabel>=0.10, pandas>=2.1, NumPy, SciPy>=1.15.2, Plotly>=6.

CPU, 8–16 GB RAM estimados para unas decenas de activos; coste proporcional a número de ajustes, folds y solvers. GPU innecesaria. El manifiesto examinado indica 1.12.5 y Python>=3.10; compatibilidad de todos los extras no verificada.

**Licencia del código:** BSD-3-Clause. Clasificación: REUTILIZACIÓN POTENCIALMENTE COMPATIBLE. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.

## Experimento de aceptación propuesto, no ejecutado

Fixture de etiquetas solapadas a 30 días con fechas irregulares. Verificar intersección vacía entre intervalos de entrenamiento y prueba, luego comparar equal weight, inverse volatility y HRP con la misma ventana. Registrar rotación neta de costes y distribución de riesgos, no solo media del Sharpe.

## Veredicto

Biblioteca prioritaria para Portfolio Risk Lens y auditoría de candidatos. BSD-3-Clause revisada. Empezar por WalkForward y baselines; añadir CPCV solo si el tamaño muestral y el horizonte lo justifican.

Puntuación editorial 85/100: utilidad 23/25; evidencia 13/15; datos 12/15; facilidad 9/12; licencia 10/10; mantenimiento 5/8; uso diario 7/8; diferenciación 6/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.

## Fuentes exactas

- [src/skfolio/model_selection/_combinatorial.py](https://github.com/skfolio/skfolio/blob/0db206ed812622088cbd33af2e34a0f4762fa71e/src/skfolio/model_selection/_combinatorial.py)
- [src/skfolio/model_selection/_walk_forward.py](https://github.com/skfolio/skfolio/blob/0db206ed812622088cbd33af2e34a0f4762fa71e/src/skfolio/model_selection/_walk_forward.py)
- [tests/test_model_selection/test_combinatorial.py](https://github.com/skfolio/skfolio/blob/0db206ed812622088cbd33af2e34a0f4762fa71e/tests/test_model_selection/test_combinatorial.py)
- [docs/user_guide/model_selection.rst](https://github.com/skfolio/skfolio/blob/0db206ed812622088cbd33af2e34a0f4762fa71e/docs/user_guide/model_selection.rst)
- [pyproject.toml](https://github.com/skfolio/skfolio/blob/0db206ed812622088cbd33af2e34a0f4762fa71e/pyproject.toml)
- [LICENSE](https://github.com/skfolio/skfolio/blob/0db206ed812622088cbd33af2e34a0f4762fa71e/LICENSE)
