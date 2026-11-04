"""Build research inventories from inspected text and editorial evaluations."""
import json,re,pathlib,hashlib
ROOT=pathlib.Path(__file__).resolve().parent
DATE='2026-11-04'
repos=json.loads((ROOT/'inspection_sources.json').read_text(encoding='utf8'))
code=json.loads((ROOT/'inspection_code.json').read_text(encoding='utf8'))
trees=json.loads((ROOT/'tree_probes.json').read_text(encoding='utf8'))
def slug(s):return re.sub('[^a-z0-9]+','-',s.lower()).strip('-')
def cid(repo):return 'crypto-'+slug(repo)
def sid(url):return 'crypto-src-'+hashlib.sha256(url.encode()).hexdigest()[:12]
def eid(url):return 'crypto-ev-'+hashlib.sha256(url.encode()).hexdigest()[:12]
deep={
 'DefiLlama/dimension-adapters':('defillama_dimensions',[25,12,10,6,0,4,6,7]),
 'hyperliquid-dex/hyperliquid-python-sdk':('hyperliquid_sdk',[24,13,12,10,10,5,7,6]),
 'Polymarket/py-sdk':('polymarket_sdk',[20,13,10,10,10,5,6,6]),
 'ccxt/ccxt':('ccxt',[24,13,11,10,10,5,6,4]),
 'Uniswap/protocol-fees':('uniswap_protocol_fees',[25,14,9,5,6,4,5,7]),
 'raydium-io/raydium-sdk-V2':('raydium_sdk',[19,12,10,6,6,4,5,6]),
 'paradigmxyz/cryo':('cryo',[22,12,10,8,10,3,6,6]),
 'ponder-sh/ponder':('ponder',[20,13,10,6,10,4,5,6]),
 'graphsense/graphsense-lib':('graphsense',[21,12,8,6,10,4,5,7]),
 'bmoscon/cryptofeed':('cryptofeed',[19,12,10,7,6,4,5,5])}
