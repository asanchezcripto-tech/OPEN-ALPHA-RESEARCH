"""Analyst-written static reviews; source links pinned to observed commits."""
import json,re
from pathlib import Path
B=Path(__file__).parent; OUT=B.parent.parent/'03_DEEP_TECHNICAL_REVIEWS'
repos={r['slug']:r for r in json.loads((B/'observations_repos.json').read_text(encoding='utf-8'))}
catalog={c['id']:c for c in json.loads((B/'candidates.json').read_text(encoding='utf-8'))}
hf={r['rid']:r for r in json.loads((B/'observations_hf.json').read_text(encoding='utf-8'))}
def code(s,path):return 'https://github.com/'+repos[s]['repo']+'/blob/'+repos[s]['commit']+'/'+path
def model(rid,path='README.md'):return 'https://huggingface.co/'+rid+'/blob/'+hf[rid]['commit']+'/'+path
TEXTS={
'chronos':'''## Decisión y capacidad aprovechable

Prioridad alta como comparador experimental de magnitudes económicas —fees, actividad, volatilidad—, con baseline sencillo y evaluación prospectiva. La ventaja funcional observable es una interfaz única para series y covariables; no se ha verificado una ventaja de inversión. La [card de Chronos2]({hf:amazon/chronos-2}) declara120M parámetros, inferencia CPU/GPU y cuantiles; los resultados de velocidad son de sus autores y no se reproducen aquí.

## Ruta técnica inspeccionada

En [Chronos2Pipeline]({code:src/chronos/chronos2/pipeline.py}), `predict_df` recibe identificador, timestamp, objetivo(s) y `future_df`. Las columnas presentes solo en historia son covariables pasadas; las presentes también en `future_df` se interpretan como conocidas a futuro. La implementación normaliza el dataframe, prepara tensores y llama al predictor; `predict_fev` conecta explícitamente con tareas fev. Se observan generación de cuantiles, interpolación de niveles y extensión de horizontes por desenrollado. Esto justifica V3 estático, sin afirmar exactitud numérica ejecutada.

La unidad de observación financiera debe quedar fuera del modelo: USD/día de fees no equivale a USD/mes de revenue. Las frecuencias y series se sincronizan antes de inferir; `cross_learning=False` es un punto de partida prudente. Si se activa, fijar una misma fecha de conocimiento para todo el grupo: una serie actualizada después que otra podría filtrar información aunque sus columnas tengan el mismo timestamp económico. Un calendario contractual puede ser covariable futura; un M2 revisado, volumen futuro o precio posterior no.

## Interfaces, dependencias y pruebas

[config.py]({code:src/chronos/chronos2/config.py}) separa configuración del núcleo y forecasting. PyTorch, Transformers, NumPy/Pandas y einops aparecen en la ruta; la adaptación ligera depende de PEFT cuando se usa. [test_chronos2.py]({code:test/test_chronos2.py}) contiene casos de frecuencia irregular, `future_df` incompleto, dtype, predicciones, embeddings y efecto de cross-learning. Se inspeccionó el caso que exige resultados distintos al activarlo: demuestra que la composición del lote importa, no que mejore la predicción. No se ejecutó ningún test ni se descargaron pesos.

## Licencia, hardware y límites

LICENSE del código Apache2.0 fue leído. La card de pesos declara Apache2.0; los datasets de entrenamiento mantienen condiciones propias.120M pesos FP32 ocuparían aproximadamente0.48GB solo en tensores, cálculo aritmético que excluye activaciones, runtime y datos. Para experimentar con pocas series propongo CPU y8–16GB RAM como presupuesto, no requisito mínimo medido; GPU opcional, sin comprometer una compra. La extrapolación a18meses y el cambio de régimen requieren validación específica.

## Experimento mínimo propuesto

Congelar un panel semanal de fees/volumen con disponibilidad real; comparar naive, seasonal-naive y MLForecast contra Chronos2 en cortes móviles y un periodo prospectivo intocable. Medir WQL, MAE, cobertura por régimen y tiempo de preparación. Exigir mejora predefinida, por ejemplo≥5% de WQL sin peor cobertura en protocolos pequeños, además de estabilidad de errores; el umbral es propuesta, no resultado. Registrar cada intento y excluir capitalizaciones futuras. Aprovechar pipeline y cuantiles; evitar fine-tuning o SageMaker antes de demostrar utilidad local.
''',
'timesfm':'''## Decisión y hallazgo determinante

TimesFM3 existe y tiene implementación examinable. Su código actual es Apache2.0, pero los [pesos oficiales3.0]({hf:google/timesfm-3.0-pytorch}) llevan una [licencia propia]({hflic:google/timesfm-3.0-pytorch}) que restringe finalidad comercial y producción y define ampliamente los usos de resultados. La publicación de pesos no autoriza automáticamente un asistente de inversión operativo. Clasificación de esos pesos: SOLO INVESTIGACIÓN / RESTRICCIONES; aclarar el uso antes de adoptarlos. Esta conclusión no es asesoramiento jurídico definitivo. [TimesFM2.5]({hf:google/timesfm-2.5-200m-pytorch}) conserva declaración Apache2.0 en su card y merece comparación separada.

## Arquitectura y rutas

El módulo [timesfm3_forecaster.py]({code:src/timesfm3/timesfm3_forecaster.py}) es ahora un puente de compatibilidad. La ruta efectiva está en [torch/timesfm3_forecaster.py]({code:src/timesfm3/torch/timesfm3_forecaster.py}). La separación importa para no auditar solamente el alias. Se observaron `TimesFM3Forecaster`, `predict`, `predict_batch`, configuración de consulta y `ForecastOutput`, que distingue forecast puntual —mediana— y cuantiles. `_Query` distingue targets, covariables pasadas y covariables pasado/futuro; no incorporar valores futuros reconstruidos como si fueran conocidos.

La ruta también implementa interpolación lineal de NaN por fila y normalización con defensas frente a media/varianza no finitas. Inferencia propia: imputar usando observaciones posteriores al corte convertiría una prueba retrospectiva en información anticipada. Por eso recortar por `knowledge_time` antes de cualquier transformación; retener máscara de imputación y comparar con ausencia explícita. Los huecos de publicación macro no son necesariamente datos perdidos intercambiables con huecos de sensor.

## Dependencias, estado y pruebas

[pyproject.toml]({code:pyproject.toml}) declara versión3.0.2, Python≥3.10, NumPy, Hugging Face Hub y safetensors, con extras separados para torch/MLX/flax/xreg. [backward_compat_test.py]({code:src/timesfm3/backward_compat_test.py}) comprueba rutas de importación antiguas; no constituye validación económica ni paridad numérica. Se observó el árbol de tests general, pero no se ejecutó. El commit está fijado; no se reconstruyó su hora de disponibilidad al cierre del3.

## Coste y comparación

La card describe aproximadamente0.3B parámetros FP32:≈1.2GB para pesos es solo una estimación aritmética, no RAM total. Presupuesto experimental16GB RAM y GPU opcional, sujeto a longitud, lote y backend; latencia no medida. Chronos2 ofrece una alternativa documentalmente más simple para permisos y una integración fev observada. La versión más reciente no debe ganar por nombre: comparar TimesFM2.5,3.0 —solo en uso permitido— y naive en exactamente los mismos cortes.

## Primera utilidad y aceptación

Probar escenarios de fees/actividad agregada y sensibilidad a covariables con un archivo histórico congelado. Exigir que una mejora agregada sobreviva al desglose por activo, periodo y nivel de missingness; medir también cobertura y abstención. No usar forecast de precio para derivar automáticamente un precio objetivo de token. Aprovechar tipado de inputs, normalización controlada y diseño multivariable; aplazar integración operativa de pesos3.0 hasta resolver permisos y validación independiente.
''',
'uni2ts':'''## Decisión

Uni2TS aporta una arquitectura útil para estudiar observaciones faltantes, máscaras y forecasting probabilístico. El código es Apache2.0; [Moirai2.0-R-small]({hf:Salesforce/moirai-2.0-R-small}) y [Moirai1.1-R-small]({hf:Salesforce/moirai-1.1-R-small}) declaran CC-BY-NC4.0. No clasificar el conjunto como reutilización permisiva. El tamaño pequeño de Moirai2 reduce una barrera de hardware, pero ni su licencia ni su precisión financiera se deducen de ese tamaño.

## Arquitectura observada

[Moirai2Forecast]({code:src/uni2ts/model/moirai2/forecast.py}) construye un `PyTorchPredictor` de GluonTS, utiliza `TFTInstanceSplitter` con ventanas de pasado/futuro y genera `QuantileForecastGenerator` a partir de los niveles del módulo. Diferencia covariables dinámicas conocidas de covariables solo pasadas; añade indicadores de observación. El camino univariado usa imputación causal en su transformación por defecto. [Moirai2Module]({code:src/uni2ts/model/moirai2/module.py}) contiene escalado empaquetado, máscara de atención causal, TransformerEncoder y bloques de embedding; se inspeccionaron imports, constructor e interfaces.

La diferencia entre máscara técnica y disponibilidad económica es decisiva: una cifra revisada puede estar presente en un dataframe sin haber sido pública en la fecha simulada. El modelo no conoce esa diferencia. Para crypto, separar ausencia de actividad real, ausencia de indexación y métrica que todavía no se publicó. Un cero imputado sin motivo puede parecer un colapso económico.

## Calidad y mantenimiento

[pyproject.toml]({code:pyproject.toml}) y las interfaces muestran PyTorch/Lightning, GluonTS y componentes propios. [test_moirai.py]({code:test/model/test_moirai.py}) incluye pruebas de pretraining, transformación, forecast y modificación temporal de hiperparámetros. Son rutas de Moirai original: su presencia no demuestra cobertura completa de Moirai2. No se han ejecutado pruebas ni benchmarks. El repositorio accesible no archivado no basta para afirmar cadencia de mantenimiento sostenible.

## Datos, recursos y límites

La card de Moirai2 declara11.4M parámetros y mezcla de datos públicos, sintéticos y operativos internos; no puede reconstruirse todo el preentrenamiento con lo examinado.≈46MB FP32 es memoria de pesos calculada, no RAM de proceso. Un presupuesto8–16GB RAM/CPU para pocas series es una estimación de experimento; GPU no imprescindible por principio, rendimiento local pendiente. Los benchmarks genéricos y datasets internos reducen la capacidad de evaluar contaminación financiera global.

## Oportunidad independiente y contraste

Propuesta: usar la distinción observación/máscara como componente de un monitor de calidad de fundamentales y comparar el forecast de ingresos de protocolo con naive y Chronos2. Medir degradación al introducir huecos artificiales y cambios de frecuencia, manteniendo un mismo corte de conocimiento. Criterio propuesto: conservar cobertura de intervalos y no producir alertas económicas por fallos de ingesta. Una mejora de forecasting puede reducir ruido de revisión diaria sin anticipar retornos.

Aprovechar las transformaciones y conceptos bajo licencia de código compatible, fijando atribución y versiones. Aplazar uso operativo de pesos y entrenamiento propio hasta resolver permisos y comprobar que un baseline estadístico no cumple ya la función. No preentrenar otra foundation model para este usuario.
''',
'fev':'''## Decisión

Es una de las piezas más útiles del área: convierte una comparación informal de modelos en una tarea con identidad, horizonte, cortes y resultados repetibles. La utilidad no depende de que gane ningún modelo. Se propone adoptar como biblioteca de evaluación después de una prueba aislada autorizada, pendiente en este mandato. Código Apache2.0 inspeccionado; datasets evaluados conservan sus propias condiciones.

## Qué implementa la ruta crítica

[task.py]({code:src/fev/task.py}) contiene `Task` y `EvaluationWindow`. `_get_past_future_test_data` corta pasado/futuro y elimina targets y covariables solo pasadas de la porción futura que se entrega al modelo. `get_ground_truth` mantiene aparte la verdad para evaluar. `clean_and_validate_predictions` normaliza salidas al esquema de la tarea; `evaluation_summary` y fingerprints permiten identificar configuraciones. La división explícita limita una clase concreta de fuga, pero no verifica por sí misma que el usuario haya marcado correctamente una covariable como conocida.

[metrics.py]({code:src/fev/metrics.py}) implementa MAE/MASE/RMSSE y pérdidas de cuantiles, entre otras. La normalización debe interpretarse según la variable: MAPE cerca de cero y escalas con poca variación pueden resultar inestables. No mezclar el score de fees, precio y retornos en una cifra de éxito económico sin ponderación explícita. Este juicio es metodológico, no un resultado observado en la biblioteca.

## Tests, dependencias y vacíos

[test_task.py]({code:test/test_task.py}) se examinó como texto junto con rutas de validación; no se ejecutó. La biblioteca usa Hugging Face datasets, Arrow, NumPy, Pandas y Pydantic según imports/configuración. Es más pequeña que un entrenador universal, aunque la descarga predeterminada de datasets podría ser muy grande: registrar manifest y seleccionar una muestra propia. La licencia Apache del motor no convierte `autogluon/fev_datasets` o `chronos_datasets`, con licencias por configuración, en una colección de permiso uniforme.

## Límite financiero importante

Si se suministra macro revisada con fechas originales, el corte temporal parecerá correcto y la prueba será errónea. Construir primero una vista `available_at<=cutoff`, versionada, con latencia de publicación, universo histórico y reservas sobre rectificaciones. Para horizontes solapados, la incertidumbre de métricas requiere bloques temporales; fev no equivale a purged cross-validation de etiquetas de trading. La organización AutoGluon participa en modelos comparados: un leaderboard mantenido por un proveedor no es una prueba independiente ciega.

## Experimento mínimo

Crear una tarea semanal de actividad/fees para5–10protocolos y un target de volatilidad realizada; congelar schema, unidad, universo, cortes y hash de fuentes. Comparar naive, StatsForecast, MLForecast y un único modelo preentrenado. Registrar resultados por protocolo y régimen y coste de inferencia. Criterio propuesto: reconstruir exactamente una tarea desde su manifest, rechazar deliberadamente entradas futuras y reproducir las métricas en una segunda revisión. La utilidad inmediata es detectar comparaciones inválidas antes de invertir tiempo en modelos.

CPU y8GB RAM son presupuesto orientativo para panel pequeño; el consumo lo determinarán los datos/modelos. Evitar AutoML masivo, GPU y dashboards de ranking antes de fijar esta disciplina.
''',
'mlforecast':'''## Decisión

MLForecast merece prioridad sobre entrenar un Transformer desde cero: expone lags, transformaciones, modelos tabulares y validación temporal en un flujo relativamente compacto. La recomendación es condicional al problema: predecir actividad, volatilidad o clasificar riesgo, comparando siempre con naive. No se propone convertir un forecast de retorno en señal automática. LICENSE Apache2.0 leído; dependencias y datos siguen requiriendo revisión separada.

## Arquitectura inspeccionada

[core.py]({code:mlforecast/core.py}) representa series agrupadas y construye features locales/pooled, transformaciones de targets y predicción recursiva o por múltiples horizontes. La ruta importa `coreforecast`, `utilsforecast`, NumPy, Pandas, Narwhals y estimadores compatibles con scikit-learn. [forecast.py]({code:mlforecast/forecast.py}) coordina `fit`, `predict`, `cross_validation`, intervalos y transferencia/recalibración. Se examinó `_check_out_of_sample`, que rechaza ventanas anteriores al fin de entrenamiento para evitar calibrar intervalos sobre datos de ajuste.

`cross_validation` permite fijar ventanas, horizonte, paso y frecuencia de refit; esto es mejor que una partición aleatoria de filas para series. Sin embargo, no garantiza embargo/purga para etiquetas de retornos solapadas ni que la selección de variables se haga dentro de cada ventana. La identidad de serie debe ser estable: reutilizar un ticker para otro activo puede contaminar estado y transferencias.

## Calidad, seguridad y alternativas

[test_forecast.py]({code:tests/test_forecast.py}) y el árbol de tests muestran casos de forecasting, conformal y actualización; se inspeccionaron rutas y firmas, sin ejecución ni medición de cobertura. El uso de cloudpickle/fsspec en persistencia significa que un futuro desarrollo debe cargar solo artefactos propios de procedencia conocida; no se cargó ninguno. La complejidad crece con pooled features y horizontes: empezar con lags explícitos y un único estimador LightGBM o regresión sencilla. StatsForecast es mejor si basta un baseline univariado; Chronos2 es comparación útil cuando el histórico propio es escaso.

## Uso de medio plazo

Entradas: panel semanal por protocolo con ingresos, incentivos, supply y liquidez, cada uno con fecha de disponibilidad. Salida: rango esperado de actividad y error residual; no precio justo automático. Para un Screener, un residuo inusual debe abrir una hipótesis y señalar las features causantes, no activar una compra. Los intervalos conformales presuponen que los errores de calibración son representativos; shocks persistentes y cambios de mecanismo de fees pueden romper esa aproximación.

## Primer experimento

Tres features de pasado, una covariable de calendario y horizonte4semanas. Comparar contra naive en ventanas móviles y un tramo prospectivo. Medir MAE/WQL según salida, cobertura por régimen y estabilidad de ranking de anomalías. Criterio propuesto: alerta útil identificada por revisión humana, con menos falsas alarmas que z-score simple, y coste de mantenimiento asumible. Si no mejora, conservar solo la normalización/validación.

CPU con8–16GB RAM para un panel pequeño es una estimación razonable de presupuesto, no un benchmark; árboles grandes y muchas variantes pueden excederlo. Reutilizar biblioteca y tests conceptuales; evitar entrenamiento continuo, búsqueda de cientos de hiperparámetros y carga de modelos externos.
''',
'river':'''## Decisión y oportunidad poco obvia

Usar River como monitor de cambios en el error de nuestros indicadores y en la calidad de datos, además de cambios del mercado. Si el proveedor cambia una definición de revenue, puede ser más útil detectar ese cambio que predecir el precio siguiente. ADWIN es un componente proporcionado para esto; su alarma significa incompatibilidad estadística con el historial reciente, no una nueva oportunidad rentable.

## Implementación comprobada

[adwin.py]({code:river/drift/adwin.py}) expone `delta`, `clock`, `max_buckets`, `min_window_length` y `grace_period`; mantiene estimación, varianza y anchura y reinicia su helper después de una detección. La implementación pesada está ahora en [rust_src/adwin.rs]({code:rust_src/adwin.rs}). Se inspeccionaron inserción con actualización de varianza, compresión de buckets, exploración de cortes y umbral dependiente de tamaños/varianza. No se debe presentar como código puramente Python: la construcción usa Rust/maturin.

El umbral depende de `delta`, pero no se ha demostrado aquí que la tasa de falsas alarmas en funding o fees autocorrelacionados sea ese valor. La interpretación cripto exige controlar estacionalidad, escala, outliers, faltantes y actualizaciones tardías. Actualizar el detector primero con una observación y después evaluar su error puede introducir contaminación de la evaluación: en aprendizaje online se conserva la secuencia predecir→observar→puntuar→actualizar.

## Tests y requisitos

[test_adwin_regression.py]({code:tests/drift/test_adwin_regression.py}) contiene casos de saltos, ausencia de drift, estadísticas exactas, parámetros, valores grandes/negativos y serialización. También hay tests Rust en el archivo del motor; no se ejecutaron. [pyproject.toml]({code:pyproject.toml}) declara versión0.26.1, Python≥3.11, NumPy/SciPy/Narwhals. El Python3.10 observado en la máquina no cumple esta versión; sería necesario un entorno futuro adecuado, no modificar ahora el del usuario. Licencia BSD3-Clause inspeccionada.

## Diseño mínimo de uso

Entradas: pérdida predictiva normalizada, fracción de datos ausentes y diferencia entre dos fuentes para una métrica. Mantener un detector por señal y registrar cada cambio con snapshot, parámetros, observaciones y ventana. Salida: alerta con evidencia y etiqueta provisional «mercado», «cambio de definición» o «fallo de ingesta». La clasificación final requiere revisión y comparación cruzada; el detector no identifica causalidad.

## Experimento y decisión de adopción

Reproducir una serie estable sintética y una con cambios conocidos en un entorno aislado futuro; después insertar huecos/revisiones en una copia de datos y comparar contra EWMA/robust z-score. Medir demora de detección, falsas alarmas por mes y tiempo humano de diagnóstico. Criterio propuesto: mantener el presupuesto de alertas acordado —por ejemplo≤2falsas/mes por panel— y mejorar la detección de errores de fuente sin disparar más revisiones innecesarias. No optimizar delta sobre el periodo de evaluación.

CPU basta para estos streams; presupuesto8GB RAM incluye entorno y datos pequeños, no medición. Reutilizar detector y representación incremental; no desplegar Kafka ni entrenar un agente que elija detectores si unas pocas señales predefinidas resuelven el problema. Alternativa `ruptures` para segmentación retrospectiva: responde una pregunta distinta de detección online.
''',
'tradingagents':'''## Veredicto

El repositorio actual contiene controles temporales concretos que merecen extraerse; descartarlo solo por ser multiagente ignoraría trabajo útil. Tampoco sus debates constituyen evidencia de ventaja de mercado. Priorizar controles as-of, abstención y estado de investigación; mantener el sistema completo como referencia hasta medir coste y exactitud frente a un flujo sencillo. Código Apache2.0 inspeccionado; proveedores de datos/LLM son contratos separados.

## Arquitectura y controles observados

[trading_graph.py]({code:tradingagents/graph/trading_graph.py}) coordina configuración de agentes, identidad del instrumento, memoria, checkpoints y reportes; observa `asset_type` crypto y estado de cartera. La firma de ejecución incluye parámetros que cambian el análisis, evitando reutilizar un checkpoint bajo otra configuración. `_memory_as_of` impone un corte a lecciones históricas; para ejecución del día el filtro cambia. Estos detalles son útiles para Thesis Tracker porque el pasado de una tesis no debe enriquecerse silenciosamente con lecciones posteriores.

[date_window.py]({code:tradingagents/dataflows/date_window.py}) limita la fecha solicitada por una herramienta a la fecha del análisis, canonicaliza fechas y valida ventanas. También retiene perfiles live-only sin vintage e información de operaciones sin fecha de divulgación en análisis históricos. Esto reconoce que timestamp del evento y del conocimiento son distintos. No garantiza que todos los proveedores estén completos ni que un LLM no recuerde hechos posteriores por preentrenamiento.

## Evidencia de pruebas y límites

[test_tool_date_enforcement.py]({code:tests/test_tool_date_enforcement.py}) comprueba fechas futuras, identidad del instrumento, fechas omitidas y ventanas inválidas. [test_fundamentals_lookahead.py]({code:tests/test_fundamentals_lookahead.py}) exige retirar perfiles actuales en retrospectiva, incluso no realizar la llamada. Son verificaciones estáticas de diseño de tests, sin ejecución ni cobertura cuantificada. No es correcto afirmar que «no existe control de leakage» para este commit; sí es correcto que lo observado no resuelve contaminación del modelo ni todos los datos revisados.

## Riesgos prácticos

LangGraph y clientes LLM amplían superficie de dependencias. Noticias y documentos son entradas no confiables: una cita no debe convertirse en instrucción de herramientas. Permisos de lectura sola, destinos permitidos, límite de gasto y salida con referencias son controles a añadir/verificar para un producto futuro. No se probó aislamiento frente a prompt injection. El precio depende de tokens, número de agentes, rondas y proveedores: no se proporciona una tarifa inventada. CPU local8–16GB puede alojar orquestación, pero no implica capacidad de inferencia local del modelo elegido.

## Experimento propuesto

Veinte preguntas sobre cambios de tesis, cada una con fuentes congeladas y respuesta humana. Comparar flujo determinista + un modelo frente a debate de múltiples agentes usando el mismo corpus y presupuesto. Puntuar exactitud de citas, cifras recalculadas, contradicciones detectadas, abstención y minutos de revisión. Incluir documentos adversariales y futuras publicaciones que deben excluirse. Adoptar pasos extra solo si mejoran resultados fuera del conjunto usado para ajustar prompts.

Aprovechar controles temporales y trazabilidad; evitar tomar rating final, consenso narrativo o backtest con conocimiento retrospectivo como recomendación de inversión.
''',
'docling':'''## Decisión

Docling es candidato prioritario para convertir informes, gobernanza y documentación en evidencia inspeccionable. Su valor es la extracción estructurada con estados y ubicación, antes de generar respuestas. El código MIT no significa que cualquier OCR/VLM añadido tenga la misma licencia. Para páginas HTML sencillas, Trafilatura será más proporcionado; reservar Docling para tablas, PDF y formatos heterogéneos.

## Arquitectura comprobada

[document_converter.py]({code:docling/document_converter.py}) selecciona backend/opciones por formato y ejecuta pipelines, con configuración de errores, caché de inicialización y procesamiento por lotes. Se inspeccionó `_execute_pipeline`: distingue entrada inválida, falta de pipeline y conversión; descarga recursos del documento cuando corresponde. [base_models.py]({code:docling/datamodel/base_models.py}) define estados como éxito parcial/fallo, elementos de página, estructuras de tablas y reportes de confianza. El resultado estructurado permite conservar información que se pierde al aplanar todo a texto.

El contrato de un futuro extractor financiero debe conservar documento/hash, página y región, tabla/fila/columna, unidad, valor textual y valor interpretado, así como `published_at` y `acquired_at`. Es propuesta de diseño: Docling no determina por sí mismo el momento en que una información fue pública ni si un fee es revenue del tenedor. Un campo numérico debe pasar comprobaciones de escala, signos, moneda y suma antes de formar parte de una tesis.

## Tests y seguridad observados

[test_failed_pages.py]({code:tests/test_failed_pages.py}) distingue éxito parcial y páginas presentes; una nota del propio archivo indica que ciertos fixtures ya no ejercitan fallos con una versión reciente de docling-parse. Por tanto, no afirmar cobertura completa de páginas fallidas a partir de su nombre. [test_hf_model_download_security.py]({code:tests/test_hf_model_download_security.py}) verifica revisión fijada por SHA y el comportamiento de advertencia/rechazo cuando se confía en código remoto no fijado. Una revisión fijada no es una auditoría del código: estos tests reducen movilidad de dependencia, no demuestran seguridad integral. No se ejecutó conversión ni se descargó modelo.

## Costes y permisos

Hay rutas locales y opciones de modelos/servicios que cambian coste, precisión y permisos. Estimación para piloto: CPU,16GB RAM, decenas de documentos seleccionados; GPU opcional si la muestra demuestra necesidad. No confundir este presupuesto con requisitos universales ni con benchmark de tablas. Dependencias principales observadas: docling-core, backends de formatos, Pydantic y componentes de pipeline. Antes de habilitar OCR/VLM revisar su card, formato de pesos y descargas; no atribuirle al paquete la licencia de todas las entradas.

## Primera capacidad útil y aceptación

Extraer50hechos de5documentos públicos de protocolos y conservar enlace exacto al fragmento. Una persona marca tabla/unidad/fecha correctas; la aritmética se calcula de forma determinista. Métricas: precisión de campos numéricos, cobertura de referencias, porcentaje de abstención y tiempo de corrección. Criterio propuesto:100% de cifras utilizadas con fuente localizable y ninguna página fallida tratada como completa; exactitud mínima y tamaño de muestra deben predefinirse. Si falla una tabla, abstenerse o usar lectura manual.

Evitar primero bases vectoriales distribuidas y agentes complejos. Un índice local sobre documentos con buen provenance aporta más que una conversación fluida sin coordenadas de evidencia.
''',
'fingpt':'''## Decisión crítica

FinGPT es un conjunto amplio de tareas y ejemplos, no un modelo único con una licencia única. Su código MIT es reutilizable con condiciones; pesos base, adapters, noticias y proveedores deben evaluarse aparte. La ruta Forecaster tiene suficiente evidencia estática para identificar riesgos temporales concretos. No la recomendaría como motor de previsión financiera sin corregirlos y probarla prospectivamente. Sí conservaría sus ideas de corpus y tareas para diseñar una evaluación propia.

## Flujo y hallazgo reproducible

[data_pipeline.py]({code:fingpt/FinGPT_Forecaster/data_pipeline.py}) encadena adquisición, preparación de prompts, consulta a GPT y transformación de dataset. [data.py]({code:fingpt/FinGPT_Forecaster/data.py}) conecta precios/noticias/fundamentales y `gpt4_to_llama` transforma respuestas de entrenamiento generadas condicionando el razonamiento al movimiento conocido. Es una técnica de creación de etiquetas/explicaciones; no es demostración de que un modelo habría anticipado ese movimiento con información real disponible.

[prompt.py]({code:fingpt/FinGPT_Forecaster/prompt.py}) obtiene perfiles de empresa mediante Finnhub y de crypto mediante `yfinance.Ticker.info`; incluye capitalización actual y otros atributos, y `get_all_prompts` reutiliza la introducción al construir prompts históricos. Inferencia técnica: reconstruir hoy un prompt pasado por esta ruta puede añadir información de hoy. La presencia de tal riesgo en esta ruta no demuestra que todos los experimentos o módulos FinGPT lo sufran.

## Correcciones existentes y alcance

[basics.py]({code:fingpt/FinGPT_Forecaster/basics.py}) ya intenta evitar usar resultados al cierre del trimestre: añade45días como disponibilidad estimada. Es mejor que igualar periodo contable y publicación, pero no registra una fecha real de publicación ni protege frente a revisiones posteriores del proveedor. No tratar45días como regla financiera universal. Separar valor observado, vintage y estimación de disponibilidad; si falta la fecha real, marcar incertidumbre/abstención.

Se inspeccionaron requisitos, imports e interfaces de Forecaster. Dependencias incluyen Finnhub/yfinance, datasets, Pandas y cliente de LLM; hay costes/condiciones externas. No se ejecutaron tests, pipelines ni notebooks. La calidad de otras áreas de FinGPT no fue auditada por completo. El tamaño del repositorio y la cantidad de modelos listados no equivalen a cobertura de pruebas.

## Alternativa y utilidad recuperable

Una biblioteca de extractores con corpus propio y respuestas verificables es más proporcionada que fine-tuning inicial. Para Thesis Tracker, pedir al modelo hechos citados y contradicciones; calcular cifras fuera del LLM. TradingAgents actual ofrece controles as-of inspeccionados que sirven de contraste, aunque tampoco elimina el conocimiento futuro interno de un LLM moderno.

## Experimento mínimo para rehabilitar la ruta

Preparar inputs históricos con perfiles/supply de la fecha, noticias adquiridas entonces y reglas de rechazo. Comparar prompts con/sin introducción actual para cuantificar cuánto cambia el resultado; registrar esto como diagnóstico de leakage, no como rentabilidad. Luego evaluar de forma prospectiva con baseline simple, umbral de abstención y costes. Entrenar solo después de reservar empresas, periodos y fuentes fuera de ajuste. El criterio primero es fidelidad temporal100% de los inputs usados, después precisión de extracción y calibración.

Presupuesto de inferencia depende del LLM y proveedor;8–16GB RAM sirven para orquestar pequeños corpus, no para entrenar7B–13B. No hay cifra de coste recurrente verificada ni justificación actual para comprar GPU.
''',
'finbert':'''## Decisión y licencia

FinBERT sigue siendo una referencia útil de clasificación de sentimiento financiero en inglés; no es un predictor de rendimientos. En el snapshot, el repositorio contiene aviso de12-oct-2026 que limita Apache2.0 al código y remite los pesos a su [card]({hf:ProsusAI/finbert}), donde se declara CC-BY-NC-SA4.0. Financial PhraseBank tiene condiciones separadas CC-BY-NC-SA3.0 y el preentrenamiento utiliza Reuters TRC2 con términos propios. No asumir uso comercial libre porque la carpeta de código contiene Apache.

## Ruta técnica observada

[finbert.py]({code:finbert/finbert.py}) segmenta texto en frases, convierte a features, ejecuta el clasificador en modo evaluación y calcula softmax para tres clases. Su función legacy `predict` fija64tokens por frase en la conversión y construye un score como diferencia entre positivo y negativo. [utils.py]({code:finbert/utils.py}) contiene tokenización/padding, softmax y métricas por clase. El score de softmax no está calibrado como probabilidad de subida de un token. Frases largas sobre gobernanza o tokenomics pueden perder información decisiva en un camino con truncado corto; una integración Transformers moderna es una interfaz distinta que debe configurarse y probarse.

## Datos y pertinencia para crypto

Las etiquetas financieras inglesas no cubren automáticamente lenguaje de comunidades, ironía, vocabulario técnico ni texto español. Una noticia positiva para uso de protocolo puede ser negativa para captura de valor del token; una quema puede ser financiada por emisión superior. Conviene separar tono textual, hecho económico, mecanismo afectado y activo. Para un monitor de narrativas, el primer target debería ser recuperación/clasificación de temas con anotaciones propias, y solo después tono.

## Pruebas y hardware

Se inspeccionaron implementación y entorno; no se ejecutaron modelos ni se verificó una suite completa de tests del repositorio. La card especifica arquitectura BERT-base de12capas y tres clases. Un proceso pequeño sobre CPU puede ser viable; se propone presupuesto8GB RAM para prueba, sin medir latencia. No se descargaron pesos. Un modelo pequeño evita algunos costes de LLM remoto, pero no resuelve permisos ni cambio de dominio.

## Experimento recomendado

Etiquetar un corpus propio de100–200fragmentos de protocolos, preservando documento/fecha y separando idiomas. Dos anotadores —o revisión humana en dos pasadas— distinguen tono y efecto económico; incluir negativos difíciles: incentivos que aumentan volumen sin revenue, explotación con recuperación parcial y recompras sin burn. Dividir por documento y fecha, evitando que paráfrasis del mismo anuncio aparezcan en train y test. Medir macro-F1, matriz de confusión y calibración de etiquetas; no usar PnL como sustituto de la calidad de extracción.

Criterio propuesto: justificar una mejora frente a reglas/TF-IDF con coste y tasa de errores aceptables para revisión humana. Antes de uso operativo aclarar condiciones de pesos/datos. Aprovechar la tarea y el baseline metodológico; no ajustar decisiones de cartera por sumar sentimiento diario ni suponer que una etiqueta positiva informa sobre valoración a18meses.
'''
}
for slug,body in TEXTS.items():
 c=catalog['AI-'+slug];r=repos[slug]
 body=re.sub(r'\{code:([^}]+)\}',lambda m:code(slug,m.group(1)),body)
 body=re.sub(r'\{hflic:([^}]+)\}',lambda m:model(m.group(1),'LICENSE'),body)
 body=re.sub(r'\{hf:([^}]+)\}',lambda m:model(m.group(1)),body)
 header='# '+c['name']+' — revisión técnica estática\n\n'
 header+='ID: `'+c['id']+'`. Verificado:2026-11-04. Referencia estratégica:2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.\n\n'
 header+='Commit: `'+r['commit']+'`. [Repositorio]('+c['url']+'). [Licencia de código]('+str(c['license_url'])+'). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.\n\n'
 header+='Puntuación editorial: **'+str(sum(c['scores'].values()))+'/100**. Desglose: '+', '.join(k+'='+str(v) for k,v in c['scores'].items())+'. Confianza: '+c['confidence']+'. Los bloqueos de licencia/datos prevalecen.\n\n'
 (OUT/('ai_'+slug+'.md')).write_text(header+body,encoding='utf-8')
print('10 revisiones escritas')
