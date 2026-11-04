"""Generate the evidence-ledger and readable catalogue from reviewed notes."""
import collections,csv,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[1];I=ROOT/'inventories'
def read(p):return json.loads(p.read_text(encoding='utf-8')) if p.exists() else []
def write(name,rows):
    (I/(name+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    fields=list(dict.fromkeys(k for r in rows for k in r))
    with (I/(name+'.csv')).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()})
def all_area(name):
    result=[]
    for a in ['infra','quant','crypto','ai']:result+=read(ROOT/'workstreams'/a/(name+'.json'))
    return result
aliases={};projects=[];byurl={}
source_lookup={s['id']:s for s in all_area('sources')}
for r in all_area('candidates'):
    url=r['url'].lower().rstrip('/')
    if 'github.com/' in url and url in byurl:
        prior=byurl[url];aliases[r['id']]=prior['id']
        for k in ['categories','source_ids','evidence_ids']:
            prior[k]=list(dict.fromkeys(prior.get(k,[])+r.get(k,[])))
        prior.setdefault('duplicate_evaluations',[]).append(r['id'])
        continue
    projects.append(r);byurl[url]=r
for p in all_area('papers'):
    if p['id'] not in {x['id'] for x in projects}:
        r=dict(p);r.setdefault('name',r.get('title'));r.setdefault('resource_type','paper / línea de investigación');r.setdefault('description',r.get('contribution'));r.setdefault('evidence_ids',[]);r.setdefault('adoption_mode','Investigar más');r.setdefault('blockers',['Solo abstract/metadatos; no auditoría del trabajo completo.']);r.setdefault('scores',None)
        r.setdefault('url',next((source_lookup[s]['url'] for s in r.get('source_ids',[]) if s in source_lookup),None))
        r.setdefault('verification_level','V1');r.setdefault('verified_at','2026-11-04');r.setdefault('maintenance_status','Publicación/pista de investigación; sin seguimiento editorial completo.');r.setdefault('confidence','media sobre existencia; baja sobre resultados no reproducidos.');r.setdefault('license_status','LICENCIA NO VERIFICADA');r.setdefault('categories',['D','G']);r.setdefault('version_or_commit',r.get('publication'))
        projects.append(r)
for r in projects:
    if r.get('verification_level')=='D0':
        r['scores']=None;r['checked_at']=r.get('verified_at');r['verified_at']=None
    if r.get('resource_type','').lower().startswith('dataset') and str(r.get('license_code','')).startswith('CC-'):
        r['license_data']=r['license_code'];r['license_code']=None
    r['score_total']=sum(r['scores'].values()) if isinstance(r.get('scores'),dict) else None
    r.setdefault('license_weights',None);r.setdefault('license_data',None)
    r.setdefault('languages',None);r.setdefault('last_significant_release',None)
    r.setdefault('hardware','No medido; ver revisión/familia antes de elegir equipo.')
    r.setdefault('tests_executed',False)
    r.setdefault('coverage_measured',None)
    # An unexamined field is explicitly unknown, never an implicit positive result.
    for field in ['open_issues_reviewed','tests_located','tests_inspected','documentation_quality',
                  'history_availability','implementation_complexity','immediate_use']:
        r.setdefault(field,None)
    r.setdefault('evaluation_scope','Ver nivel y fuentes: los campos nulos no se comprobaron o no aplican; no implican ausencia de riesgo.')
sources=all_area('sources');evidences=all_area('evidence')
for e in evidences:
    if e.get('candidate_id') in aliases:e['candidate_id']=aliases[e['candidate_id']]
relations=all_area('relations')
for n,r in enumerate(relations,1):
    r.setdefault('id',f'relation-{n:04}');r.setdefault('verified_at','2026-11-04')
    for k in ['from_id','to_id']:
        if r.get(k) in aliases:r[k]=aliases[r[k]]
papers=all_area('papers');models=all_area('models');datasets=all_area('datasets');providers=all_area('providers')
for r in projects:
    kind=r.get('resource_type','').lower()
    dataset_linked_ids={x.get('candidate_id',x['id']) for x in datasets}
    if (kind.startswith('dataset') or kind in ['modelo/dataset','proveedor/dataset']) and r['id'] not in dataset_linked_ids:datasets.append(r)
    if any(s in kind for s in ['proveedor','api','servicio']) and r['id'] not in {x['id'] for x in providers}:providers.append(r)
    if kind in ['model','modelo'] and r['id'] not in {x['id'] for x in models}:models.append(r)
