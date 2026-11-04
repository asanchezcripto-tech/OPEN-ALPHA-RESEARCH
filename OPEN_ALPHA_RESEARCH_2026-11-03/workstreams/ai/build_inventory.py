"""Build research records from observed metadata and analyst annotations (no third-party execution)."""
import json,re,hashlib
from pathlib import Path
BASE=Path(__file__).parent; DATE='2026-11-04'
repos=json.loads((BASE/'observations_repos.json').read_text(encoding='utf-8'))
hf=json.loads((BASE/'observations_hf.json').read_text(encoding='utf-8'))
code=json.loads((BASE/'observations_code.json').read_text(encoding='utf-8'))
# name | category | practical function | input -> output | limiting condition | alternative
ANNOTATIONS='''
chronos|Chronos forecasting library|H,G|Forecast probabilístico con covariables y comparación zero-shot|Series regulares y covariables conocidas -> cuantiles por horizonte|Cross-learning exige sincronizar el conocimiento entre series; no valida rentabilidad|MLForecast + modelo naive
timesfm|TimesFM library|H,G|Estudiar forecasting multivariable y comparar generaciones de modelos|Historia y covariables -> mediana y cuantiles|Código Apache no cubre pesos3.0; imputación no debe cruzar el corte temporal|Chronos2; TimesFM2.5
uni2ts|Uni2TS / Moirai|H,G|Aprovechar tratamiento de máscaras y adaptación de horizontes|Series con missingness -> pronósticos probabilísticos|Pesos Moirai CC-BY-NC; tests de Moirai1 no certifican Moirai2|Chronos2
gift-eval|GIFT-Eval|G,H|Reutilizar protocolo de evaluación y separación pretrain/test|Datasets heterogéneos -> tabla comparable de errores|Benchmark creado por proveedor de modelos; contaminación global no queda descartada|fev y evaluación prospectiva propia
fev|Forecast Evaluation (fev)|G,H|Definir tareas con cortes, covariables y fingerprints reproducibles|Datasets + tarea -> métricas por ventana e ítem|Known-future depende de clasificación del analista; no comprueba publicación macro|MLForecast cross_validation
autogluon|AutoGluon|H,G|Comparar modelos tabulares y temporales dentro de un experimento|Tablas/series -> selección y ensembles|AutoML amplía búsqueda múltiple y coste; modelos integrados tienen licencias propias|MLForecast con baseline fijo
gluonts|GluonTS|H,G|Modelos probabilísticos y representaciones de forecasts|Series y splits -> distribuciones/estimaciones|No aplica automáticamente costes, universos históricos ni reglas financieras|StatsForecast
statsforecast|StatsForecast|H,G|Baselines ARIMA/ETS/Theta y naive económicos en CPU|Series univariadas regulares -> forecasts e intervalos|Estacionalidad y persistencia de magnitudes no prueban predecibilidad del retorno|MLForecast
mlforecast|MLForecast|H,G|Lags y boosting con validación temporal reproducible|Panel por identificador/fecha -> forecasts e intervalos|La CV no es purged CV financiera ni reconstruye vintages|StatsForecast; Chronos2
neuralforecast|NeuralForecast|H,G|Comparación de NBEATS/NHITS/TFT y otras arquitecturas|Series multivariadas -> forecasts|Mayor coste de búsqueda y ajuste; GPU puede ser útil|MLForecast
darts|Darts|H,G|Interfaz común para forecasting, backtesting y anomalías|TimeSeries -> forecasts y anomaly scores|Superficie/dependencias amplias para pocas series; covariables futuras pueden filtrar información|sktime; MLForecast
sktime|sktime|H,G|Pipelines y validación temporal con múltiples estimadores|Series/paneles -> predicciones/clasificación/cambios|Abstracción no sustituye diseño del experimento financiero|aeon; StatsForecast
pytorch-forecasting|PyTorch Forecasting|H,G|TFT y redes con interfaces de entrenamiento|Dataset temporal -> pronósticos entrenados|Datos propios y GPU para entrenamiento; evitar modelo grande sin baseline|NeuralForecast
timeseries-library|Time-Series-Library|H,G|Extraer implementaciones comparables de modelos académicos|Datasets de forecasting/clasificación -> resultados|README abril2026 avisa menor desarrollo y benchmarks anticuados|fev; aeon
lag-llama|Lag-Llama|H|Estudiar pronósticos probabilísticos con lags|Historia -> muestras probabilísticas|Licencia de pesos no revisada; documentación registra corrección crítica de KV cache|Chronos2
moment|MOMENT|H|Explorar representación general para clasificación/anomalías|Ventanas de series -> embeddings y tareas adaptadas|Pesos/datos de Timeseries-PILE no auditados; requiere experimento específico|TSFEL + boosting
granite-tsfm|IBM Granite TSFM|H|Explorar forecasters compactos y ajuste ligero|Series -> forecast; utilidades de serving|Variantes de pesos/horizonte/frecuencia deben seleccionarse explícitamente|Chronos-Bolt
tirex|TiRex|H|Referencia xLSTM de forecasting|Serie -> cuantiles|NXAI Community License no es licencia permisiva estándar; versión2 separada|TiRex2; Chronos2
tabpfn|TabPFN|H|Baseline para pequeños paneles de características|Tabla de features -> predicciones tabulares|Licencia de código no cubre automáticamente cada generación de pesos; GPU recomendada por autores|LightGBM
lightgbm|LightGBM|H,F|Baseline de árboles para factores y clasificación de escenarios|Features tabulares -> scores/predicciones|Necesita splits temporales; riesgo de proxies de identidad y leakage|CatBoost
catboost|CatBoost|H,F|Comparar árboles con variables categóricas de protocolos|Features numéricas/categóricas -> scores|No interpretar importancia de variable como causalidad|LightGBM
xgboost|XGBoost|H,F|Baseline de boosting ampliamente reutilizable|Features -> regresión/clasificación|Optimización reiterada requiere holdout protegido y registro de pruebas|LightGBM
river|River|H,B,M|Detectar drift en residuos y métricas de calidad de datos|Observaciones ordenadas -> cambios/estadísticos online|ADWIN detecta cambios de distribución, no regímenes rentables; dependencia temporal altera falsas alarmas|ruptures; EWMA
pyod|PyOD|H,F|Comparar detectores de anomalías multivariadas|Features normalizadas -> anomaly scores|Contaminación/escala y dependencia temporal; componente agentic opcional no necesario|River; robust z-score
merlion|Merlion|H|Extraer arquitectura de ensembles de anomalías|Series -> alertas/forecasts|Repositorio archivado observado; no adoptar como nueva dependencia central|River; Darts
adtk|ADTK|H|Detectores interpretables basados en reglas y agregadores|Series -> eventos anómalos|MPL2.0 y compatibilidad de versiones por revisar antes de adaptar|River; reglas robustas propias
alibi-detect|Alibi Detect|H|Referencia de drift multivariable y pruebas de distribución|Datos referencia/actuales -> drift scores|BSL1.1 actual limita producción; no asumir Apache histórico|Evidently; River
evidently|Evidently|H,M|Informes de calidad y drift de entradas/salidas|Tablas/referencias -> métricas e informes|Cloud separado del código; drift no identifica causa económica|Pandera + River
dowhy|DoWhy|J,H|Explicitar supuestos causales y refutaciones de hipótesis|DAG y datos -> estimación/refutaciones|Identificación causal depende de supuestos no verificables solo con datos|Event study controlado
econml|EconML|J,H|Explorar efectos heterogéneos y double ML|Tratamiento/outcome/covariables -> efectos condicionales|Confusión no observada e interferencia entre activos invalidan estimaciones|DoWhy; regresión preespecificada
causal-learn|causal-learn|J,H|Descubrimiento causal como generador de hipótesis|Datos y supuestos -> grafo causal candidato|No convierte independencia estadística en causalidad económica demostrada|DoWhy
fingpt|FinGPT|I,H,J|Extraer tareas financieras y estudiar errores de diseño temporal|Noticias/series/API -> corpus, análisis y adapters LLM|Ruta Forecaster usa perfil actual en histórico y rationale condicionado al resultado; pesos y datos separados|Flujo determinista con evidencia
finrobot|FinRobot|I,H|Referencia de organización de herramientas y análisis financiero|Documentos/APIs + LLM -> informes|Framework no es evidencia de rentabilidad ni datos crypto completos; proveedores cerrados|Pydantic AI mínimo
tradingagents|TradingAgents|I,G|Extraer controles as-of, abstención y registro de contexto|Datos fechados y herramientas -> informes/decisiones simuladas|Filtros de herramientas no borran memoria de entrenamiento del LLM; coste de debates|Flujo determinista + un revisor
ai-hedge-fund|AI Hedge Fund|I|Referencia educativa de análisis por agentes|APIs financieras + LLM -> señales simuladas|PoC; datos externos; README ofrece ruta de pago con wallet que queda excluida|Thesis Tracker con lectura sola
finbert|FinBERT code|H,J|Baseline de sentimiento y estudio de truncado/calibración|Texto inglés -> positivo/negativo/neutro|Pesos CC-BY-NC-SA4.0 y datos CC-BY-NC-SA3.0; sentimiento no es retorno|Clasificador local entrenado sobre etiquetas propias
finqa|FinQA code / benchmark repository|H,I|Evaluar aritmética verificable sobre informes|Tabla/texto -> programa y resultado numérico|README documenta antiguo label leakage corregido; MIT de código no prueba permisos de documentos|TAT-QA; test propio
tatqa|TAT-QA|H,I|Evaluar combinación de tabla y texto financiero|Contexto híbrido -> respuesta y operaciones|Datos de empresas cotizadas no cubren tokenomics; permisos subyacentes por revisar|FinQA
financebench|FinanceBench repository|H,I|Referencia de preguntas con evidencias documentales|150 casos públicos -> evaluación de QA|No LICENSE encontrado en rutas estándar; card HF separada CC-BY-NC; 10231 no todos públicos|Dataset propio de protocolo
convfinqa|ConvFinQA|H,I|Pruebas de razonamiento numérico conversacional|Conversaciones + tablas -> cadena de operaciones|Dependencias antiguas y datos heredados FinQA; benchmark fijo puede estar contaminado|FinQA propio prospectivo
docling|Docling|I,J,M|Extraer tablas y contenido con estados de fallo para citar fuentes|PDF/HTML/Office -> documento estructurado|MIT de código no licencia todos los modelos OCR/VLM; formato correcto no implica cifra correcta|Trafilatura para HTML
unstructured|Unstructured library|I,M|Particionar documentos en elementos|PDF/HTML/Office -> bloques estructurados|API Transform v2 y modelos alojados son producto aparte; no atribuir sus resultados al OSS|Docling
marker|Marker|I,M|Conversión PDF a formato procesable|PDF -> Markdown/JSON|Código Apache actual, pesos con licencia propia y umbral comercial; no licencia única|Docling
trafilatura|Trafilatura|I,J|Extracción ligera de texto y metadatos web|HTML -> texto estructurado|Derechos de páginas y fecha publicada deben comprobarse aparte; versiones antiguas GPL|Docling HTML
sentence-transformers|Sentence Transformers|I,H|Embeddings y rerankers para recuperar evidencia|Texto -> vectores/scores|Licencia por checkpoint independiente; similitud semántica no verifica una cifra|BM25
flagembedding|FlagEmbedding|I,H|Recuperación híbrida/multilingüe BGE|Texto -> embeddings/sparse/reranking|Cada peso y tokenizer requiere su propia revisión; latencia por medir|Sentence Transformers
haystack|Haystack|I|Pipelines de recuperación y composición verificable|Documentos/queries -> contexto y respuesta|Demasiados componentes pueden dificultar trazabilidad; modelo/servicio aparte|Funciones simples + Pydantic
llamaindex|LlamaIndex framework|I|Conectores y herramientas de documentos|Documentos -> índice/consultas/agentes|README diferencia foco comercial LlamaParse; conectores no transfieren permisos|Haystack
langgraph|LangGraph|I|Estado durable y pasos explícitos de investigación|Estado y herramientas -> grafo de ejecución|Multiagente es opción, no ventaja probada; servicio LangSmith separado|Pydantic AI o máquina de estados simple
pydantic-ai|Pydantic AI|I|Esquemas de salida, herramientas tipadas y validación|Evidencias/queries -> salidas estructuradas|Validación de esquema no demuestra verdad de contenido|Funciones + JSON Schema
dspy|DSPy|I,H|Optimizar prompts/pipelines contra tareas medibles|Ejemplos etiquetados -> programa optimizado|Optimización del evaluador puede sobreajustar; reservar conjunto humano|Prompt fijo + evaluación ciega
ragas|Ragas|I,H|Medir aspectos de recuperación y respuesta|Queries/contextos/respuestas -> métricas|Juez LLM no es evidencia independiente y puede compartir errores|Inspect AI con gold set humano
inspect-ai|Inspect AI|I,H|Evaluaciones reproducibles de LLM y tool use|Tareas/scorers -> logs y puntuaciones|Scorer debe comprobar fuentes y aritmética; inferencia puede costar|Promptfoo
garak|garak|I|Ensayar resistencia a fallos e inyección en entorno controlado|Prompts/targets -> vulnerabilidades observadas|No certifica ausencia de fallos; ataques solo sobre sistema propio autorizado|Pruebas adversariales específicas
pyrit|PyRIT (repositorio observado)|I|Referencia histórica de evaluación de riesgo|Prompts y objetivos -> resultados de pruebas|Repositorio observado archivado; sucesor no verificado|garak; Inspect AI
promptfoo|Promptfoo|I|Comparar prompts y automatizar evaluaciones|Casos/configuración -> matriz de resultados|Proveedores/API y SaaS separados; costes multiplican por prueba|Inspect AI
llm-guard|LLM Guard|I|Referencia de scanners de contenido|Texto -> detecciones/sanitización|Repositorio archivado; detector de inyección no crea frontera de confianza|Allowlist de herramientas + separación de datos
tsfel|TSFEL|H,F|Features estadísticas/temporales/espectrales de bajo coste|Ventanas temporales -> vector de características|Elegir docenas de features sin holdout multiplica falsos hallazgos|TSFresh reducido
tsfresh|TSFresh|H,F|Extracción y selección estadística de features|Series etiquetadas -> features seleccionadas|Selección debe ocurrir dentro del fold; control FDR no elimina dependencia temporal|TSFEL + selección preespecificada
aeon|aeon|H|Clasificación, clustering y anomalías de series con interfaces comunes|Colecciones de series -> tareas ML|No es suite de inversión; verificar entrenamiento solo con pasado|sktime
tirex2|TiRex-2|H|Alternativa actual multivariable al TiRex original|Series/covariables -> forecast|Licencia Apache del código verificada; pesos aún no auditados; no heredar issue viejo de flashrnn sin revisar versión|Chronos2
finllm-eval|Tencent finLLM-Eval|I,H|Separar hechos, cadenas lógicas y tripletas activo-fecha-métrica|Respuesta + RAG -> evaluación de consistencia|README dice que evaluación de cifras depende de base interna no incluida; licencia no localizada|Gold set propio + cálculo determinista
'''.strip()
ann={}
for row in ANNOTATIONS.splitlines():
 s,n,c,p,io,lim,alt=row.split('|');ann[s]=(n,c.split(','),p,io,lim,alt)
