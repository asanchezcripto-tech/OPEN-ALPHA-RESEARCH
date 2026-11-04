# Continuidad del área IA

Observación: 2026-11-04. Referencia del mandato: 2026-11-03. Estado cerrado documentalmente: 80 recursos diferenciados, 260 fuentes, 162 registros de evidencia, 15 consultas de descubrimiento, 10 revisiones profundas, 3 papers examinados solo a nivel de abstract/historial, 5 métodos y 6 comparaciones.

El catálogo separa 62 repositorios y 18 cards (11 modelos y 7 datasets). Distribución: V1=10, V2=60, V3=10. No todos los repositorios son bibliotecas; no todas las cards permiten reutilización comercial. Los papers adicionales y ForecastBench no se incorporaron como nuevos candidatos para inflar cobertura.

Punto de entrada: `findings.md`. Revisiones en `../../03_DEEP_TECHNICAL_REVIEWS/ai_*.md`. Para la consolidación usar `candidates.json`, `sources.json`, `evidence.json`, `relations.json`, `models.json`, `datasets.json`, `papers.json`, `algorithms.json`, `comparisons.json`, `search_log.json`. La revisión crítica del blueprint OP-02 y del protocolo está en `critical_review.md`.

Las observaciones conservan URL exacta, HTTP/status, SHA de revisión y hash de bytes obtenidos. El texto/código de terceros se retiró mediante `sanitize_observations.py`; no entregar copias de código ni de datasets. Los scripts `collect_*` y `inspect_paths.py` son utilidades propias de lectura pública, no herramientas financieras. No ejecutan los contenidos descargados. Para un nuevo barrido deben actualizar fecha y alcance; no asumir que volver a leer una rama reproduce el snapshot actual. Para una comprobación concreta, usar el URL inmutable ya inventariado.

Generación offline de los documentos del área, si fuera necesaria: `build_inventory.py` → `write_reviews.py` → `finish_research.py`; después comprobar integridad y preservar las mejoras editoriales posteriores. Estas utilidades usan las observaciones y anotaciones propias, no importan dependencias investigadas. No volver a recolectar todos los proyectos para revisar una sola afirmación.

Limitaciones principales: pruebas sin ejecución, mantenimiento observado sin auditoría de cadencia, permisos de pesos/datasets por separado, sin precisión/latencia local, sin prueba de rentabilidad. El equipo actual tiene Python 3.10 observado; River actual declara >=3.11. No se instaló ningún entorno ni modelo.

Próximos controles: verificar timestamp del commit si se exige corte estricto al 3 de noviembre; revisar licencias de pesos TiRex 2 y baselines adicionales; auditar FinVerse más allá del abstract; piloto prospectivo de citas/cifras y benchmark acotado sobre datos de protocolo con permisos. No ampliar arquitectura antes de demostrar utilidad medible.
