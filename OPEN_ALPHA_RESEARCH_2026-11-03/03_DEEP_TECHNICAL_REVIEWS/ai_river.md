# River — revisión técnica estática

ID: `AI-river`. Verificado: 2026-11-04. Referencia estratégica: 2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.

Commit: `4768de0579f977315e65cd23ee658534c1d62c26`. [Repositorio](https://github.com/online-ml/river). [Licencia de código](https://raw.githubusercontent.com/online-ml/river/4768de0579f977315e65cd23ee658534c1d62c26/LICENSE). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.

Puntuación editorial: **84/100**. Desglose: utility=22, evidence=13, data=12, ease=10, license=9, maintenance=6, usability=6, differentiation=6. Confianza: media-alta sobre rutas observadas; no sobre eficacia financiera. Los bloqueos de licencia/datos prevalecen.

## Decisión y oportunidad poco obvia

Usar River como monitor de cambios en el error de nuestros indicadores y en la calidad de datos, además de cambios del mercado. Si el proveedor cambia una definición de revenue, puede ser más útil detectar ese cambio que predecir el precio siguiente. ADWIN es un componente proporcionado para esto; su alarma significa incompatibilidad estadística con el historial reciente, no una nueva oportunidad rentable.

## Implementación comprobada

[adwin.py](https://github.com/online-ml/river/blob/4768de0579f977315e65cd23ee658534c1d62c26/river/drift/adwin.py) expone `delta`, `clock`, `max_buckets`, `min_window_length` y `grace_period`; mantiene estimación, varianza y anchura y reinicia su helper después de una detección. La implementación pesada está ahora en [rust_src/adwin.rs](https://github.com/online-ml/river/blob/4768de0579f977315e65cd23ee658534c1d62c26/rust_src/adwin.rs). Se inspeccionaron inserción con actualización de varianza, compresión de buckets, exploración de cortes y umbral dependiente de tamaños/varianza. No se debe presentar como código puramente Python: la construcción usa Rust/maturin.

El umbral depende de `delta`, pero no se ha demostrado aquí que la tasa de falsas alarmas en funding o fees autocorrelacionados sea ese valor. La interpretación cripto exige controlar estacionalidad, escala, outliers, faltantes y actualizaciones tardías. Actualizar el detector primero con una observación y después evaluar su error puede introducir contaminación de la evaluación: en aprendizaje online se conserva la secuencia predecir→observar→puntuar→actualizar.

## Tests y requisitos

[test_adwin_regression.py](https://github.com/online-ml/river/blob/4768de0579f977315e65cd23ee658534c1d62c26/tests/drift/test_adwin_regression.py) contiene casos de saltos, ausencia de drift, estadísticas exactas, parámetros, valores grandes/negativos y serialización. También hay tests Rust en el archivo del motor; no se ejecutaron. [pyproject.toml](https://github.com/online-ml/river/blob/4768de0579f977315e65cd23ee658534c1d62c26/pyproject.toml) declara versión 0.26.1, Python≥3.11, NumPy/SciPy/Narwhals. El Python 3.10 observado en la máquina no cumple esta versión; sería necesario un entorno futuro adecuado, no modificar ahora el del usuario. Licencia BSD3-Clause inspeccionada.

## Diseño mínimo de uso

Entradas: pérdida predictiva normalizada, fracción de datos ausentes y diferencia entre dos fuentes para una métrica. Mantener un detector por señal y registrar cada cambio con snapshot, parámetros, observaciones y ventana. Salida: alerta con evidencia y etiqueta provisional «mercado», «cambio de definición» o «fallo de ingesta». La clasificación final requiere revisión y comparación cruzada; el detector no identifica causalidad.

## Experimento y decisión de adopción

Reproducir una serie estable sintética y una con cambios conocidos en un entorno aislado futuro; después insertar huecos/revisiones en una copia de datos y comparar contra EWMA/robust z-score. Medir demora de detección, falsas alarmas por mes y tiempo humano de diagnóstico. Criterio propuesto: mantener el presupuesto de alertas acordado —por ejemplo≤2 falsas/mes por panel— y mejorar la detección de errores de fuente sin disparar más revisiones innecesarias. No optimizar delta sobre el periodo de evaluación.

CPU basta para estos streams; presupuesto 8 GB RAM incluye entorno y datos pequeños, no medición. Reutilizar detector y representación incremental; no desplegar Kafka ni entrenar un agente que elija detectores si unas pocas señales predefinidas resuelven el problema. Alternativa `ruptures` para segmentación retrospectiva: responde una pregunta distinta de detección online.
