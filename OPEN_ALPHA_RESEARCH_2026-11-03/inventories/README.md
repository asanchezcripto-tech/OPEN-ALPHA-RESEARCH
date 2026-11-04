# Diccionario y uso de los inventarios

Los JSON son la representación estructurada principal. Cada inventario tabular tiene un CSV UTF-8 equivalente, con listas y objetos serializados como JSON dentro de celdas entrecomilladas. Un valor vacío en CSV corresponde a `null` o a un campo ausente; consultar JSON para distinguirlos. No abrir ni ejecutar contenido remoto para consultar estos archivos.

| Inventario | Unidad de una fila | Relación y límite |
|---|---|---|
| projects | Recurso diferenciado | Catálogo principal; `id` es estable, no sumar sus vistas |
| libraries | Biblioteca/framework/SDK/cliente seleccionado por tipo | Vista del catálogo, no nuevos candidatos |
| models | Modelo o checkpoint | Licencia de pesos y entrenamiento separada del runtime |
| datasets | Dataset o ficha de datos | Puede referenciar `candidate_id`; derechos y disponibilidad por fuente |
| papers | Paper o línea de investigación | Leer `reading_scope`/limitaciones; varios solo tienen revisión de abstract |
| algorithms | Método transferible | `implementations`/`supporting_ids`, supuestos, validación y fallos |
| licenses | Permisos observados por recurso | Código, pesos, datos y dependencias separados; no dictamen jurídico |
| providers | Proveedor o servicio público/documentado | Acceso y clientes abiertos no implican servicio abierto o gratuito ilimitado |
| opportunities | Concepto propio, sin implementar | Score editorial y arquitectura; `blueprint_path` solo para cinco |
| comparisons | Decisión entre alternativas bajo un escenario | `candidate_ids` y fuentes; no ranking universal |
| sources | Consulta a una URL o archivo | Puede ser intento fallido; `status` no prueba capacidades |
| evidence | Afirmación ligada a una fuente | `candidate_id` → projects; `source_id` → sources |
| relations | Arista tipada entre recursos | `from_id`/`to_id`; dependencias y relaciones conceptuales se distinguen |
| selected_components | Selección editorial de 22 piezas | Incluye técnicas/referencias con restricciones; no instalación conjunta |
| search_log | Consulta de descubrimiento | No equivale a una verificación ni a todas las aperturas directas |
| deduplication | Alias consolidado | Mantiene la procedencia de evaluaciones solapadas |
| stage_log | Cierre documental de una etapa A–K | Examina, verifica, descarta, pendientes, oportunidades y reutilización |

`coverage_stats.json` contiene recuentos derivados, sin CSV porque es un objeto jerárquico. `quality_checks.json` registra la comprobación de integridad de la entrega, no pruebas de software externo. El manifiesto está en la raíz.

## Campos comunes y valores desconocidos

`id`, `name`, `url`, `categories`, `verified_at`, `version_or_commit`, `maintenance_status` y `confidence` identifican el recurso y el alcance de la observación. Las categorías A–N se definen en [cobertura](../01_SEARCH_COVERAGE.md). Las fuentes usan `accessed_at` cuando corresponde a un intento, no una verificación positiva. Las afirmaciones heredan contexto de su recurso y enlazan su propia fuente. Mantenimiento no aplica como ciclo de desarrollo a una fila de evidencia; debe consultarse el recurso vinculado.

`null` significa desconocido, no registrado o no aplicable según el contexto; nunca cero, inexistente o libre de restricciones. Una lista vacía de problemas no certifica ausencia de problemas. No se midió cobertura de pruebas: `coverage_measured=null`; `tests_executed=false`. Las notas de tests describen localización o lectura estática, no ejecución.

`verification_level`: D0 es comprobación insuficiente; V1 confirma existencia/alcance/card/abstract; V2 añade documentación y licencia o archivo técnico; V3 revisa rutas críticas y límites. Son grados de investigación documental. `deep_review_path` y `blueprint_path` se resuelven desde la raíz de la entrega. `url` de una oportunidad es un enlace relativo desde este directorio; las URLs de fuentes son exactas.

`scores` contiene ocho dimensiones con máximos 25/15/15/12/10/8/8/7 y `score_total` su suma. Puntuación, confianza, madurez, bloqueantes y decisión de reutilización son campos diferentes. D0 queda sin score. Las cifras no representan probabilidad de éxito, retorno esperado ni una medición de calidad de producción.

## Seguir una afirmación

1. Buscar un `id` en projects y leer sus límites, nivel y revisión.
2. Seguir `evidence_ids` a evidence; identificar qué afirma y con qué limitación.
3. Seguir `source_id` a sources; comprobar URL, status, versión y fecha.
4. Revisar el permiso de la capa concreta y los bloqueantes antes de pensar en reutilización.

Ejemplo: `quant-fredapi` permite localizar la revisión y el método de selección de vintages. La existencia de una función as-of no demuestra que produzca una sola fila por periodo ni que toda una canalización evite información futura.

## Continuación y reproducción

Los inventarios de `workstreams/` conservan las notas originales por área; los de este directorio son la versión consolidada. No editar ambas copias sin registrar la reconciliación. Los generadores documentan la elaboración, pero algunos auxiliares de área dependían de cachés ya retiradas y los informes tienen correcciones editoriales posteriores. No ejecutar todos los scripts en cadena ni repetir el barrido por defecto.

Para revisar una afirmación, adquirir solo su fuente fijada por commit/card, registrar una observación nueva y comparar hashes. Una página mutable puede haber cambiado; una respuesta distinta no invalida automáticamente la consulta antigua. Para regenerar las tablas finales sin red: `consolidate.py`, `write_reports.py`, `finalize_docs.py`, `finish_delivery.py` y `validate_delivery.py`, preservando antes cualquier edición narrativa propia. El último genera el registro QA. El empaquetado se realiza con `package_delivery.py` y rehace el manifiesto; no publica nada.
