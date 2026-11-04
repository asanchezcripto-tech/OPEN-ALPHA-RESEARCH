"""Metadata and small cards only: no weights or dataset rows."""
import json, concurrent.futures
from collect_public_metadata import fetch,BASE,DATE
RESOURCES=[('model','amazon/chronos-2'),('model','amazon/chronos-bolt-small'),('model','google/timesfm-3.0-pytorch'),('model','google/timesfm-2.5-200m-pytorch'),('model','Salesforce/moirai-2.0-R-small'),('model','Salesforce/moirai-1.1-R-small'),('model','ProsusAI/finbert'),('model','BAAI/bge-m3'),('model','BAAI/bge-small-en-v1.5'),('model','ibm-granite/granite-timeseries-ttm-r2'),('model','NX-AI/TiRex'),('dataset','PatronusAI/financebench'),('dataset','takala/financial_phrasebank'),('dataset','ibm/finqa'),('dataset','Salesforce/GiftEval'),('dataset','Salesforce/GiftEvalPretrain'),('dataset','autogluon/chronos_datasets'),('dataset','autogluon/fev_datasets')]
def task(pair):
    kind,rid=pair; base='https://huggingface.co/'+('datasets/' if kind=='dataset' else '')+rid
    meta=fetch('https://huggingface.co/api/'+('datasets/' if kind=='dataset' else 'models/')+rid)
    t=meta.pop('text','{}')
    try: data=json.loads(t)
    except Exception:data={}
    sha=data.get('sha'); ref=sha or 'main'; files={}
    for path in ['README.md','LICENSE','config.json']:
        if path=='config.json' and kind=='dataset':continue
        f=fetch(base+'/resolve/'+ref+'/'+path)
        if 'text'in f:f['excerpt']=f.pop('text')[:18000]
        files[path]=f
    return {'kind':kind,'rid':rid,'url':base,'commit':sha,'lastModified':data.get('lastModified'),'license_declared':data.get('cardData',{}).get('license'),'gated':data.get('gated'),'metadata_source':meta,'files':files,'accessed_at':DATE}
if __name__=='__main__':
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for r in pool.map(task,RESOURCES):
            results.append(r);(BASE/'observations_hf.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
            print(json.dumps({k:r[k]for k in ['rid','commit','license_declared','gated']}),flush=True)
