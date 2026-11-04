# FinGPT — revisión técnica estática

ID: `AI-fingpt`. Verificado: 2026-11-04. Referencia estratégica: 2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.

Commit: `ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8`. [Repositorio](https://github.com/AI4Finance-Foundation/FinGPT). [Licencia de código](https://raw.githubusercontent.com/AI4Finance-Foundation/FinGPT/ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8/LICENSE). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.

Puntuación editorial: **51/100**. Desglose: utility=14, evidence=8, data=6, ease=4, license=7, maintenance=4, usability=4, differentiation=4. Confianza: media-alta sobre rutas observadas; no sobre eficacia financiera. Los bloqueos de licencia/datos prevalecen.

## Decisión crítica

FinGPT es un conjunto amplio de tareas y ejemplos, no un modelo único con una licencia única. Su código MIT es reutilizable con condiciones; pesos base, adapters, noticias y proveedores deben evaluarse aparte. La ruta Forecaster tiene suficiente evidencia estática para identificar riesgos temporales concretos. No la recomendaría como motor de previsión financiera sin corregirlos y probarla prospectivamente. Sí conservaría sus ideas de corpus y tareas para diseñar una evaluación propia.

## Flujo y hallazgo reproducible

[data_pipeline.py](https://github.com/AI4Finance-Foundation/FinGPT/blob/ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8/fingpt/FinGPT_Forecaster/data_pipeline.py) encadena adquisición, preparación de prompts, consulta a GPT y transformación de dataset. [data.py](https://github.com/AI4Finance-Foundation/FinGPT/blob/ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8/fingpt/FinGPT_Forecaster/data.py) conecta precios/noticias/fundamentales y `gpt4_to_llama` transforma respuestas de entrenamiento generadas condicionando el razonamiento al movimiento conocido. Es una técnica de creación de etiquetas/explicaciones; no es demostración de que un modelo habría anticipado ese movimiento con información real disponible.

[prompt.py](https://github.com/AI4Finance-Foundation/FinGPT/blob/ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8/fingpt/FinGPT_Forecaster/prompt.py) obtiene perfiles de empresa mediante Finnhub y de crypto mediante `yfinance.Ticker.info`; incluye capitalización actual y otros atributos, y `get_all_prompts` reutiliza la introducción al construir prompts históricos. Inferencia técnica: reconstruir hoy un prompt pasado por esta ruta puede añadir información de hoy. La presencia de tal riesgo en esta ruta no demuestra que todos los experimentos o módulos FinGPT lo sufran.

## Correcciones existentes y alcance

[basics.py](https://github.com/AI4Finance-Foundation/FinGPT/blob/ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8/fingpt/FinGPT_Forecaster/basics.py) ya intenta evitar usar resultados al cierre del trimestre: añade 45 días como disponibilidad estimada. Es mejor que igualar periodo contable y publicación, pero no registra una fecha real de publicación ni protege frente a revisiones posteriores del proveedor. No tratar 45 días como regla financiera universal. Separar valor observado, vintage y estimación de disponibilidad; si falta la fecha real, marcar incertidumbre/abstención.

Se inspeccionaron requisitos, imports e interfaces de Forecaster. Dependencias incluyen Finnhub/yfinance, datasets, Pandas y cliente de LLM; hay costes/condiciones externas. No se ejecutaron tests, pipelines ni notebooks. La calidad de otras áreas de FinGPT no fue auditada por completo. El tamaño del repositorio y la cantidad de modelos listados no equivalen a cobertura de pruebas.

## Alternativa y utilidad recuperable

Una biblioteca de extractores con corpus propio y respuestas verificables es más proporcionada que fine-tuning inicial. Para Thesis Tracker, pedir al modelo hechos citados y contradicciones; calcular cifras fuera del LLM. TradingAgents actual ofrece controles as-of inspeccionados que sirven de contraste, aunque tampoco elimina el conocimiento futuro interno de un LLM moderno.

## Experimento mínimo para rehabilitar la ruta

Preparar inputs históricos con perfiles/supply de la fecha, noticias adquiridas entonces y reglas de rechazo. Comparar prompts con/sin introducción actual para cuantificar cuánto cambia el resultado; registrar esto como diagnóstico de leakage, no como rentabilidad. Luego evaluar de forma prospectiva con baseline simple, umbral de abstención y costes. Entrenar solo después de reservar empresas, periodos y fuentes fuera de ajuste. El criterio primero es fidelidad temporal 100% de los inputs usados, después precisión de extracción y calibración.

Presupuesto de inferencia depende del LLM y proveedor; 8–16 GB RAM sirven para orquestar pequeños corpus, no para entrenar 7 B–13 B. No hay cifra de coste recurrente verificada ni justificación actual para comprar GPU.