DEEP=['chronos','timesfm','uni2ts','fev','mlforecast','river','tradingagents','docling','fingpt','finbert']
PRIORITY={
'chronos':[21,12,11,8,9,6,5,6],'timesfm':[17,11,10,6,4,6,4,5],
'uni2ts':[17,11,10,6,4,5,4,5],'fev':[23,13,13,10,9,6,6,6],
'mlforecast':[23,13,12,10,9,6,6,5],'river':[22,13,12,10,9,6,6,6],
'tradingagents':[18,11,8,6,9,6,5,5],'docling':[23,13,12,9,8,6,6,6],
'fingpt':[14,8,6,4,7,4,4,4],'finbert':[16,10,8,9,4,4,6,3],
'statsforecast':[22,11,12,11,9,6,6,4],'trafilatura':[22,11,12,11,9,6,7,4]}
PRIORITY.update({
'gift-eval':[18,9,11,8,9,5,5,5], 'autogluon':[19,9,10,6,9,5,5,4],
'gluonts':[17,9,10,7,9,5,5,4], 'neuralforecast':[17,9,9,6,9,5,5,4],
'darts':[19,9,10,8,9,5,6,4], 'sktime':[18,9,10,8,9,5,5,4],
'pytorch-forecasting':[16,9,8,5,9,5,4,4], 'timeseries-library':[14,8,8,5,9,3,4,4],
'lag-llama':[14,8,8,6,7,4,4,4], 'moment':[17,9,8,6,7,5,4,6],
'granite-tsfm':[19,9,10,8,8,5,5,5], 'tirex':[17,9,9,6,3,5,5,5],
'tabpfn':[16,9,9,6,6,5,5,5], 'lightgbm':[22,10,11,10,9,5,6,4],
'catboost':[20,9,11,9,9,5,6,4], 'xgboost':[20,9,11,9,9,5,6,4],
'pyod':[20,9,11,9,9,5,6,5], 'merlion':[15,8,9,6,9,1,5,4],
'adtk':[17,9,10,9,7,4,6,4], 'alibi-detect':[18,9,10,6,3,5,5,5],
'evidently':[20,9,11,9,9,5,6,5], 'dowhy':[19,9,7,6,9,5,4,6],
'econml':[16,9,6,5,9,5,4,6], 'causal-learn':[16,9,6,5,9,5,4,6],
'finrobot':[16,8,7,5,9,5,4,4], 'ai-hedge-fund':[12,8,6,5,9,5,4,3],
'finqa':[18,9,9,7,8,4,5,5], 'tatqa':[18,9,9,6,8,4,5,5],
'financebench':[18,8,9,8,1,4,5,5], 'convfinqa':[16,8,8,6,8,4,5,5],
'unstructured':[19,9,11,7,8,5,6,4], 'marker':[18,9,10,7,6,5,6,5],
'sentence-transformers':[21,9,11,9,8,5,6,4], 'flagembedding':[20,9,11,8,8,5,6,5],
'haystack':[18,9,9,7,9,5,5,4], 'llamaindex':[17,9,9,7,9,4,5,4],
'langgraph':[18,9,9,7,9,5,5,4], 'pydantic-ai':[21,9,10,9,9,5,6,5],
'dspy':[17,9,8,6,9,5,4,6], 'ragas':[19,9,9,7,9,5,5,4],
'inspect-ai':[21,9,10,8,9,5,5,5], 'garak':[17,9,8,6,9,5,4,5],
'pyrit':[12,8,8,5,9,1,4,4], 'promptfoo':[20,9,10,8,9,5,6,4],
'llm-guard':[12,8,8,6,9,1,5,3], 'tsfel':[19,9,11,10,9,5,6,5],
'tsfresh':[18,9,10,8,9,5,5,5], 'aeon':[17,9,10,8,9,5,5,4],
'tirex2':[19,9,10,7,8,5,5,5], 'finllm-eval':[16,7,5,4,1,4,4,6]})
KEYS=['utility','evidence','data','ease','license','maintenance','usability','differentiation']
def classify_license(t):
 if not t:return None,'LICENCIA NO VERIFICADA'
 if 'Business Source License' in t:return 'BUSL-1.1','SOLO INVESTIGACIÓN / RESTRICCIONES'
 if 'NXAI COMMUNITY LICENSE' in t:return 'NXAI Community License','SOLO INVESTIGACIÓN / RESTRICCIONES'
 if 'Mozilla Public License Version 2.0' in t:return 'MPL-2.0','COMPATIBLE CON OBLIGACIONES'
 if 'Apache License' in t:return 'Apache-2.0','REUTILIZACIÓN POTENCIALMENTE COMPATIBLE'
 if 'BSD 3-Clause' in t or 'Neither the name' in t or 'neither the name' in t:return 'BSD-3-Clause','REUTILIZACIÓN POTENCIALMENTE COMPATIBLE'
 if 'BSD 2-Clause' in t:return 'BSD-2-Clause','REUTILIZACIÓN POTENCIALMENTE COMPATIBLE'
 if 'Permission is hereby granted, free of charge' in t:return 'MIT','REUTILIZACIÓN POTENCIALMENTE COMPATIBLE'
 return None,'LICENCIA NO VERIFICADA'
