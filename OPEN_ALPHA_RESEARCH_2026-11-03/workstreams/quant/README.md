# Área quant, macro y riesgo

Leer primero [findings.md](findings.md), después `candidates.json`, las diez revisiones `../../03_DEEP_TECHNICAL_REVIEWS/quant_*.md` y `methods.json`. `coverage.json` contiene la cobertura real; D0 no cuenta como verificación directa.

Los JSON son notas propias y metadatos: conservan URL exacta, commit y SHA256 de archivos revisados. No contienen código de terceros ni datasets descargados. Las referencias a ramas dinámicas de documentación conservan fecha de consulta y deben revalidarse. No se ejecutaron tests ni benchmarks externos.

`collect_quant.py` y `inspect_quant.py` son auxiliares propios que solo leen HTTP y escriben observaciones temporales. No son una herramienta financiera. Los scripts de consolidación contienen el juicio editorial de esta sesión: no convertirlos en un actualizador automático de recomendaciones. Una nueva recopilación requiere revisar cambios de código, licencia y semántica, y no solo volver a generar textos.

Los ficheros `_temporary_observations.json` y `_temporary_deep.json` se eliminaron tras consolidar hashes y notas; no deben incluirse en un repositorio o archivo de entrega. `collect_quant.py` puede recrear observaciones actuales, pero para reproducir la revisión histórica deben usarse los commits de `sources.json`, sin asumir que HEAD coincide.

En una continuación, priorizar: documentación ECB/Treasury inaccesible; permisos por serie; historial de mantenimiento y releases; comparación real de forks mediante diffs; datos de ETFs; timestamp de disponibilidad de datos24/7; y experimentos de aceptación que aquí solo están diseñados.

La clasificación de licencias es potencial y específica de la fuente. NCSA no se etiquetó MIT; EconML se documentó como MIT con componentes BSD-3-Clause; las licencias de R leídas en DESCRIPTION son declaraciones de paquete, no auditorías de todo el árbol. Las restricciones de vectorbt, pykalman, RQAlpha y MLFinLab se distinguen expresamente.