libraries=[r for r in projects if any(s in r.get('resource_type','').lower() for s in ['biblioteca','framework','sdk','cliente'])]
licenses=[{k:r.get(k) for k in ['id','name','url','version_or_commit','verified_at','license_code','license_weights','license_data','license_status','license_url','blockers','commercial_dependencies','confidence']} for r in projects]
methods=all_area('methods')+all_area('algorithms');comparisons=all_area('comparisons');searches=all_area('search_log')
project_lookup={r['id']:r for r in projects}
for collection in [datasets,providers,papers,methods,comparisons,models]:
    for row in collection:
        row.setdefault('verified_at','2026-11-04');row.setdefault('maintenance_status','No evaluado longitudinalmente; ver fuente/versión.');row.setdefault('confidence','media documental; no resultados propios ejecutados.')
        row.setdefault('categories',project_lookup.get(row.get('candidate_id'),{}).get('categories',[]))
        if not row.get('source_ids') and row.get('supporting_ids'):
            row['source_ids']=list(dict.fromkeys(s for cid in row['supporting_ids'] for s in project_lookup.get(cid,{}).get('source_ids',[])))
        row.setdefault('url',next((source_lookup[s]['url'] for s in row.get('source_ids',[]) if s in source_lookup),None))
for m in methods:
    m.setdefault('problem',m.get('hypothesis'));m.setdefault('assumptions','Definiciones, identidades y fechas verificables; no se validó empíricamente el método propuesto.')
    m.setdefault('data_frequency',m.get('inputs','Según tarea, con disponibilidad temporal explícita.'))
    m.setdefault('common_failures',m.get('failure_modes',m.get('failure')))
    m.setdefault('implementations',m.get('supporting_ids',[]));m.setdefault('simple_implementation',m.get('simple_reuse','Ledger o tabla pequeña; ver diseño y componentes enlazados.'))
    m.setdefault('crypto_value',m.get('hypothesis'));m.setdefault('do_not_use_when','Sin cobertura, definiciones o supuestos verificables; registrar abstención.')
provider_aliases={'crypto-provider-dune':'infra-provider-dune-service','crypto-provider-token-terminal':'infra-provider-tokenterminal-service'}
for old,new in provider_aliases.items():
    oldrow=next((r for r in providers if r['id']==old),None);newrow=next((r for r in providers if r['id']==new),None)
    if oldrow and newrow:
        newrow['source_ids']=list(dict.fromkeys(newrow.get('source_ids',[])+oldrow.get('source_ids',[])))
        newrow['additional_notes']={k:v for k,v in oldrow.items() if k not in ['id','source_ids']}
providers=[r for r in providers if r['id'] not in provider_aliases]
for c in comparisons:
    c['candidate_ids']=[aliases.get(x,x) for x in (c.get('candidate_ids') or c.get('candidates',[]))]
    c.setdefault('name',c.get('topic',c['id'].removeprefix('crypto-compare-')))
    c['provider_ids']=[provider_aliases.get(x,x) for x in c.get('provider_ids',[])]
    if not c.get('source_ids'):
        c['source_ids']=list(dict.fromkeys(s for r in projects if r['id'] in c['candidate_ids'] for s in r.get('source_ids',[])))
    if not c.get('url'):c['url']=next((source_lookup[s]['url'] for s in c.get('source_ids',[]) if s in source_lookup),None)
opportunities=read(I/'opportunities.json')
for o in opportunities:
    o['scores']=dict(zip(['utility','evidence','data','ease','license','maintenance','usability','differentiation'],o.pop('score_values',list(o.get('scores',{}).values()))))
    o['score_total']=sum(o['scores'].values())
    o['url']=o.get('blueprint_path') or '../11_PRODUCT_OPPORTUNITIES.md#'+o['id'].lower()
    o['maintenance_status']='diseño, sin implementación'
    o['source_refs']=['../06_DATA_AND_INFRASTRUCTURE.md','../08_TECHNOLOGY_COMPARISONS.md','../10_NOVEL_COMBINATIONS.md']
    if o.get('blueprint_path'):o['url']='../'+o['blueprint_path']