sources=[];evidence=[];candidates=[];relations=[]
def src(sid,url,title,kind,commit,status=200,notes=None,sha=None):
 if not any(s['id']==sid for s in sources):sources.append(dict(id=sid,url=url,title=title,accessed_at=DATE,source_type=kind,status=status,version_or_commit=commit,notes=notes,sha256=sha))
 return sid
def ev(cid,sid,claim,etype,lim):
 eid='E-'+cid+'-'+str(sum(e['candidate_id']==cid for e in evidence)+1)
 evidence.append(dict(id=eid,candidate_id=cid,source_id=sid,claim=claim,evidence_type=etype,limitations=lim));return eid
for r in repos:
 s=r['slug']; cid='AI-'+s; n,cat,use,io,lim,alt=ann[s]; eids=[];sids=[]
 root=r['root'];url=root.get('resolved_url',root['url']);org=url.split('/')[3]
 sids.append(src('S-AI-'+s+'-root',root['url'],n+' repositorio','repositorio',r['commit'],root['status'],'Snapshot observado, no reconstrucción garantizada al cierre del 3 de noviembre.',root.get('sha256')))
 for k,f in r['files'].items():
  sid=src('S-AI-'+s+'-'+k,f['url'],n+' '+k,'licencia' if k=='license' else 'documentación',r['commit'],f['status'],sha=f.get('sha256'));sids.append(sid)
  eids.append(ev(cid,sid,'Licencia del código inspeccionada; alcance separado de pesos/datos.' if k=='license' else use,'texto de licencia' if k=='license' else 'documentación primaria','No ejecución; no auditoría de todas las dependencias.'))
 lic,lstat=classify_license(r['files'].get('license',{}).get('excerpt',''))
 if r.get('license_verified') is not None:
  lic,lstat=r['license_verified'],r['license_status_verified']
 cs=[]
 if s in DEEP:
  cs=[x for x in code if x['slug']==s and x['status']==200 and (x.get('excerpt') or x.get('inspected_static'))]
  for idx,x in enumerate(cs):
   sid=src('S-AI-'+s+'-code-'+str(idx+1),x['url'],x['path'],'tests' if 'test' in x['path'] else 'código/configuración',r['commit'],200,'Consulta estática; alcance en revisión técnica.',x.get('sha256'));sids.append(sid)
  eids.append(ev(cid,sids[-1],'Se inspeccionaron rutas de implementación y límites; véase revisión técnica.','revisión estática','Sin ejecutar tests, modelos ni dependencias.'))
 vals=PRIORITY.get(s,[17,9,9,8,9 if lic else 2,5,5,4]);vals=list(vals)
 if lstat=='SOLO INVESTIGACIÓN / RESTRICCIONES':vals[4]=3
 if r['archived']:vals[5]=1
 if lic is None:vals[4]=1
 blockers=[]
 if s in ['timesfm','uni2ts','finbert']:blockers.append('Revisar licencia de pesos antes de uso operativo o redistribución; el código por sí solo no autoriza los pesos.')
 if s in ['alibi-detect','tirex']:blockers.append('Licencia restringida; estudiar versión y uso antes de adoptar.')
 if not lic:blockers.append('Licencia no localizada en rutas estándar; no adaptar código sin aclaración.')
 if s=='fingpt':blockers.append('No validar inversión con ruta Forecaster sin corregir reconstrucción temporal y evaluar prospectivamente.')
 if s=='ai-hedge-fund':blockers.append('Excluir ejecución/pagos/credenciales de wallet; solo referencia educativa en este mandato.')
 c=dict(id=cid,name=n,url=url,organization=org,categories=cat,resource_type='biblioteca/framework' if s not in ['finqa','tatqa','convfinqa','financebench','gift-eval','finllm-eval'] else 'benchmark/repositorio de investigación',description=use,verification_level='V3' if s in DEEP else ('V2' if lic else 'V1'),verified_at=DATE,version_or_commit=r['commit'],maintenance_status='archivado observado' if r['archived'] else 'no archivado observado; cadencia no cuantificada',license_code=lic,license_status=lstat,license_url=r['files'].get('license',{}).get('url'),dependencies=['ver revisión técnica'] if s in DEEP else ['no auditadas'],data_inputs=io.split(' -> ')[0],outputs=io.split(' -> ')[-1],practical_use=use,limitations=[lim,'Snapshot de rama observado el 4; fecha exacta del commit no reconstruida.'],alternatives=[alt],evidence_ids=eids,source_ids=sids,scores=dict(zip(KEYS,vals)),confidence='media-alta sobre rutas observadas; no sobre eficacia financiera' if s in DEEP else 'media documental',blockers=blockers,commercial_dependencies=['API/modelo opcional según configuración; no contratados'] if s in ['fingpt','finrobot','tradingagents','ai-hedge-fund','haystack','llamaindex','pydantic-ai','dspy','ragas','promptfoo'] else [],maturity='revisión estática; ejecución no verificada',cost_relative='bajo' if s in ['river','statsforecast','mlforecast','trafilatura','tsfel'] else 'medio; depende del modelo y datos',adoption_mode='Adoptar biblioteca' if s in ['fev','mlforecast','river','docling','statsforecast','trafilatura'] else ('Conservar como referencia' if r['archived'] else 'Investigar más'),deep_review_path='03_DEEP_TECHNICAL_REVIEWS/ai_'+s+'.md' if s in DEEP else None,languages=['Python; otras rutas no auditadas'],last_significant_release='no comprobado; commit fijado',tests_reviewed=[x['path']for x in cs if 'test' in x['path']],tests_executed=False,score_rationale='Utilidad para investigación personal y evidencia estática; mantenimiento limitado a observación, sin estrellas como indicador. Penalización explícita por licencia o archivo; riesgo bloqueante prevalece sobre puntuación.')
 candidates.append(c)
