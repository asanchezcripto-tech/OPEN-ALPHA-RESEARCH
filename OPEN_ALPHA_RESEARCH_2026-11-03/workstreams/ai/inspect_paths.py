"""Inspect public source paths as text; no downloaded code is executed."""
import json,re,sys,concurrent.futures
from collect_public_metadata import fetch,BASE
repos={x['slug']:x for x in json.loads((BASE/'observations_repos.json').read_text(encoding='utf-8'))}
TARGETS={
'chronos':['src/chronos/chronos2/pipeline.py','src/chronos/chronos2/config.py','test/test_chronos2.py','pyproject.toml'],
'timesfm':['src','src/timesfm','src/timesfm_3','pyproject.toml'],
'uni2ts':['src/uni2ts/model/moirai2/forecast.py','src/uni2ts/model/moirai2/module.py','pyproject.toml','test'],
'fev':['src/fev/task.py','src/fev/metrics.py','src/fev','test','pyproject.toml'],
'mlforecast':['mlforecast/forecast.py','mlforecast/core.py','pyproject.toml','tests'],
'river':['river/drift/adwin.py','river/drift/test_drift_detectors.py','pyproject.toml'],
'tradingagents':['tradingagents/graph/trading_graph.py','tradingagents/dataflows/interface.py','tradingagents/agents/utils/memory.py','tests','pyproject.toml'],
'docling':['docling/document_converter.py','docling/datamodel/base_models.py','tests/test_document_converter.py','pyproject.toml'],
'fingpt':['fingpt','requirements.txt'],
'finbert':['finbert/finbert.py','finbert/utils.py','environment.yml'],
}
def task(item):
 slug,path=item;r=repos[slug]; repo=r['repo'];commit=r['commit'] or r['branch']
 if '.' not in path.split('/')[-1]:
  x=fetch('https://github.com/'+repo+'/tree/'+commit+'/'+path);txt=x.pop('text','')
  x['paths']=list(dict.fromkeys(re.findall(r'"path":"([^"]+)"',txt)));x['excerpt']=''
 else:
  x=fetch('https://raw.githubusercontent.com/'+repo+'/'+commit+'/'+path);x['excerpt']=x.pop('text','')
 x.update({'slug':slug,'path':path,'commit':commit});return x
if __name__=='__main__':
 items=[(s,p)for s,paths in TARGETS.items()for p in paths]
 out=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for r in pool.map(task,items):
   out.append(r);print(json.dumps({k:r.get(k)for k in ['slug','path','status','paths']}),flush=True)
 (BASE/'observations_code.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