# Specific editorial use, limitations and alternatives. No commercial returns are scored.
notes={
'ccxt/ccxt':('velas, trades, funding, OI y metadatos por exchange','objetos normalizados con payload info','Comparar fuerza relativa y estrés entre venues','Intervalos de funding, inverse/linear y contractSize siguen siendo específicos; históricos y cuotas dependen del proveedor','Pybit; conectores Binance; API directa'),
'hummingbot/hummingbot':('feeds y configuración de estrategias','conectores y motor de ejecución','Conservar como referencia de conectores','Arquitectura orientada a ejecución/HFT; coste de operación innecesario para horizonte 3–18 meses','CCXT; Cryptofeed'),
'DefiLlama/defillama-adapters':('balances on-chain y precios','TVL por protocolo y cadena','Examinar composición de TVL y dobles conteos','TVL cambia por precio; wrappers y préstamos pueden reciclar capital; licencia no localizada','RPC directo; Cryo'),
'DefiLlama/dimension-adapters':('logs, llamadas RPC, subgraphs e indexadores','fees, revenue, holders revenue, volumen','Extraer contabilidad de captura de valor versionada','Endpoints privados, fallbacks a estado actual y cambios metodológicos impiden asumir reproducibilidad histórica','reconstrucción selectiva de eventos; Dune como contraste'),
'DefiLlama/bridges-server':('logs de bridges','depósitos y retiros con txHash','Referencia de esquemas de transferencia entre cadenas','README anuncia migración de adaptadores a dimension-adapters/bridges; no adoptar repositorio anterior','DefiLlama dimension-adapters/bridges'),
'DefiLlama/yield-server':('datos on-chain de pools y recompensas','APY base y componentes incentivados','Separar rendimiento económico de subvenciones','APY retrospectivo/instantáneo no garantiza rendimiento; riesgos de smart contract y datos separados','contratos de lending; Token Terminal para contraste'),
'DefiLlama/defillama-sdk':('ABI, contratos, bloques y RPC','balances y llamadas agrupadas','Aprender patrones de multicall y normalización','Licencia no localizada; configuración y dependencias amplias para uso personal','Viem; Web3.py; Multicall.py'),
'DefiLlama/emissions-adapters':('calendarios de vesting anunciados','emisiones y unlocks pretendidos','Conservar pista referenciada en documentación oficial','Acceso directo al repositorio falló; no se verificó implementación, licencia ni cobertura','contratos de vesting; documentos originales de tokens'),
'hyperliquid-dex/hyperliquid-python-sdk':('Info API, meta, estados de cuentas, funding, libros','JSON de mercado y cuenta','Monitor de estrés de lectura pública','SDK no proporciona automáticamente archivo histórico completo ni censo de wallets; Info abre WebSocket salvo skip_ws','HTTP directo; CCXT si soporta campo específico'),
'hyperliquid-dex/node':('red Hyperliquid y binarios oficiales','bloques, fills, estados y logs locales','Referencia de qué datos serían observables con nodo','README prescribe 128GB RAM y hasta ~100GB/día de logs por defecto; motor completo no verificado como código fuente abierto','Info API y snapshots limitados'),
'Polymarket/py-sdk':('Gamma/Data/CLOB públicos','objetos tipados, páginas, precios Decimal','Incorporar mercados predictivos como evidencia contextual','Migraciones rápidas 0.x; límites de profundidad; resolución y selección sesgada de mercados; no confundir precio con probabilidad objetiva','API pública directa; SDK TypeScript'),
'Polymarket/ts-sdk':('endpoints oficiales Polymarket','cliente TypeScript y tipos compartidos','Alternativa para frontend o herramienta TS','README advierte cambios potencialmente incompatibles en releases menores0.x','Polymarket py-sdk'),
'Polymarket/py-clob-client':('API CLOB heredada','cliente anterior','Documentar migración, no nueva adopción','README dice archivado y no funcional para integraciones; licencia MIT no resuelve incompatibilidad','Polymarket py-sdk'),
'Polymarket/py-clob-client-v2':('CLOB v2','cliente transitorio','Documentar migración en dos pasos','Deprecado explícitamente; no es ya el sucesor recomendado','Polymarket py-sdk'),
'Polymarket/polymarket-subgraph':('logs de Polygon y contratos CTF','actividad, OI, PnL y fills indexados','Reconstrucción acotada de eventos y liquidación','No demuestra cobertura de nuevas versiones de contratos; operación Graph y RPC; licencia LGPL','API Data; indexador propio acotado'),
'Polymarket/ctf-exchange':('órdenes y activos CTF','contrato de liquidación legacy','Referencia de semántica histórica','README archivado; direcciones actualizadas; no usar como contrato actual','Polymarket ctf-exchange-v2'),
'Polymarket/ctf-exchange-v2':('activos CTF y órdenes firmadas','semántica de liquidación actual documentada','Mapear versiones de eventos de mercados','Sólo README/licencia inspeccionados; no verificado estado desplegado ni ejecución','Polymarket py-sdk para lecturas'),
'Uniswap/v2-core':('reservas y swaps','AMM producto constante y eventos','Modelo base de fees y actividad DEX','Volumen no equivale a demanda neta; implementación histórica no prueba feeTo activo','Uniswap protocol-fees'),
'Uniswap/v3-core':('ticks, liquidez y swaps','AMM de liquidez concentrada','Aprender contabilidad de fees por rango','Licencia BUSL contiene cambio a GPL2+ en2023; excepciones por archivo; LP fees no son UNI revenue','Uniswap protocol-fees; subgraph'),
'Uniswap/v4-core':('PoolManager y hooks','contabilidad de pools singleton','Evaluar nuevos mecanismos de actividad y fees','Hooks cambian semántica; BUSL por archivo; no asumir todo volumen uniforme ni licencia permisiva','Uniswap v3; protocol-fees'),
'Uniswap/sdks':('estado de pools y rutas','cálculos de SDKs por paquete','Bibliotecas puntuales para interpretar liquidez','Monorepo: licencia declarada de sdk-core no cubre automáticamente todos los paquetes','Viem y ABI mínimas'),
'Uniswap/v3-subgraph':('eventos v3','tablas GraphQL de pools y tokens','Obtener muestra histórica de pools sin diseñar indexador','Esquema, retraso y estado del endpoint no probados; datos de v3 no cubrenv4','Cryo; Ponder'),
'Uniswap/protocol-fees':('fees en TokenJar, resource token y threshold','releases y destino de token elegido','Auditar cadena fees→conversión→quema','Código permite verificar mecanismo, no ejecución ni tasa efectiva por pool; transfers0xdead no son necesariamente decremento totalSupply','RPC event reconciliation; DefiLlama como contraste'),
'raydium-io/raydium-sdk-V2':('cuentas Solana, programas y pools','layouts y cotizaciones','Investigar actividad por tipo de pool y fee vigente','GPL3; Token2022 y fees dinámicas complican comparación; no inferir buyback ejecutado por una constante de reparto','lectura RPC mínima; contratos Raydium'),
'raydium-io/raydium-clmm':('ticks y cuentas de pools Solana','mecánica CLMM','Referencia para validar fees y liquidez','Implementación no equivale a estado desplegado; liquidez depende del rango de precio','SDK V2; Orca con revisión de licencia'),
'raydium-io/raydium-cp-swap':('reservas y configuración de pools','AMM constante con Token22','Comprender pools sencillos y comisiones','Token con transfer fee altera importes; comprobar versión del programa','SDK V2; extracción selectiva de cuentas'),
'pump-fun/pump-public-docs':('IDL y reglas de programas Pump/PumpSwap','especificaciones de curve, fees y migración','Reconstruir embudo emisión→graduación→actividad durable','Documentación pública no prueba código íntegro abierto; fees retenidas y barridos introducen desfase; licencia no localizada','eventos Solana y metadatos de programas'),
'duneanalytics/spellbook':('tablas raw/decoded de Dune','modelos SQL y métricas compartidas','Leer transformaciones y comparar definición de volumen','BUSL con restricción Data/Analytics Platform hasta cambio indicado2027; SQL público no da derechos sobre dataset hospedado','Cryo/Ponder con datos propios'),
'duneanalytics/dune-client':('API Dune y query IDs','resultados tabulares de consultas','Cliente para contrastar métricas ya calculadas','Servicio cerrado con clave, límites y posibles costes; licencia Apache cliente separada del servicio','consulta web manual; RPC selectivo'),
'blockchain-etl/ethereum-etl':('RPC Ethereum','CSV de bloques/logs/transferencias','Alternativa Python de extracción simple','Archival RPC para ciertos históricos; CSV no resuelve reorg/provenance/entidades','Cryo; SQD'),
'blockchain-etl/bitcoin-etl':('RPC de cadenas UTXO','JSON de bloques/transacciones','Estudios de flujos BTC y UTXO','Requiere nodo/proveedor; salida transaccional no identifica beneficiario económico','Coin Metrics; GraphSense'),
'paradigmxyz/cryo':('rangos EVM, RPC y filtros','Parquet/CSV/JSON/dataframes','Obtener evidencia pequeña, reproducible y portable','README WIP; defaults agresivos para RPC; limitar tráfico; archive/traces pueden costar; caché existente no garantiza finality','Ethereum ETL; Ponder para seguimiento continuo'),
'ponder-sh/ponder':('ABI, filtros y logs EVM','Postgres y consultas SQL/GraphQL','Indexación continua acotada con rollback de reorg','Más operación que batch Parquet; reorg profundo produce error; finality local configurable','Cryo para batch; SQD para multichain'),
'subsquid/squid-sdk':('SQD Network, RPC y filtros','ETL Ethereum/Solana/Substrate','Acelerar extracción multichain selectiva','Dependencia de cobertura y condiciones de red; licencia SDK no cubre hospedaje','Ponder; Cryo'),
'graphprotocol/graph-node':('RPC, manifests y mappings','GraphQL indexado','Reutilizar subgraphs cuando encajan exactamente','Postgres/IPFS/RPC y mantenimiento altos para una herramienta personal','Ponder; API existente'),
'graphsense/graphsense-lib':('transacciones, TagPacks y taxonomías','grafos, validación y atribuciones','Extraer esquema de etiquetas con fuente y confianza','Plataforma completa requiere Cassandra/Postgres; confidence es categoría, no probabilidad calibrada','esquema mínimo propio documentado; TagPacks'),
'graphsense/graphsense-tagpacks':('fuentes públicas de atribución','etiquetas interoperables de direcciones','Arrancar diccionario trazable de entidades','MIT del repositorio no acredita exactitud ni derechos de todas las fuentes originales; direcciones no equivalen a usuarios','lista manual revisada y versionada'),
'graphsense/graphsense-tagpack-tool':('TagPacks y taxonomías','validación legacy','Referencia histórica de diseño de esquema','Archivado y migrado a graphsense-lib; no duplicar dependencia','graphsense-lib'),
'citp/BlockSci':('blockchain UTXO local','clusters y consultas analíticas','Extraer heurísticas y límites de clustering','README dice sin desarrollo activo desde2020; no recomendar instalación; CoinJoin invalida heurísticas comunes','GraphSense; métodos de clustering validados'),
'banteg/multicall.py':('llamadas ABI a un bloque','resultados de múltiples contratos','Reducir lecturas RPC de una cartera pequeña','Agrupar llamadas no valida datos; fijar block_id para consistencia','Viem multicall; Web3.py'),
'ethereum/web3.py':('RPC EVM y ABI','lecturas y decodificación Ethereum','Capa de evidencia de contratos y eventos','Repositorio redirige a ApeWorX; métodos de escritura también presentes; condiciones RPC separadas','Viem; Cryo'),
'wevm/viem':('RPC, ABI e identidad de cadena','cliente Ethereum TypeScript','Lecturas tipadas de contratos y logs','No ofrece históricos ni etiquetas por sí mismo','Web3.py; Ponder'),
'coinmetrics/api-client-python':('API Coin Metrics','dataframes de métricas cripto','Consultar series macro/on-chain documentadas','Cobertura Community frente a pago; cliente no otorga derechos sobre datos','Community Data; APIs propias de cadenas'),
'coinmetrics/data':('métricas Community','series históricas CSV','Base ligera para indicadores de red','CC BY-NC4.0 de datos; licencia separada del cliente; cambios metodológicos','datos propios on-chain'),
'tardis-dev/tardis-python':('API Tardis y tick data','replay con timestamps locales y exchange','Diseñar validación de libro y microestructura','MPL2 del cliente; históricos amplios dependen de servicio y API key; no asumir gratuitos','Binance Public Data; registrar prospectivamente'),
'bmoscon/cryptofeed':('feeds REST/WebSocket de exchanges','trades, libros, funding y liquidaciones normalizados','Monitor granular de estrés con cobertura explícita','AGPL3+atribución; liquidaciones observadas no censo; semántica side y tamaño difieren','CCXT para baja frecuencia; SDKs oficiales'),
'binance/binance-public-data':('archivos públicos de exchange','trades y velas por día/mes','Backtests y eventos con datos descargables selectivamente','Spot desde2025 usa microsegundos; publicación posterior; licencia de dataset no verificada','captura propia; Coin Metrics para agregado'),
'binance/binance-connector-python':('endpoints Binance','SDKs por producto','Ruta oficial cuando normalización pierde campo','Migración a paquetes generados; Python>=3.11; API pública no implica permisos de redistribución','CCXT'),
'bybit-exchange/pybit':('API Bybit HTTP/WebSocket','payloads de exchange','Validar fuente de liquidaciones y OI','Condiciones/retención del servicio separadas; no normaliza otros venues','Cryptofeed; CCXT'),
'gmx-io/gmx-synthetics':('collateral, oracles y posiciones','contratos de derivados on-chain','Estudiar riesgo de pools y reparto económico','BUSL indica cambioGPL2+ agosto2026; oracle/PnL de LP no son ingreso tokenholder','Drift; Hyperliquid documentación'),
'drift-labs/protocol-v2':('cuentas y mercados Solana','contratos y SDK de derivados','Estudiar liquidaciones/colateral como contraste','Monorepo y operación elevados; no verificados programas desplegados','Hyperliquid API; Pybit'),
'jito-foundation/geyser-grpc-plugin':('validador Solana','stream cuentas y slots','Referencia de capa de adquisición','Versión plugin debe coincidir con validador; demasiado pesado inicialmente','RPC filtrado; Yellowstone como servicio autorizado'),
'rpcpool/yellowstone-grpc':('Geyser Solana','streams filtrados bloques y cuentas','Captura prospectiva Solana para muestras concretas','AGPL; servidor/servicio especializado; README declara límite de reconstrucción de bloques','RPC de cuentas; SQD'),
'orca-so/whirlpools':('estado de pools Solana','AMM concentrado y SDKs','Comparar mecánica y esquema de pool','Licencia Orca propia desde2025; no tratar como Apache general; sólo investigación pendiente revisión','Raydium CLMM Apache2'),
'balancer/balancer-v3-monorepo':('pools y Vault','contratos y utilidades AMM','Extraer métodos de pools ponderados y hooks','GPL; README avisa componentes no necesariamente production-ready','DeFiPy para simulaciones'),
'aave/aave-v3-core':('préstamos y garantías','contratos v3 heredados','Semántica histórica de liquidaciones','Deprecated; licencia cambioMIT2023 no remedia obsolescencia','aave-dao/aave-v3-origin'),
'aave-dao/aave-v3-origin':('préstamos, garantías y parámetros','base actual de Aave V3','Fuente de implementación para estudiar riesgo de préstamos','Revisión limitada a README/licencia; no se auditó solvencia ni despliegues','documentación por mercado y datos de contratos'),
'snapshot-labs/snapshot.js':('espacios y mensajes de gobernanza','acceso SDK a Snapshot','Calendario de cambios y catalizadores','Voto no es ejecución; propuestas pueden no tener efecto vinculante','HTTP/GraphQL Snapshot; contratos Governor'),
'Co-Messi/HyperData-Terminal':('feeds públicos y wallets muestreadas','terminal de estrés y estados de calidad','Referencia de UX y distinción confirmado/estimado','Afirmaciones principales sólo contrastadas en docs de integridad; universo de wallets sesgado; código crítico no auditado','monitor simple CCXT/Hyperliquid'),
'0xBaro/hyperliquid':('fills/TWAP públicos Hyperliquid según autores','estudio de impacto de metaórdenes','Hipótesis: separar flujos informados de ejecución programada','Dataset completo, licencia y resultados no reproducidos; wallets no son entidades','muestra propia pequeña y event study'),
'Gaserd/prediction-markets-api':('APIs de mercados predictivos','objetos normalizados multivenue','Comparación de mercados con denominador y timestamps comunes','Cobertura declarada no probada; equivalencia semántica de eventos no automatizable sin revisión','SDK oficial Polymarket'),
'defipy-devs/defipy':('estado sintético o pool observado','primitivas y simulaciones AMM','Analizar liquidez y respuesta a shocks sin trading','Matemática exacta no modela arbitrajistas ni costes reales automáticamente','fórmulas AMM con validación contra contratos'),
'DefiLlama/peggedassets-server':('adaptadores de balances y oferta por cadena','oferta circulante stablecoins y bridges','Estudiar base monetaria cripto y redistribución entre redes','Mint/burn no prueba entrada/salida fiat; evitar duplicar tokens bridged; licencia no localizada','balances oficiales emisores y contratos')
}
sources=[]; evidence=[]; candidates=[]; rejected=[]
scores_keys=['utility','evidence','data','ease','license','maintenance','usability','differentiation']
def classify_license(repo,docs):
 license_docs=[d for d in docs if d.get('status')==200 and (re.search('license|copying',d.get('path',''),re.I))]
 txt='\n'.join(d.get('text','') for d in license_docs)
 substantial_license_docs=[d for d in license_docs if len(d.get('text',''))>80]
 url=substantial_license_docs[0]['url'] if substantial_license_docs else None
 code=None; status='LICENCIA NO VERIFICADA'
 if repo=='Uniswap/protocol-fees':
  d=next((d for d in docs if d.get('path')=='src/TokenJar.sol' and d.get('status')==200),None)
  if d: return 'AGPL-3.0-only (SPDX de rutas examinadas)','COMPATIBLE CON OBLIGACIONES',d['url']
 if repo=='Uniswap/sdks':return 'MIT declarado para sdk-core; alcance de otros paquetes no verificado',status,None
 if repo=='Uniswap/v3-core' and txt: return 'BUSL-1.1; Change License GPL-2.0-or-later desde 2023-04-01 para texto examinado','COMPATIBLE CON OBLIGACIONES',url
 if repo=='gmx-io/gmx-synthetics' and txt:return 'BUSL-1.1; Change License GPL-2.0-or-later desde 2026-08-31 para texto examinado','COMPATIBLE CON OBLIGACIONES',url
 if repo=='aave/aave-v3-core' and txt:return 'BUSL-1.1; Change License MIT desde 2023-01-27 para texto examinado','REUTILIZACIÓN POTENCIALMENTE COMPATIBLE',url
 if 'Orca License' in txt:return 'Orca License (2025), restricciones de uso','SOLO INVESTIGACIÓN / RESTRICCIONES',url
 if 'Business Source License' in txt:return 'BUSL-1.1','SOLO INVESTIGACIÓN / RESTRICCIONES',url
 if 'Attribution-NonCommercial 4.0' in txt:return 'CC-BY-NC-4.0','SOLO INVESTIGACIÓN / RESTRICCIONES',url
 if 'GNU AFFERO GENERAL PUBLIC LICENSE' in txt:
  code='AGPL-3.0-or-later + atribución adicional' if repo=='bmoscon/cryptofeed' else 'AGPL-3.0 (ver texto/versiones por archivo)'
 elif 'GNU LESSER GENERAL PUBLIC LICENSE' in txt:code='LGPL-3.0 (ver texto/versiones por archivo)'
 elif 'GNU GENERAL PUBLIC LICENSE' in txt:code='GPL-3.0 (ver texto/versiones por archivo)'
 elif 'Mozilla Public License Version 2.0' in txt:code='MPL-2.0'
 elif 'MIT License' in txt or 'The MIT License' in txt:code='MIT'
 elif 'Apache License' in txt or 'Licensed under the Apache License, Version 2.0' in txt:code='Apache-2.0'
 if repo in ['paradigmxyz/cryo','graphprotocol/graph-node'] and txt:code='MIT OR Apache-2.0'
 if code:status='COMPATIBLE CON OBLIGACIONES' if code.startswith(('AGPL','GPL','LGPL','MPL')) else 'REUTILIZACIÓN POTENCIALMENTE COMPATIBLE'
 return code,status,url
