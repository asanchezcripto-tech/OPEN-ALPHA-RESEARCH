import json,pathlib,collections,csv
ROOT=pathlib.Path(__file__).resolve().parents[1];I=ROOT/'inventories'
def read(n):return json.loads((I/(n+'.json')).read_text(encoding='utf-8'))
projects=read('projects');P={x['id']:x for x in projects};stats=read('coverage_stats');sources=read('sources')
selected=[
('infra-duckdb','Consultas locales y joins explícitos; fijar compatibilidad.'),
('infra-pandera','Contratos de tablas y cuarentena, sin ocultar rechazos.'),
('infra-datacompy','Revisiones de datos y reconciliación.'),
('infra-marimo','Exploración reproducible y lectura de escenarios.'),
('crypto-ccxt-ccxt','Lectura de mercados manteniendo contrato/unidad nativos.'),
('crypto-hyperliquid-dex-hyperliquid-python-sdk','Lectura pública acotada de Hyperliquid.'),
('crypto-polymarket-py-sdk','SDK vigente para datos y reglas de mercados.'),
('crypto-defillama-dimension-adapters','Referencia de fórmulas; no copiar sin licencia verificada.'),
('crypto-uniswap-protocol-fees','Estudiar mecanismos y eventos; no desplegar contratos.'),
('crypto-paradigmxyz-cryo','Extracción batch EVM selectiva; RPC y permisos separados.'),
('quant-fredapi','Vintages con selección correcta en el consumidor.'),
('quant-statsmodels','Bases econométricas antes de modelos complejos.'),
('quant-arch','Bootstrap y comparación múltiple de experimentos.'),
('quant-ruptures','Segmentación y replay de detección, sin anticipación ficticia.'),
('quant-skfolio','Walk-forward y cartera con purga configurada.'),
('quant-pyportfolioopt','Riesgo/covarianza y escenarios de concentración.'),
('AI-statsforecast','Baselines estadísticos de magnitudes económicas.'),
('AI-mlforecast','Forecast con features y boosting controlables.'),
('AI-fev','Contrato común de tareas y evaluación.'),
('AI-river','Cambios en errores/fuentes, no señal automática de compra.'),
('AI-docling','Extracción con estructura y evidencia localizable.'),
('AI-chronos','Comparador probabilístico opcional contra base simple.')]
chosen=[]
for cid,reason in selected:
 r=P[cid];chosen.append(dict(id=cid,name=r['name'],url=r['url'],reason=reason,score_total=r.get('score_total'),license_status=r.get('license_status'),adoption_mode=r.get('adoption_mode'),blockers=r.get('blockers'),verified_at=r.get('verified_at'),confidence=r.get('confidence'),deep_review_path=r.get('deep_review_path')))
