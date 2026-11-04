"""Consolida notas propias y metadatos de investigación. No importa código externo."""
import json,re,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent.parent
DATE='2026-11-04'
OBS=json.loads((BASE/'_temporary_observations.json').read_text(encoding='utf8'))
DEEP=json.loads((BASE/'_temporary_deep.json').read_text(encoding='utf8'))
sources=[]; evidence=[]; relations=[]; candidates=[]
def uid(prefix,text):return prefix+hashlib.sha256(text.encode()).hexdigest()[:12]
def slug(s):return re.sub('[^a-z0-9]+','-',s.lower()).strip('-')
def source(url,title,kind='repository',status=200,commit=None,notes=None,sha=None):
 id=uid('src-quant-',url)
 if not any(s['id']==id for s in sources):sources.append(dict(id=id,url=url,title=title,accessed_at=DATE,source_type=kind,status=status,version_or_commit=commit,sha256=sha,notes=notes))
 return id
def ev(cid,sid,claim,kind='observación estática',limitations='Sin ejecución; no demuestra exactitud económica ni rentabilidad.'):
 id=uid('ev-quant-',cid+sid+claim);evidence.append(dict(id=id,candidate_id=cid,source_id=sid,claim=claim,evidence_type=kind,limitations=limitations));return id
def dump(name,obj):(BASE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf8')
def url(d,p):return 'https://github.com/'+d['repo']+'/blob/'+d['commit']+'/'+p
def link(d,p,label=None):return '['+(label or p)+']('+url(d,p)+')'

SPECIAL={
'microsoft/qlib':('MIT','REUTILIZACIÓN POTENCIALMENTE COMPATIBLE'),
'py-why/EconML':('MIT; componentes econml.tree/econml.grf derivados bajo BSD-3-Clause','REUTILIZACIÓN POTENCIALMENTE COMPATIBLE'),
'polakowo/vectorbt':('Apache-2.0 WITH Commons-Clause','SOLO INVESTIGACIÓN / RESTRICCIONES'),
'bashtage/arch':('NCSA','REUTILIZACIÓN POTENCIALMENTE COMPATIBLE'),
'bashtage/linearmodels':('NCSA','REUTILIZACIÓN POTENCIALMENTE COMPATIBLE'),
'pykalman/pykalman':('BSD modificado: restricciones de canales de distribución','SOLO INVESTIGACIÓN / RESTRICCIONES'),
'ricequant/rqalpha':('Apache-2.0 modificado: uso comercial sujeto a autorización','SOLO INVESTIGACIÓN / RESTRICCIONES'),
'hudson-and-thames/mlfinlab':('Acuerdo propietario Hudson & Thames; referencias internas ambiguas a ArbitrageLab','SOLO INVESTIGACIÓN / RESTRICCIONES'),
}

REVIEWS={
'microsoft/qlib':{
'title':'Qlib: conservar el diseño point-in-time antes que adoptar toda la plataforma',
'score':[22,13,9,6,10,5,5,6], 'dependencies':['pandas>=1.1','mlflow<3.13','filelock>=3.16.0,<3.30','LightGBM','CVXPY','PyArrow'],
'input':'Panel de instrumentos y features, calendarios, fecha del periodo contable y fecha de disponibilidad de cada revisión.',
'output':'Features consultables en el momento de observación, datasets de entrenamiento y evaluación de señales.',
'architecture':'La capa de datos separa proveedores de calendario, instrumentos, features, expresiones y PIT. El operador P colapsa una serie por periodos a cada fecha de observación: invoca la carga de la feature con cur_time y conserva el último valor disponible. PRef fija el periodo contable. Esta separación sirve para fundamentación DeFi revisada, aunque los recolectores de referencia son de acciones.',
'observed':'En qlib/data/pit.py se rechaza una ventana que refiera a un periodo futuro; la ausencia de fichero produce warning y serie vacía. En tests/test_pit.py hay fixtures de publicaciones revisadas, pruebas de consultas, expresiones y datos inexistentes. Se leyó también la interfaz PITProvider y la documentación de datos. El test de normalización con fecha ausente introduce una fecha por regla: un dato imputado no debe convertirse en fecha de publicación comprobada.',
'temporal':'El motor solo puede respetar la disponibilidad que recibe. Un historical dump reconstruido hoy, un universo que excluya tokens muertos o una fecha de publicación imputada pueden seguir introduciendo sesgo. El PIT de Qlib no convierte por sí solo una API actual de revenue en un archivo histórico de conocimiento.',
'tradeoff':'Para 3–18 meses aporta disciplina de experimentos y features; desplegar toda la plataforma solo para diez métricas es excesivo. Priorizar una tabla append-only con event_time, available_at y acquired_at; considerar Qlib cuando existan muchos factores y un universo point-in-time.',
'hardware':'Estimación editorial para datos diarios de decenas de activos: CPU y 8–16 GB RAM; GPU innecesaria para la capa PIT o un baseline lineal. MLflow/Redis y extensiones de compilación aumentan superficie operativa. No se midió uso real.',
'experiment':'Construir en un entorno futuro autorizado un fixture con dos revisiones de revenue, un token retirado y una fecha desconocida. Exigir que la consulta t no cambie al añadir una revisión disponible después de t; lo desconocido debe generar abstención o rango, no una fecha exacta inventada.',
'decision':'Extraer el patrón temporal y la interfaz de features; investigar más antes de adoptar el framework completo. Alternativa proporcional: DuckDB/Parquet más as-of explícito y un registro de experimentos. Qlib no acredita alpha cripto por contener modelos o integrar RD-Agent.',
'paths':['qlib/data/pit.py','qlib/data/data.py','tests/test_pit.py','docs/component/data.rst','pyproject.toml','LICENSE'],
},
'polakowo/vectorbt':{
'title':'vectorbt: exploración rápida con costes explícitos y licencia restringida',
'score':[20,13,10,9,4,5,7,5],'dependencies':['NumPy>=2.4.6','pandas>=3.0.3,<4.0','Numba>=0.66','SciPy','Plotly','vectorbt-rust opcional'],
'input':'Precios/barras, señales u órdenes, tamaño, costes, deslizamiento, agrupación y capital inicial.',
'output':'Registros de órdenes, cash, posiciones, métricas y comparaciones de muchas variantes.',
'architecture':'Portfolio.from_orders y from_signals normalizan y difunden arrays antes de pasarlos a kernels. Las rutas Numba leídas implementan ejecución con estado, cash compartido y resolución de señales. El manifiesto actual añade engine y backend Rust opcional: no se verificó paridad de ambos backends.',
'observed':'buy_nb aplica precio multiplicado por 1+slippage y sell_nb por 1-slippage; ambos consideran fees, límites de tamaño y cash. simulate_from_signal_func_nb tiene costes por defecto cero y configuración de stops. tests/test_portfolio.py contiene casos concretos de fees, slippage, partial fills, cash sharing y call sequence; se inspeccionaron nombres y fragmentos, no se ejecutó la suite.',
'temporal':'El usuario controla cuándo la señal conoce el cierre y cuándo opera. El motor no audita automáticamente disponibilidad de fundamentales ni garantiza orden intrabar de high/low. La simultaneidad entre columnas y cash sharing exige revisar la secuencia de órdenes.',
'tradeoff':'Adecuado para comparar reglas semanales y escenarios de coste. Su rapidez abarata también el sobreajuste: cada intento debe registrarse, incluidos resultados descartados. Comparar con bt para asignación de activos y con un motor por eventos únicamente cuando el orden temporal cambie la conclusión.',
'hardware':'CPU y 8–16 GB RAM para paneles diarios modestos, estimación editorial. Una matriz T×N×P crece con todas las variantes; limitar lotes. El commit requiere Python>=3.11,<3.15 y nuevas versiones NumPy/pandas; no asumir compatibilidad con notebooks históricos.',
'experiment':'Tomar una regla semanal simple y un ledger manual de diez operaciones. Comparar comisiones dobles, spread, señal retrasada una barra y secuencia de rebalanceo. Aceptar solo coincidencia contable y robustez de conclusiones ante esos cambios; no seleccionar la variante de Sharpe máximo sin ajuste por búsqueda.',
'decision':'Uso personal exploratorio condicionado. LICENSE.md declara Apache 2.0 con Commons Clause: no es Apache permisiva sin restricciones. Antes de vender un producto/servicio derivado hace falta revisión del alcance. El módulo PRO comercial es otro recurso; sus capacidades no se atribuyen a este repositorio.',
'paths':['vectorbt/portfolio/base.py','vectorbt/portfolio/nb.py','tests/test_portfolio.py','pyproject.toml','LICENSE.md'],
},
'robertmartin8/PyPortfolioOpt':{
'title':'PyPortfolioOpt: mejores estimadores de riesgo antes de maximizar Sharpe',
'score':[22,13,12,10,10,5,7,4],'dependencies':['CVXPY>=1.1.19','NumPy>=1.26,<3','pandas<4','scikit-base<0.14','scikit-learn','SciPy'],
'input':'Retornos o precios alineados, frecuencia anual, covarianza, restricciones de pesos y, opcionalmente, expectativas.',
'output':'Matriz de riesgo regularizada, pesos condicionados a supuestos y métricas teóricas de la cartera.',
'architecture':'risk_models separa estimación de covarianza de EfficientFrontier, que formula objetivos y restricciones mediante CVXPY. CovarianceShrinkage ofrece objetivos de varianza constante, factor único y correlación constante. Se revisaron riesgo y max_sharpe, no todos los módulos Black-Litterman o HRP.',
'observed':'La reparación espectral de matrices sustituye autovalores negativos por cero y avisa; esto corrige factibilidad numérica, no errores económicos de datos. Ledoit-Wolf de varianza constante usa np.nan_to_num antes del estimador: el tratamiento previo de faltantes debe ser explícito. max_sharpe exige al menos una expectativa superior al tipo libre de riesgo y transforma variables. Tests de sample covariance, log returns y semidefinición usan respuestas esperadas.',
'temporal':'La covarianza por defecto se anualiza a 252 periodos; en cripto diario 24/7 no trasladar esa convención sin decisión explícita. Historial desigual por token y deslistados cambian la muestra. Ajustar estimadores solo con entrenamiento, con rebalanceo fuera de muestra.',
'tradeoff':'La capacidad útil inmediata es comparar exposición y concentración bajo covarianzas distintas; la frontera eficiente puede ser frágil a medias estimadas. Comparar pesos iguales, BTC/ETH y mínima volatilidad con límites por activo antes de optimizar retornos.',
'hardware':'CPU y 8 GB RAM suelen bastar para decenas de activos y problemas convexos pequeños; estimación no benchmark. Solvers y restricciones no convexas pueden elevar dificultad. El pyproject inspeccionado declara 1.6.0; esto no prueba instalación ni release estable en este equipo.',
'experiment':'Usar 12 ventanas de rebalanceo con datos previos exclusivamente. Medir concentración máxima, rotación, ES realizado y sensibilidad al borrar una semana de datos. Aceptación: pesos factibles, contabilidad reproducible, y menor fragilidad frente a equal weight; ninguna obligación de mejorar rentabilidad.',
'decision':'Adoptar como biblioteca de escenarios de riesgo. Licencia MIT revisada. La URL antigua robertmartin8 redirige actualmente a PyPortfolio/PyPortfolioOpt; conservar canonicalización y commit. skfolio ofrece validación integrada; Riskfolio-Lib amplía familias de riesgo con más complejidad.',
'paths':['pypfopt/risk_models.py','pypfopt/efficient_frontier/efficient_frontier.py','tests/test_risk_models.py','pyproject.toml','LICENSE'],
},
'skfolio/skfolio':{
'title':'skfolio: validación de carteras; la purga no viene activada por el nombre',
'score':[23,13,12,9,10,5,7,6],'dependencies':['scikit-learn>=1.6','CVXPY-base>=1.5','Clarabel>=0.10','pandas>=2.1','NumPy','SciPy>=1.15.2','Plotly>=6'],
'input':'Matriz temporal de retornos, reglas de entrenamiento/prueba, horizonte de etiquetas, costes y restricciones.',
'output':'Carteras por ventana y poblaciones de trayectorias comparables, en lugar de un único backtest elegido.',
'architecture':'Estimadores compatibles con scikit-learn, optimizadores convexos y splitters específicos. WalkForward soporta tamaños por observación y calendario. CombinatorialPurgedCV construye combinaciones de folds y recompone trayectorias; introduce un máximo de combinaciones para impedir configuraciones explosivas.',
'observed':'El constructor verificado fija n_folds=10, n_test_folds=8, purged_size=0 y embargo_size=0. split usa índices de filas y elimina posiciones alrededor de fronteras. Los tests incluyen folds desiguales, límites de purga/embargo, errores de configuración y regresión de índices concatenados. No se midió cobertura porcentual ni se ejecutaron.',
'temporal':'CPCV puede entrenar con bloques posteriores al bloque evaluado: ayuda a estimar dispersión de selección bajo supuestos, pero no sustituye una simulación prospectiva walk-forward. Una purga en filas requiere traducir el horizonte real y tratar calendarios irregulares. Etiquetas de 90–540 días dejan muy pocas observaciones efectivamente independientes.',
'tradeoff':'La integración reduce trabajo de validación de carteras y obliga a comparar trayectorias. Para un screener fundamental simple puede bastar walk-forward con embargo explícito. No usar KFold barajado ni elegir a posteriori el mejor camino CPCV como evidencia de desempeño futuro.',
'hardware':'CPU, 8–16 GB RAM estimados para unas decenas de activos; coste proporcional a número de ajustes, folds y solvers. GPU innecesaria. El manifiesto examinado indica 1.12.5 y Python>=3.10; compatibilidad de todos los extras no verificada.',
'experiment':'Fixture de etiquetas solapadas a 30 días con fechas irregulares. Verificar intersección vacía entre intervalos de entrenamiento y prueba, luego comparar equal weight, inverse volatility y HRP con la misma ventana. Registrar rotación neta de costes y distribución de riesgos, no solo media del Sharpe.',
'decision':'Biblioteca prioritaria para Portfolio Risk Lens y auditoría de candidatos. BSD-3-Clause revisada. Empezar por WalkForward y baselines; añadir CPCV solo si el tamaño muestral y el horizonte lo justifican.',
'paths':['src/skfolio/model_selection/_combinatorial.py','src/skfolio/model_selection/_walk_forward.py','tests/test_model_selection/test_combinatorial.py','docs/user_guide/model_selection.rst','pyproject.toml','LICENSE'],
},
'bashtage/arch':{
'title':'arch: una biblioteca de inferencia que vale más que otro optimizador',
'score':[24,14,13,10,10,5,7,6],'dependencies':['NumPy','pandas','SciPy','statsmodels','packaging; Cython/Meson para compilación'],
'input':'Pérdidas de un benchmark y de todas las variantes sobre las mismas fechas; o retornos para modelos de volatilidad.',
'output':'Pruebas SPA/StepM, conjuntos de confianza MCS, intervalos bootstrap y distribuciones condicionadas.',
'architecture':'bootstrap/base implementa remuestreo temporal; multiple_comparison aplica pérdidas diferenciales, varianzas de largo plazo y remuestreo para comparación múltiple. El código admite stationary, circular y moving block bootstrap; la inferencia queda separada del motor que produjo resultados.',
'observed':'SPA exige benchmark unidimensional y alternativas T×K, pérdidas finitas y muestras compatibles. La longitud de bloque por defecto depende de sqrt(T), pero el propio contrato recomienda elegirla para los datos. nested=True con studentize requiere aproximadamente reps² remuestreos, por lo que es una opción cara. Los tests leídos comprueban kernels, studentización dentro del bootstrap, pérdidas idénticas, errores y reproducibilidad de semillas.',
'temporal':'Los bloques conservan dependencia local mejor que barajar retornos sueltos, pero no crean observaciones independientes ni arreglan series con look-ahead. Si cambia el régimen, la estacionariedad aproximada necesaria para extrapolar se debilita. La longitud de bloque debe probarse en un rango predefinido.',
'tradeoff':'Permite rechazar una colección de señales que no supera un baseline bajo búsqueda múltiple. Evitar interpretar p-value como probabilidad de que una estrategia sea rentable. MCS devuelve alternativas indistinguibles a un nivel dado, no una orden de comprar la mejor.',
'hardware':'CPU y 8 GB RAM estimados para pocas decenas de señales diarias; RAM/tiempo crecen con T,K,reps. El método MCS revisado forma tensores de comparaciones por pares; un catálogo inmenso no es gratis. No se ejecutó benchmark.',
'experiment':'Registrar primero 20 reglas y benchmark, producir pérdidas netas homogéneas y aplicar SPA con tres longitudes de bloque justificadas. Añadir un control deliberadamente sin señal y un caso con fuga temporal para comprobar que la auditoría de datos, separada, lo rechaza. Exigir un resultado estable o abstenerse.',
'decision':'Adoptar biblioteca. Licencia NCSA verificada en pyproject y texto, no etiquetarla MIT por parecido. Prioridad alta para un Evidence/Backtest Auditor independiente; reutiliza técnicas de estadística antes de incorporar agentes generadores de estrategias.',
'paths':['arch/bootstrap/multiple_comparison.py','arch/bootstrap/base.py','arch/tests/bootstrap/test_multiple_comparison.py','pyproject.toml','LICENSE.md'],
},
'deepcharles/ruptures':{
'title':'ruptures: segmentación útil, con obligación de medir el retraso de detección',
'score':[23,13,13,11,10,5,7,6],'dependencies':['NumPy','SciPy; Cython para ciertas rutas compiladas'],
'input':'Serie univariable o matriz temporal de variables escaladas; penalización, coste y segmento mínimo.',
'output':'Índices de ruptura de una segmentación retrospectiva, no probabilidades de un régimen económico.',
'architecture':'La interfaz BaseEstimator separa fit/predict de funciones de coste. Pelt acumula el error de cada segmento más penalización y poda candidatos. CostL2 suma varianzas por feature multiplicadas por longitud del tramo; por ello unidades y escalado afectan directamente al resultado.',
'observed':'Pelt usa por defecto model=l2, min_size=2 y jump=5. predict comprueba que la segmentación sea posible. fit almacena toda la señal; la recursión evalúa particiones hasta el final recibido. tests/test_detection.py existe y fue leído a nivel de estructura; no se ejecutó ni se midió cobertura.',
'temporal':'Aplicar una vez PELT a toda la historia y usar retrospectivamente sus rupturas como alertas produce conocimiento futuro. Para evaluar utilidad operativa, recalcular con prefijos de datos y guardar cuándo apareció cada alerta, cuánto se movió y si desapareció al llegar nuevos puntos.',
'tradeoff':'Una pequeña librería de costes es más proporcional que entrenar un transformer para detectar cambios de nivel, volatilidad o correlación. No identifica automáticamente bull/bear ni causalidad macro. La elección de coste, ventana y penalización determina qué cambio puede verse.',
'hardware':'CPU y 4–8 GB RAM estimados para paneles diarios pequeños; el coste depende del algoritmo y de candidatos conservados. No afirmar complejidad lineal universal. GPU innecesaria. Estandarización debe estimarse solo con datos disponibles.',
'experiment':'Crear un replay semanal de funding, volatilidad realizada y crecimiento de stablecoins. Comparar PELT con CUSUM o umbrales robustos, bajo presupuesto fijo de falsas alarmas. Aceptar si reduce retraso o trabajo de revisión sin multiplicar alarmas, medido sobre periodos retenidos.',
'decision':'Adoptar para exploración y extraer técnica para Market Regime Navigator; no vender sus rupturas retrospectivas como anticipación. BSD-2-Clause revisada. strucchange ofrece monitorización y tests econométricos alternativos; HMM añade estados latentes a costa de más supuestos.',
'paths':['src/ruptures/detection/pelt.py','src/ruptures/costs/costl2.py','tests/test_detection.py','LICENSE'],
},
'nautechsystems/nautilus_trader':{
'title':'NautilusTrader: referencia de relojes y eventos, adopción completa aplazada',
'score':[17,14,8,4,8,5,4,6],'dependencies':['Rust; crates nautilus-common/model/execution/system; bindings Python; modelos de fill y fees'],
'input':'Instrumentos, eventos de mercado con timestamps, venues, saldos iniciales, estrategias y modelos de ejecución.',
'output':'Eventos de órdenes/fills, estados de cartera y resultados de una simulación configurable.',
'architecture':'El núcleo Rust BacktestEngine coordina un kernel, reloj virtual, iterador de datos, venues simulados y callbacks. add_data puede ordenar por ts_init; la separación de tiempo del evento y de inicialización resulta valiosa para un laboratorio con disponibilidad diferida. No debe confundirse ts_init importado con fecha histórica de conocimiento verificada.',
'observed':'run revisa errores previos de callbacks, funding y balances, y aborta en estados inválidos. Se leyeron tests dentro de engine.rs sobre secuencias de modificaciones, fills, timers, cambios de instrumentos y restauración. FillModel permite un libro sintético y rutas probabilísticas; la existencia de una interfaz realista no garantiza una calibración realista.',
'temporal':'La reproducción ordenada sigue necesitando feeds completos, precisión de timestamps y políticas de latencia. Una configuración de liquidez ilimitada o fill dentro del spread puede fabricar una ejecución favorable si no se documenta. No se verificó equivalencia de datos históricos y feed en vivo.',
'tradeoff':'Valioso cuando una hipótesis swing depende de orden de eventos, funding y fills multivenue. Para valoración de protocolos a seis meses es más complejo que lo necesario. Extraer diseño de reloj e identidad de instrumento antes de montar un motor de trading.',
'hardware':'Estimación: 16–32 GB RAM y SSD para replay intradía; datos diarios requieren mucho menos. Rust y bindings implican más mantenimiento. No se descargaron wheels, compiladores ni histórico, y no se midió rendimiento.',
'experiment':'Si una hipótesis futura depende de ejecución, usar un caso pequeño con orden retrasada, funding, cambio de instrumento y hueco de feed. Exigir coincidencia con ledger manual, error explícito ante inconsistencias y sensibilidad al doble de spread/latencia. Comparar con simulación por barras para demostrar necesidad del motor.',
'decision':'Conservar como referencia y adoptar solo bajo necesidad demostrada. LGPL-3.0 revisada con obligaciones a evaluar según distribución/enlace. No atribuir beneficios o fidelidad empírica al calificativo production-grade.',
'paths':['crates/backtest/src/engine.rs','crates/execution/src/models/fill.rs','crates/backtest/Cargo.toml','LICENSE'],
},
'QuantConnect/Lean':{
'title':'LEAN: un buen motor multiactivo no incluye por sí mismo buenos históricos',
'score':[18,14,8,5,10,5,5,4],'dependencies':['.NET/C#','integración Python','proveedores y modelos de brokerage/datos'],
'input':'Suscripciones e instrumentos, slices temporales, estrategia, universo y modelos de comisiones/slippage/fill.',
'output':'Simulación por eventos, órdenes, posiciones y reportes.',
'architecture':'AlgorithmManager recorre slices de datos y coordina warmup, algoritmo, transacciones, resultados y reloj. Los fill models son componentes intercambiables. Se inspeccionó EquityFillModel como ejemplo concreto; no se extrapolan sus reglas a perpetuos cripto.',
'observed':'MarketFill obtiene bid/ask según tipos de datos realmente suscritos y añade slippage. La ruta stop-limit examinada rechaza barras cuyo cierre no sea posterior a la orden. Los tests comprueban datos obsoletos, precio bid/ask, horas de mercado y órdenes antes de la barra. Esto es mejor evidencia de implementación que una lista comercial de activos soportados.',
'temporal':'Un motor con controles no corrige un universo creado con información futura ni una base ajustada retrospectivamente mal documentada. Horarios de acciones, splits y ajustes no se trasladan directamente a mercados 24/7. La prueba examinada es de equity; funding/liquidación de cripto exige revisión separada.',
'tradeoff':'Aporta más valor para investigaciones multiactivo que mezclen renta variable, futuros y cripto. La nube QuantConnect, datasets y paquetes de datos tienen condiciones separadas del motor. No presupuestar cero porque el repositorio sea Apache.',
'hardware':'CPU, 8–16 GB RAM y entorno .NET estimados para backtests modestos; almacenamiento depende de resolución. Mantener motor completo tiene más coste técnico que una biblioteca de métricas o cartera. No ejecución ni instalación.',
'experiment':'Reproducir una estrategia de asignación mensual con ledger independiente, precios sin ajustes y ajustados, activo deslistado y retraso de publicación. Antes de preferir LEAN, demostrar un fallo material que un backtest simple no pueda representar. Verificar datos y permisos fuera del motor.',
'decision':'Conservar como referencia; adoptar para una necesidad multiactivo definida. Apache-2.0 revisada. Para el mandato inicial priorizar skfolio/PyPortfolioOpt y métodos de inferencia; construir motor propio no se justifica.',
'paths':['Engine/AlgorithmManager.cs','Common/Orders/Fills/EquityFillModel.cs','Tests/Common/Orders/Fills/EquityFillModelTests.cs','LICENSE'],
},
'openbq-org/OpenBB':{
'title':'OpenBB/OpenBQ: transición real en 2026 y pérdida de vintages en una ruta concreta',
'score':[22,13,11,7,10,4,8,4],'dependencies':['openbb-core','extensiones por proveedor','Pydantic','pandas','diskcache','lxml; Python>=3.11 en proveedor FRED'],
'input':'Consulta tipada, identificadores de series, fechas y credenciales del proveedor cuando se exijan.',
'output':'Objetos normalizados con datos y metadata para terminales, APIs o análisis.',
'architecture':'Fetcher define etapas transform_query, extract/aextract_data y transform_data, además de una ruta de streaming. El proveedor FRED implementa consultas y transporte específicos; no existe una licencia universal para los datos que circulan por el framework.',
'observed':'En models/series.py se llama a series/observations y series para valores y metadata; se usa fred_get con caché/rate limiter. Antes de formar la serie se eliminan realtime_start y realtime_end, se convierten valores a float y se descartan faltantes. Esta ruta concreta devuelve una serie útil para lectura actual pero destruye columnas necesarias para auditar vintages; otras rutas FRED no se juzgan aquí. Tests del proveedor están presentes y sus casos fueron inspeccionados.',
'temporal':'La publicación oficial del 1-oct-2026 sitúa la continuidad en OpenBQ. La release v5 del 30-sep anuncia Apache-2.0 y eliminación de proveedores; el LICENSE actual confirma Apache. No combinar instrucciones de v4/AGPL y capacidades de v5. Guardar respuestas brutas de proveedor fuera de transformaciones que eliminen fechas de revisión.',
'tradeoff':'Puede ahorrar conectores cuando se usan varias fuentes. Para solo ALFRED, un cliente mínimo que preserve vintages es más claro. La continuidad institucional y compatibilidad de extensiones son riesgos a revisar tras el traspaso; actividad de repositorio no demuestra que todos los endpoints funcionen.',
'hardware':'CPU y 8–16 GB RAM estimados para consultas pequeñas; costes variables de proveedores, sin tarifas verificadas. No se probaron endpoints con clave ni el escritorio. El proveedor FRED pyproject declara 2.0.0 y Python>=3.11.',
'experiment':'Comparar respuesta original FRED con objeto normalizado para una serie revisada, con un dato faltante y dos vintages. Exigir preservación de campos en el almacén propio y documentar qué transformación pierde información. Probar tres endpoints gratuitos antes de elegirlo como base de una herramienta.',
'decision':'Investigar más/adoptar conectores seleccionados con versionado. Apache-2.0 del código actual no cubre cada proveedor. Evitar una dependencia global del terminal cuando bastan dos clientes ligeros.',
'paths':['openbb_platform/core/openbb_core/provider/abstract/fetcher.py','openbb_platform/providers/fred/openbb_fred/models/series.py','openbb_platform/providers/fred/tests/test_fred_fetchers.py','openbb_platform/providers/fred/pyproject.toml','LICENSE'],
},
'mortada/fredapi':{
'title':'fredapi + ALFRED: distinguir todas las vintages de la última conocida',
'score':[24,12,13,11,10,3,7,5],'dependencies':['pandas','urllib/XML de biblioteca estándar'],
'input':'Identificador FRED, fecha de consulta, rango temporal y clave pública de desarrollador emitida por el proveedor.',
'output':'Series actuales o filas con date, realtime_start y value para publicaciones y revisiones.',
'architecture':'Cliente pequeño con transporte XML y conversión pandas. get_series_all_releases recupera vintages; get_series_first_release agrupa por periodo y toma la primera fila. Se pueden mantener datos de observación y conocimiento por separado sin instalar un terminal financiero completo.',
'observed':'get_series_as_of_date convierte la fecha y filtra realtime_start<=as_of_date, pero retorna ese DataFrame completo: puede contener varias revisiones para el mismo periodo, pese a que el docstring describe último dato conocido. El consumidor debe ordenar por fecha de conocimiento y seleccionar última fila por date, sin eliminar el historial original. Los tests leídos usan urlopen simulado y validan consultas/errores, no se ejecutaron.',
'temporal':'ALFRED incorpora revisiones tras su publicación y puede utilizar primera disponibilidad en FRED si no se conoce la fecha original. Su granularidad de fecha no garantiza el instante intradía de llegada al mercado. Un análisis diario debe aplicar una convención conservadora y guardar acquired_at propio. Primera revisión de un periodo no equivale al último dato conocido en una fecha posterior.',
'tradeoff':'Pequeño, legible y útil para Market Regime Navigator. Requiere lógica de normalización propia y vigilancia del API; ni Apache ni la disponibilidad de un endpoint autorizan redistribuir todas las series de terceros. API FRED requiere clave; este mandato no la solicitó ni realizó descargas autenticadas.',
'hardware':'CPU y 4–8 GB RAM para decenas de series macro, estimación editorial. Coste operativo relativo bajo, sin precio externo contratado. No GPU. Los metadatos de setup.py contienen clasificadores antiguos; no son evidencia de mantenimiento reciente ni de compatibilidad de versiones.',
'experiment':'Fixture manual de un trimestre con tres publicaciones. Exigir tres vistas diferentes: first-release, todas las vintages antes de t y última vintage por periodo a t. La tercera debe cambiar solo cuando cruza una fecha de disponibilidad, y conservar la fuente/versionado.',
'decision':'Adoptar biblioteca ligera con wrapper de semántica temporal, o llamar directamente a API oficial. Apache-2.0 del código revisada; derechos por serie pendientes. Esta comprobación de cinco líneas tiene más valor para evitar sesgo que añadir un modelo predictivo complejo.',
'paths':['fredapi/fred.py','fredapi/tests/test_fred.py','setup.py','LICENSE'],
},
}

LIMITS={
'freqtrade/freqtrade':'Bot orientado a trading; aprovechar lookahead-analysis y recursive-analysis, no ejecución. Un resultado sin sesgos detectados no garantiza ausencia de todos los sesgos.',
'ranaroussi/quantstats':'Métricas y reportes no garantizan consistencia de frecuencia, benchmark, retornos frente a precios ni exactitud del histórico.',
'dcajasn/Riskfolio-Lib':'Muchas medidas de riesgo aumentan opciones de búsqueda y sensibilidad; verificar solvers, ventanas y supuestos.',
'pmorissette/bt':'Útil para rebalanceos; no modelar microestructura de perpetuos por analogía con asignación de activos.',
'kernc/backtesting.py':'Barras OHLC no revelan recorrido intrabar; AGPL exige revisar el escenario de redistribución/servicio.',
'mementum/backtrader':'Base histórica amplia; no se auditó continuidad ni compatibilidad actual; preferir componente mínimo si solo se necesitan métricas.',
'hudson-and-thames/mlfinlab':'Licencia propia ambigua, no tratar como biblioteca open source adoptable. Técnicas científicas deben buscarse en papers/alternativas compatibles.',
'ricequant/rqalpha':'Licencia comercial restringida y convenciones de mercado chino; sin ventaja evidente para fundamentales cripto.',
'pykalman/pykalman':'Licencia modificada por canal de distribución; filtrar online difiere de suavizar usando el futuro. Evaluar alternativa statsmodels.',
'hmmlearn/hmmlearn':'Estados latentes no son regímenes económicos demostrados. No confundir posterior suavizada con filtrado disponible en vivo.',
'py-why/dowhy':'Un grafo causal no prueba sus supuestos; confusión no observada y spillovers cripto limitan identificación.',
'py-why/EconML':'Efectos heterogéneos requieren identificación, overlap y controles plausibles; no convertir asociación en causalidad.',
'LemaireJean-Baptiste/eventstudy':'Calendarios y modelos de mercado de acciones requieren adaptación cripto 24/7; causalidad no se deriva de CAR.',
'abhinay/skepsis':'Proyecto alpha 0.1.0 en manifiesto. Existe golden test DSR inspeccionado, pero algoritmo completo no auditado ni benchmark independiente verificado.',
'terence-lim/financial-data-science':'Gran valor educativo en ALFRED/eventos, pero varios lectores se apoyan en datasets financieros con acceso o derechos separados.',
'bis-med-it/gingado':'Herramienta macro de un organismo público, no prueba de alpha cripto; datasets y modelos requieren validación propia.',
'cran/strucchange':'Mirror CRAN identificado; origen Codeberg inaccesible por web en esta sesión. No contarlo como implementación distinta del original.',
}
def classify_license(d):
 fs=[f for f in d['files'] if f.get('license_text')]
 if d['repo'] in SPECIAL:return (*SPECIAL[d['repo']],fs[0]['url'] if fs else None)
 text='\n'.join(f.get('license_text','') for f in fs)
 code=None
 if 'GNU AFFERO GENERAL' in text:code='AGPL-3.0'
 elif 'GNU LESSER GENERAL' in text:code='LGPL-3.0'
 elif 'GNU GENERAL PUBLIC' in text:code='GPL-2.0' if 'Version 2, June 1991' in text else 'GPL-3.0'
 elif 'Apache License' in text:code='Apache-2.0'
 elif 'BSD 2-Clause' in text:code='BSD-2-Clause'
 elif 'BSD 3-Clause' in text or ('Neither the name' in text and 'Redistribution and use' in text):code='BSD-3-Clause'
 elif 'Permission is hereby granted, free of charge' in text:code='MIT'
 elif 'Redistribution and use' in text:code='BSD; variante a revisar'
 if code:return code,('COMPATIBLE CON OBLIGACIONES' if 'GPL' in code else 'REUTILIZACIÓN POTENCIALMENTE COMPATIBLE'),fs[0]['url']
 for f in d['files']:
  m=re.search(r'^License:\s*(.+)',f.get('manifest_text',''),re.M)
  if m:return m.group(1)+' (declaración DESCRIPTION)', 'COMPATIBLE CON OBLIGACIONES',f['url']
 return None,'LICENCIA NO VERIFICADA',None

for d in OBS:
 cid='quant-'+slug(d['repo'].split('/')[-1]);d['id']=cid
 srcs=[];evs=[]
 p=d['page']; canonical=p.get('resolved_url','https://github.com/'+d['repo'])
 sid=source(canonical,d['name'],'repository',p['status'],d['commit'],'HTML original: identidad, estructura y commit; no auditoría de actividad.',p.get('sha256'));srcs.append(sid)
 evs.append(ev(cid,sid,d['description'],'descripción/estructura original','Solo confirma alcance declarado, no implementación completa.'))
 for f in d['files']:
  sid=source(f['url'],d['name']+' / '+f['path'],'license' if 'license_text' in f else 'documentation' if 'readme_text' in f else 'manifest',f['status'],d['commit'],'Archivo leído como texto; nunca importado/ejecutado.',f.get('sha256'));srcs.append(sid)
  if 'license_text' in f or f['path']=='DESCRIPTION':evs.append(ev(cid,sid,'Condiciones de licencia o declaración de paquete examinadas; ver license_code.','licencia/manifiesto','No cubre datos, servicios, modelos ni dependencias por transitividad.'))
 lic,status,lurl=classify_license(d)
 rev=REVIEWS.get(d['repo']);isdeep=bool(rev)
 di=next((z for z in DEEP if z['repo']==d['repo']),None)
 if di:
  for f in di['files']:
   sid=source(f['url'],d['name']+' / '+f['path'],'tests' if 'test' in f['path'].lower() else 'source_code',f['status'],d['commit'],f.get('error') or 'Revisión estática de rutas y fragmentos seleccionados.',f.get('sha256'));srcs.append(sid)
   if f['status']==200:evs.append(ev(cid,sid,rev['observed'] if rev and f['path']==rev['paths'][0] else 'Archivo técnico leído; estructura/interfaces/tests descritos en revisión o findings.'))
 verified='V3' if isdeep else 'V2' if lic else 'V1' if p['status']==200 else 'D0'
 score=rev['score'] if rev else [18,8,10,8,8 if status=='REUTILIZACIÓN POTENCIALMENTE COMPATIBLE' else 5 if status=='COMPATIBLE CON OBLIGACIONES' else 2,3,5,3]
 blockers=[]
 if status=='SOLO INVESTIGACIÓN / RESTRICCIONES':blockers=['Revisar condiciones exactas antes de adaptar, distribuir o comercializar; no licencia permisiva simple.']
 if lic is None:blockers=['Licencia no verificada; no copiar código hasta resolverla.']
 tests=[f['path'] for f in (di or {}).get('files',[]) if 'test' in f['path'].lower() and f['status']==200]
 row=dict(id=cid,name=d['name'],url=canonical,organization=canonical.split('/')[3] if 'github.com' in canonical else d['repo'].split('/')[0],categories=d['categories'],resource_type='mirror' if d['repo']=='cran/strucchange' else 'fork mantenido: continuidad técnica por verificar' if 'reloaded' in d['repo'] else 'biblioteca' if not d['repo'] in ['microsoft/qlib','freqtrade/freqtrade','nautechsystems/nautilus_trader','QuantConnect/Lean','openbq-org/OpenBB','ricequant/rqalpha','vnpy/vnpy'] else 'framework',description=d['description'],verification_level=verified,verified_at=DATE,version_or_commit=d['commit'],maintenance_status='No archivado según HTML; historial, releases e issues no auditados exhaustivamente' if not d['archived'] else 'Archivado según HTML',last_significant_release=None,license_code=lic,license_status=status,license_url=lurl,dependencies=rev['dependencies'] if rev else ['Consultar manifiestos enlazados; resolución transitiva no revisada'],data_inputs=rev['input'] if rev else 'Series/retornos o datos de proveedor según alcance; históricos y derechos requieren comprobación por caso.',outputs=rev['output'] if rev else d['description'],practical_use=rev['decision'] if rev else 'Componente o referencia del catálogo; validar adaptación a investigación personal antes de integrarlo.',limitations=[LIMITS.get(d['repo'], 'No se auditó la implementación completa, calidad de históricos ni compatibilidad con cripto.')]+([rev['temporal']] if rev else []),alternatives=['Ver comparaciones de quant y revisión técnica; no elegir solo por popularidad'],evidence_ids=evs,source_ids=list(dict.fromkeys(srcs)),scores=dict(zip(['utility','evidence','data','ease','license','maintenance','usability','differentiation'],score)) if verified!='D0' else None,confidence='alta para observaciones puntuales de código/licencia; media para adopción' if isdeep else 'media para identidad/licencia; baja para idoneidad integral',blockers=blockers,commercial_dependencies='Datos/servicios/solvers adicionales: revisar separadamente; ninguno contratado',maturity='Revisión estática; madurez operativa no medida',cost_relative='medio-alto' if d['repo'] in ['microsoft/qlib','nautechsystems/nautilus_trader','QuantConnect/Lean'] else 'bajo-medio; estimación editorial',adoption_mode='Adoptar biblioteca' if d['repo'] in ['bashtage/arch','deepcharles/ruptures','skfolio/skfolio','robertmartin8/PyPortfolioOpt','mortada/fredapi'] else 'Extraer una técnica' if status=='SOLO INVESTIGACIÓN / RESTRICCIONES' else 'Investigar más',deep_review_path='03_DEEP_TECHNICAL_REVIEWS/quant_'+slug(d['repo'].split('/')[-1])+'.md' if isdeep else None,tests_examined=tests or ['No se inspeccionó suite completa; no ejecutada'],documentation_reviewed=[f['url'] for f in d['files'] if 'readme_text' in f],security_review='Ninguna ejecución/instalación; no auditoría de supply chain ni vulnerabilidades',hardware=rev['hardware'] if rev else 'No medido; revisar según tamaño de datos y algoritmo.',implemented_vs_announced='Ver revisión: rutas concretas inspeccionadas' if isdeep else 'Alcance documentado; no afirmar implementación de todas las funciones',known_open_issues='No revisión sistemática de issues; pendiente',weights_license='No aplica salvo modelos externos; no hereda licencia de código',data_license='No cubierta por la licencia del código; revisión por fuente pendiente',score_rationale='Puntuación editorial conservadora. Evidencia limitada a archivos examinados; mantenimiento no recibe puntuación alta sin auditar historial.')
 candidates.append(row)
 if rev:
  lines=['# '+rev['title'],'',f"Candidato `{cid}` · observación {DATE} · nivel V3 (estático). Commit `{d['commit']}`.",'',f"La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.",'','## Capacidad y alcance','',rev['architecture'],'',f"**Entradas:** {rev['input']}\n\n**Salidas:** {rev['output']}",'','## Evidencia técnica y límites','',rev['observed'],'',rev['temporal'],'','## Adopción proporcional','',rev['tradeoff'],'',f"**Dependencias observadas:** {', '.join(rev['dependencies'])}.",'',rev['hardware'],'',f"**Licencia del código:** {lic}. Clasificación: {status}. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.",'','## Experimento de aceptación propuesto, no ejecutado','',rev['experiment'],'','## Veredicto','',rev['decision'],'',f"Puntuación editorial {sum(rev['score'])}/100: utilidad {rev['score'][0]}/25; evidencia {rev['score'][1]}/15; datos {rev['score'][2]}/15; facilidad {rev['score'][3]}/12; licencia {rev['score'][4]}/10; mantenimiento {rev['score'][5]}/8; uso diario {rev['score'][6]}/8; diferenciación {rev['score'][7]}/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.",'','## Fuentes exactas','']
  lines += ['- '+link(d,p) for p in rev['paths']]
  if d['repo']=='openbq-org/OpenBB': lines += ['- [Anuncio oficial de continuidad en OpenBQ](https://openbb.co/)','- [Release v5 y cambio de licencia](https://github.com/openbq-org/OpenBB/releases)']
  if d['repo']=='mortada/fredapi':lines += ['- [ALFRED: ayuda y determinación de vintages](https://alfred.stlouisfed.org/help)','- [API: observaciones y parámetros realtime](https://fred.stlouisfed.org/docs/api/fred/series_observations.html)']
  (ROOT/row['deep_review_path']).write_text('\n'.join(lines)+'\n',encoding='utf8')

DOCS=[
('alfred','FRED / ALFRED','https://alfred.stlouisfed.org/help','proveedor/dataset','A','Vintages de series macro; distinguir fecha del periodo, publicación y disponibilidad.', 'La documentación confirma archivo de revisiones; fechas desconocidas pueden asignarse por primera disponibilidad en FRED. API requiere clave; derechos de cada serie separados.','V1'),
('fred-md','FRED-MD','https://www.stlouisfed.org/research/economists/mccracken/fred-databases','dataset','A','Panel macro mensual con transformaciones y vintages.', 'No mezclar current.csv con evaluación histórica; vintage mensual no reproduce todos los instantes de publicación.','V1'),
('fred-qd','FRED-QD','https://www.stlouisfed.org/research/economists/mccracken/fred-databases','dataset','A','Panel macro trimestral para factores y nowcasting.', 'Frecuencia trimestral y revisiones impiden tratar cada día como observación independiente.','V1'),
('bis-api','BIS SDMX API','https://data.bis.org/help/tools','proveedor','A,M','API de datos y metadata estadística del BIS.', 'Uso exige atribución, evitar afiliación implícita y restricciones del portal; no confundir API v1/v2.','V2'),
('ecb-api','ECB Data Portal API','https://data.ecb.europa.eu/help/api/data','proveedor','A,M','Estadísticas monetarias y financieras via SDMX.', 'Documentación indexada consultada; apertura directa devolvió 503. updatedAfter informa cambios; no equivale a archivo point-in-time completo.','V1'),
('treasury-fiscal','US Treasury Fiscal Data / DTS','https://fiscaldata.treasury.gov/api-documentation/','proveedor','A,M','Datos de caja del Tesoro y deuda pública.', 'Documentación API devolvió 403. Página oficial Receipts & Outlays confirma DTS al siguiente día hábil; endpoints no probados.','D0'),
('nyfed-sofr','NY Fed Markets / SOFR','https://markets.newyorkfed.org/static/docs/markets-api.html','proveedor','A','Tasas overnight de financiación garantizada y referencias monetarias.', 'Página API accesible sin líneas extraídas; términos anunciados por fuente oficial; API no probada ni derechos completos revisados.','V1'),
('ofr-fsi','OFR Financial Stress Index','https://www.financialresearch.gov/financial-stress-index/','dataset','A,K','Índice diario de estrés financiero global.', 'Publica con retraso de dos días hábiles; aviso de corrección de feed en mayo2026 demuestra riesgo de revisiones. No es señal cripto validada.','V1'),
('nfci','Chicago Fed NFCI / ANFCI','https://www.chicagofed.org/research/data/nfci/current-data','dataset','A,K','Condiciones financieras semanales de EEUU.', 'Índice revisable; distinguir fechado de semana, publicación y descarga. Verificar vintage por fecha antes de backtest.','V1'),
('gdpnow','Atlanta Fed GDPNow','https://www.atlantafed.org/research-and-data/data/gdpnow','modelo/dataset','A','Nowcast del PIB antes de la publicación oficial.', 'Nowcast macro no anticipación de retornos; cobertura de históricos intravintage no auditada.','V1'),
('bis-gli','BIS Global Liquidity Indicators','https://data.bis.org/topics/GLI','dataset','A','Crédito a prestatarios no bancarios, incluido crédito en divisas.', 'Serie trimestral; no igualar GLI con M2 ni con liquidez negociable de un exchange.','V2'),
('dsr-paper','The Deflated Sharpe Ratio','https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf','paper','G','Corrección por selección de ensayos y no normalidad del Sharpe.', 'Requiere registrar experimentos y estimar su dependencia; no corrige datos con leakage. Versión31-jul-2014 consultada.','V1'),
('pbo-paper','The Probability of Backtest Overfitting','https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf','paper','G','CSCV para cuantificar deterioro de selección dentro/fuera de muestra.', 'PBO depende del conjunto de pruebas y de supuestos de partición; no sustituye test prospectivo. Versión27-feb-2015 consultada.','V1'),
('bsts-paper','Inferring causal impact using Bayesian structural time-series models','https://arxiv.org/abs/1506.00356','paper','J,A','Contrafactual mediante modelo estructural bayesiano de series.', 'Se leyó abstract/ficha y alcance, no se reprodujeron experimentos; exige controles no afectados y estabilidad pre/post.','V1'),
]
for id,name,u,typ,cats,desc,lim,level in DOCS:
 cid='quant-'+id;sid=source(u,name,'paper' if typ=='paper' else 'official_documentation','403' if id=='treasury-fiscal' else '503 apertura; extracto indexado leído' if id=='ecb-api' else 200,None,lim)
 extra=[]
 if id in ['bis-api','bis-gli']:extra.append(source('https://data.bis.org/help/legal','BIS permitted use','terms',200,None,'Atribución y condiciones; no dictamen jurídico.'))
 if id=='alfred':extra.append(source('https://fred.stlouisfed.org/docs/api/fred/series_observations.html','FRED series/observations','official_documentation'))
 if id=='treasury-fiscal':extra.append(source('https://home.treasury.gov/data/receipts-outlays','Treasury Receipts & Outlays','official_documentation',200,None,'Fuente oficial de descubrimiento; API pendiente.'))
 eid=ev(cid,sid,desc+' '+lim,'documentación primaria', 'No descarga completa ni reproducción de dataset/modelo.')
 candidates.append(dict(id=cid,name=name,url=u,organization='Autor/organismo original indicado en la URL',categories=cats.split(','),resource_type=typ,description=desc,verification_level=level,verified_at=DATE,version_or_commit='2014-07-31' if id=='dsr-paper' else '2015-02-27' if id=='pbo-paper' else 'arXiv:1506.00356' if id=='bsts-paper' else None,maintenance_status='Fuente primaria actual consultada; historial no auditado',last_significant_release='2026-10-29' if id=='bis-gli' else None,license_code='Condiciones BIS, no licencia de software' if id in ['bis-api','bis-gli'] else None,license_status='COMPATIBLE CON OBLIGACIONES' if id in ['bis-api','bis-gli'] else 'LICENCIA NO VERIFICADA',license_url='https://data.bis.org/help/legal' if id in ['bis-api','bis-gli'] else None,dependencies=[],data_inputs=desc,outputs=desc,practical_use='Método de validación' if typ=='paper' else 'Contexto macro para escenarios de inversión, con timestamps y revisión de permisos',limitations=[lim],alternatives=['Consultar métodos y comparaciones del área'],evidence_ids=[eid],source_ids=[sid]+extra,scores=None,confidence='media para alcance; limitada para reutilización o disponibilidad histórica',blockers=['Resolver acceso y términos específicos antes de ingesta o redistribución'] if level=='D0' else ['Permisos y timestamps por serie pendientes'] if not id in ['bis-api','bis-gli'] and typ!='paper' else [],commercial_dependencies='No contratado; algunas series subyacentes pueden tener derechos de terceros',maturity='Fuente científica/oficial; no validación de utilidad cripto',cost_relative='bajo para lectura; integración no estimada',adoption_mode='Extraer una técnica' if typ=='paper' else 'Investigar más',deep_review_path=None))

for name,u,notes in [
('OpenBB announcement','https://openbb.co/','Continuidad OpenBQ anunciada 1-oct-2026.'),
('OpenBB releases','https://github.com/openbq-org/OpenBB/releases','v5: Apache-2.0 y retirada de proveedores; no inferir capacidades de v4.'),
('BIS liquidity interpretation','https://www.bis.org/publications/global-liquidity-indicators-background-and-interpretation','Liquidez global multidimensional; no un único indicador suficiente.'),
('Codeberg strucchange','https://codeberg.org/zeileis/strucchange','Origen enlazado por mirror CRAN; inaccesible en web tool.'),
('arch comparisons','https://bashtage.github.io/arch/multiple-comparison/multiple-comparisons.html','SPA, StepM y MCS documentados.')]:source(u,name,'official_documentation','inaccesible' if 'codeberg' in u else 200,None,notes)

byrepo={d['repo']:d for d in OBS}
def rel(fr,to,kind,ref):
 d=byrepo[fr];relations.append(dict(from_id=d['id'],to_id=byrepo[to]['id'] if to in byrepo else None,to_url='https://github.com/'+to if '/' in to else to,relation=kind,evidence_source_id=uid('src-quant-',url(d,ref).replace('https://github.com/','https://raw.githubusercontent.com/').replace('/blob/','/'))))
for fr,to,kind,ref in [('robertmartin8/PyPortfolioOpt','cvxpy/cvxpy','dependencia de código declarada','pyproject.toml'),('microsoft/qlib','cvxpy/cvxpy','dependencia de código declarada','pyproject.toml'),('bashtage/arch','statsmodels/statsmodels','dependencia de código declarada','pyproject.toml'),('braverock/PortfolioAnalytics','braverock/PerformanceAnalytics','dependencia de código declarada','DESCRIPTION'),('stefan-jansen/alphalens-reloaded','quantopian/alphalens','continuación/fork: historia completa no comparada','README.md'),('stefan-jansen/empyrical-reloaded','quantopian/empyrical','continuación/fork: historia completa no comparada','README.md')]:rel(fr,to,kind,ref)
for fr,to in [('skfolio/skfolio','bashtage/arch'),('deepcharles/ruptures','mortada/fredapi'),('polakowo/vectorbt','bashtage/arch')]:relations.append(dict(from_id=byrepo[fr]['id'],to_id=byrepo[to]['id'],relation='combinación propuesta, no dependencia existente',evidence_source_id=None))

QUERIES=[('site.github.com polakowo vectorbt license commons clause','Licencia restringida verificada.'),('site.github.com microsoft qlib point in time data','PIT localizado; consulta devolvió también homónimo irrelevante descartado.'),('site.stlouisfed.org ALFRED vintage dates API','Documentación original y fechas de vintage.'),('site.github.com bashtage arch bootstrap multiple comparison','SPA/MCS y documentación original.'),('site.github.com "skfolio" walk forward CombinatorialPurgedCV','Splitter y tests seleccionados.'),('site.github.com "ruptures" "License"','BSD2 y PELT.'),('site.github.com "OpenBB" "openbq-org"','Transición2026 y v5.'),('site.github.com "mlfinpy" cross validation purged','Sin candidato cualificado suficiente; no incorporado.'),('site.github.com financial econometrics "eventstudy" Python','eventstudy y Financial Data Science.'),('site.codeberg.org quantitative finance backtesting','Cobertura escasa; origen strucchange hallado mediante mirror.'),('site.gitlab.com financial econometrics bootstrap package','Sin candidato cualificado incorporado.'),('site.github.com 量化 回测 rqalpha vnpy','Ecosistema chino; revisar restricciones RQAlpha.'),('"mlfinpy" github repository','Sin evidencia suficiente en resultados recuperados.'),('site.github.com "eventstudy" "lemairejean-baptiste"','Proyecto GPL y documentación.'),('site.bis.org data portal API SDMX statistics','API/metadatos/condiciones BIS.'),('site.data.ecb.europa.eu API SDMX data revision','updatedAfter; fallo503 en apertura posterior.'),('site.davidhbailey.com "Deflated Sharpe"','Paper fuente autor.'),('site.davidhbailey.com "Probability of Backtest Overfitting"','Paper fuente autor.'),('site.github.com "sdmx1" "sdmx"','sdmx1/khaeru identificado.'),('site.github.com "financial-data-science" "terence-lim"','Lectores ALFRED y eventos.'),('site.stlouisfed.org FRED MD QD McCracken Ng monthly database 2026','Vintages macro.'),('site.financialresearch.gov financial stress index data csv','Retraso2d y corrección feed2026.'),('site.chicagofed.org NFCI adjusted national financial conditions index data','Serie semanal.'),('site.atlantafed.org GDPNow download data model','Nowcast y modelo.'),('site.newyorkfed.org SOFR reference rates API markets data','API original, términos separados.'),('site.fiscaldata.treasury.gov API documentation daily treasury statement operating cash','DTS; API403.'),('site.arxiv.org "Inferring causal impact using Bayesian structural time-series models"','Paper autor, evidencia general no cripto.'),('site.bis.org "Global liquidity indicators" methodology credit dollar','Distinguir crédito, dinero y liquidez de negociación.')]
searchlog=[dict(id='query-quant-'+str(i+1).zfill(3),query=q,engine='web.search',date=DATE,results=n,limitations='Resultados de búsqueda utilizados para descubrimiento; ver sources para comprobación directa.') for i,(q,n) in enumerate(QUERIES)]
searchlog.append(dict(id='query-quant-029',query='Barrido HTTP GET de 51 repositorios originales; seguimiento selectivo de README/LICENSE/manifiestos/código/tests',engine='urllib biblioteca estándar, lectura estática',date=DATE,results='Todos los repositorios respondieron tras corregir pywhy/dowhy→py-why/dowhy. No API GitHub, clonación, instalaciones ni importaciones externas.',limitations='Lectura selectiva; sin auditoría completa de issues, releases o dependencias. Código temporal eliminado al consolidar.'))

dump('candidates.json',candidates);dump('sources.json',sources);dump('evidence.json',evidence);dump('relations.json',relations);dump('search_log.json',searchlog)
dump('datasets.json',[c for c in candidates if c['resource_type']=='dataset' or 'dataset' in c['resource_type']])
dump('papers.json',[c for c in candidates if c['resource_type']=='paper'])
dump('providers.json',[c for c in candidates if 'proveedor' in c['resource_type']])
dump('coverage.json',dict(candidates=len(candidates),directly_verified=sum(c['verification_level']!='D0' for c in candidates),deep_reviews=len(REVIEWS),levels={l:sum(c['verification_level']==l for c in candidates) for l in ['D0','V1','V2','V3']},queries=len(searchlog),sources=len(sources),evidence=len(evidence),external_code_executed=False,as_of=DATE))
print(json.dumps(json.loads((BASE/'coverage.json').read_text()),ensure_ascii=False))
