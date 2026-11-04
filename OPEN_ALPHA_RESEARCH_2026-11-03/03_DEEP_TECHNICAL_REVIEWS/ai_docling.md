# Docling — revisión técnica estática

ID: `AI-docling`. Verificado: 2026-11-04. Referencia estratégica: 2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.

Commit: `0634e2f74561e5950d69b2cace67ef95400506ad`. [Repositorio](https://github.com/docling-project/docling). [Licencia de código](https://raw.githubusercontent.com/docling-project/docling/0634e2f74561e5950d69b2cace67ef95400506ad/LICENSE). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.

Puntuación editorial: **83/100**. Desglose: utility=23, evidence=13, data=12, ease=9, license=8, maintenance=6, usability=6, differentiation=6. Confianza: media-alta sobre rutas observadas; no sobre eficacia financiera. Los bloqueos de licencia/datos prevalecen.

## Decisión

Docling es candidato prioritario para convertir informes, gobernanza y documentación en evidencia inspeccionable. Su valor es la extracción estructurada con estados y ubicación, antes de generar respuestas. El código MIT no significa que cualquier OCR/VLM añadido tenga la misma licencia. Para páginas HTML sencillas, Trafilatura será más proporcionado; reservar Docling para tablas, PDF y formatos heterogéneos.

## Arquitectura comprobada

[document_converter.py](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/docling/document_converter.py) selecciona backend/opciones por formato y ejecuta pipelines, con configuración de errores, caché de inicialización y procesamiento por lotes. Se inspeccionó `_execute_pipeline`: distingue entrada inválida, falta de pipeline y conversión; descarga recursos del documento cuando corresponde. [base_models.py](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/docling/datamodel/base_models.py) define estados como éxito parcial/fallo, elementos de página, estructuras de tablas y reportes de confianza. El resultado estructurado permite conservar información que se pierde al aplanar todo a texto.

El contrato de un futuro extractor financiero debe conservar documento/hash, página y región, tabla/fila/columna, unidad, valor textual y valor interpretado, así como `published_at` y `acquired_at`. Es propuesta de diseño: Docling no determina por sí mismo el momento en que una información fue pública ni si un fee es revenue del tenedor. Un campo numérico debe pasar comprobaciones de escala, signos, moneda y suma antes de formar parte de una tesis.

## Tests y seguridad observados

[test_failed_pages.py](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/tests/test_failed_pages.py) distingue éxito parcial y páginas presentes; una nota del propio archivo indica que ciertos fixtures ya no ejercitan fallos con una versión reciente de docling-parse. Por tanto, no afirmar cobertura completa de páginas fallidas a partir de su nombre. [test_hf_model_download_security.py](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/tests/test_hf_model_download_security.py) verifica revisión fijada por SHA y el comportamiento de advertencia/rechazo cuando se confía en código remoto no fijado. Una revisión fijada no es una auditoría del código: estos tests reducen movilidad de dependencia, no demuestran seguridad integral. No se ejecutó conversión ni se descargó modelo.

## Costes y permisos

Hay rutas locales y opciones de modelos/servicios que cambian coste, precisión y permisos. Estimación para piloto: CPU, 16 GB RAM, decenas de documentos seleccionados; GPU opcional si la muestra demuestra necesidad. No confundir este presupuesto con requisitos universales ni con benchmark de tablas. Dependencias principales observadas: docling-core, backends de formatos, Pydantic y componentes de pipeline. Antes de habilitar OCR/VLM revisar su card, formato de pesos y descargas; no atribuirle al paquete la licencia de todas las entradas.

## Primera capacidad útil y aceptación

Extraer 50 hechos de 5 documentos públicos de protocolos y conservar enlace exacto al fragmento. Una persona marca tabla/unidad/fecha correctas; la aritmética se calcula de forma determinista. Métricas: precisión de campos numéricos, cobertura de referencias, porcentaje de abstención y tiempo de corrección. Criterio propuesto: 100% de cifras utilizadas con fuente localizable y ninguna página fallida tratada como completa; exactitud mínima y tamaño de muestra deben predefinirse. Si falla una tabla, abstenerse o usar lectura manual.

Evitar primero bases vectoriales distribuidas y agentes complejos. Un índice local sobre documentos con buen provenance aporta más que una conversación fluida sin coordenadas de evidencia.
