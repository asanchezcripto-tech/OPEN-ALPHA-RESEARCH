import json
from inspect_public import ROOT,fetch
W=ROOT/'workstreams/infra'
def read(name):return json.loads((W/(name+'.json')).read_text(encoding='utf-8'))
def save(name,data):(W/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
projects=read('candidates');sources=read('sources');ev=read('evidence')
providers=[
('defillama-api','DefiLlama: servicio y metodología','https://docs.llama.fi/',['E','D','M'],'Agregados DeFi; permisos y acceso del servicio se revisan aparte de adaptadores.'),
('hyperliquid-api','Hyperliquid: API pública','https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api',['B','C','M'],'Contexto/info de mercados; diferenciar snapshot actual, histórico y retención.'),
('polymarket-api','Polymarket: API de datos','https://docs.polymarket.com/api-reference/predictions/overview',['N','J','M'],'Datos de eventos, mercados, precios e historial; no se invocaron operaciones.'),
('dune-service','Dune Analytics API','https://docs.dune.com/api-reference/overview/introduction',['D','M','L'],'Servicio de consultas/resultados: referencia funcional cerrada; clientes/Spellbook tienen permisos diferentes.'),
('tokenterminal-service','Token Terminal: métricas','https://tokenterminal.com/explorer/metrics/tokenholder_revenue',['E','L'],'Referencia comercial de definiciones; no implica datos/código abiertos ni validación independiente.')]
for key,name,url,categories,desc in providers:
 cid='infra-provider-'+key;sid='infra-provider-source-'+key;eid='infra-provider-evidence-'+key
 m,body=fetch(url)
 if cid in {r['id'] for r in projects}:continue
 sources.append(dict(id=sid,url=url,title=name,accessed_at='2026-11-04',source_type='official_provider_documentation',status=m['status'],sha256=m.get('sha256'),version_or_commit=None,notes='Consulta de documentación pública; no se probó cobertura de API ni permisos completos.'))
 ev.append(dict(id=eid,candidate_id=cid,source_id=sid,claim=desc,evidence_type='documentación primaria',limitations='Servicio no ejecutado/contratado; no licencia de datos inferida de documentación pública.'))
 projects.append(dict(id=cid,name=name,url=url,organization=name.split(':')[0],categories=categories,resource_type='proveedor/API o servicio comercial de referencia',description=desc,verification_level='V1' if m['status']==200 else 'D0',verified_at='2026-11-04',version_or_commit=None,maintenance_status='documentación consultada; SLA/actividad no auditados',license_code=None,license_data='Términos del servicio/dataset pendientes de caso concreto',license_status='LICENCIA NO VERIFICADA',license_url=None,source_ids=[sid],evidence_ids=[eid],scores=None,confidence='media en alcance documental; baja en acceso operativo',blockers=['Verificar condiciones, retención, límites y coste antes de usar datos.'],commercial_dependencies=['Servicio externo; no contratado.'],maturity='No probada mediante llamadas operativas',cost_relative='No cotizado',adoption_mode='Conservar como referencia',practical_use=desc,data_inputs='Consultas y parámetros permitidos',outputs='Datos/documentación según servicio; disponibilidad no ensayada',limitations=['La documentación puede cambiar; no constituye garantía de acceso gratuito ni de reutilización.'],alternatives=['Consulta manual o captura propia permitida con alcance menor'],dependencies=[],deep_review_path=None))
save('candidates',projects);save('sources',sources);save('evidence',ev)
providers_out=[r for r in projects if r['id'].startswith('infra-provider-')]
save('providers',providers_out)
pid={r['id']:r for r in projects}
compdata=[
('storage','Almacén local frente a servidor',['duckdb','sqlite','polars','clickhouse','questdb','timescaledb'],'DuckDB/Parquet para análisis local; SQLite para tesis/metadatos; servidor solo ante escala medida.','Ficheros simples requieren disciplina de versiones; servidor añade operación.'),
('quality','Validación estructural',['pandera','patito','pydantic','great-expectations','soda-core'],'Pandera para varios backends, Patito para Polars; Pydantic para objetos.','No duplicar validadores; ninguna biblioteca conoce por sí sola la semántica económica. Soda actual tiene restricciones.'),
('ui','Interfaz de investigación',['marimo','streamlit','datasette','panel','perspective'],'marimo para explorar supuestos; Streamlit/Panel para panel; Datasette para tablas; Perspective para pivotes.','Exportar solo lo necesario; reactividad no garantiza frescura; hosting separado.'),
('ingest','Ingesta y caché',['dlt','requests-cache','hishel','httpx','ingestr'],'HTTPX/requests y snapshots para pocos endpoints; dlt al crecer conectores.','Caché no es archivo; cursor puede perder revisiones; ingestr FSL.'),
('temporal','Conocimiento temporal',['qfs','xtdb','sirix','alpha-lake','point-in-time-datawarehouse'],'Extraer invariantes y usar tabla append-only antes de operar otro sistema.','QFS y warehouse sin licencia verificada; no copiar. XTDB/otros añaden coste de operación.'),
('diff','Reconciliación de fuentes',['datacompy','data-diff','sqlglot'],'DataComPy o SQL pequeño para cambios entre snapshots.','data-diff archivado; linaje SQL no implica procedencia económica por fila.')]
comparisons=[]
for key,title,ids,pref,trade in compdata:
 ids=['infra-'+i for i in ids]
 comparisons.append(dict(id='cmp-infra-'+key,name=title,candidate_ids=ids,preferred=pref,tradeoff=trade,confidence='media; revisión estática',verified_at='2026-11-04',source_ids=list(dict.fromkeys(s for i in ids for s in pid[i]['source_ids']))))
save('comparisons',comparisons)
relations=[]
for a,b,why in [('patito','polars','dependencia declarada'),('patito','pydantic','dependencia declarada'),('dlt','duckdb','destino opcional; manifiesto restringe <2'),('marimo','duckdb','extra SQL declarado'),('qfs','duckdb','import observado'),('qfs','polars','import observado'),('datacompy','polars','backend observado'),('requests-cache','httpx','comparación de alternativas, NO dependencia')]:
 rr=pid['infra-'+a];sid=next((s for s in rr['source_ids'] if any(x['id']==s and 'pyproject.toml' in x['url'] for x in sources)),rr['source_ids'][0])
 relations.append(dict(from_id='infra-'+a,to_id='infra-'+b,relation=why,evidence_source_id=sid))
save('relations',relations)
methods=[]
for key,name,problem,assumptions,validation,failures,impl,value,avoid in [
('bitemporal-join','Selección bitemporal por ventanas','Elegir datos conocidos sin usar revisiones posteriores.','Identidad y tiempos de evento/conocimiento distintos.','Invariancia de consultas pasadas al añadir futuro.','ASOF por fecha económica; empates no resueltos; eventos futuros conocidos excluidos.',['infra-duckdb','infra-qfs'],'Hace auditables fundamentales y macro.','No inventar fecha de publicación; si falta, marcar reconstrucción.'),
('reconciliation','Reconciliación y tolerancias por unidad','Distinguir cambios de proveedor de cambios económicos.','Misma definición, unidad, cobertura y claves.','Cambios sintéticos materiales/no materiales y revisión humana.','Tolerancia global oculta cambios; referencia numérica asimétrica.',['infra-datacompy','infra-pandera'],'Detecta artefactos de revenue/supply antes de rankear.','No comparar métricas con beneficiarios o periodos distintos.'),
('freshness','Presupuesto de frescura y retraso','Evitar que fallos se interpreten como calma de mercado.','Timestamp original/acquisición y política por métrica.','Cortes simulados, datos caducados y estado de abstención.','HTTP200 desde caché tratado como dato nuevo.',['infra-requests-cache','infra-dlt'],'Reduce alertas financieras basadas en feed congelado.','No afirmar latencia exacta sin hora pública verificable.'),
('dependency-graph','Grafo de dependencias de cálculos','Recalcular solo lo afectado al cambiar supuestos.','Dependencias explícitas y entradas versionadas.','Modificar un supuesto y cotejar descendientes/resultados.','Estado externo, llamada repetida o datos cambiantes fuera del grafo.',['infra-marimo'],'Exploración reproducible de tesis y escenarios.','No usar como sustituto de provenance de datos.')]:
 methods.append(dict(id='method-infra-'+key,name=name,url=pid[impl[0]]['url'],categories=['M','G'],verified_at='2026-11-04',maintenance_status='método; implementaciones versionadas',confidence='alta sobre principio; utilidad propuesta no medida',problem=problem,assumptions=assumptions,data_frequency='Según métrica; diario/semanal en el alcance inicial.',validation=validation,common_failures=failures,implementations=impl,simple_implementation='Consultar diseño y revisión del componente; no se implementó aquí.',crypto_value=value,do_not_use_when=avoid,source_ids=pid[impl[0]]['source_ids']))
save('methods',methods)
print('Infrastructure extras saved',len(providers_out),len(comparisons),len(methods))
