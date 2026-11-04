# PyPortfolioOpt: mejores estimadores de riesgo antes de maximizar Sharpe

Candidato `quant-pyportfolioopt` · observación 2026-11-04 · nivel V3 (estático). Commit `a6638d2e06dae6f444fd022cfd4b3c528902a85b`.

La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.

## Capacidad y alcance

risk_models separa estimación de covarianza de EfficientFrontier, que formula objetivos y restricciones mediante CVXPY. CovarianceShrinkage ofrece objetivos de varianza constante, factor único y correlación constante. Se revisaron riesgo y max_sharpe, no todos los módulos Black-Litterman o HRP.

**Entradas:** Retornos o precios alineados, frecuencia anual, covarianza, restricciones de pesos y, opcionalmente, expectativas.

**Salidas:** Matriz de riesgo regularizada, pesos condicionados a supuestos y métricas teóricas de la cartera.

## Evidencia técnica y límites

La reparación espectral de matrices sustituye autovalores negativos por cero y avisa; esto corrige factibilidad numérica, no errores económicos de datos. Ledoit-Wolf de varianza constante usa np.nan_to_num antes del estimador: el tratamiento previo de faltantes debe ser explícito. max_sharpe exige al menos una expectativa superior al tipo libre de riesgo y transforma variables. Tests de sample covariance, log returns y semidefinición usan respuestas esperadas.

La covarianza por defecto se anualiza a 252 periodos; en cripto diario 24/7 no trasladar esa convención sin decisión explícita. Historial desigual por token y deslistados cambian la muestra. Ajustar estimadores solo con entrenamiento, con rebalanceo fuera de muestra.

## Adopción proporcional

La capacidad útil inmediata es comparar exposición y concentración bajo covarianzas distintas; la frontera eficiente puede ser frágil a medias estimadas. Comparar pesos iguales, BTC/ETH y mínima volatilidad con límites por activo antes de optimizar retornos.

**Dependencias observadas:** CVXPY>=1.1.19, NumPy>=1.26,<3, pandas<4, scikit-base<0.14, scikit-learn, SciPy.

CPU y 8 GB RAM suelen bastar para decenas de activos y problemas convexos pequeños; estimación no benchmark. Solvers y restricciones no convexas pueden elevar dificultad. El pyproject inspeccionado declara 1.6.0; esto no prueba instalación ni release estable en este equipo.

**Licencia del código:** MIT. Clasificación: REUTILIZACIÓN POTENCIALMENTE COMPATIBLE. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.

## Experimento de aceptación propuesto, no ejecutado

Usar 12 ventanas de rebalanceo con datos previos exclusivamente. Medir concentración máxima, rotación, ES realizado y sensibilidad al borrar una semana de datos. Aceptación: pesos factibles, contabilidad reproducible, y menor fragilidad frente a equal weight; ninguna obligación de mejorar rentabilidad.

## Veredicto

Adoptar como biblioteca de escenarios de riesgo. Licencia MIT revisada. La URL antigua robertmartin8 redirige actualmente a PyPortfolio/PyPortfolioOpt; conservar canonicalización y commit. skfolio ofrece validación integrada; Riskfolio-Lib amplía familias de riesgo con más complejidad.

Puntuación editorial 83/100: utilidad 22/25; evidencia 13/15; datos 12/15; facilidad 10/12; licencia 10/10; mantenimiento 5/8; uso diario 7/8; diferenciación 4/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.

## Fuentes exactas

- [pypfopt/risk_models.py](https://github.com/robertmartin8/PyPortfolioOpt/blob/a6638d2e06dae6f444fd022cfd4b3c528902a85b/pypfopt/risk_models.py)
- [pypfopt/efficient_frontier/efficient_frontier.py](https://github.com/robertmartin8/PyPortfolioOpt/blob/a6638d2e06dae6f444fd022cfd4b3c528902a85b/pypfopt/efficient_frontier/efficient_frontier.py)
- [tests/test_risk_models.py](https://github.com/robertmartin8/PyPortfolioOpt/blob/a6638d2e06dae6f444fd022cfd4b3c528902a85b/tests/test_risk_models.py)
- [pyproject.toml](https://github.com/robertmartin8/PyPortfolioOpt/blob/a6638d2e06dae6f444fd022cfd4b3c528902a85b/pyproject.toml)
- [LICENSE](https://github.com/robertmartin8/PyPortfolioOpt/blob/a6638d2e06dae6f444fd022cfd4b3c528902a85b/LICENSE)