for r in repos:
 repo=r['repo']; docs=r['documents']+[x for x in code if x['repo']==repo]
 if repo not in notes:
  rejected.append({'url':'https://github.com/'+repo,'reason':'URL candidata no confirmada por contenido original suficiente; retirada del catálogo cualificado','attempts':[{'url':d['url'],'status':d['status']} for d in docs]});continue
 good=[d for d in docs if d['status']==200]
 li,ls,lu=classify_license(repo,docs)
 text='\n'.join(d.get('text','')[:2500] for d in good if 'readme' in d.get('path','').lower())
 archived=bool(re.search('no longer (maintained|actively developing|functional)|repository.*archived|repository moved|repository is DEPRECATED',text,re.I))
 deprecated=archived or repo in ['Polymarket/py-clob-client-v2','DefiLlama/bridges-server']
 level='V3' if repo in deep else ('V2' if good and (li is not None or any(d in code for d in good)) else ('V1' if good else 'D0'))
 inp,out,use,lim,alt=notes[repo]
 blockers=[]
 if ls=='LICENCIA NO VERIFICADA':blockers.append('Reutilización de código bloqueada hasta aclarar licencia; lectura y estudio no equivalen a permiso de copia.')
 if ls=='SOLO INVESTIGACIÓN / RESTRICCIONES':blockers.append('Restricciones de licencia: revisar alcance concreto antes de integrar o redistribuir.')
 if deprecated:blockers.append('Repositorio deprecado/archivado o en migración; no nueva dependencia.')
 if level=='D0':blockers.append('Existencia/capacidad no verificada directamente.')
 if repo=='hyperliquid-dex/node':blockers.append('Recursos operativos desproporcionados para primer prototipo; fuente del motor binario no verificada.')
 if repo=='DefiLlama/dimension-adapters':blockers.append('Algunas rutas dependen de LLAMA_HL_INDEXER y snapshots no disponibles públicamente; históricos no uniformemente point-in-time.')
 score=deep[repo][1] if repo in deep else [20 if 'E' in r['categories'] else 17,7 if level=='V2' else 5,8,7,10 if ls=='REUTILIZACIÓN POTENCIALMENTE COMPATIBLE' else (6 if ls=='COMPATIBLE CON OBLIGACIONES' else 0),2,5,4]
 if deprecated:score=[8,7,5,3,score[4],0,2,3]
 if level=='D0':score=None
 adoption='Adoptar biblioteca'
 if deprecated:adoption='Conservar como referencia'
 elif ls in ['LICENCIA NO VERIFICADA','SOLO INVESTIGACIÓN / RESTRICCIONES']:adoption='Extraer una técnica'
 if repo in ['hyperliquid-dex/node','0xBaro/hyperliquid','Co-Messi/HyperData-Terminal']:adoption='Investigar más'
 if repo=='Uniswap/protocol-fees':adoption='Extraer una técnica'
 if repo in ['hummingbot/hummingbot','graphprotocol/graph-node','jito-foundation/geyser-grpc-plugin']:adoption='Conservar como referencia'
 dependencies=[]
 for d in good:
  if d['path'].endswith('package.json'):
   try:dependencies+=list(json.loads(d['text']).get('dependencies',{}))[:12]
   except:pass
 # Repository scope and manifest dependencies are explicitly limited.
 ids=[];eids=[]
 for d in docs:
  s=sid(d['url']); ids.append(s)
  sources.append({'id':s,'url':d['url'],'title':repo+' / '+d['path'],'accessed_at':DATE,'source_type':'license' if re.search('license|copying',d['path'],re.I) else ('documentation' if 'readme' in d['path'].lower() else 'source_code_or_manifest'),'status':'consultado' if d['status']==200 else 'inaccesible','version_or_commit':r['sha'],'content_sha256':d.get('sha256'),'notes':'Lectura estática, sin ejecutar. '+(d.get('error','') if d['status']!=200 else '')})
  if d['status']==200:
   e=eid(d['url']);eids.append(e)
   claim=('Documentación describe: '+r['description']) if 'readme' in d['path'].lower() else ('Texto de licencia examinado; clasificación: '+str(li)) if re.search('license|copying',d['path'],re.I) else ('Ruta inspeccionada: '+d['path']+'; alcance técnico detallado en revisión o notas, sin ejecución')
   evidence.append({'id':e,'candidate_id':cid(repo),'source_id':s,'claim':claim,'evidence_type':'static_source_inspection','limitations':'No demuestra comportamiento en ejecución, exactitud de datos ni estado desplegado. Hash identifica contenido recuperado; fecha de commit no recuperada en todos los casos.'})
 resource='biblioteca/SDK'
 if 'adapters' in repo or repo.startswith('DefiLlama/'):resource='adaptadores/infraestructura de referencia'
 if repo in ['coinmetrics/data','graphsense/graphsense-tagpacks','binance/binance-public-data']:resource='dataset o catálogo de datos'
 if repo in ['Uniswap/v2-core','Uniswap/v3-core','Uniswap/v4-core','Uniswap/protocol-fees','raydium-io/raydium-clmm','raydium-io/raydium-cp-swap','Polymarket/ctf-exchange','Polymarket/ctf-exchange-v2','gmx-io/gmx-synthetics','drift-labs/protocol-v2','orca-so/whirlpools','balancer/balancer-v3-monorepo','aave/aave-v3-core','aave-dao/aave-v3-origin']:resource='implementación de protocolo; despliegue no validado'
 if repo=='pump-fun/pump-public-docs':resource='documentación e IDL; no equivale a motor completo abierto'
 if repo=='hyperliquid-dex/node':resource='documentación y distribución de binarios; código del motor no verificado'
 if repo=='0xBaro/hyperliquid':resource='investigación/paper; dataset y reproducción no verificados'
 if repo=='Co-Messi/HyperData-Terminal':resource='herramienta funcional declarada; ejecución no comprobada'
 candidates.append({'id':cid(repo),'name':r['name'],'url':'https://github.com/'+('ApeWorX/web3.py' if repo=='ethereum/web3.py' else repo),'original_url':'https://github.com/'+repo,'organization':repo.split('/')[0],'categories':r['categories'],'resource_type':resource,'description':r['description'],'languages':None,'verification_level':level,'verified_at':DATE if good else None,'version_or_commit':r['sha'],'maintenance_status':'Deprecado/archivado/migración documentada' if deprecated else 'Repositorio accesible; fecha de última actividad significativa no comprobada sistemáticamente','last_significant_release':None,'license_code':li,'license_status':ls,'license_url':lu,'license_data':'No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset','dependencies':list(dict.fromkeys(dependencies)) or ['No inventariadas exhaustivamente; véase revisión cuando exista'],'data_inputs':[inp],'outputs':[out],'practical_use':use,'limitations':[lim],'alternatives':alt.split('; '),'evidence_ids':eids,'source_ids':list(dict.fromkeys(ids)),'scores':dict(zip(scores_keys,score)) if score else None,'total_score':sum(score) if score else None,'score_basis':'Juicio editorial de utilidad personal; evidencia de revisión estática. Mantenimiento limitado a señales documentadas, no estrellas. Bloqueantes prevalecen sobre puntos.','confidence':'Alta sobre rutas estáticas; media sobre adopción' if level=='V3' else ('Media documental' if level=='V2' else 'Baja/incompleta'),'blockers':blockers,'commercial_dependencies':['RPC/exchange/indexador: condiciones e históricos separados de código; no se contrataron servicios'],'maturity':'Estática, sin prueba operacional local','cost_relative':'Alto para nodo/indexación global; bajo para lecturas acotadas' if repo in ['hyperliquid-dex/node','graphprotocol/graph-node','graphsense/graphsense-lib'] else 'Bajo a medio; dominado por datos/retención, no medido','adoption_mode':adoption,'deep_review_path':'03_DEEP_TECHNICAL_REVIEWS/crypto_'+deep[repo][0]+'.md' if repo in deep else None,'implemented_vs_announced':'Sólo rutas de código señaladas en revisión V3 inspeccionadas; resto de funciones se consideran declaradas por documentación','test_coverage':'No medida. Archivos de tests seleccionados cuando constan en fuentes. Ningún test externo ejecutado.','historical_data_quality':'No descargado dataset completo ni comprobada integridad; revisar temporalidad, truncamiento y revisiones.'})