for r in hf:
 slug=re.sub('[^a-z0-9]+','-',r['rid'].lower());cid='AI-'+r['kind']+'-'+slug
 rid=r['rid'];lic=r['license_declared'];lic=';'.join(lic) if isinstance(lic,list) else lic
 lstat='REUTILIZACIÓN POTENCIALMENTE COMPATIBLE' if lic in ['apache-2.0','mit'] else ('SOLO INVESTIGACIÓN / RESTRICCIONES' if lic and 'nc' in lic else 'LICENCIA NO VERIFICADA')
 if rid=='google/timesfm-3.0-pytorch':lic='TimesFM Non-Commercial License v1.0';lstat='SOLO INVESTIGACIÓN / RESTRICCIONES'
 if rid=='NX-AI/TiRex':lic='NXAI Community License';lstat='SOLO INVESTIGACIÓN / RESTRICCIONES'
 ismodel=r['kind']=='model';sids=[];eids=[]
 for fname,f in r['files'].items():
  if f.get('status')!=200:continue
  sid=src('S-'+cid+'-'+fname.replace('.','-'),f['url'],rid+' '+fname,'model card / licencia / config' if ismodel else 'dataset card',r['commit'],200,'Sin descargar pesos ni filas del dataset.',f.get('sha256'));sids.append(sid)
  eids.append(ev(cid,sid,'Fuente declara licencia '+str(lic)+'; las condiciones de datos y servicios asociados son independientes.','model/dataset card' if fname=='README.md' else 'configuración/licencia','Declaración del titular examinada; no auditoría jurídica ni prueba de inferencia.'))
 descriptions={
 'amazon/chronos-2':'Modelo120M para forecasting multivariable con covariables y cuantiles.',
 'amazon/chronos-bolt-small':'Baseline compacto de forecasting univariado por patches.',
 'google/timesfm-3.0-pytorch':'Pesos multivariables TimesFM3, licencia no comercial/no producción.',
 'google/timesfm-2.5-200m-pytorch':'Checkpoint200M anterior con declaración Apache2.0.',
 'Salesforce/moirai-2.0-R-small':'Modelo11.4M, cuantiles, máscaras de observación; CC-BY-NC.',
 'Salesforce/moirai-1.1-R-small':'Checkpoint Moirai anterior útil como comparación; CC-BY-NC.',
 'ProsusAI/finbert':'Pesos de sentimiento financiero inglés; CC-BY-NC-SA4.0.',
 'BAAI/bge-m3':'Recuperación multilingüe densa, sparse y multivector.',
 'BAAI/bge-small-en-v1.5':'Embeddings compactos para documentos en inglés.',
 'ibm-granite/granite-timeseries-ttm-r2':'Familia compacta TinyTimeMixer; variante por frecuencia/horizonte.',
 'NX-AI/TiRex':'Pesos35M xLSTM con licencia comunitaria.',
 'PatronusAI/financebench':'Muestra pública150 casos QA con evidencia; CC-BY-NC4.0.',
 'takala/financial_phrasebank':'Frases financieras inglesas con etiquetas de sentimiento y acuerdo.',
 'ibm/finqa':'Distribución HF de preguntas aritméticas financieras; declarar origen/versiones.',
 'Salesforce/GiftEval':'Benchmark heterogéneo de forecasting; validar permisos por componente.',
 'Salesforce/GiftEvalPretrain':'Colección de preentrenamiento de gran tamaño; no descargar para este fin.',
 'autogluon/chronos_datasets':'Colección multi-origen con licencias por configuración.',
 'autogluon/fev_datasets':'Colección para tareas de forecasting con condiciones por subdataset.'}
 vals=[18,10,9,7,8 if lstat.startswith('REUTIL')else 3,5,5,5]
 candidates.append(dict(id=cid,name=rid,url=r['url'],organization=rid.split('/')[0],categories=['H','G'] if 'finbert' not in rid and 'bge' not in rid else ['H','I','J'],resource_type=r['kind'],description=descriptions[rid],verification_level='V2' if ismodel and r['files'].get('config.json',{}).get('status')==200 else 'V1',verified_at=DATE,version_or_commit=r['commit'],maintenance_status='lastModified '+str(r.get('lastModified'))+'; cadencia no auditada',license_code=None,license_weights=lic if ismodel else None,license_data=lic if not ismodel else 'fuentes de preentrenamiento no licenciadas por la licencia de pesos',license_status=lstat,license_url=r['files']['LICENSE']['url'] if r['files'].get('LICENSE',{}).get('status')==200 else r['files']['README.md']['url'],dependencies=['runtime y tokenizer deben fijarse por versión'],data_inputs='series temporales' if 'bge' not in rid and 'finbert' not in rid and ismodel else ('texto' if ismodel else 'consulta/evaluación'),outputs='pronósticos/cuantiles' if 'bge' not in rid and 'finbert' not in rid and ismodel else ('embeddings' if 'bge' in rid else ('sentimiento' if ismodel else 'casos/series de benchmark')),practical_use=descriptions[rid],limitations=['No inferencia ni descarga de pesos/datasets. La licencia indicada procede de card o archivo citado; no transfiere derechos de todas las fuentes subyacentes.','Benchmark general o de acciones no valida rentabilidad crypto ni horizonte3-18meses.'],alternatives=['Baselines simples y test prospectivo propio'],evidence_ids=eids,source_ids=sids,scores=dict(zip(KEYS,vals)),confidence='media documental',blockers=['Permisos por aclarar antes de uso operativo o redistribución.'] if lstat!='REUTILIZACIÓN POTENCIALMENTE COMPATIBLE' else [],commercial_dependencies=[],maturity='checkpoint/dataset accesible; rendimiento no reproducido',cost_relative='sin medición local; ver matriz de hardware',adoption_mode='Investigar más',deep_review_path=None,tests_executed=False))
