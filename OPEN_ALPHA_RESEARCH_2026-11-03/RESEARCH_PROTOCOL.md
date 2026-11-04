# Protocolo común de OPEN ALPHA

Fecha de referencia: 2026-11-03. Observación de fuentes: 2026-11-04. Si el contenido observado cambió después del corte, marcarlo: no reconstruir retrospectivamente lo que se sabía el día 3 sin un commit fechado.

Mandato: investigación independiente; no tocar CIE, instalar/importar/ejecutar código externo, operar, pedir secretos, pagar servicios ni publicar repositorios. Se permite código propio auxiliar para reunir metadatos y generar documentos de investigación. No construir herramientas financieras.

## Cobertura y verificación

- D0: candidato descubierto, sin confirmación directa suficiente.
- V1: fuente original consultada directamente y existencia/función confirmadas. No equivale a verificar la implementación.
- V2: documentación más licencia o archivo técnico examinados; registrar exactamente qué falta.
- V3: revisión estática de rutas críticas, dependencias/interfaces y tests si existen. No equivale a ejecución, auditoría integral ni prueba de rentabilidad.

La licencia queda NO VERIFICADA si no se inspecciona su fuente. No inferir MIT por familiaridad. Registrar permisos de código, pesos, datos y servicios por separado. Un fallo de acceso no implica inexistencia.

Precisar si el permiso procede de LICENSE, declaración del titular en card o etiqueta del hosting. V1/V2 no certifican adopción ni eficacia. Para pruebas, separar localizado, inspeccionado y ejecutado; en esta investigación `tests_executed=false` y `coverage_measured=null`. Un hash acredita los bytes observados, no la verdad de la fuente ni su disponibilidad histórica. Las conclusiones deben distinguir código observado, declaración de autores, resultado externo no reproducido e inferencia/propuesta propia.

## Archivos por área

Cada investigador escribe solamente `workstreams/<area>/` y revisiones con prefijo de su área en `03_DEEP_TECHNICAL_REVIEWS/`. No editar informes consolidados de otros. Crear `candidates.json`, `sources.json`, `evidence.json`, `search_log.json`, `relations.json`, `findings.md`. Se admiten inventarios complementarios de métodos, modelos, papers, datasets o proveedores.

Campos comunes de candidatos: id (prefijo y slug estable), name, url, organization, categories (letras A-N), resource_type, description, verification_level, verified_at, version_or_commit, maintenance_status, license_code, license_status, license_url, dependencies, data_inputs, outputs, practical_use, limitations, alternatives, evidence_ids, source_ids, scores, confidence, blockers, commercial_dependencies, maturity, cost_relative, adoption_mode, deep_review_path.

Usar null o `no comprobado` en lo que falte. `scores` contiene utility/25, evidence/15, data/15, ease/12, license/10, maintenance/8, usability/8, differentiation/7; no puntuar D0 como si estuvieran comprobados. Puntuación editorial, no métrica de rentabilidad. Valores enteros y justificación en revisión o findings. `license_status` debe usar una de las cinco clases del mandato.

Fuentes: id, url exacta, title, accessed_at, source_type, status, version_or_commit, notes. Evidencias: id, candidate_id, source_id, claim, evidence_type, limitations. Relaciones: from_id, to_id o to_url, relation, evidence_source_id; distinguir dependencia de código, comparación y combinación propuesta.

Cada revisión profunda debe citar fuentes originales, preferentemente rutas inmutables; inspeccionar código más allá de README; distinguir evidencia observada e inferencia; incluir entradas/salidas, dependencias, licencia, límites temporales, tests examinados o ausencia de comprobación, requisitos estimados, alternativa, decisión concreta y experimento propuesto SIN ejecutarlo.

## Disciplina de consultas

Registrar consulta, motor/sitio, fecha, resultados relevantes y fallos. Hacer búsquedas especializadas y contracorriente, incluyendo idiomas distintos del inglés cuando ayuden. No perseguir cuotas con candidatos irrelevantes. No descargar dependencias ni datasets completos. No copiar código externo al paquete de entrega. Conservar URL/commit/hash o notas propias; citas literales muy breves. Respetar límites públicos, no eludir cuotas.

## Coordinación

crypto: DeFi, protocolos, mercados y derivados, on-chain, fuentes cripto, SDKs. quant: macro, métodos cuantitativos, backtesting, eventos, cartera/riesgo. ai: modelos, datasets, benchmarks, agentes y extracción documental. coordinator: infraestructura, calidad/provenance, visualización, integración de informes, diseños y revisión crítica.

Objetivos orientativos por área: 60-75 candidatos relevantes descubiertos, 25-35 directamente verificados y 8-10 revisiones profundas. La cobertura final será contada por evidencia real, deduplicada y declarada sin exageración.
