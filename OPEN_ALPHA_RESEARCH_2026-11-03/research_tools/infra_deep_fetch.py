import concurrent.futures,json,pathlib
from inspect_public import fetch,ROOT
rows={r['id']:r for r in json.loads((ROOT/'workstreams/infra/inspection.json').read_text(encoding='utf-8'))}
paths={
'duckdb':['src/execution/operator/join/physical_asof_join.cpp','test/sql/join/asof/asof_join.test','CMakeLists.txt'],
'polars':['py-polars/src/polars/dataframe/frame.py','py-polars/tests/unit/operations/test_join_asof.py','py-polars/pyproject.toml'],
'pandera':['pandera/api/pandas/container.py','pandera/backends/pandas/container.py','tests/core/test_schemas.py','pyproject.toml'],
'dlt':['dlt/extract/incremental/__init__.py','tests/extract/test_incremental.py','pyproject.toml'],
'requests-cache':['requests_cache/session.py','requests_cache/policy/actions.py','tests/unit/test_session.py','pyproject.toml'],
'marimo':['marimo/_runtime/dataflow/graph.py','marimo/_runtime/dataflow.py','tests/_runtime/test_dataflow.py','pyproject.toml'],
'qfs':['qfs/store.py','tests/test_point_in_time.py','pyproject.toml'],
'datacompy':['datacompy/core.py','datacompy/polars.py','tests/test_core.py','pyproject.toml'],
'patito':['src/patito/validators.py','src/patito/pydantic.py','tests/test_validators.py','pyproject.toml'],
}
tasks=[]
for key,files in paths.items():
 r=rows['infra-'+key]; repo='/'.join(r['url'].split('/')[-2:]);sha=r['current_oid']
 for path in files: tasks.append((r['id'],path,f'https://raw.githubusercontent.com/{repo}/{sha}/{path}'))
def get(t):
 rid,path,url=t;meta,body=fetch(url)
 return dict(meta,candidate_id=rid,path=path)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: data=list(pool.map(get,tasks))
(ROOT/'workstreams/infra/deep_files.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
for r in data: print(r['candidate_id'],r['path'],r['status'],r.get('bytes'))
