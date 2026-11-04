"""Read-only public metadata collection. Never imports or executes downloaded code."""
import concurrent.futures, hashlib, json, re, urllib.request, urllib.error
from pathlib import Path
BASE=Path(__file__).parent
DATE='2026-11-04'
REPOS=[
('chronos','amazon-science/chronos-forecasting'),('timesfm','google-research/timesfm'),
('uni2ts','SalesforceAIResearch/uni2ts'),('gift-eval','SalesforceAIResearch/gift-eval'),
('fev','autogluon/fev'),('autogluon','autogluon/autogluon'),
('gluonts','awslabs/gluonts'),('statsforecast','Nixtla/statsforecast'),
('mlforecast','Nixtla/mlforecast'),('neuralforecast','Nixtla/neuralforecast'),
('darts','unit8co/darts'),('sktime','sktime/sktime'),('pytorch-forecasting','sktime/pytorch-forecasting'),
('timeseries-library','thuml/Time-Series-Library'),('lag-llama','time-series-foundation-models/lag-llama'),
('moment','moment-timeseries-foundation-model/moment'),('granite-tsfm','ibm-granite/granite-tsfm'),
('tirex','NX-AI/tirex'),('tabpfn','PriorLabs/TabPFN'),('lightgbm','microsoft/LightGBM'),
('catboost','catboost/catboost'),('xgboost','dmlc/xgboost'),('river','online-ml/river'),
('pyod','yzhao062/pyod'),('merlion','salesforce/Merlion'),('adtk','arundo/adtk'),
('alibi-detect','SeldonIO/alibi-detect'),('evidently','evidentlyai/evidently'),
('dowhy','py-why/dowhy'),('econml','py-why/EconML'),('causal-learn','py-why/causal-learn'),
('fingpt','AI4Finance-Foundation/FinGPT'),('finrobot','AI4Finance-Foundation/FinRobot'),
('tradingagents','TauricResearch/TradingAgents'),('ai-hedge-fund','virattt/ai-hedge-fund'),
('finbert','ProsusAI/finBERT'),('finqa','/czyssrs/FinQA'),('tatqa','NExTplusplus/TAT-QA'),
('financebench','patronus-ai/financebench'),('convfinqa','czyssrs/ConvFinQA'),
('docling','docling-project/docling'),('unstructured','Unstructured-IO/unstructured'),
('marker','datalab-to/marker'),('trafilatura','adbar/trafilatura'),
('sentence-transformers','UKPLab/sentence-transformers'),('flagembedding','FlagOpen/FlagEmbedding'),
('haystack','deepset-ai/haystack'),('llamaindex','run-llama/llama_index'),
('langgraph','langchain-ai/langgraph'),('pydantic-ai','pydantic/pydantic-ai'),
('dspy','stanfordnlp/dspy'),('ragas','explodinggradients/ragas'),('inspect-ai','UKGovernmentBEIS/inspect_ai'),
('garak','NVIDIA/garak'),('pyrit','Azure/PyRIT'),('promptfoo','promptfoo/promptfoo'),
('llm-guard','protectai/llm-guard'),('tsfel','fraunhoferportugal/tsfel'),
('tsfresh','blue-yonder/tsfresh'),('aeon','aeon-toolkit/aeon')]

def fetch(url,limit=1200000):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'OpenAlphaResearch/1.0 (read-only research)'})
        with urllib.request.urlopen(req,timeout=25) as res:
            b=res.read(limit+1)
            return {'url':url,'resolved_url':res.url,'status':res.status,'sha256':hashlib.sha256(b).hexdigest(),'truncated':len(b)>limit,'text':b[:limit].decode('utf-8','replace')}
    except Exception as e:return {'url':url,'status':'error','error':str(e)}

def repo_task(pair):
    slug,repo=pair; repo=repo.strip('/'); root=fetch('https://github.com/'+repo)
    html=root.pop('text',''); branch=re.search(r'"defaultBranch":"([^"]+)"',html)
    oid=re.search(r'"currentOid":"([0-9a-f]{40})"',html)
    branch=branch.group(1) if branch else 'main'; commit=oid.group(1) if oid else None
    refs=commit or branch; files={}; reads=[]
    for kind,paths in [('readme',['README.md','README.rst']),('license',['LICENSE','LICENSE.md','LICENSE.txt'])]:
        for path in paths:
            item=fetch('https://raw.githubusercontent.com/'+repo+'/'+refs+'/'+path)
            if item.get('status')==200:
                text=item.pop('text'); item['excerpt']=text[:9500] if kind=='readme' else text[:12500]
                files[kind]=item;break
            reads.append(item)
    archived='This repository was archived by the owner' in html
    return {'slug':slug,'repo':repo,'root':root,'branch':branch,'commit':commit,'archived':archived,'files':files,'failed_reads':reads,'accessed_at':DATE}

if __name__=='__main__':
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for r in pool.map(repo_task,REPOS):
            results.append(r)
            (BASE/'observations_repos.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
            print(json.dumps({'slug':r['slug'],'status':r['root']['status'],'commit':r['commit'],'files':list(r['files']),'archived':r['archived']}),flush=True)
