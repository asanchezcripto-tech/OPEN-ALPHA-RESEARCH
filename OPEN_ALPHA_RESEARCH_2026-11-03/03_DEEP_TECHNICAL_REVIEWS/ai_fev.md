# Forecast Evaluation (fev) — revisión técnica estática

ID: `AI-fev`. Verificado: 2026-11-04. Referencia estratégica: 2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.

Commit: `13b1913881bb7c680d47262bbc32327304bb0571`. [Repositorio](https://github.com/autogluon/fev). [Licencia de código](https://raw.githubusercontent.com/autogluon/fev/13b1913881bb7c680d47262bbc32327304bb0571/LICENSE). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.

Puntuación editorial: **86/100**. Desglose: utility=23, evidence=13, data=13, ease=10, license=9, maintenance=6, usability=6, differentiation=6. Confianza: media-alta sobre rutas observadas; no sobre eficacia financiera. Los bloqueos de licencia/datos prevalecen.

## Decisión

Es una de las piezas más útiles del área: convierte una comparación informal de modelos en una tarea con identidad, horizonte, cortes y resultados repetibles. La utilidad no depende de que gane ningún modelo. Se propone adoptar como biblioteca de evaluación después de una prueba aislada autorizada, pendiente en este mandato. Código Apache 2.0 inspeccionado; datasets evaluados conservan sus propias condiciones.

## Qué implementa la ruta crítica

[task.py](https://github.com/autogluon/fev/blob/13b1913881bb7c680d47262bbc32327304bb0571/src/fev/task.py) contiene `Task` y `EvaluationWindow`. `_get_past_future_test_data` corta pasado/futuro y elimina targets y covariables solo pasadas de la porción futura que se entrega al modelo. `get_ground_truth` mantiene aparte la verdad para evaluar. `clean_and_validate_predictions` normaliza salidas al esquema de la tarea; `evaluation_summary` y fingerprints permiten identificar configuraciones. La división explícita limita una clase concreta de fuga, pero no verifica por sí misma que el usuario haya marcado correctamente una covariable como conocida.

[metrics.py](https://github.com/autogluon/fev/blob/13b1913881bb7c680d47262bbc32327304bb0571/src/fev/metrics.py) implementa MAE/MASE/RMSSE y pérdidas de cuantiles, entre otras. La normalización debe interpretarse según la variable: MAPE cerca de cero y escalas con poca variación pueden resultar inestables. No mezclar el score de fees, precio y retornos en una cifra de éxito económico sin ponderación explícita. Este juicio es metodológico, no un resultado observado en la biblioteca.

## Tests, dependencias y vacíos

[test_task.py](https://github.com/autogluon/fev/blob/13b1913881bb7c680d47262bbc32327304bb0571/test/test_task.py) se examinó como texto junto con rutas de validación; no se ejecutó. La biblioteca usa Hugging Face datasets, Arrow, NumPy, Pandas y Pydantic según imports/configuración. Es más pequeña que un entrenador universal, aunque la descarga predeterminada de datasets podría ser muy grande: registrar manifest y seleccionar una muestra propia. La licencia Apache del motor no convierte `autogluon/fev_datasets` o `chronos_datasets`, con licencias por configuración, en una colección de permiso uniforme.

## Límite financiero importante

Si se suministra macro revisada con fechas originales, el corte temporal parecerá correcto y la prueba será errónea. Construir primero una vista `available_at<=cutoff`, versionada, con latencia de publicación, universo histórico y reservas sobre rectificaciones. Para horizontes solapados, la incertidumbre de métricas requiere bloques temporales; fev no equivale a purged cross-validation de etiquetas de trading. La organización AutoGluon participa en modelos comparados: un leaderboard mantenido por un proveedor no es una prueba independiente ciega.

## Experimento mínimo

Crear una tarea semanal de actividad/fees para 5–10 protocolos y un target de volatilidad realizada; congelar schema, unidad, universo, cortes y hash de fuentes. Comparar naive, StatsForecast, MLForecast y un único modelo preentrenado. Registrar resultados por protocolo y régimen y coste de inferencia. Criterio propuesto: reconstruir exactamente una tarea desde su manifest, rechazar deliberadamente entradas futuras y reproducir las métricas en una segunda revisión. La utilidad inmediata es detectar comparaciones inválidas antes de invertir tiempo en modelos.

CPU y 8 GB RAM son presupuesto orientativo para panel pequeño; el consumo lo determinarán los datos/modelos. Evitar AutoML masivo, GPU y dashboards de ranking antes de fijar esta disciplina.