for collection in [comparisons,methods]:
    for row in collection:
        if not row.get('categories'):
            linked=row.get('candidate_ids',[])+row.get('supporting_ids',[])
            linked += [x for x in row.get('implementations',[]) if isinstance(x,str)]
            row['categories']=list(dict.fromkeys(c for rid in linked for c in project_lookup.get(rid,{}).get('categories',[])))
source_categories={}
for p in projects:
    for sid in p.get('source_ids',[]):
        source_categories.setdefault(sid,set()).update(p.get('categories',[]))
for s in sources:
    s.setdefault('categories',sorted(source_categories.get(s['id'],set())))
    s.setdefault('maintenance_status','No aplica al registro de consulta; ver recurso vinculado.')
    s.setdefault('confidence','Registro de adquisición; su status/hash no demuestra la afirmación técnica.')
for e in evidences:
    p=project_lookup.get(e.get('candidate_id'),{});s=source_lookup.get(e.get('source_id'),{})
    e.setdefault('url',s.get('url'));e.setdefault('categories',p.get('categories',[]))
    e.setdefault('verified_at',s.get('accessed_at',s.get('verified_at','2026-11-04')))
    e.setdefault('maintenance_status','Afirmación vinculada a una versión/fuente; no auditoría longitudinal.')
    e.setdefault('confidence',p.get('confidence','Limitada al tipo de evidencia y sus restricciones.'))