(I/'selected_components.json').write_text(json.dumps(chosen,ensure_ascii=False,indent=2),encoding='utf-8')
with (I/'selected_components.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=chosen[0].keys());w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in chosen)
weights='''| Criterio | Máximo |
|---|---:|
| Utilidad para análisis e inversión personal |25|
| Calidad técnica y evidencia |15|
| Datos disponibles/verificables |15|
| Facilidad de reutilización |12|
| Licencia/compatibilidad |10|
| Mantenimiento/sostenibilidad |8|
| Uso diario |8|
| Diferenciación |7|
| **Total** |**100**|
'''
cover=f'''# Cobertura y metodología

Referencia solicitada:2026-11-03. Observación efectiva:2026-11-04. No se retrofechó ninguna verificación. Se fijaron commits/cards cuando fue posible; no se reconstruyó sistemáticamente qué commit estaba disponible al cierre del día3. Las conclusiones sobre estado actual se refieren al contenido observado el4.

## Resultado contado y límites de cada nivel

| Magnitud | Resultado |
|---|---:|
| Recursos diferenciados en catálogo principal |{stats['catalog_resources']}|
| Consulta original suficiente para el nivel declarado |{stats['directly_verified']}|
| V3: revisiones técnicas estáticas de rutas críticas |{stats['verification_levels']['V3']}|
| V2: documentación más licencia o archivo técnico |{stats['verification_levels']['V2']}|
| V1: existencia/alcance/card/abstract |{stats['verification_levels']['V1']}|
| D0: comprobación insuficiente |{stats['verification_levels']['D0']}|
| Registros de fuentes, incluidos fallos |{stats['source_records']}|
| URLs de fuente distintas |{stats['distinct_source_urls']}|
| Evidencias registradas |{stats['evidence_records']}|
| Consultas de búsqueda registradas |{stats['search_queries']}|
| Métodos / comparaciones |{stats['algorithms']} / {stats['comparisons']}|
| Componentes seleccionados |{len(chosen)}|
| Conceptos / diseños preliminares |16 /5|

La meta orientativa de250–500candidatos,100recursos verificados y30–50revisiones se alcanza **bajo estas definiciones**. No significa auditar288proyectos completos: muchos son bibliotecas de apoyo, cards, datasets, servicios o referencias académicas. Los inventarios especializados son vistas o fichas complementarias; no deben sumarse como recursos nuevos. FRED-MD/FRED-QD comparten URL pero son datasets distintos. Dos duplicados de repositorio —DoWhy/EconML— se consolidaron, conservando fuentes de ambas áreas. Las licencias/capas de pesos y código se mantienen separadas.

Los registros de fuentes incluyen archivos distintos del mismo proyecto y rutas fallidas. Hay982registros con estado200/consultado; el resto son fallos/lecturas insuficientes. Ese conteo no son982proyectos ni982afirmaciones verificadas. El hash identifica contenido, no certifica veracidad. V3 tampoco implica ejecutar tests, medir cobertura, auditar todas las dependencias o probar una estrategia.

## Pasadas realizadas

**A — Cartografía.** Puntos de partida del mandato, consultas especializadas, organizaciones de protocolos, documentación, repositorios y cards. Búsquedas en inglés, español, chino y una consulta alemana; amplitud lingüística limitada. Priorización de horizonte3–18meses y preguntas económicas, no de funcionalidades de trading.

**B — Relaciones.** Seguir manifiestos, módulos, tests, referencias, SDK→servicio, código→pesos→datos y sucesores oficiales. No se descargaron dependencias ni se clonó masivamente. Se conserva un grafo con aristas tipadas en [relations](inventories/relations.json).

**C — Contracorriente.** Bibliotecas de reconciliación, contratos, monitorización y benchmarks; prototipos bitemporales y recursos macro. Se valoran por el error que pueden evitar, no por estrellas. Algunos prototipos se conservan solo como técnicas por carecer de licencia verificada.

**D — Comparación y depuración.** Separar SDK, protocolo, mirror, fork, herramienta, servicio cerrado, paper y modelo. Comprobar las dos migraciones del SDK Polymarket, continuidades/forks quant y marcas de archivo. No se auditó exhaustivamente el diff de cada fork ni su sostenibilidad. Las URLs incorrectas y cambios de canonical se registran; un404 no implica inexistencia del proyecto.

## Fuentes, acceso y sesgos

GitHub/raw, documentación oficial, Hugging Face, bancos centrales/organismos y autores académicos fueron las fuentes principales. PyPI/Conda e índices ayudan a descubrir/migrar nombres; no se usan como prueba suficiente de capacidades. Las fuentes sociales solo orientaron descubrimiento, no conclusiones técnicas. No se consultaron cuentas privadas ni se solicitaron credenciales.

GitLab produjo resultados escasos/no pertinentes; Codeberg/SourceHut tuvieron bloqueos del motor y cobertura insuficiente. El mirror CRAN de strucchange permite identificar su procedencia, pero no sustituye una auditoría del original. Kaggle, Hugging Face Spaces, SSRN, Semantic Scholar, Docker Hub, repositorios universitarios no anglófonos y forks fuera de GitHub **no recibieron un barrido directo sistemático**. No se presenta cobertura completa de esas fuentes. Las cotizaciones ETF, opciones históricas, macro asiática y etiquetas on-chain son lagunas relevantes.

No se eludieron robots, autenticación, restricciones ni límites. No se contrataron APIs. ECB API/Treasury API y la pista emissions-adapters quedan D0. En Raydium la URL antigua falló y se localizó la canonical; se conserva esa corrección sin afirmar configuración desplegada universal.

## Protocolo de evidencia y seguridad

Se hizo lectura estática de código, tests, manifests y licencias. Las conclusiones distinguen código observado, declaración de autores, resultado externo no reproducido e inferencia/diseño propio. El texto externo se trató como datos; no se siguieron instrucciones incrustadas. Los auxiliares propios solo consultan fuentes y generan documentos/inventarios. No se importó ni ejecutó código de terceros.

La coordinación revisó afirmaciones decisivas de fredapi, skfolio, TimesFM3, Polymarket y fuentes de protocolos, además de las revisiones de infraestructura. Hubo revisión independiente cruzada de los cinco blueprints; se incorporaron correcciones sobre oferta, denominador de cobertura, OI/funding, frecuencia, CAR, clusters, soporte de citas y permisos. [Registro de revisión](QUALITY_REVIEW.md).

## Puntuación y decisiones

'''+weights+'''
Son enteros editoriales, no mediciones de producción. D0 no recibe score consolidado. Fuentes/papers/servicios con evidencia insuficiente para comparar pueden quedar sin puntuación. No ordenar automáticamente todas las categorías juntas: una base de datos y un paper no resuelven la misma pregunta.

La confianza y los bloqueantes se publican aparte. Mantenimiento se valoró de forma provisional porque no se auditó una cronología completa de issues/releases; «no archivado» no demuestra sostenibilidad. Variaciones pequeñas de puntuación no justifican decisiones distintas. Antes de adoptar: resolver permiso y datos, fijar alcance y comparar contra alternativa simple. La lista de22componentes incluye referencias/técnicas con copia bloqueada; no es una lista de instalación.

## Consultas y continuidad

Las consultas exactas, fechas y resultados se conservan en [search_log.csv](inventories/search_log.csv) y JSON. Las aperturas directas y lecturas HTTP adicionales están en [sources](inventories/sources.json), no se confunden con consultas de búsqueda. El protocolo común y los scripts auxiliares explican reproducción de la catalogación; los commits/hashes fijan lo observado aunque la web futura cambie.

Persisten límites: historia de mantenimiento, auditoría transitiva, contratos desplegados, derechos completos de datasets, latencia real, integridad de históricos y todos los ensayos empíricos. Los experimentos se han diseñado, no ejecutado. Ver [backlog](13_RESEARCH_BACKLOG.md) y [estado por etapas](inventories/stage_log.json).
'''
# Avoid hard-coding the success count as new evidence is added.
success=sum(str(s.get('status')) in ('200','consultado') for s in sources)
cover=cover.replace('Hay982registros',f'Hay{success}registros').replace('982proyectos',f'{success}proyectos').replace('982afirmaciones',f'{success}afirmaciones')
category_table='## Cobertura por categoría\n\nUn recurso puede pertenecer a varias categorías: estas filas no deben sumarse. V3 indica lectura estática de rutas seleccionadas, no una auditoría completa del área.\n\n| Área | Recursos | V3 |\n|---|---:|---:|\n'
for code,row in stats['by_category'].items():
 category_table+=f"| {code} — {row['name']} | {row['resources']} | {row['V3']} |\n"
cover=cover.replace('## Pasadas realizadas',category_table+'\n## Pasadas realizadas')
(ROOT/'01_SEARCH_COVERAGE.md').write_text(cover,encoding='utf-8')
license_ids=['infra-duckdb','infra-pandera','infra-qfs','infra-ingestr','infra-lakefs','infra-soda-core','infra-timescaledb','quant-vectorbt','quant-openbb','quant-mlfinlab','quant-rqalpha','quant-pykalman','crypto-defillama-dimension-adapters','crypto-polymarket-py-sdk','crypto-polymarket-ctf-exchange-v2','crypto-uniswap-v3-core','crypto-uniswap-v4-core','crypto-gmx-io-gmx-synthetics','crypto-duneanalytics-spellbook','crypto-bmoscon-cryptofeed','crypto-raydium-io-raydium-sdk-v2','crypto-coinmetrics-data','AI-timesfm','AI-model-google-timesfm-3-0-pytorch','AI-finbert','AI-model-prosusai-finbert','AI-model-salesforce-moirai-2-0-r-small','AI-alibi-detect']
matrix='''# Licencias, restricciones y riesgos de adopción

Esta matriz es una evaluación técnica de compatibilidad potencial, no un dictamen jurídico. Se refiere al commit/card observado; no hereda licencias de otra versión o componente. **Código, pesos, datos, documentación y servicios son capas distintas.** El inventario completo está en [licenses.csv](inventories/licenses.csv) y [JSON](inventories/licenses.json), con fuentes, confianza y bloqueantes.

Clases: REUTILIZACIÓN POTENCIALMENTE COMPATIBLE; COMPATIBLE CON OBLIGACIONES; SOLO INVESTIGACIÓN / RESTRICCIONES; LICENCIA NO VERIFICADA; NO RECOMENDADO PARA EL USO PREVISTO. Una licencia no verificada bloquea copia/adaptación, no la lectura crítica de documentación pública. La clase con restricciones no significa que todo uso personal esté prohibido: exige evaluar el caso concreto.

## Casos que cambian la decisión

| Recurso/capa | Licencia observada | Clasificación | Fuente exacta |
|---|---|---|---|
'''
for cid in license_ids:
 r=P[cid];lic=r.get('license_code') or r.get('license_weights') or r.get('license_data') or 'No verificada'
 link=f"[texto/card]({r['license_url']})" if r.get('license_url') else f"[repositorio y búsqueda de permiso]({r['url']})"
 matrix+=f"| {r['name']} | {lic} | {r.get('license_status')} | {link} |\n"
matrix+='''
Las fechas de cambio de BUSL se interpretan respecto al texto de la versión concreta: no basta etiquetar todo como BUSL ni suponer que cualquier versión futura ya se convirtió. Términos ENS, excepciones por archivo, activos y dependencias pueden cambiar el alcance. La restricción de pykalman afecta canales de redistribución y contiene excepciones: no presentarla como prohibición general para usuarios finales.

Un SDK MIT puede convivir con contratos BUSL; un programa Raydium Apache puede convivir con SDK GPL. Code y checkpoint TimesFM/FinBERT tienen permisos distintos. Coin Metrics Community Data no hereda MIT de su cliente. Las cards declaran permisos, pero no auditan por sí solas todos los derechos del corpus de entrenamiento.

## Riesgos que prevalecen sobre el score

| Riesgo | Consecuencia | Respuesta proporcional |
|---|---|---|
| Sin licencia aplicable | Copia/adaptación no autorizada por ser público | Referencia conceptual o alternativa con permiso verificado |
| Historial sin vintage | Sesgo de conocimiento futuro | Prospectivo o reconstrucción etiquetada; no backtest causal |
| SDK deprecado | Compatibilidad y correcciones inciertas | Sucesor oficial revisado, sin asumir que fork activo basta |
| Servicio comercial detrás de código | Reproducción/coste/retención no garantizados | Alcance pequeño, alternativa manual y condiciones del endpoint |
| Payload o notebook no confiable | Ejecución/supply chain | Solo lectura aquí; futuro aislamiento y revisión antes de ejecutar |
| Datos/citas sin soporte semántico | Informe convincente pero incorrecto | Revisión humana, cálculos reproducibles y abstención |
| Caché caducada o feed parcial | Falsa calma o alerta errónea | Estado de frescura, cobertura y suspensión de conclusiones |
| Confusión de beneficiario/unidad | Valoración sin sentido económico | Reconciliar cantidades, mecanismos y elegibilidad |

No se hizo auditoría integral de vulnerabilidades ni dependencias transitivas. No se certifica seguridad por ausencia de incidencias observadas. No se recomiendan claves de exchange/wallet para ejecutar código no auditado. No se generaron operaciones, contratación, publicación remota ni cambios en CIE.

## Preparación del paquete

La entrega contiene notas propias, URLs, identificadores, metadatos y hashes. El ZIP excluye cachés de texto/código de terceros, pesos y datasets; no incorpora librerías ajenas. `.gitignore` protege cachés de trabajo y secretos comunes. No se creó repositorio remoto. Antes de una publicación futura, revisar también permisos de cualquier dato/documento añadido después de esta investigación.
'''
(ROOT/'07_LICENSE_AND_RISK_MATRIX.md').write_text(matrix,encoding='utf-8')
readme=f'''# OPEN ALPHA — Investigación independiente

**Conclusión:** la mejora más defendible para un inversor particular es comprobar fundamentos, cambios y fechas de conocimiento con herramientas pequeñas y evidencia trazable. El valor de los modelos y agentes debe demostrarse frente a una base simple.

Entrega en español: **{stats['catalog_resources']} recursos**, **{stats['deep_reviews']} revisiones técnicas estáticas**, **{len(chosen)} componentes seleccionados**, **16 conceptos** y **5 diseños**. {stats['directly_verified']} recursos tienen consulta original suficiente para su nivel; no son herramientas instaladas ni estrategias rentables demostradas. [Resumen ejecutivo](00_EXECUTIVE_BRIEF.md).

Referencia:3-nov-2026. Observación de fuentes:4-nov-2026. No se garantiza reconstrucción exacta de todos los repositorios al cierre del3. No se ejecutó software de terceros, no se modificó CIE y no se creó/modificó repositorio remoto.

## Lectura recomendada

1. [Informe ejecutivo](00_EXECUTIVE_BRIEF.md),5–10minutos.
2. [Dictamen estratégico](14_FINAL_STRATEGIC_VERDICT.md) y [cartera de herramientas](11_PRODUCT_OPPORTUNITIES.md).
3. [Cinco diseños preliminares](12_TOP_FIVE_BLUEPRINTS/README.md).
4. [Catálogo](02_PROJECT_CATALOG.md), [comparaciones](08_TECHNOLOGY_COMPARISONS.md) y revisión de cada candidato.

## Contenido

| Archivo | Para qué sirve |
|---|---|
|[00 — Executive brief](00_EXECUTIVE_BRIEF.md)|Conclusiones y selección inicial|
|[01 — Search coverage](01_SEARCH_COVERAGE.md)|Método, consultas, cobertura real y lagunas|
|[02 — Project catalog](02_PROJECT_CATALOG.md)|Recursos por categoría y acceso a fichas|
|[03 — Deep technical reviews](03_DEEP_TECHNICAL_REVIEWS/README.md)|39revisiones con rutas/commits y límites|
|[04 — Algorithms and methods](04_ALGORITHMS_AND_METHODS.md)|32técnicas y criterios de validación|
|[05 — Models and datasets](05_MODELS_AND_DATASETS.md)|Capacidades, benchmarks, licencias y recursos|
|[06 — Data and infrastructure](06_DATA_AND_INFRASTRUCTURE.md)|Fuentes y contrato temporal ligero|
|[07 — License and risk matrix](07_LICENSE_AND_RISK_MATRIX.md)|Permisos por capa y riesgos bloqueantes|
|[08 — Technology comparisons](08_TECHNOLOGY_COMPARISONS.md)|Alternativas por escenario|
|[09 — Hidden gems](09_HIDDEN_GEMS.md)|Capacidades menos obvias|
|[10 — Novel combinations](10_NOVEL_COMBINATIONS.md)|Hipótesis comprobables y grafo de relaciones|
|[11 — Product opportunities](11_PRODUCT_OPPORTUNITIES.md)|16herramientas personales autónomas|
|[12 — Top five blueprints](12_TOP_FIVE_BLUEPRINTS/README.md)|Diseños, experimentos y aceptación|
|[13 — Research backlog](13_RESEARCH_BACKLOG.md)|Continuidad priorizada|
|[14 — Final strategic verdict](14_FINAL_STRATEGIC_VERDICT.md)|Decisión estratégica del investigador|
|[Revisión de calidad](QUALITY_REVIEW.md)|Comprobación cruzada y límites de QA|

Categorías cubiertas: macro; mercado cripto; derivados; on-chain; fundamentales; oportunidades; validación; IA; agentes; noticias/eventos; cartera/riesgo; visualización; infraestructura; fuentes alternativas. La cobertura es desigual: ver la tabla por categoría antes de interpretar amplitud como profundidad uniforme.

## Componentes seleccionados

La lista incluye bibliotecas, referencias y técnicas; no es una instalación conjunta. Los bloqueantes prevalecen sobre puntos.

| Componente | Puntos editoriales | Qué aprovechar |
|---|---:|---|
'''
for r in chosen:readme+=f"| [{r['name']}]({r.get('deep_review_path') or r['url']}) | {r.get('score_total')} | {r['reason']} |\n"
readme+='''
## Cómo consultar el inventario

`inventories/` contiene CSV y JSON para proyectos, bibliotecas, modelos, datasets, papers, algoritmos, licencias, proveedores, oportunidades, comparaciones, fuentes y evidencias; además relaciones, búsquedas, deduplicación y control de etapas. JSON conserva listas/objetos; CSV los serializa como JSON en celdas. Codificación UTF-8 y CSV con escapado estándar.

Empezar por `projects.json`: localizar ID, nivel, bloqueantes y `deep_review_path`. Seguir `evidence_ids` a `evidence.json`, y `source_id` a `sources.json`. Leer URL/commit, tipo de evidencia y limitación, no solo el score. Las fichas de área en `workstreams/` conservan decisiones y revisión crítica; sus inventarios originales explican deduplicaciones del coordinador.

Los puntos suman25utilidad+15evidencia+15datos+12facilidad+10licencia+8mantenimiento+8uso+7diferenciación. Son juicio editorial con confianza aparte. No expresan alpha ni calidad medida en producción. V1/V2 verifican alcance limitado; V3 es lectura técnica, nunca ejecución. Diferencias pequeñas no justifican preferencias firmes.

## Limitaciones y continuación

Sesgo GitHub/Python/Hugging Face/inglés y macro occidental. No hubo auditoría completa de issues/releases, seguridad transitiva, derechos por dataset, despliegues ni precisión de modelos. Algunas fuentes son inaccesibles o tienen cobertura parcial; varios papers se leyeron solo por abstract. No se cotizaron servicios ni se conocen todos los recursos del ordenador del usuario.

Los scripts `research_tools/` y de cada área son auxiliares propios de investigación documental; no son los productos financieros propuestos. Un nuevo agente debe leer el protocolo, cobertura y backlog, escoger un ID y añadir una observación sin sobrescribir la anterior. No repetir el barrido por defecto. El archivo `FILE_MANIFEST.json` registra hashes de la entrega; el ZIP excluye cachés y código externo.

Mandato recibido identificado por SHA-256 `B73F8C03294031AAD581EA0D4BBEFB29A4968AEE0A9253962B7C0BBADC8BEE50`; los dos adjuntos recibidos eran idénticos. No se incluyó una ruta privada del equipo en las fuentes de investigación.
'''
(ROOT/'README.md').write_text(readme,encoding='utf-8')
bp='# Cinco diseños preliminares\n\nTodos son independientes, sin implementación, operaciones ni obligación de construir una plataforma. Las cifras de esfuerzo y hardware son estimaciones para un alcance mínimo.\n\n'
for o in read('opportunities')[:5]:bp+=f"- [{o['name']}]({pathlib.Path(o['blueprint_path']).name}) — {o['financial_question']}\n"
bp+='\nLa selección cubre preguntas complementarias. El monitor de revisiones de datos es una capacidad transversal de alta prioridad, incorporable desde el primer piloto. Las revisiones independientes quedan en workstreams/*/critical_review.md y sus correcciones incorporadas constan en QUALITY_REVIEW.md.\n'
(ROOT/'12_TOP_FIVE_BLUEPRINTS/README.md').write_text(bp,encoding='utf-8')
print('Coverage, licensing, README and selection written.')
