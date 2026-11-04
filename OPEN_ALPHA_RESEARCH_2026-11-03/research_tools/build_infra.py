"""Consolidate the coordinator's reviewed research notes, not financial software."""
import json, pathlib, re
from inspect_public import ROOT, fetch
W=ROOT/'workstreams/infra'
rows=json.loads((W/'inspection.json').read_text(encoding='utf-8'))
deep=json.loads((W/'deep_files.json').read_text(encoding='utf-8'))
notes=json.loads((W/'review_notes.json').read_text(encoding='utf-8'))
sources=[];evidence=[];candidates=[];url_ids={}
def source(meta,title,kind,sha=None):
    url=meta['url']
    if url in url_ids:return url_ids[url]
    sid=f'infra-S{len(sources)+1:04}'
    sources.append(dict(id=sid,url=url,title=title,accessed_at='2026-11-04',source_type=kind,status=meta.get('status'),version_or_commit=sha,sha256=meta.get('sha256'),notes='Consulta estática; contenido observado el 4, sin reconstruir su disponibilidad al cierre del 3.'))
    url_ids[url]=sid;return sid
def ev(cid,sid,claim,kind,limits):
    eid=f'infra-E{len(evidence)+1:04}'
    evidence.append(dict(id=eid,candidate_id=cid,source_id=sid,claim=claim,evidence_type=kind,limitations=limits))
    return eid