for a,b,relation in [('AI-chronos','AI-model-amazon-chronos-2','runtime para pesos'),('AI-chronos','AI-fev','integración implementada predict_fev'),('AI-timesfm','AI-model-google-timesfm-3-0-pytorch','runtime para pesos; licencias distintas'),('AI-uni2ts','AI-model-salesforce-moirai-2-0-r-small','runtime para pesos; licencias distintas'),('AI-uni2ts','AI-gluonts','dependencia observada en forecast.py'),('AI-mlforecast','AI-lightgbm','combinación propuesta; estimador compatible'),('AI-tradingagents','AI-langgraph','dependencia observada en tests y orquestación'),('AI-finbert','AI-model-prosusai-finbert','código separado de checkpoint'),('AI-model-prosusai-finbert','AI-dataset-takala-financial-phrasebank','datos de fine-tuning declarados'),('AI-docling','AI-model-baai-bge-m3','combinación propuesta para extracción y búsqueda'),('AI-river','AI-mlforecast','combinación propuesta: monitorizar error predictivo'),('AI-fingpt','AI-tradingagents','comparación de controles de conocimiento temporal'),('AI-tirex','AI-tirex2','generación sucesora; revisar licencia por versión'),('AI-gift-eval','AI-dataset-salesforce-gifteval','benchmark y colección asociada'),('AI-fev','AI-dataset-autogluon-fev-datasets','tareas sobre datasets asociados')]:
 ca=next(c for c in candidates if c['id']==a);relations.append(dict(from_id=a,to_id=b,relation=relation,evidence_source_id=ca['source_ids'][1] if len(ca['source_ids'])>1 else ca['source_ids'][0]))
for name,data in [('candidates',candidates),('sources',sources),('evidence',evidence),('relations',relations),('models',[c for c in candidates if c['resource_type']=='model']),('datasets',[c for c in candidates if c['resource_type']=='dataset'])]:
 (BASE/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'candidates':len(candidates),'sources':len(sources),'evidence':len(evidence),'deep':len(DEEP),'levels':{k:sum(c['verification_level']==k for c in candidates)for k in ['V1','V2','V3']}}))
