# MLForecast — revisión técnica estática

ID: `AI-mlforecast`. Verificado: 2026-11-04. Referencia estratégica: 2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.

Commit: `74ba65e49cb39282e5f490c8dfd25e4bacacedaf`. [Repositorio](https://github.com/Nixtla/mlforecast). [Licencia de código](https://raw.githubusercontent.com/Nixtla/mlforecast/74ba65e49cb39282e5f490c8dfd25e4bacacedaf/LICENSE). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.

Puntuación editorial: **84/100**. Desglose: utility=23, evidence=13, data=12, ease=10, license=9, maintenance=6, usability=6, differentiation=5. Confianza: media-alta sobre rutas observadas; no sobre eficacia financiera. Los bloqueos de licencia/datos prevalecen.

## Decisión

MLForecast merece prioridad sobre entrenar un Transformer desde cero: expone lags, transformaciones, modelos tabulares y validación temporal en un flujo relativamente compacto. La recomendación es condicional al problema: predecir actividad, volatilidad o clasificar riesgo, comparando siempre con naive. No se propone convertir un forecast de retorno en señal automática. LICENSE Apache 2.0 leído; dependencias y datos siguen requiriendo revisión separada.

## Arquitectura inspeccionada

[core.py](https://github.com/Nixtla/mlforecast/blob/74ba65e49cb39282e5f490c8dfd25e4bacacedaf/mlforecast/core.py) representa series agrupadas y construye features locales/pooled, transformaciones de targets y predicción recursiva o por múltiples horizontes. La ruta importa `coreforecast`, `utilsforecast`, NumPy, Pandas, Narwhals y estimadores compatibles con scikit-learn. [forecast.py](https://github.com/Nixtla/mlforecast/blob/74ba65e49cb39282e5f490c8dfd25e4bacacedaf/mlforecast/forecast.py) coordina `fit`, `predict`, `cross_validation`, intervalos y transferencia/recalibración. Se examinó `_check_out_of_sample`, que rechaza ventanas anteriores al fin de entrenamiento para evitar calibrar intervalos sobre datos de ajuste.

`cross_validation` permite fijar ventanas, horizonte, paso y frecuencia de refit; esto es mejor que una partición aleatoria de filas para series. Sin embargo, no garantiza embargo/purga para etiquetas de retornos solapadas ni que la selección de variables se haga dentro de cada ventana. La identidad de serie debe ser estable: reutilizar un ticker para otro activo puede contaminar estado y transferencias.

## Calidad, seguridad y alternativas

[test_forecast.py](https://github.com/Nixtla/mlforecast/blob/74ba65e49cb39282e5f490c8dfd25e4bacacedaf/tests/test_forecast.py) y el árbol de tests muestran casos de forecasting, conformal y actualización; se inspeccionaron rutas y firmas, sin ejecución ni medición de cobertura. El uso de cloudpickle/fsspec en persistencia significa que un futuro desarrollo debe cargar solo artefactos propios de procedencia conocida; no se cargó ninguno. La complejidad crece con pooled features y horizontes: empezar con lags explícitos y un único estimador LightGBM o regresión sencilla. StatsForecast es mejor si basta un baseline univariado; Chronos 2 es comparación útil cuando el histórico propio es escaso.

## Uso de medio plazo

Entradas: panel semanal por protocolo con ingresos, incentivos, supply y liquidez, cada uno con fecha de disponibilidad. Salida: rango esperado de actividad y error residual; no precio justo automático. Para un Screener, un residuo inusual debe abrir una hipótesis y señalar las features causantes, no activar una compra. Los intervalos conformales presuponen que los errores de calibración son representativos; shocks persistentes y cambios de mecanismo de fees pueden romper esa aproximación.

## Primer experimento

Tres features de pasado, una covariable de calendario y horizonte 4 semanas. Comparar contra naive en ventanas móviles y un tramo prospectivo. Medir MAE/WQL según salida, cobertura por régimen y estabilidad de ranking de anomalías. Criterio propuesto: alerta útil identificada por revisión humana, con menos falsas alarmas que z-score simple, y coste de mantenimiento asumible. Si no mejora, conservar solo la normalización/validación.

CPU con 8–16 GB RAM para un panel pequeño es una estimación razonable de presupuesto, no un benchmark; árboles grandes y muchas variantes pueden excederlo. Reutilizar biblioteca y tests conceptuales; evitar entrenamiento continuo, búsqueda de cientos de hiperparámetros y carga de modelos externos.
