# TimesFM library — revisión técnica estática

ID: `AI-timesfm`. Verificado: 2026-11-04. Referencia estratégica: 2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.

Commit: `e51928e27119cb17bebc005be2696b75e0a9e688`. [Repositorio](https://github.com/google-research/timesfm). [Licencia de código](https://raw.githubusercontent.com/google-research/timesfm/e51928e27119cb17bebc005be2696b75e0a9e688/LICENSE). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.

Puntuación editorial: **63/100**. Desglose: utility=17, evidence=11, data=10, ease=6, license=4, maintenance=6, usability=4, differentiation=5. Confianza: media-alta sobre rutas observadas; no sobre eficacia financiera. Los bloqueos de licencia/datos prevalecen.

## Decisión y hallazgo determinante

TimesFM3 existe y tiene implementación examinable. Su código actual es Apache 2.0, pero los [pesos oficiales 3.0](https://huggingface.co/google/timesfm-3.0-pytorch/blob/43046b85ec22d584a13f8098c2ed39c889e129c2/README.md) llevan una [licencia propia](https://huggingface.co/google/timesfm-3.0-pytorch/blob/43046b85ec22d584a13f8098c2ed39c889e129c2/LICENSE) que restringe finalidad comercial y producción y define ampliamente los usos de resultados. La publicación de pesos no autoriza automáticamente un asistente de inversión operativo. Clasificación de esos pesos: SOLO INVESTIGACIÓN / RESTRICCIONES; aclarar el uso antes de adoptarlos. Esta conclusión no es asesoramiento jurídico definitivo. [TimesFM2.5](https://huggingface.co/google/timesfm-2.5-200m-pytorch/blob/1d952420fba87f3c6dee4f240de0f1a0fbc790e3/README.md) conserva declaración Apache 2.0 en su card y merece comparación separada.

## Arquitectura y rutas

El módulo [timesfm 3_forecaster.py](https://github.com/google-research/timesfm/blob/e51928e27119cb17bebc005be2696b75e0a9e688/src/timesfm3/timesfm3_forecaster.py) es ahora un puente de compatibilidad. La ruta efectiva está en [torch/timesfm 3_forecaster.py](https://github.com/google-research/timesfm/blob/e51928e27119cb17bebc005be2696b75e0a9e688/src/timesfm3/torch/timesfm3_forecaster.py). La separación importa para no auditar solamente el alias. Se observaron `TimesFM3Forecaster`, `predict`, `predict_batch`, configuración de consulta y `ForecastOutput`, que distingue forecast puntual —mediana— y cuantiles. `_Query` distingue targets, covariables pasadas y covariables pasado/futuro; no incorporar valores futuros reconstruidos como si fueran conocidos.

La ruta también implementa interpolación lineal de NaN por fila y normalización con defensas frente a media/varianza no finitas. Inferencia propia: imputar usando observaciones posteriores al corte convertiría una prueba retrospectiva en información anticipada. Por eso recortar por `knowledge_time` antes de cualquier transformación; retener máscara de imputación y comparar con ausencia explícita. Los huecos de publicación macro no son necesariamente datos perdidos intercambiables con huecos de sensor.

## Dependencias, estado y pruebas

[pyproject.toml](https://github.com/google-research/timesfm/blob/e51928e27119cb17bebc005be2696b75e0a9e688/pyproject.toml) declara versión 3.0.2, Python≥3.10, NumPy, Hugging Face Hub y safetensors, con extras separados para torch/MLX/flax/xreg. [backward_compat_test.py](https://github.com/google-research/timesfm/blob/e51928e27119cb17bebc005be2696b75e0a9e688/src/timesfm3/backward_compat_test.py) comprueba rutas de importación antiguas; no constituye validación económica ni paridad numérica. Se observó el árbol de tests general, pero no se ejecutó. El commit está fijado; no se reconstruyó su hora de disponibilidad al cierre del 3.

## Coste y comparación

La card describe aproximadamente 0.3 B parámetros FP32:≈1.2 GB para pesos es solo una estimación aritmética, no RAM total. Presupuesto experimental 16 GB RAM y GPU opcional, sujeto a longitud, lote y backend; latencia no medida. Chronos 2 ofrece una alternativa documentalmente más simple para permisos y una integración fev observada. La versión más reciente no debe ganar por nombre: comparar TimesFM2.5, 3.0 —solo en uso permitido— y naive en exactamente los mismos cortes.

## Primera utilidad y aceptación

Probar escenarios de fees/actividad agregada y sensibilidad a covariables con un archivo histórico congelado. Exigir que una mejora agregada sobreviva al desglose por activo, periodo y nivel de missingness; medir también cobertura y abstención. No usar forecast de precio para derivar automáticamente un precio objetivo de token. Aprovechar tipado de inputs, normalización controlada y diseño multivariable; aplazar integración operativa de pesos 3.0 hasta resolver permisos y validación independiente.
