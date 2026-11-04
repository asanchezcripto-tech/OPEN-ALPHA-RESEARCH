import concurrent.futures, json, re, pathlib, sys
from collect_sources import fetch, collect, ROOT
repos=sys.argv[1:]
out=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for repo,r in zip(repos,ex.map(lambda r:fetch('https://github.com/'+r),repos)):
  tx=r.get('text','')
  paths=list(dict.fromkeys(re.findall(r'"path":"([^"\\]+)"',tx)))
  titles=re.findall(r'<title>(.*?)</title>',tx)
  print(json.dumps({'repo':repo,'status':r['status'],'title':titles[:1],'paths':paths[:100],'archive':bool(re.search('This repository was archived by the owner',tx))},ensure_ascii=True))
  out.append({'repo':repo,'status':r['status'],'sha256':r.get('sha256'),'paths':paths,'archive':bool(re.search('This repository was archived by the owner',tx))})
p=ROOT/'tree_probes.json'
old=json.loads(p.read_text(encoding='utf8')) if p.exists() else []
p.write_text(json.dumps(old+out,ensure_ascii=False,indent=2),encoding='utf8')