sources=list({x['id']:x for x in sources}.values()); evidence=list({x['id']:x for x in evidence}.values())
relations=[]
def rel(a,b,kind,path=None):
 r=next((r for r in repos if r['repo']==a),None)
 url='https://raw.githubusercontent.com/'+a+'/'+r['sha']+'/'+(path or 'README.md') if r and r['sha'] else 'https://github.com/'+a
 relations.append({'from_id':cid(a),'to_id':cid(b),'relation':kind,'evidence_source_id':sid(url)})
rel('Polymarket/py-clob-client','Polymarket/py-sdk','sucesor oficial indicado en README')
rel('Polymarket/py-clob-client-v2','Polymarket/py-sdk','migración indicada en README')
rel('Polymarket/ctf-exchange','Polymarket/ctf-exchange-v2','sucesor oficial indicado en README')
rel('graphsense/graphsense-tagpack-tool','graphsense/graphsense-lib','migración de repositorio indicada en README')
rel('aave/aave-v3-core','aave-dao/aave-v3-origin','sucesor indicado en README')
rel('DefiLlama/bridges-server','DefiLlama/dimension-adapters','migración a subdirectorio bridges indicada en README')
rel('DefiLlama/dimension-adapters','DefiLlama/defillama-sdk','dependencia de código declarada en manifest','package.json')
rel('DefiLlama/defillama-adapters','DefiLlama/defillama-sdk','dependencia de código declarada en manifest','package.json')
rel('graphsense/graphsense-lib','graphsense/graphsense-tagpacks','compatibilidad de esquema; no requiere importar todo dataset','src/graphsenselib/tagpack/tagpack_schema.py')
rel('Uniswap/protocol-fees','Uniswap/v4-core','importación de Currency en ruta inspeccionada','src/TokenJar.sol')
rel('raydium-io/raydium-sdk-V2','raydium-io/raydium-clmm','cliente y protocolo relacionado; contraste propuesto','src/raydium/clmm/layout.ts')
for name,data in [('candidates',candidates),('sources',sources),('evidence',evidence),('relations',relations),('rejected_candidates',rejected)]:
 (ROOT/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'candidates':len(candidates),'verified':sum(x['verification_level']!='D0' for x in candidates),'deep':sum(x['verification_level']=='V3' for x in candidates),'sources':len(sources),'evidence':len(evidence),'rejected_urls':len(rejected)},ensure_ascii=True))
