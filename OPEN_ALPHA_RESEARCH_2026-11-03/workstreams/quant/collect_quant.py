"""Auxiliar propio de investigación: solo HTTP GET y metadatos, sin importar terceros."""
import urllib.request, urllib.error, concurrent.futures, json, re, hashlib, html
from pathlib import Path
BASE = Path(__file__).resolve().parent
DATE = '2026-11-04'
REPOS = '''microsoft/qlib|Qlib|G,H,F|Framework de investigación cuantitativa y modelos con datos point-in-time.
freqtrade/freqtrade|Freqtrade|G,B|Backtesting cripto, análisis de sesgos y motor de trading; ejecución fuera de alcance.
nautechsystems/nautilus_trader|NautilusTrader|G,C|Motor por eventos con instrumentos y simulación de ejecución.
QuantConnect/Lean|LEAN|G,K|Motor multiactivo de backtest y ejecución con modelos de realidad.
polakowo/vectorbt|vectorbt|G,B|Simulación vectorizada y barridos de parámetros.
ranaroussi/quantstats|QuantStats|K,G,L|Métricas de rentabilidad, riesgo y reportes.
robertmartin8/PyPortfolioOpt|PyPortfolioOpt|K|Optimización de cartera, covariance shrinkage, Black-Litterman y HRP.
openbq-org/OpenBB|OpenBB / OpenBQ|A,B,C,K|Plataforma de acceso uniforme a proveedores financieros.
bashtage/arch|arch|G,K|Volatilidad condicional, bootstrap, cointegración y comparación múltiple.
statsmodels/statsmodels|statsmodels|A,G,J|Modelos econométricos, estados espaciales y series temporales.
deepcharles/ruptures|ruptures|A,B,F|Detección offline de cambios estructurales.
skfolio/skfolio|skfolio|G,K|Selección y validación de carteras con interfaz scikit-learn.
dcajasn/Riskfolio-Lib|Riskfolio-Lib|K|Optimización de carteras con medidas de riesgo alternativas.
pmorissette/bt|bt|G,K|Backtesting de estrategias de asignación de activos.
kernc/backtesting.py|Backtesting.py|G|Motor compacto de backtesting sobre barras.
mementum/backtrader|Backtrader|G|Framework histórico de backtesting por eventos.
stefan-jansen/zipline-reloaded|Zipline-reloaded|G|Continuación de Zipline con bundles, calendarios y datos de acciones.
stefan-jansen/pyfolio-reloaded|Pyfolio-reloaded|K,G|Continuación de reportes de rendimiento de Pyfolio.
stefan-jansen/empyrical-reloaded|Empyrical-reloaded|K|Métricas financieras reutilizables.
stefan-jansen/alphalens-reloaded|Alphalens-reloaded|G,F|Continuación de análisis de factores transversales.
quantopian/alphalens|Alphalens original|G,F|Análisis original de factores; contrastar con forks mantenidos.
quantopian/empyrical|Empyrical original|K|Origen de métricas financieras; contrastar mantenimiento.
hudson-and-thames/mlfinlab|MLFinLab|G,H|Implementaciones de machine learning financiero; verificar acceso y licencia.
hudson-and-thames/arbitragelab|ArbitrageLab|G|Métodos de cointegración y estrategias relativas.
ricequant/rqalpha|RQAlpha|G|Framework chino de backtesting y trading modular.
vnpy/vnpy|VeighNa / vn.py|G|Framework chino de trading y extensiones cuantitativas.
pmorissette/ffn|ffn|K,G|Funciones de análisis de activos y carteras.
bashtage/linearmodels|linearmodels|A,J,G|Paneles, variables instrumentales y estimación econométrica.
hmmlearn/hmmlearn|hmmlearn|A,B,H|Modelos ocultos de Markov para estados latentes.
pykalman/pykalman|pykalman|A,H|Filtros y suavizadores de Kalman.
pywhy/dowhy|DoWhy|J,H|Identificación, estimación y refutación causal.
py-why/EconML|EconML|J,H|Estimación de efectos heterogéneos con ML.
alexiosg/rugarch|rugarch|K,H|Modelos GARCH en R.
braverock/PerformanceAnalytics|PerformanceAnalytics|K|Analítica de rentabilidad y riesgo en R.
braverock/PortfolioAnalytics|PortfolioAnalytics|K|Especificación y optimización de carteras en R.
braverock/quantstrat|quantstrat|G|Framework R de estrategias y reglas sobre datos financieros.
joshuaulrich/quantmod|quantmod|A,B|Modelización y adquisición de series financieras en R.
joshuaulrich/TTR|TTR|B,G|Funciones técnicas de series en R.
cran/strucchange|strucchange (mirror CRAN)|A,B,J|Tests de cambio estructural; mirror de paquete original.
LemaireJean-Baptiste/eventstudy|eventstudy|J,G|Estudios de eventos con retornos anormales.
pydata/pandas-datareader|pandas-datareader|A,M|Conectores para fuentes económicas y financieras.
mortada/fredapi|fredapi|A,M|Cliente FRED/ALFRED con datos históricos por vintage.
py-econometrics/pyfixest|PyFixest|J,A|Efectos fijos, inferencia y diferencias en diferencias.
khaeru/sdmx|sdmx1|A,M|Cliente y objetos SDMX para estadísticas oficiales.
dr-leo/pandaSDMX|pandaSDMX|A,M|Cliente SDMX para bancos centrales y agencias.
terence-lim/financial-data-science|Financial Data Science|A,G,J|Herramientas de investigación, lectores macro y estudios de eventos.
QuantEcon/QuantEcon.py|QuantEcon.py|A,G|Métodos computacionales económicos, cadenas de Markov y simulación.
bis-med-it/gingado|gingado|A,H|Caja de herramientas de ML para economía del BIS.
cvxgrp/cvxportfolio|cvxportfolio|K,G|Optimización de cartera y simulación considerando costes.
cvxpy/cvxpy|CVXPY|K|Modelado de optimización convexa como componente matemático.
abhinay/skepsis|skepsis|G|Validación y auditoría estadística de backtests; candidato reciente.
'''

