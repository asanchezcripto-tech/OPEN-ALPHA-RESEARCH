"""Lectura estática de rutas seleccionadas; no ejecuta el código leído."""
import json,re,concurrent.futures
from collect_quant import BASE,fetch

PATHS={
'microsoft/qlib':['qlib/data/pit.py','qlib/data/data.py','tests/test_pit.py','docs/component/data.rst'],
'polakowo/vectorbt':['vectorbt/portfolio/base.py','vectorbt/portfolio/nb.py','tests/test_portfolio.py'],
'robertmartin8/PyPortfolioOpt':['pypfopt/risk_models.py','pypfopt/efficient_frontier/efficient_frontier.py','tests/test_risk_models.py'],
'skfolio/skfolio':['src/skfolio/model_selection/_combinatorial.py','src/skfolio/model_selection/_walk_forward.py','tests/test_model_selection/test_combinatorial.py','docs/user_guide/model_selection.rst'],
'bashtage/arch':['arch/bootstrap/multiple_comparison.py','arch/bootstrap/base.py','arch/tests/bootstrap/test_multiple_comparison.py'],
'deepcharles/ruptures':['src/ruptures/detection/pelt.py','src/ruptures/costs/costl2.py','tests/test_detection.py'],
'nautechsystems/nautilus_trader':['crates/backtest/src/engine.rs','crates/execution/src/models/fill.rs','crates/backtest/Cargo.toml'],
'QuantConnect/Lean':['Engine/AlgorithmManager.cs','Common/Orders/Fills/EquityFillModel.cs','Tests/Common/Orders/Fills/EquityFillModelTests.cs'],
'openbq-org/OpenBB':['openbb_platform/providers/fred/openbb_fred/models/series.py','openbb_platform/core/openbb_core/provider/abstract/fetcher.py','openbb_platform/providers/fred/pyproject.toml','openbb_platform/providers/fred/tests/test_fred_fetchers.py'],
'mortada/fredapi':['fredapi/fred.py','fredapi/tests/test_fred.py','setup.py'],
'freqtrade/freqtrade':['docs/lookahead-analysis.md','docs/recursive-analysis.md'],
'abhinay/skepsis':['tests/golden/test_dsr_paper_example.py'],
}
def read_repo(d):
 files=[]
 for p in PATHS[d['repo']]:
  u='https://raw.githubusercontent.com/'+d['repo']+'/'+d['commit']+'/'+p
  z=fetch(u); z['path']=p; files.append(z)
 return {'repo':d['repo'],'commit':d['commit'],'files':files}

if __name__=='__main__':
 ds=json.loads((BASE/'_temporary_observations.json').read_text(encoding='utf8'))
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
  rows=list(ex.map(read_repo,[d for d in ds if d['repo'] in PATHS]))
 (BASE/'_temporary_deep.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
 for d in rows:
  print(d['repo'])
  for f in d['files']:
   t=f.get('text',''); print(f['path'],f['status'],len(t));
   defs=re.findall(r'^(?:class |def |    def |pub (?:struct|enum|fn) |    pub fn |        public |        protected ).*$',t,re.M)
   print('\n'.join(defs[:40]))
