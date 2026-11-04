# FinBERT code — revisión técnica estática

ID: `AI-finbert`. Verificado: 2026-11-04. Referencia estratégica: 2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.

Commit: `3b4bfed383a8bb6b013db2f1ce9c766ff5100d24`. [Repositorio](https://github.com/ProsusAI/finBERT). [Licencia de código](https://raw.githubusercontent.com/ProsusAI/finBERT/3b4bfed383a8bb6b013db2f1ce9c766ff5100d24/LICENSE). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.

Puntuación editorial: **60/100**. Desglose: utility=16, evidence=10, data=8, ease=9, license=4, maintenance=4, usability=6, differentiation=3. Confianza: media-alta sobre rutas observadas; no sobre eficacia financiera. Los bloqueos de licencia/datos prevalecen.

## Decisión y licencia

FinBERT sigue siendo una referencia útil de clasificación de sentimiento financiero en inglés; no es un predictor de rendimientos. En el snapshot, el repositorio contiene aviso de 12-oct-2026 que limita Apache 2.0 al código y remite los pesos a su [card](https://huggingface.co/ProsusAI/finbert/blob/0bc2ac10dda6929bcb1f77ccc43c7ec5c424f031/README.md), donde se declara CC-BY-NC-SA4.0. Financial PhraseBank tiene condiciones separadas CC-BY-NC-SA3.0 y el preentrenamiento utiliza Reuters TRC2 con términos propios. No asumir uso comercial libre porque la carpeta de código contiene Apache.

## Ruta técnica observada

[finbert.py](https://github.com/ProsusAI/finBERT/blob/3b4bfed383a8bb6b013db2f1ce9c766ff5100d24/finbert/finbert.py) segmenta texto en frases, convierte a features, ejecuta el clasificador en modo evaluación y calcula softmax para tres clases. Su función legacy `predict` fija 64 tokens por frase en la conversión y construye un score como diferencia entre positivo y negativo. [utils.py](https://github.com/ProsusAI/finBERT/blob/3b4bfed383a8bb6b013db2f1ce9c766ff5100d24/finbert/utils.py) contiene tokenización/padding, softmax y métricas por clase. El score de softmax no está calibrado como probabilidad de subida de un token. Frases largas sobre gobernanza o tokenomics pueden perder información decisiva en un camino con truncado corto; una integración Transformers moderna es una interfaz distinta que debe configurarse y probarse.

## Datos y pertinencia para crypto

Las etiquetas financieras inglesas no cubren automáticamente lenguaje de comunidades, ironía, vocabulario técnico ni texto español. Una noticia positiva para uso de protocolo puede ser negativa para captura de valor del token; una quema puede ser financiada por emisión superior. Conviene separar tono textual, hecho económico, mecanismo afectado y activo. Para un monitor de narrativas, el primer target debería ser recuperación/clasificación de temas con anotaciones propias, y solo después tono.

## Pruebas y hardware

Se inspeccionaron implementación y entorno; no se ejecutaron modelos ni se verificó una suite completa de tests del repositorio. La card especifica arquitectura BERT-base de 12 capas y tres clases. Un proceso pequeño sobre CPU puede ser viable; se propone presupuesto 8 GB RAM para prueba, sin medir latencia. No se descargaron pesos. Un modelo pequeño evita algunos costes de LLM remoto, pero no resuelve permisos ni cambio de dominio.

## Experimento recomendado

Etiquetar un corpus propio de 100–200 fragmentos de protocolos, preservando documento/fecha y separando idiomas. Dos anotadores —o revisión humana en dos pasadas— distinguen tono y efecto económico; incluir negativos difíciles: incentivos que aumentan volumen sin revenue, explotación con recuperación parcial y recompras sin burn. Dividir por documento y fecha, evitando que paráfrasis del mismo anuncio aparezcan en train y test. Medir macro-F1, matriz de confusión y calibración de etiquetas; no usar PnL como sustituto de la calidad de extracción.

Criterio propuesto: justificar una mejora frente a reglas/TF-IDF con coste y tasa de errores aceptables para revisión humana. Antes de uso operativo aclarar condiciones de pesos/datos. Aprovechar la tarea y el baseline metodológico; no ajustar decisiones de cartera por sumar sentimiento diario ni suponer que una etiqueta positiva informa sobre valoración a 18 meses.