for name,rows in [('projects',projects),('libraries',libraries),('models',models),('datasets',datasets),('papers',papers),('algorithms',methods),('licenses',licenses),('providers',providers),('opportunities',opportunities),('comparisons',comparisons),('sources',sources),('evidence',evidences),('relations',relations),('search_log',searches)]:write(name,rows)
write('deduplication',[dict(alias_id=k,canonical_id=v,reason='Mismo repositorio canónico; se conservan fuentes y evaluaciones de ambas áreas.') for k,v in aliases.items()])
cats=dict(zip('ABCDEFGHIJKLMN',['Macro','Mercado cripto','Derivados','On-chain','Fundamentales y valoración','Oportunidades','Validación cuantitativa','IA y modelos','Agentes','Noticias y eventos','Cartera y riesgo','Visualización','Datos e infraestructura','Fuentes alternativas']))
stats={'reference_date':'2026-11-03','observed_at':'2026-11-04','catalog_resources':len(projects),'directly_verified':sum(r.get('verification_level')!='D0' for r in projects),'verification_levels':dict(collections.Counter(r.get('verification_level') for r in projects)),'deep_reviews':len([r for r in projects if r.get('deep_review_path')]),'source_records':len(sources),'distinct_source_urls':len({s['url'] for s in sources}),'evidence_records':len(evidences),'search_queries':len(searches),'models':len(models),'datasets':len(datasets),'papers':len(papers),'algorithms':len(methods),'libraries':len(libraries),'providers':len(providers),'opportunities':len(opportunities),'comparisons':len(comparisons),'relationships':len(relations),'duplicate_repo_entries_removed':len(aliases),'by_category':{k:{'name':v,'resources':sum(k in r.get('categories',[]) for r in projects),'V3':sum(k in r.get('categories',[]) and r.get('verification_level')=='V3' for r in projects)} for k,v in cats.items()}}
(I/'coverage_stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
catalog='# Catálogo de recursos\n\n'+f"{len(projects)} entradas diferenciadas; {stats['directly_verified']} con consulta original suficiente para el nivel declarado. No son {len(projects)} herramientas listas para uso. Bibliotecas, pesos, datasets y papers son recursos distintos; se relacionan sin confundir sus derechos.\n\nD0: descubierto sin comprobación suficiente. V1: existencia/función o card/abstract. V2: documentación más licencia o archivo técnico. V3: ruta crítica y pruebas/dependencias examinadas estáticamente. Ningún nivel implica ejecución ni rentabilidad.\n\nUna sola entrada por recurso; la categoría principal organiza la tabla, el resto se conserva en JSON/CSV. FRED-MD y FRED-QD comparten página pero son datasets distintos. Los inventarios de bibliotecas/modelos/etc. son vistas del catálogo, no candidatos que deban sumarse de nuevo.\n\n"
def clean(v):return str(v or '—').replace('|','/').replace('\n',' ')
for k,v in cats.items():
    selected=[r for r in projects if (r.get('categories') or ['?'])[0]==k]
    if not selected:continue
    catalog+=f'## {k} — {v}\n\n| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |\n|---|---|---|---|---|\n'
    for r in selected:
        lic=r.get('license_code') or r.get('license_weights') or r.get('license_data') or 'No verificada'
        link=f"[{r['name']}]({r['url']})"
        if r.get('deep_review_path'):link+=f" · [revisión]({r['deep_review_path']})"
        catalog+=f"| `{r['id']}` {link} | {clean(r.get('resource_type'))} / {r.get('verification_level')} | {clean(r.get('description'))} | {clean(lic)} | {r.get('score_total') if r.get('score_total') is not None else 'sin puntuación'} / {clean(r.get('adoption_mode'))} |\n"
catalog+='\nLas fichas completas —commit, dependencias, fuentes, riesgos, confianza, limitaciones y puntos por criterio— están en [projects.json](inventories/projects.json) y [projects.csv](inventories/projects.csv). Para reproducir una afirmación, seguir evidence_ids → evidence → source_id → sources. No usar la tabla abreviada como autorización de adopción.\n'
(ROOT/'02_PROJECT_CATALOG.md').write_text(catalog,encoding='utf-8')
index='# Revisiones técnicas estáticas\n\nSe inspeccionaron rutas críticas y sus límites; no se ejecutaron proyectos ni tests de terceros. Una revisión parcial no es auditoría completa de seguridad, licencia transitiva o desempeño.\n\n'
for r in projects:
    if r.get('deep_review_path'):index+=f"- [{r['name']}]({pathlib.Path(r['deep_review_path']).name}) — `{r['id']}`, commit `{r.get('version_or_commit')}`.\n"
(ROOT/'03_DEEP_TECHNICAL_REVIEWS/README.md').write_text(index,encoding='utf-8')
products='# Cartera de herramientas personales\n\n'+f'{len(opportunities)} conceptos, todos sin implementar. Las cinco primeras prioridades tienen diseños propios. El orden estratégico pondera el objetivo financiero y la complementariedad; no es una ordenación automática del score editorial. OP-13 puntúa alto como capacidad transversal y debe incluirse desde el primer piloto; OP-14 puede resolverse inicialmente con herramientas existentes. Ninguno obliga a construir una plataforma.\n\nLos costes en jornadas son estimaciones de ingeniería para un alcance pequeño, no presupuestos cerrados ni plazos prometidos. El hardware no se midió. Una alternativa pública no implica datos ilimitados o redistribuibles.\n\n| Prioridad | Concepto | Puntos | Primera pregunta |\n|---|---|---|---|\n'
for o in opportunities:products+=f"| {o['rank']} | [{o['name']}]({o.get('blueprint_path') or '#'+o['id'].lower()}) | {o['score_total']} | {o['financial_question']} |\n"
labels={'problem':'Problema','target_user':'Usuario','financial_question':'Pregunta financiera','data':'Datos','libraries':'Bibliotecas','algorithms':'Métodos','workflow':'Flujo','minimal_architecture':'Arquitectura mínima','visible_result':'Resultado','frequency':'Frecuencia','consultation_time':'Tiempo de consulta','limitations':'Limitaciones','technical_cost_estimate':'Coste técnico estimado','recurring_cost':'Coste recurrente potencial','risks':'Riesgos','utility_metrics':'Cómo demostrar utilidad','increments':'Incrementos'}
for o in opportunities:
    products+=f"\n<a id=\"{o['id'].lower()}\"></a>\n\n## {o['id']} — {o['name']}\n\n"
    for k,label in labels.items():products+=f"**{label}:** {o[k]}\n\n"
    if o.get('blueprint_path'):products+=f"[Diseño preliminar completo]({o['blueprint_path']}).\n"
(ROOT/'11_PRODUCT_OPPORTUNITIES.md').write_text(products,encoding='utf-8')
print(json.dumps(stats,ensure_ascii=False))
