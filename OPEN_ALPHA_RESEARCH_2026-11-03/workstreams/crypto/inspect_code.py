import concurrent.futures,json,pathlib,sys
from collect_sources import ROOT,fetch,collect
base=json.loads((ROOT/'inspection_sources.json').read_text(encoding='utf8'))
by={x['repo']:x for x in base}
TARGETS={
'DefiLlama/dimension-adapters':['package.json','fees/hyperliquid.ts','fees/hyperliquid/index.ts','fees/hyperliquid-hlp.ts','fees/raydium/index.ts','fees/pump/index.ts','fees/uniswap/index.ts','helpers/hyperliquid.ts','adapters/types.ts'],
'hyperliquid-dex/hyperliquid-python-sdk':['pyproject.toml','hyperliquid/info.py','hyperliquid/websocket_manager.py','tests/info_test.py'],
'Polymarket/py-sdk':['pyproject.toml','src/polymarket/clients/public.py','src/polymarket/clients/_transport.py','src/polymarket/pagination.py','tests/unit/test_date_field_contract.py','tests/unit/test_public_calls_surface.py','tests/unit/test_data_retry.py'],
'ccxt/ccxt':['package.json','python/ccxt/base/exchange.py','python/ccxt/binance.py','python/ccxt/test/base/test_parse_precision.py'],
'Uniswap/protocol-fees':['src/TokenJar.sol','src/releasers/ExchangeReleaser.sol','src/releasers/Firepit.sol','test/Firepit.t.sol','foundry.toml'],
'raydium-io/raydium-sdk-V2':['package.json','src/raydium/clmm/layout.ts','src/raydium/clmm/clmm.ts','src/raydium/cpmm/cpmm.ts','test/cpmmSwapQuote.test.js'],
'paradigmxyz/cryo':['Cargo.toml','LICENSE-MIT','LICENSE-APACHE','crates/freeze/src/freeze.rs','crates/freeze/src/types/sources.rs','crates/freeze/src/types/schemas.rs'],
'ponder-sh/ponder':['packages/core/package.json','packages/core/src/sync-realtime/index.ts','packages/core/src/sync-realtime/index.test.ts'],
'graphsense/graphsense-lib':['pyproject.toml','src/graphsenselib/tagpack/confidence.py','src/graphsenselib/tagpack/tagpack_schema.py','src/graphsenselib/tagpack/schema.py'],
'bmoscon/cryptofeed':['pyproject.toml','cryptofeed/exchanges/binance.py','cryptofeed/exchanges/bybit.py','tests/unit/test_bybit_liquidations.py','tests/unit/test_binance_depth_stream.py'],
'banteg/multicall.py':['readme.md','license','pyproject.toml'],
'DefiLlama/defillama-sdk':['package.json'],
'DefiLlama/defillama-adapters':['package.json'],
'Uniswap/v4-core':['licenses/BUSL-1.1','src/PoolManager.sol'],
'Uniswap/sdks':['sdks/sdk-core/package.json'],
'pump-fun/pump-public-docs':['docs/FEE_PROGRAM_README.md','docs/PUMP_PROGRAM_README.md','docs/instructions/SWEEP_FEES.md'],
'graphprotocol/graph-node':['LICENSE-APACHE','LICENSE-MIT'],
'Co-Messi/HyperData-Terminal':['pyproject.toml','docs/DATA_INTEGRITY.md']
}
def one(item):
 repo,path=item;sha=by[repo]['sha'] or 'HEAD'
 v=fetch('https://raw.githubusercontent.com/'+repo+'/'+sha+'/'+path)
 v.update(repo=repo,path=path,commit=sha);return v
tasks=[(r,p) for r,paths in TARGETS.items() for p in paths]
out=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for x in ex.map(one,tasks):
  out.append(x)
  print(x['repo'],x['path'],x['status'],len(x.get('text','')),flush=True)
(ROOT/'inspection_code.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