def fetch(url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'OpenAlphaResearch/1.0 (static research)'})
        with urllib.request.urlopen(req,timeout=25) as r:
            raw=r.read(1800000)
            return {'url':url,'resolved_url':r.url,'status':r.status,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'text':raw.decode('utf-8',errors='replace')}
    except Exception as e: return {'url':url,'status':'error','error':str(e)}

def process(line):
    repo,name,cats,desc=line.split('|',3)
    result={'repo':repo,'name':name,'categories':cats.split(','),'description':desc,'files':[]}
    page=fetch('https://github.com/'+repo)
    result['page']={k:v for k,v in page.items() if k!='text'}
    txt=page.get('text','')
    branches=re.findall(r'"defaultBranch"\s*:\s*"([^\"]+)"',txt)
    commits=re.findall(r'"currentOid"\s*:\s*"([a-f0-9]{40})"',txt)
    result['branch']=branches[0] if branches else None
    result['commit']=commits[0] if commits else None
    result['archived']='"isArchived":true' in txt
    descriptions=re.findall(r'<meta name="description" content="([^"]*)"',txt)
    result['observed_description']=html.unescape(descriptions[0]) if descriptions else None
    result['listed_files']=list(dict.fromkeys(re.findall(r'"path"\s*:\s*"([^\"]+)"',txt)))[:100]
    result['observed_timestamps']=list(dict.fromkeys(re.findall(r'datetime="([^"]+)"',txt)))[:10]
    if result['commit']:
        files=result['listed_files']
        targets=[p for p in files if p.lower() in ['readme.md','readme.rst','readme','license','license.md','license.txt','copying','pyproject.toml','setup.py','requirements.txt']]
        for path in targets[:6]:
            f=fetch('https://raw.githubusercontent.com/'+repo+'/'+result['commit']+'/'+path)
            body=f.pop('text','')
            f['path']=path
            if path.lower().startswith('license') or path.lower()=='copying': f['license_text']=body[:25000]
            elif path.lower().startswith('readme'): f['readme_text']=body[:35000]
            else: f['manifest_text']=body[:25000]
            result['files'].append(f)
    return result

if __name__=='__main__':
    rows=[s for s in REPOS.strip().splitlines() if s]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        data=list(pool.map(process,rows))
    # Local working notes: source text is temporary and excluded from the delivery inventories.
    (BASE/'_temporary_observations.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps([{'repo':d['repo'],'status':d['page']['status'],'commit':d['commit'],'archived':d['archived'],'files':[f['path'] for f in d['files']],'description':d['observed_description']} for d in data],ensure_ascii=False,indent=2))
