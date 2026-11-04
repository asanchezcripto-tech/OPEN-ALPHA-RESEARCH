"""Research-only HTTP/text metadata collector. Never imports fetched software."""
import concurrent.futures, datetime, hashlib, json, pathlib, re, subprocess, urllib.request, urllib.error
ROOT=pathlib.Path(__file__).resolve().parent
REPOS=[
('ccxt/ccxt','CCXT','B,C,M','Biblioteca de normalización de datos y acceso a exchanges'),
('hummingbot/hummingbot','Hummingbot','B,C,G','Framework de negociación; referencia de conectores, no prioridad de ejecución'),
('DefiLlama/defillama-adapters','DefiLlama TVL adapters','D,E,M','Adaptadores de TVL y composición de activos'),
('DefiLlama/dimension-adapters','DefiLlama dimension adapters','C,E,M','Adaptadores de fees, revenue, volumen y dimensiones de protocolos'),
('DefiLlama/stablecoins-server','DefiLlama stablecoins server','A,D,M','Seguimiento de oferta de stablecoins'),
('DefiLlama/bridges-server','DefiLlama bridges server','D,M','Seguimiento de actividad de bridges'),
('DefiLlama/yield-server','DefiLlama yield server','E,N,M','Adaptadores y datos de rendimientos DeFi'),
('DefiLlama/defillama-sdk','DefiLlama SDK','D,E,M','Utilidades de llamadas on-chain y balances'),
('DefiLlama/emissions-adapters','DefiLlama emissions adapters','E,F,N','Adaptadores de emisiones y desbloqueos'),
('DefiLlama/defillama-server','DefiLlama server','D,E,M','Backend de publicación de agregados'),
('hyperliquid-dex/hyperliquid-python-sdk','Hyperliquid Python SDK','B,C,D,M','Cliente oficial para datos y órdenes Hyperliquid'),
('hyperliquid-dex/node','Hyperliquid node','D,M','Distribución y documentación de nodo Hyperliquid'),
('Polymarket/py-sdk','Polymarket unified Python SDK','B,J,N,M','Cliente oficial unificado de datos y cuenta'),
('Polymarket/ts-sdk','Polymarket unified TypeScript SDK','B,J,N,M','Cliente oficial unificado TypeScript'),
('Polymarket/py-clob-client','Polymarket legacy Python CLOB','B,N,M','SDK heredado archivado; candidato para descarte'),
('Polymarket/py-clob-client-v2','Polymarket Python CLOB v2','B,N,M','SDK de transición deprecado; revisar migración'),
('Polymarket/polymarket-subgraph','Polymarket subgraphs','D,N,M','Indexación de eventos de mercados predictivos'),
('Polymarket/ctf-exchange','Polymarket CTF Exchange','D,N','Contratos de liquidación de mercados'),
('Uniswap/v2-core','Uniswap v2 core','D,E','Contratos AMM de producto constante'),
('Uniswap/v3-core','Uniswap v3 core','D,E','Contratos de liquidez concentrada'),
('Uniswap/v4-core','Uniswap v4 core','D,E','Contratos AMM con hooks y contabilidad singleton'),
('Uniswap/sdks','Uniswap SDKs','D,E,M','Herramientas para interpretar pools y cotizaciones'),
('Uniswap/v3-subgraph','Uniswap v3 subgraph','D,E,M','Indexador GraphQL de pools y swaps'),
('Uniswap/protocol-fees','Uniswap protocol fees','E,N','Contratos de captura de fees y quema de UNI'),
('raydium-io/raydium-sdk-V2','Raydium SDK V2','D,E,M','SDK de pools Raydium y datos Solana'),
('raydium-io/raydium-clmm','Raydium CLMM','D,E','Contratos de liquidez concentrada'),
('raydium-io/raydium-cp-swap','Raydium CPMM','D,E','AMM de producto constante con Token2022'),
('pump-fun/pump-public-docs','Pump public docs','D,E,N','Documentación e IDLs de bonding curve, migración y fees'),
('duneanalytics/spellbook','Dune Spellbook','D,E,M','Modelos SQL públicos de datos blockchain'),
('duneanalytics/dune-client','Dune Python client','D,E,M','Cliente de servicio analítico Dune'),
('blockchain-etl/ethereum-etl','Ethereum ETL','D,M','Extracción tabular de bloques, logs y transferencias EVM'),
('blockchain-etl/bitcoin-etl','Bitcoin ETL','D,M','Extracción de bloques y transacciones Bitcoin'),
('paradigmxyz/cryo','Cryo','D,M','Extracción EVM hacia formatos analíticos'),
('ponder-sh/ponder','Ponder','D,M','Indexación TypeScript de eventos EVM con gestión de reorg'),
('subsquid/squid-sdk','SQD Squid SDK','D,M','ETL multichain con datos de SQD Network'),
('graphprotocol/graph-node','Graph Node','D,M','Indexador de subgraphs para consultas GraphQL'),
('graphsense/graphsense-lib','GraphSense lib','D,N','Análisis de transacciones y agrupación de direcciones'),
('graphsense/graphsense-tagpacks','GraphSense TagPacks','D,N','Atribuciones públicas con fuente y esquema'),
('graphsense/graphsense-tagpack-tool','GraphSense TagPack Tool','D,M','Validación y gestión de atribuciones de wallets'),
('citp/BlockSci','BlockSci','D,N','Análisis de blockchain UTXO y heurísticas de clusters'),
('banteg/abiregistry','ABI Registry','D,M','Registro de ABI para decodificar contratos'),
('banteg/multicall.py','Multicall.py','D,M','Lecturas agrupadas de contratos EVM'),
('ethereum/web3.py','Web3.py','D,M','Cliente RPC Ethereum Python'),
('wevm/viem','Viem','D,M','Cliente Ethereum TypeScript tipado'),
('nansen-ai/evmchain-data','Nansen EVM chain data','D,M','Recurso candidato de datos EVM; verificar disponibilidad'),
('coinmetrics/api-client-python','Coin Metrics Python client','A,B,D,M','Cliente de métricas de red y mercado'),
('coinmetrics/data','Coin Metrics Community Data','A,B,D','Datos comunitarios de métricas cripto'),
('tardis-dev/tardis-python','Tardis Python','B,C,M','Cliente de datos históricos de mercado y replay'),
('bmoscon/cryptofeed','Cryptofeed','B,C,M','Normalización de feeds WebSocket y libros de órdenes'),
('binance/binance-public-data','Binance Public Data','B,C,G','Archivos de operaciones y velas públicos'),
('binance/binance-connector-python','Binance Python connectors','B,C,M','Clientes oficiales REST y WebSocket'),
('bybit-exchange/pybit','Pybit','B,C,M','Cliente oficial Bybit Python'),
('deribit/deribit-api-clients','Deribit API clients','C,M','Clientes de API de derivados y opciones'),
('gmx-io/gmx-synthetics','GMX Synthetics','C,D,E','Contratos de derivados on-chain'),
('drift-labs/protocol-v2','Drift protocol v2','C,D,E','Protocolo de derivados Solana'),
('jito-foundation/geyser-grpc-plugin','Geyser gRPC plugin','D,M','Streaming de datos Solana'),
('rpcpool/yellowstone-grpc','Yellowstone gRPC','D,M','Streaming Solana con filtros'),
('orca-so/whirlpools','Orca Whirlpools','D,E','AMM de liquidez concentrada en Solana'),
('balancer/balancer-v3-monorepo','Balancer v3','D,E','Contratos AMM y pools composables'),
('aave/aave-v3-core','Aave v3 core','C,D,E','Contratos de préstamos y liquidaciones'),
('snapshot-labs/snapshot.js','Snapshot.js','E,N','Cliente de propuestas y votación de gobernanza'),
('Co-Messi/HyperData-Terminal','HyperData Terminal','B,C,L','Terminal de datos públicos y estrés Hyperliquid; revisar estimaciones'),
('0xBaro/hyperliquid','Hyperliquid market-impact research','C,G','Investigación de metaórdenes y dataset Hyperliquid'),
('Gaserd/prediction-markets-api','Prediction markets API','B,N,M','Normalización multi-venue de mercados predictivos'),
('defipy-devs/defipy','DeFiPy','D,E,G','Simulación de AMMs para investigación de liquidez')
]
def fetch(url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'OpenAlpha-Research/1.0 (+static source inspection)'})
        with urllib.request.urlopen(req,timeout=20) as f:
            data=f.read(1500000)
            return {'url':url,'status':f.status,'final_url':f.url,'sha256':hashlib.sha256(data).hexdigest(),'text':data.decode('utf-8','replace')}
    except Exception as e:
        return {'url':url,'status':'failed','error':str(e)}
def collect(item):
    repo,name,cats,desc=item
    try:
        p=subprocess.run(['git','ls-remote','https://github.com/'+repo+'.git','HEAD'],capture_output=True,text=True,timeout=30)
        sha=p.stdout.split()[0] if p.returncode==0 and p.stdout.strip() else None
    except Exception:
        sha=None
    ref=sha or 'HEAD'
    base='https://raw.githubusercontent.com/'+repo+'/'+ref+'/'
    docs=[]
    for path in ['README.md','README.rst','README']:
        r=fetch(base+path);r['path']=path;docs.append(r)
        if r['status']==200:break
    for path in ['LICENSE','LICENSE.md','LICENSE.txt','COPYING']:
        r=fetch(base+path);r['path']=path;docs.append(r)
        if r['status']==200:break
    return {'repo':repo,'name':name,'categories':cats.split(','),'description':desc,'sha':sha,'documents':docs}
if __name__=='__main__':
    out=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for v in ex.map(collect,REPOS):
            out.append(v)
            (ROOT/'inspection_sources.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
            print(v['repo'],v['sha'],[(d['path'],d['status']) for d in v['documents']],flush=True)
    print('TOTAL',len(out))
