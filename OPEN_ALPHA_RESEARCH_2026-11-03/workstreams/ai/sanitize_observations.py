"""Keep provenance, not third-party source bodies, in the deliverable."""
import json,re
from pathlib import Path
B=Path(__file__).parent
catalog={c['id']:c for c in json.loads((B/'candidates.json').read_text(encoding='utf-8'))}
for filename in ['observations_repos.json','observations_hf.json','observations_code.json']:
 data=json.loads((B/filename).read_text(encoding='utf-8'))
 if filename=='observations_repos.json':
  for r in data:
   c=catalog['AI-'+r['slug']];r['license_verified']=c['license_code'];r['license_status_verified']=c['license_status']
 if filename=='observations_code.json':
  for r in data:
   if r.get('excerpt'):
    r['inspected_static']=True
    r['scope_note']='Texto obtenido para revisión estática; alcance concreto y limitaciones en ai_<slug>.md. Sin ejecución.'
 def clean(x):
  if isinstance(x,list):return [clean(y)for y in x]
  if isinstance(x,dict):return {k:clean(v)for k,v in x.items()if k not in ['excerpt','text']}
  return x
 (B/filename).write_text(json.dumps(clean(data),ensure_ascii=False,indent=2),encoding='utf-8')
print('Textos de terceros retirados; metadatos, hashes y URLs conservados.')
