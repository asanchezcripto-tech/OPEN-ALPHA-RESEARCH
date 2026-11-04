# Uni 2 TS / Moirai — revisión técnica estática

ID: `AI-uni2ts`. Verificado: 2026-11-04. Referencia estratégica: 2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.

Commit: `cfd46d4510ed8896f263116f32928eede05b0a75`. [Repositorio](https://github.com/SalesforceAIResearch/uni2ts). [Licencia de código](https://raw.githubusercontent.com/SalesforceAIResearch/uni2ts/cfd46d4510ed8896f263116f32928eede05b0a75/LICENSE.txt). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.

Puntuación editorial: **62/100**. Desglose: utility=17, evidence=11, data=10, ease=6, license=4, maintenance=5, usability=4, differentiation=5. Confianza: media-alta sobre rutas observadas; no sobre eficacia financiera. Los bloqueos de licencia/datos prevalecen.

## Decisión

Uni 2 TS aporta una arquitectura útil para estudiar observaciones faltantes, máscaras y forecasting probabilístico. El código es Apache 2.0; [Moirai 2.0-R-small](https://huggingface.co/Salesforce/moirai-2.0-R-small/blob/30f43ff08c8494f4943ae1521e9d4e94a0fbb389/README.md) y [Moirai 1.1-R-small](https://huggingface.co/Salesforce/moirai-1.1-R-small/blob/0c24ab99db2c1a70ea2a0fc03bf113329772ac64/README.md) declaran CC-BY-NC4.0. No clasificar el conjunto como reutilización permisiva. El tamaño pequeño de Moirai 2 reduce una barrera de hardware, pero ni su licencia ni su precisión financiera se deducen de ese tamaño.

## Arquitectura observada

[Moirai 2 Forecast](https://github.com/SalesforceAIResearch/uni2ts/blob/cfd46d4510ed8896f263116f32928eede05b0a75/src/uni2ts/model/moirai2/forecast.py) construye un `PyTorchPredictor` de GluonTS, utiliza `TFTInstanceSplitter` con ventanas de pasado/futuro y genera `QuantileForecastGenerator` a partir de los niveles del módulo. Diferencia covariables dinámicas conocidas de covariables solo pasadas; añade indicadores de observación. El camino univariado usa imputación causal en su transformación por defecto. [Moirai 2 Module](https://github.com/SalesforceAIResearch/uni2ts/blob/cfd46d4510ed8896f263116f32928eede05b0a75/src/uni2ts/model/moirai2/module.py) contiene escalado empaquetado, máscara de atención causal, TransformerEncoder y bloques de embedding; se inspeccionaron imports, constructor e interfaces.

La diferencia entre máscara técnica y disponibilidad económica es decisiva: una cifra revisada puede estar presente en un dataframe sin haber sido pública en la fecha simulada. El modelo no conoce esa diferencia. Para crypto, separar ausencia de actividad real, ausencia de indexación y métrica que todavía no se publicó. Un cero imputado sin motivo puede parecer un colapso económico.

## Calidad y mantenimiento

[pyproject.toml](https://github.com/SalesforceAIResearch/uni2ts/blob/cfd46d4510ed8896f263116f32928eede05b0a75/pyproject.toml) y las interfaces muestran PyTorch/Lightning, GluonTS y componentes propios. [test_moirai.py](https://github.com/SalesforceAIResearch/uni2ts/blob/cfd46d4510ed8896f263116f32928eede05b0a75/test/model/test_moirai.py) incluye pruebas de pretraining, transformación, forecast y modificación temporal de hiperparámetros. Son rutas de Moirai original: su presencia no demuestra cobertura completa de Moirai 2. No se han ejecutado pruebas ni benchmarks. El repositorio accesible no archivado no basta para afirmar cadencia de mantenimiento sostenible.

## Datos, recursos y límites

La card de Moirai 2 declara 11.4 M parámetros y mezcla de datos públicos, sintéticos y operativos internos; no puede reconstruirse todo el preentrenamiento con lo examinado.≈46 MB FP32 es memoria de pesos calculada, no RAM de proceso. Un presupuesto 8–16 GB RAM/CPU para pocas series es una estimación de experimento; GPU no imprescindible por principio, rendimiento local pendiente. Los benchmarks genéricos y datasets internos reducen la capacidad de evaluar contaminación financiera global.

## Oportunidad independiente y contraste

Propuesta: usar la distinción observación/máscara como componente de un monitor de calidad de fundamentales y comparar el forecast de ingresos de protocolo con naive y Chronos 2. Medir degradación al introducir huecos artificiales y cambios de frecuencia, manteniendo un mismo corte de conocimiento. Criterio propuesto: conservar cobertura de intervalos y no producir alertas económicas por fallos de ingesta. Una mejora de forecasting puede reducir ruido de revisión diaria sin anticipar retornos.

Aprovechar las transformaciones y conceptos bajo licencia de código compatible, fijando atribución y versiones. Aplazar uso operativo de pesos y entrenamiento propio hasta resolver permisos y comprobar que un baseline estadístico no cumple ya la función. No preentrenar otra foundation model para este usuario.