license_overrides={'ingestr':'FSL-1.1-ALv2','timescaledb':'Apache-2.0 + Timescale License por directorio','sqlite':'Dominio público en componentes identificados; revisar terceros','soda-core':'Elastic-2.0','lakefs':'BUSL-1.1; Additional Use Grant limitado','diskcache':'Apache-2.0','voila':'BSD (texto consultado; variante no resuelta)','networkx':'BSD-3-Clause','ptdata-methodology':'CC-BY-4.0 para documentación','row-level-prov':'PolyForm-Noncommercial-1.0.0'}
restricted={'ingestr','timescaledb','soda-core','lakefs','row-level-prov'}
core={'duckdb','polars','pandera','pydantic','requests-cache','httpx','marimo','datacompy','plotly','altair','sqlite','frictionless'}
heavy={'meltano','clickhouse','timescaledb','lakefs','datahub','dagster','prefect','openlineage','xtdb','sirix','alpha-lake','point-in-time-datawarehouse'}
for r in rows:
    key=r['id'].removeprefix('infra-');n=notes.get(key);sha=r.get('current_oid')
    sid=source(r['fetch'],r['name']+' — repositorio','repository',sha)
    sids=[sid];eids=[ev(r['id'],sid,r['description'],'documentation','Función declarada; no prueba de rendimiento ni de ejecución.')]
    licfiles=[f for f in r.get('inspected_files',[]) if 'licen' in f['path'].lower() or f['path'].lower().startswith('copying')]
    lic=license_overrides.get(key,r.get('license_label')) if licfiles else None
    if lic=='NOASSERTION':lic=None
    for f in r.get('inspected_files',[]):
        fs=source(f,r['name']+'/'+f['path'],'license' if f in licfiles else 'documentation',sha);sids.append(fs)
        if f in licfiles and lic:eids.append(ev(r['id'],fs,'Licencia/capa observada: '+lic,'license','No incluye automáticamente dependencias, datos, pesos ni servicios.'))
    paths=[]
    for f in [x for x in deep if x['candidate_id']==r['id']]:
        fs=source(f,r['name']+'/'+f['path'],'test' if f['path'].startswith('test') else 'code_or_manifest',sha);sids.append(fs)
        if f['status']==200:paths.append((f,fs))
    status=('LICENCIA NO VERIFICADA' if not lic else 'SOLO INVESTIGACIÓN / RESTRICCIONES' if key in restricted else 'COMPATIBLE CON OBLIGACIONES' if (lic.startswith(('GPL','MPL','CC-BY')) or key=='lightweight-charts') else 'REUTILIZACIÓN POTENCIALMENTE COMPATIBLE')
    blockers=[]
    if not lic:blockers.append('No copiar/adaptar código hasta verificar licencia aplicable.')
    if key=='data-diff':blockers.append('Repositorio archivado; no adoptar como dependencia nueva sin sucesor evaluado.')
    if key=='ydata-profiling':blockers.append('README indica migración a fg-data-profiling; sucesor fuera de revisión técnica.')
    if key in restricted:blockers.append('Revisión de términos para el uso concreto; no clasificar como open source permisivo.')
    values=n['scores'] if n else ([18,7,12,8,8 if lic else 0,4,6,3] if key not in heavy else [12,7,10,4,8 if lic else 0,4,4,4])
    if key in core and not n:values=[21,8,13,10,9 if lic else 0,4,7,4]
    if key in restricted:values[4]=3
    scores=dict(zip(['utility','evidence','data','ease','license','maintenance','usability','differentiation'],values))
    level='V3' if n else ('V2' if lic else 'V1')
    kind='biblioteca'
    if key in {'qfs','point-in-time-datawarehouse','alpha-lake','row-level-prov'}:kind='prototipo'
    if key=='ptdata-methodology':kind='especificación de servicio; documentación abierta'
    if key=='sqlite':kind='mirror oficial; motor'
    if key in {'marimo','datasette','visidata','evidence','observable-framework'}:kind='herramienta funcional'
    candidate=dict(id=r['id'],name=r['name'],url=r['url'],organization=r['organization'],categories=r['categories'],resource_type=kind,description=r['description'],verification_level=level,verified_at='2026-11-04',version_or_commit=sha,maintenance_status='archivado' if r.get('archived_notice') else 'accesible y sin aviso de archivo; cadencia no medida',last_significant_release=None,languages=None,license_code=lic,license_status=status,license_url=licfiles[0]['url'] if licfiles else None,dependencies=n['dependencies'] if n else 'No auditadas; consultar manifiesto antes de adoptar.',data_inputs='Tablas, documentos o series aportados por el usuario; no suministra por sí mismo históricos financieros.',outputs=r['description'],implemented_features=n['architecture'] if n else 'Existencia y alcance documental revisados; implementación no auditada.',announced_only='No se contrastó cada promesa de rendimiento o funcionalidad comercial.',practical_use=n['value'] if n else r['description'],limitations=n['limits'] if n else 'Revisión de selección: faltan ensayo aislado, incidencias, compatibilidad de versiones e históricos representativos.',alternatives=n['alternative'] if n else 'Consultar comparativas por familia antes de añadir una dependencia.',evidence_ids=eids,source_ids=sids,scores=scores,score_total=sum(values),confidence='media-alta en la ruta estática; baja en operación' if n else 'media en existencia/licencia; baja en idoneidad operativa',blockers=blockers,commercial_dependencies='No verificadas; el núcleo y servicios alojados deben tratarse por separado.',maturity='prototipo' if kind=='prototipo' else 'no medida mediante ejecución',cost_relative='alto coste operativo relativo' if key in heavy else 'bajo/medio; estimación de alcance local',adoption_mode='Extraer una técnica' if key=='qfs' else 'Conservar como referencia' if key in heavy or key=='data-diff' else 'Adoptar biblioteca' if key in core else 'Investigar más',hardware=n['hardware'] if n else 'No medido; proporcional al volumen y backend.',test_status=n['tests'] if n else 'No se inspeccionó batería ni se midió cobertura.',security='No ejecutado. Revisar dependencias, extensiones, serializadores y acceso de red antes de instalar.',api_credentials='La biblioteca no implica permiso ni credenciales para datos de terceros.',deep_review_path=f'03_DEEP_TECHNICAL_REVIEWS/infra_{key}.md' if n else None)
    if n:
        for f,fs in paths:
            if f['path'].endswith('.toml'):claim=n['dependencies']
            elif f['path'].startswith('test'):claim=n['tests']
            else:claim=n['architecture']
            eids.append(ev(r['id'],fs,claim,'static_inspection','Lectura de rutas relevantes; sin ejecución ni auditoría completa.'))
        text=f"# {n['title']}\n\nRecurso: [{r['name']}]({r['url']}). Commit observado: `{sha}`. Verificación: 2026-11-04; nivel V3, análisis estático.\n\n**Decisión:** {n['decision']} Puntuación editorial: **{sum(values)}/100**; riesgo bloqueante: {'; '.join(blockers) or 'ninguno identificado en esta ruta; no equivale a certificación'}.\n\n## Arquitectura e implementación observada\n\n{n['architecture']}\n\n## Qué aprovechar\n\n{n['value']}\n\n## Qué no asumir\n\n{n['limits']}\n\n## Dependencias, pruebas y requisitos\n\n{n['dependencies']}\n\n{n['tests']}\n\n{n['hardware']}\n\n## Licencia y acceso\n\n{lic or 'LICENCIA NO VERIFICADA'}. Clasificación: **{status}**. El permiso del código no se extiende a los datos ni a servicios alojados. No se investigó exhaustivamente cada dependencia o incidencia de seguridad.\n\n## Alternativa y experimento mínimo propuesto\n\n{n['alternative']}\n\n{n['experiment']} Este experimento es un diseño, no una prueba realizada.\n\n## Evidencias trazables\n\n"
        for f in r.get('inspected_files',[]):text+=f"- [{f['path']}]({f['url']}) — HTTP {f['status']}; SHA-256 `{f.get('sha256')}`.\n"
        for f,fs in paths:text+=f"- [{f['path']}]({f['url']}) — fuente `{fs}`; inspección parcial de rutas descritas.\n"
        text+='\nPuntuación por criterio (máximos 25/15/15/12/10/8/8/7): '+', '.join(f'{k}={v}' for k,v in scores.items())+'. La disponibilidad y utilidad reciben peso alto; mantenimiento no obtiene puntuación máxima porque no se auditó su sostenibilidad.\n'
        (ROOT/candidate['deep_review_path']).write_text(text,encoding='utf-8')
    candidates.append(candidate)
for name,data in [('candidates',candidates),('sources',sources),('evidence',evidence)]:
    (W/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'candidates':len(candidates),'sources':len(sources),'evidence':len(evidence),'deep_reviews':len(notes)}))
