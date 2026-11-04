# Chronos forecasting library — revisión técnica estática

ID: `AI-chronos`. Verificado: 2026-11-04. Referencia estratégica: 2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.

Commit: `1224fafa91e1ecd6674f5204066b159e40b5e4a1`. [Repositorio](https://github.com/amazon-science/chronos-forecasting). [Licencia de código](https://raw.githubusercontent.com/amazon-science/chronos-forecasting/1224fafa91e1ecd6674f5204066b159e40b5e4a1/LICENSE). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.

Puntuación editorial: **78/100**. Desglose: utility=21, evidence=12, data=11, ease=8, license=9, maintenance=6, usability=5, differentiation=6. Confianza: media-alta sobre rutas observadas; no sobre eficacia financiera. Los bloqueos de licencia/datos prevalecen.

## Decisión y capacidad aprovechable

Prioridad alta como comparador experimental de magnitudes económicas —fees, actividad, volatilidad—, con baseline sencillo y evaluación prospectiva. La ventaja funcional observable es una interfaz única para series y covariables; no se ha verificado una ventaja de inversión. La [card de Chronos 2](https://huggingface.co/amazon/chronos-2/blob/29ec3766d36d6f73f0696f85560a422f50e8498c/README.md) declara 120 M parámetros, inferencia CPU/GPU y cuantiles; los resultados de velocidad son de sus autores y no se reproducen aquí.

## Ruta técnica inspeccionada

En [Chronos 2 Pipeline](https://github.com/amazon-science/chronos-forecasting/blob/1224fafa91e1ecd6674f5204066b159e40b5e4a1/src/chronos/chronos2/pipeline.py), `predict_df` recibe identificador, timestamp, objetivo(s) y `future_df`. Las columnas presentes solo en historia son covariables pasadas; las presentes también en `future_df` se interpretan como conocidas a futuro. La implementación normaliza el dataframe, prepara tensores y llama al predictor; `predict_fev` conecta explícitamente con tareas fev. Se observan generación de cuantiles, interpolación de niveles y extensión de horizontes por desenrollado. Esto justifica V3 estático, sin afirmar exactitud numérica ejecutada.

La unidad de observación financiera debe quedar fuera del modelo: USD/día de fees no equivale a USD/mes de revenue. Las frecuencias y series se sincronizan antes de inferir; `cross_learning=False` es un punto de partida prudente. Si se activa, fijar una misma fecha de conocimiento para todo el grupo: una serie actualizada después que otra podría filtrar información aunque sus columnas tengan el mismo timestamp económico. Un calendario contractual puede ser covariable futura; un M2 revisado, volumen futuro o precio posterior no.

## Interfaces, dependencias y pruebas

[config.py](https://github.com/amazon-science/chronos-forecasting/blob/1224fafa91e1ecd6674f5204066b159e40b5e4a1/src/chronos/chronos2/config.py) separa configuración del núcleo y forecasting. PyTorch, Transformers, NumPy/Pandas y einops aparecen en la ruta; la adaptación ligera depende de PEFT cuando se usa. [test_chronos 2.py](https://github.com/amazon-science/chronos-forecasting/blob/1224fafa91e1ecd6674f5204066b159e40b5e4a1/test/test_chronos2.py) contiene casos de frecuencia irregular, `future_df` incompleto, dtype, predicciones, embeddings y efecto de cross-learning. Se inspeccionó el caso que exige resultados distintos al activarlo: demuestra que la composición del lote importa, no que mejore la predicción. No se ejecutó ningún test ni se descargaron pesos.

## Licencia, hardware y límites

LICENSE del código Apache 2.0 fue leído. La card de pesos declara Apache 2.0; los datasets de entrenamiento mantienen condiciones propias.120 M pesos FP32 ocuparían aproximadamente 0.48 GB solo en tensores, cálculo aritmético que excluye activaciones, runtime y datos. Para experimentar con pocas series propongo CPU y 8–16 GB RAM como presupuesto, no requisito mínimo medido; GPU opcional, sin comprometer una compra. La extrapolación a 18 meses y el cambio de régimen requieren validación específica.

## Experimento mínimo propuesto

Congelar un panel semanal de fees/volumen con disponibilidad real; comparar naive, seasonal-naive y MLForecast contra Chronos 2 en cortes móviles y un periodo prospectivo intocable. Medir WQL, MAE, cobertura por régimen y tiempo de preparación. Exigir mejora predefinida, por ejemplo≥5% de WQL sin peor cobertura en protocolos pequeños, además de estabilidad de errores; el umbral es propuesta, no resultado. Registrar cada intento y excluir capitalizaciones futuras. Aprovechar pipeline y cuantiles; evitar fine-tuning o SageMaker antes de demostrar utilidad local.
