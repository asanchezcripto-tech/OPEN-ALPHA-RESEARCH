# Catálogo de recursos

288 entradas diferenciadas; 285 con consulta original suficiente para el nivel declarado. No son 288 herramientas listas para uso. Bibliotecas, pesos, datasets y papers son recursos distintos; se relacionan sin confundir sus derechos.

D0: descubierto sin comprobación suficiente. V1: existencia/función o card/abstract. V2: documentación más licencia o archivo técnico. V3: ruta crítica y pruebas/dependencias examinadas estáticamente. Ningún nivel implica ejecución ni rentabilidad.

Una sola entrada por recurso; la categoría principal organiza la tabla, el resto se conserva en JSON/CSV. FRED-MD y FRED-QD comparten página pero son datasets distintos. Los inventarios de bibliotecas/modelos/etc. son vistas del catálogo, no candidatos que deban sumarse de nuevo.

## A — Macro

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `quant-openbb` [OpenBB / OpenBQ](https://github.com/openbq-org/OpenBB) · [revisión](03_DEEP_TECHNICAL_REVIEWS/quant_openbb.md) | framework / V3 | Plataforma de acceso uniforme a proveedores financieros. | Apache-2.0 | 79 / Investigar más |
| `quant-statsmodels` [statsmodels](https://github.com/statsmodels/statsmodels) | biblioteca / V2 | Modelos econométricos, estados espaciales y series temporales. | BSD-3-Clause | 63 / Investigar más |
| `quant-ruptures` [ruptures](https://github.com/deepcharles/ruptures) · [revisión](03_DEEP_TECHNICAL_REVIEWS/quant_ruptures.md) | biblioteca / V3 | Detección offline de cambios estructurales. | BSD-2-Clause | 88 / Adoptar biblioteca |
| `quant-linearmodels` [linearmodels](https://github.com/bashtage/linearmodels) | biblioteca / V2 | Paneles, variables instrumentales y estimación econométrica. | NCSA | 63 / Investigar más |
| `quant-hmmlearn` [hmmlearn](https://github.com/hmmlearn/hmmlearn) | biblioteca / V2 | Modelos ocultos de Markov para estados latentes. | BSD-3-Clause | 63 / Investigar más |
| `quant-pykalman` [pykalman](https://github.com/pykalman/pykalman) | biblioteca / V2 | Filtros y suavizadores de Kalman. | BSD modificado: restricciones de canales de distribución | 57 / Extraer una técnica |
| `quant-quantmod` [quantmod](https://github.com/joshuaulrich/quantmod) | biblioteca / V2 | Modelización y adquisición de series financieras en R. | GPL-3.0 | 60 / Investigar más |
| `quant-strucchange` [strucchange (mirror CRAN)](https://github.com/cran/strucchange) | mirror / V2 | Tests de cambio estructural; mirror de paquete original. | GPL-2 / GPL-3 (declaración DESCRIPTION) | 60 / Investigar más |
| `quant-pandas-datareader` [pandas-datareader](https://github.com/pydata/pandas-datareader) | biblioteca / V2 | Conectores para fuentes económicas y financieras. | BSD-3-Clause | 63 / Investigar más |
| `quant-fredapi` [fredapi](https://github.com/mortada/fredapi) · [revisión](03_DEEP_TECHNICAL_REVIEWS/quant_fredapi.md) | biblioteca / V3 | Cliente FRED/ALFRED con datos históricos por vintage. | Apache-2.0 | 85 / Adoptar biblioteca |
| `quant-sdmx` [sdmx1](https://github.com/khaeru/sdmx) | biblioteca / V2 | Cliente y objetos SDMX para estadísticas oficiales. | Apache-2.0 | 63 / Investigar más |
| `quant-pandasdmx` [pandaSDMX](https://github.com/dr-leo/pandaSDMX) | biblioteca / V2 | Cliente SDMX para bancos centrales y agencias. | Apache-2.0 | 63 / Investigar más |
| `quant-financial-data-science` [Financial Data Science](https://github.com/terence-lim/financial-data-science) | biblioteca / V2 | Herramientas de investigación, lectores macro y estudios de eventos. | MIT | 63 / Investigar más |
| `quant-quantecon-py` [QuantEcon.py](https://github.com/QuantEcon/QuantEcon.py) | biblioteca / V2 | Métodos computacionales económicos, cadenas de Markov y simulación. | MIT | 63 / Investigar más |
| `quant-gingado` [gingado](https://github.com/bis-med-it/gingado) | biblioteca / V2 | Caja de herramientas de ML para economía del BIS. | Apache-2.0 | 63 / Investigar más |
| `quant-alfred` [FRED / ALFRED](https://alfred.stlouisfed.org/help) | proveedor/dataset / V1 | Vintages de series macro; distinguir fecha del periodo, publicación y disponibilidad. | No verificada | sin puntuación / Investigar más |
| `quant-fred-md` [FRED-MD](https://www.stlouisfed.org/research/economists/mccracken/fred-databases) | dataset / V1 | Panel macro mensual con transformaciones y vintages. | No verificada | sin puntuación / Investigar más |
| `quant-fred-qd` [FRED-QD](https://www.stlouisfed.org/research/economists/mccracken/fred-databases) | dataset / V1 | Panel macro trimestral para factores y nowcasting. | No verificada | sin puntuación / Investigar más |
| `quant-bis-api` [BIS SDMX API](https://data.bis.org/help/tools) | proveedor / V2 | API de datos y metadata estadística del BIS. | Condiciones BIS, no licencia de software | sin puntuación / Investigar más |
| `quant-ecb-api` [ECB Data Portal API](https://data.ecb.europa.eu/help/api/data) | proveedor / D0 | Estadísticas monetarias y financieras via SDMX. | No verificada | sin puntuación / Investigar más |
| `quant-treasury-fiscal` [US Treasury Fiscal Data / DTS](https://fiscaldata.treasury.gov/api-documentation/) | proveedor / D0 | Datos de caja del Tesoro y deuda pública. | No verificada | sin puntuación / Investigar más |
| `quant-nyfed-sofr` [NY Fed Markets / SOFR](https://markets.newyorkfed.org/static/docs/markets-api.html) | proveedor / V1 | Tasas overnight de financiación garantizada y referencias monetarias. | No verificada | sin puntuación / Investigar más |
| `quant-ofr-fsi` [OFR Financial Stress Index](https://www.financialresearch.gov/financial-stress-index/) | dataset / V1 | Índice diario de estrés financiero global. | No verificada | sin puntuación / Investigar más |
| `quant-nfci` [Chicago Fed NFCI / ANFCI](https://www.chicagofed.org/research/data/nfci/current-data) | dataset / V1 | Condiciones financieras semanales de EEUU. | No verificada | sin puntuación / Investigar más |
| `quant-gdpnow` [Atlanta Fed GDPNow](https://www.atlantafed.org/research-and-data/data/gdpnow) | modelo/dataset / V1 | Nowcast del PIB antes de la publicación oficial. | No verificada | sin puntuación / Investigar más |
| `quant-bis-gli` [BIS Global Liquidity Indicators](https://data.bis.org/topics/GLI) | dataset / V2 | Crédito a prestatarios no bancarios, incluido crédito en divisas. | Condiciones BIS, no licencia de software | sin puntuación / Investigar más |
| `crypto-coinmetrics-api-client-python` [Coin Metrics Python client](https://github.com/coinmetrics/api-client-python) | biblioteca/SDK / V2 | Cliente de métricas de red y mercado | MIT | 60 / Adoptar biblioteca |
| `crypto-coinmetrics-data` [Coin Metrics Community Data](https://github.com/coinmetrics/data) | dataset o catálogo de datos / V2 | Datos comunitarios de métricas cripto | CC-BY-NC-4.0 | 50 / Extraer una técnica |
| `crypto-defillama-peggedassets-server` [DefiLlama pegged assets](https://github.com/DefiLlama/peggedassets-server) | adaptadores/infraestructura de referencia / V1 | Adaptadores y servidor de oferta de stablecoins | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | 48 / Extraer una técnica |
## B — Mercado cripto

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `infra-provider-hyperliquid-api` [Hyperliquid: API pública](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api) | proveedor/API o servicio comercial de referencia / V1 | Contexto/info de mercados; diferenciar snapshot actual, histórico y retención. | Términos del servicio/dataset pendientes de caso concreto | sin puntuación / Conservar como referencia |
| `quant-ttr` [TTR](https://github.com/joshuaulrich/TTR) | biblioteca / V2 | Funciones técnicas de series en R. | GPL-2.0 | 60 / Investigar más |
| `crypto-ccxt-ccxt` [CCXT](https://github.com/ccxt/ccxt) · [revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_ccxt.md) | biblioteca/SDK / V3 | Biblioteca de normalización de datos y acceso a exchanges | MIT | 83 / Adoptar biblioteca |
| `crypto-hummingbot-hummingbot` [Hummingbot](https://github.com/hummingbot/hummingbot) | biblioteca/SDK / V2 | Framework de negociación; referencia de conectores, no prioridad de ejecución | Apache-2.0 | 60 / Conservar como referencia |
| `crypto-hyperliquid-dex-hyperliquid-python-sdk` [Hyperliquid Python SDK](https://github.com/hyperliquid-dex/hyperliquid-python-sdk) · [revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_hyperliquid_sdk.md) | biblioteca/SDK / V3 | Cliente oficial para datos y órdenes Hyperliquid | MIT | 87 / Adoptar biblioteca |
| `crypto-polymarket-py-sdk` [Polymarket unified Python SDK](https://github.com/Polymarket/py-sdk) · [revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_polymarket_sdk.md) | biblioteca/SDK / V3 | Cliente oficial unificado de datos y cuenta | MIT | 80 / Adoptar biblioteca |
| `crypto-polymarket-ts-sdk` [Polymarket unified TypeScript SDK](https://github.com/Polymarket/ts-sdk) | biblioteca/SDK / V2 | Cliente oficial unificado TypeScript | MIT | 60 / Adoptar biblioteca |
| `crypto-polymarket-py-clob-client` [Polymarket legacy Python CLOB](https://github.com/Polymarket/py-clob-client) | biblioteca/SDK / V2 | SDK heredado archivado; candidato para descarte | MIT | 38 / Conservar como referencia |
| `crypto-polymarket-py-clob-client-v2` [Polymarket Python CLOB v2](https://github.com/Polymarket/py-clob-client-v2) | biblioteca/SDK / V2 | SDK de transición deprecado; revisar migración | MIT | 38 / Conservar como referencia |
| `crypto-tardis-dev-tardis-python` [Tardis Python](https://github.com/tardis-dev/tardis-python) | biblioteca/SDK / V2 | Cliente de datos históricos de mercado y replay | MPL-2.0 | 56 / Adoptar biblioteca |
| `crypto-bmoscon-cryptofeed` [Cryptofeed](https://github.com/bmoscon/cryptofeed) · [revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_cryptofeed.md) | biblioteca/SDK / V3 | Normalización de feeds WebSocket y libros de órdenes | AGPL-3.0-or-later + atribución adicional | 68 / Adoptar biblioteca |
| `crypto-binance-binance-public-data` [Binance Public Data](https://github.com/binance/binance-public-data) | dataset o catálogo de datos / V1 | Archivos de operaciones y velas públicos | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | 48 / Extraer una técnica |
| `crypto-binance-binance-connector-python` [Binance Python connectors](https://github.com/binance/binance-connector-python) | biblioteca/SDK / V2 | Clientes oficiales REST y WebSocket | MIT | 60 / Adoptar biblioteca |
| `crypto-bybit-exchange-pybit` [Pybit](https://github.com/bybit-exchange/pybit) | biblioteca/SDK / V2 | Cliente oficial Bybit Python | MIT | 60 / Adoptar biblioteca |
| `crypto-co-messi-hyperdata-terminal` [HyperData Terminal](https://github.com/Co-Messi/HyperData-Terminal) | herramienta funcional declarada; ejecución no comprobada / V2 | Terminal de datos públicos y estrés Hyperliquid; revisar estimaciones | Apache-2.0 | 60 / Investigar más |
| `crypto-gaserd-prediction-markets-api` [Prediction markets API](https://github.com/Gaserd/prediction-markets-api) | biblioteca/SDK / V2 | Normalización multi-venue de mercados predictivos | MIT | 60 / Adoptar biblioteca |
## C — Derivados

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `crypto-defillama-dimension-adapters` [DefiLlama dimension adapters](https://github.com/DefiLlama/dimension-adapters) · [revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_defillama_dimensions.md) | adaptadores/infraestructura de referencia / V3 | Adaptadores de fees, revenue, volumen y dimensiones de protocolos | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | 70 / Extraer una técnica |
| `crypto-gmx-io-gmx-synthetics` [GMX Synthetics](https://github.com/gmx-io/gmx-synthetics) | implementación de protocolo; despliegue no validado / V2 | Contratos de derivados on-chain | BUSL-1.1; Change License GPL-2.0-or-later desde 2026-08-31 para texto examinado | 59 / Adoptar biblioteca |
| `crypto-drift-labs-protocol-v2` [Drift protocol v2](https://github.com/drift-labs/protocol-v2) | implementación de protocolo; despliegue no validado / V2 | Protocolo de derivados Solana | Apache-2.0 | 63 / Adoptar biblioteca |
| `crypto-aave-aave-v3-core` [Aave v3 core](https://github.com/aave/aave-v3-core) | implementación de protocolo; despliegue no validado / V2 | Contratos de préstamos y liquidaciones | BUSL-1.1; Change License MIT desde 2023-01-27 para texto examinado | 38 / Conservar como referencia |
| `crypto-0xbaro-hyperliquid` [Hyperliquid market-impact research](https://github.com/0xBaro/hyperliquid) | investigación/paper; dataset y reproducción no verificados / V1 | Investigación de metaórdenes y dataset Hyperliquid | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | 48 / Investigar más |
| `crypto-aave-dao-aave-v3-origin` [Aave V3 Origin](https://github.com/aave-dao/aave-v3-origin) | implementación de protocolo; despliegue no validado / V2 | Repositorio sucesor de Aave V3 core | BUSL-1.1; Change Date 2027-03-06 o fecha ENS anterior a MIT; Additional Use Grant restrictiva en texto examinado | 53 / Extraer una técnica |
## D — On-chain

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `infra-networkx` [networkx](https://github.com/networkx/networkx) | biblioteca / V2 | Análisis de grafos; las direcciones no equivalen a entidades. | BSD-3-Clause | 66 / Investigar más |
| `infra-igraph` [python-igraph](https://github.com/igraph/python-igraph) | biblioteca / V2 | Bindings Python para analítica de grafos. | GPL-2.0 | 66 / Investigar más |
| `infra-provider-dune-service` [Dune Analytics API](https://docs.dune.com/api-reference/overview/introduction) | proveedor/API o servicio comercial de referencia / V1 | Servicio de consultas/resultados: referencia funcional cerrada; clientes/Spellbook tienen permisos diferentes. | Términos del servicio/dataset pendientes de caso concreto | sin puntuación / Conservar como referencia |
| `crypto-defillama-defillama-adapters` [DefiLlama TVL adapters](https://github.com/DefiLlama/defillama-adapters) | adaptadores/infraestructura de referencia / V2 | Adaptadores de TVL y composición de activos | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | 53 / Extraer una técnica |
| `crypto-defillama-bridges-server` [DefiLlama bridges server](https://github.com/DefiLlama/bridges-server) | adaptadores/infraestructura de referencia / V1 | Seguimiento de actividad de bridges | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | 28 / Conservar como referencia |
| `crypto-defillama-defillama-sdk` [DefiLlama SDK](https://github.com/DefiLlama/defillama-sdk) | adaptadores/infraestructura de referencia / V2 | Utilidades de llamadas on-chain y balances | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | 53 / Extraer una técnica |
| `crypto-hyperliquid-dex-node` [Hyperliquid node](https://github.com/hyperliquid-dex/node) | documentación y distribución de binarios; código del motor no verificado / V2 | Distribución y documentación de nodo Hyperliquid | Apache-2.0 del repositorio examinado; disponibilidad/licencia del código del motor no comprobada | 60 / Investigar más |
| `crypto-polymarket-polymarket-subgraph` [Polymarket subgraphs](https://github.com/Polymarket/polymarket-subgraph) | biblioteca/SDK / V2 | Indexación de eventos de mercados predictivos | LGPL-3.0 (ver texto/versiones por archivo) | 56 / Adoptar biblioteca |
| `crypto-polymarket-ctf-exchange` [Polymarket CTF Exchange](https://github.com/Polymarket/ctf-exchange) | implementación de protocolo; despliegue no validado / V2 | Contratos de liquidación de mercados | MIT | 38 / Conservar como referencia |
| `crypto-uniswap-v2-core` [Uniswap v2 core](https://github.com/Uniswap/v2-core) | implementación de protocolo; despliegue no validado / V2 | Contratos AMM de producto constante | GPL-3.0 (ver texto/versiones por archivo) | 59 / Adoptar biblioteca |
| `crypto-uniswap-v3-core` [Uniswap v3 core](https://github.com/Uniswap/v3-core) | implementación de protocolo; despliegue no validado / V2 | Contratos de liquidez concentrada | BUSL-1.1; Change License GPL-2.0-or-later desde 2023-04-01 para texto examinado | 59 / Adoptar biblioteca |
| `crypto-uniswap-v4-core` [Uniswap v4 core](https://github.com/Uniswap/v4-core) | implementación de protocolo; despliegue no validado / V2 | Contratos AMM con hooks y contabilidad singleton | BUSL-1.1; Change Date 2027-06-15 a MIT, con posibles modificaciones ENS; revisar versión | 53 / Extraer una técnica |
| `crypto-uniswap-sdks` [Uniswap SDKs](https://github.com/Uniswap/sdks) | biblioteca/SDK / V2 | Herramientas para interpretar pools y cotizaciones | MIT declarado para sdk-core; alcance de otros paquetes no verificado | 53 / Extraer una técnica |
| `crypto-uniswap-v3-subgraph` [Uniswap v3 subgraph](https://github.com/Uniswap/v3-subgraph) | biblioteca/SDK / V2 | Indexador GraphQL de pools y swaps | GPL-3.0 (ver texto/versiones por archivo) | 59 / Adoptar biblioteca |
| `crypto-raydium-io-raydium-sdk-v2` [Raydium SDK V2](https://github.com/raydium-io/raydium-sdk-V2) · [revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_raydium_sdk.md) | biblioteca/SDK / V3 | SDK de pools Raydium y datos Solana | GPL-3.0 (ver texto/versiones por archivo) | 68 / Adoptar biblioteca |
| `crypto-raydium-io-raydium-clmm` [Raydium CLMM](https://github.com/raydium-io/raydium-clmm) | implementación de protocolo; despliegue no validado / V2 | Contratos de liquidez concentrada | Apache-2.0 | 63 / Adoptar biblioteca |
| `crypto-raydium-io-raydium-cp-swap` [Raydium CPMM](https://github.com/raydium-io/raydium-cp-swap) | implementación de protocolo; despliegue no validado / V2 | AMM de producto constante con Token2022 | Apache-2.0 | 63 / Adoptar biblioteca |
| `crypto-pump-fun-pump-public-docs` [Pump public docs](https://github.com/pump-fun/pump-public-docs) | documentación e IDL; no equivale a motor completo abierto / V2 | Documentación e IDLs de bonding curve, migración y fees | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | 53 / Extraer una técnica |
| `crypto-duneanalytics-spellbook` [Dune Spellbook](https://github.com/duneanalytics/spellbook) | biblioteca/SDK / V2 | Modelos SQL públicos de datos blockchain | BUSL-1.1; Change Date 2027-03-03 a GPL-3.0-or-later; restricción de Data/Analytics Platform | 53 / Extraer una técnica |
| `crypto-duneanalytics-dune-client` [Dune Python client](https://github.com/duneanalytics/dune-client) | biblioteca/SDK / V2 | Cliente de servicio analítico Dune | Apache-2.0 | 63 / Adoptar biblioteca |
| `crypto-blockchain-etl-ethereum-etl` [Ethereum ETL](https://github.com/blockchain-etl/ethereum-etl) | biblioteca/SDK / V2 | Extracción tabular de bloques, logs y transferencias EVM | MIT | 60 / Adoptar biblioteca |
| `crypto-blockchain-etl-bitcoin-etl` [Bitcoin ETL](https://github.com/blockchain-etl/bitcoin-etl) | biblioteca/SDK / V2 | Extracción de bloques y transacciones Bitcoin | MIT | 60 / Adoptar biblioteca |
| `crypto-paradigmxyz-cryo` [Cryo](https://github.com/paradigmxyz/cryo) · [revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_cryo.md) | biblioteca/SDK / V3 | Extracción EVM hacia formatos analíticos | MIT OR Apache-2.0 | 77 / Adoptar biblioteca |
| `crypto-ponder-sh-ponder` [Ponder](https://github.com/ponder-sh/ponder) · [revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_ponder.md) | biblioteca/SDK / V3 | Indexación TypeScript de eventos EVM con gestión de reorg | MIT | 74 / Adoptar biblioteca |
| `crypto-subsquid-squid-sdk` [SQD Squid SDK](https://github.com/subsquid/squid-sdk) | biblioteca/SDK / V2 | ETL multichain con datos de SQD Network | Apache-2.0 | 60 / Adoptar biblioteca |
| `crypto-graphprotocol-graph-node` [Graph Node](https://github.com/graphprotocol/graph-node) | biblioteca/SDK / V2 | Indexador de subgraphs para consultas GraphQL | MIT OR Apache-2.0 | 60 / Conservar como referencia |
| `crypto-graphsense-graphsense-lib` [GraphSense lib](https://github.com/graphsense/graphsense-lib) · [revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_graphsense.md) | biblioteca/SDK / V3 | Análisis de transacciones y agrupación de direcciones | MIT | 73 / Adoptar biblioteca |
| `crypto-graphsense-graphsense-tagpacks` [GraphSense TagPacks](https://github.com/graphsense/graphsense-tagpacks) | dataset o catálogo de datos / V2 | Atribuciones públicas con fuente y esquema | MIT | 60 / Adoptar biblioteca |
| `crypto-graphsense-graphsense-tagpack-tool` [GraphSense TagPack Tool](https://github.com/graphsense/graphsense-tagpack-tool) | biblioteca/SDK / V2 | Validación y gestión de atribuciones de wallets | MIT | 38 / Conservar como referencia |
| `crypto-citp-blocksci` [BlockSci](https://github.com/citp/BlockSci) | biblioteca/SDK / V2 | Análisis de blockchain UTXO y heurísticas de clusters | GPL-3.0 (ver texto/versiones por archivo) | 34 / Conservar como referencia |
| `crypto-banteg-multicall-py` [Multicall.py](https://github.com/banteg/multicall.py) | biblioteca/SDK / V2 | Lecturas agrupadas de contratos EVM | MIT | 60 / Adoptar biblioteca |
| `crypto-ethereum-web3-py` [Web3.py](https://github.com/ApeWorX/web3.py) | biblioteca/SDK / V2 | Cliente RPC Ethereum Python | MIT | 60 / Adoptar biblioteca |
| `crypto-wevm-viem` [Viem](https://github.com/wevm/viem) | biblioteca/SDK / V2 | Cliente Ethereum TypeScript tipado | MIT | 60 / Adoptar biblioteca |
| `crypto-jito-foundation-geyser-grpc-plugin` [Geyser gRPC plugin](https://github.com/jito-foundation/geyser-grpc-plugin) | biblioteca/SDK / V2 | Streaming de datos Solana | Apache-2.0 | 60 / Conservar como referencia |
| `crypto-rpcpool-yellowstone-grpc` [Yellowstone gRPC](https://github.com/rpcpool/yellowstone-grpc) | biblioteca/SDK / V2 | Streaming Solana con filtros | AGPL-3.0 (ver texto/versiones por archivo) | 56 / Adoptar biblioteca |
| `crypto-orca-so-whirlpools` [Orca Whirlpools](https://github.com/orca-so/whirlpools) | implementación de protocolo; despliegue no validado / V2 | AMM de liquidez concentrada en Solana | Orca License (2025), restricciones de uso | 53 / Extraer una técnica |
| `crypto-balancer-balancer-v3-monorepo` [Balancer v3](https://github.com/balancer/balancer-v3-monorepo) | implementación de protocolo; despliegue no validado / V2 | Contratos AMM y pools composables | GPL-3.0 (ver texto/versiones por archivo) | 59 / Adoptar biblioteca |
| `crypto-defipy-devs-defipy` [DeFiPy](https://github.com/defipy-devs/defipy) | biblioteca/SDK / V2 | Simulación de AMMs para investigación de liquidez | Apache-2.0 | 63 / Adoptar biblioteca |
| `crypto-polymarket-ctf-exchange-v2` [Polymarket CTF Exchange V2](https://github.com/Polymarket/ctf-exchange-v2) | implementación de protocolo; despliegue no validado / V2 | Sucesor oficial de contratos de liquidacion | BUSL-1.1; sin Additional Use Grant; Change Date 2030-03-27 a MIT en texto examinado | 50 / Extraer una técnica |
| `crypto-paper-blocksci` [BlockSci: Design and applications of a blockchain analysis platform](https://www.usenix.org/conference/usenixsecurity20/presentation/kalodner) | paper / línea de investigación / V1 | Arquitectura orientada a análisis blockchain y representación eficiente | No verificada | sin puntuación / Investigar más |
| `crypto-paper-hyperliquid-paths` [Price Trajectories, Impact and Sunshine Trading](https://raw.githubusercontent.com/0xBaro/hyperliquid/c4d3743c65923c6e921f731d753e580961d2328b/README.md) | paper / línea de investigación / V1 | Pista para estudiar trayectoria de precios e impacto con datos de mercado públicos | No verificada | sin puntuación / Investigar más |
## E — Fundamentales y valoración

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `infra-provider-defillama-api` [DefiLlama: servicio y metodología](https://docs.llama.fi/) | proveedor/API o servicio comercial de referencia / V1 | Agregados DeFi; permisos y acceso del servicio se revisan aparte de adaptadores. | Términos del servicio/dataset pendientes de caso concreto | sin puntuación / Conservar como referencia |
| `infra-provider-tokenterminal-service` [Token Terminal: métricas](https://tokenterminal.com/explorer/metrics/tokenholder_revenue) | proveedor/API o servicio comercial de referencia / V1 | Referencia comercial de definiciones; no implica datos/código abiertos ni validación independiente. | Términos del servicio/dataset pendientes de caso concreto | sin puntuación / Conservar como referencia |
| `crypto-defillama-yield-server` [DefiLlama yield server](https://github.com/DefiLlama/yield-server) | adaptadores/infraestructura de referencia / V1 | Adaptadores y datos de rendimientos DeFi | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | 51 / Extraer una técnica |
| `crypto-defillama-emissions-adapters` [DefiLlama emissions adapters](https://github.com/DefiLlama/emissions-adapters) | adaptadores/infraestructura de referencia / D0 | Adaptadores de emisiones y desbloqueos | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | sin puntuación / Extraer una técnica |
| `crypto-uniswap-protocol-fees` [Uniswap protocol fees](https://github.com/Uniswap/protocol-fees) · [revisión](03_DEEP_TECHNICAL_REVIEWS/crypto_uniswap_protocol_fees.md) | implementación de protocolo; despliegue no validado / V3 | Contratos de captura de fees y quema de UNI | AGPL-3.0-only (SPDX de rutas examinadas) | 75 / Extraer una técnica |
| `crypto-snapshot-labs-snapshot-js` [Snapshot.js](https://github.com/snapshot-labs/snapshot.js) | biblioteca/SDK / V2 | Cliente de propuestas y votación de gobernanza | MIT | 63 / Adoptar biblioteca |
## G — Validación cuantitativa

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `quant-qlib` [Qlib](https://github.com/microsoft/qlib) · [revisión](03_DEEP_TECHNICAL_REVIEWS/quant_qlib.md) | framework / V3 | Framework de investigación cuantitativa y modelos con datos point-in-time. | MIT | 76 / Investigar más |
| `quant-freqtrade` [Freqtrade](https://github.com/freqtrade/freqtrade) | framework / V2 | Backtesting cripto, análisis de sesgos y motor de trading; ejecución fuera de alcance. | GPL-3.0 | 60 / Investigar más |
| `quant-nautilus-trader` [NautilusTrader](https://github.com/nautechsystems/nautilus_trader) · [revisión](03_DEEP_TECHNICAL_REVIEWS/quant_nautilus-trader.md) | framework / V3 | Motor por eventos con instrumentos y simulación de ejecución. | LGPL-3.0 | 66 / Investigar más |
| `quant-lean` [LEAN](https://github.com/QuantConnect/Lean) · [revisión](03_DEEP_TECHNICAL_REVIEWS/quant_lean.md) | framework / V3 | Motor multiactivo de backtest y ejecución con modelos de realidad. | Apache-2.0 | 69 / Investigar más |
| `quant-vectorbt` [vectorbt](https://github.com/polakowo/vectorbt) · [revisión](03_DEEP_TECHNICAL_REVIEWS/quant_vectorbt.md) | biblioteca / V3 | Simulación vectorizada y barridos de parámetros. | Apache-2.0 WITH Commons-Clause | 73 / Extraer una técnica |
| `quant-arch` [arch](https://github.com/bashtage/arch) · [revisión](03_DEEP_TECHNICAL_REVIEWS/quant_arch.md) | biblioteca / V3 | Volatilidad condicional, bootstrap, cointegración y comparación múltiple. | NCSA | 89 / Adoptar biblioteca |
| `quant-skfolio` [skfolio](https://github.com/skfolio/skfolio) · [revisión](03_DEEP_TECHNICAL_REVIEWS/quant_skfolio.md) | biblioteca / V3 | Selección y validación de carteras con interfaz scikit-learn. | BSD-3-Clause | 85 / Adoptar biblioteca |
| `quant-bt` [bt](https://github.com/pmorissette/bt) | biblioteca / V2 | Backtesting de estrategias de asignación de activos. | MIT | 63 / Investigar más |
| `quant-backtesting-py` [Backtesting.py](https://github.com/kernc/backtesting.py) | biblioteca / V2 | Motor compacto de backtesting sobre barras. | AGPL-3.0 | 60 / Investigar más |
| `quant-backtrader` [Backtrader](https://github.com/mementum/backtrader) | biblioteca / V2 | Framework histórico de backtesting por eventos. | GPL-3.0 | 60 / Investigar más |
| `quant-zipline-reloaded` [Zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded) | fork/continuación; mantenimiento no auditado / V2 | Continuación de Zipline con bundles, calendarios y datos de acciones. | Apache-2.0 | 63 / Investigar más |
| `quant-alphalens-reloaded` [Alphalens-reloaded](https://github.com/stefan-jansen/alphalens-reloaded) | fork/continuación; mantenimiento no auditado / V2 | Continuación de análisis de factores transversales. | Apache-2.0 | 63 / Investigar más |
| `quant-alphalens` [Alphalens original](https://github.com/quantopian/alphalens) | biblioteca / V2 | Análisis original de factores; contrastar con forks mantenidos. | Apache-2.0 | 63 / Investigar más |
| `quant-mlfinlab` [MLFinLab](https://github.com/hudson-and-thames/mlfinlab) | biblioteca / V2 | Implementaciones de machine learning financiero; verificar acceso y licencia. | Acuerdo propietario Hudson & Thames; referencias internas ambiguas a ArbitrageLab | 57 / Extraer una técnica |
| `quant-arbitragelab` [ArbitrageLab](https://github.com/hudson-and-thames/arbitragelab) | biblioteca / V2 | Métodos de cointegración y estrategias relativas. | BSD-3-Clause | 63 / Investigar más |
| `quant-rqalpha` [RQAlpha](https://github.com/ricequant/rqalpha) | framework / V2 | Framework chino de backtesting y trading modular. | Apache-2.0 modificado: uso comercial sujeto a autorización | 57 / Extraer una técnica |
| `quant-vnpy` [VeighNa / vn.py](https://github.com/vnpy/vnpy) | framework / V2 | Framework chino de trading y extensiones cuantitativas. | MIT | 63 / Investigar más |
| `quant-quantstrat` [quantstrat](https://github.com/braverock/quantstrat) | biblioteca / V2 | Framework R de estrategias y reglas sobre datos financieros. | GPL-3 (declaración DESCRIPTION) | 60 / Investigar más |
| `quant-skepsis` [skepsis](https://github.com/abhinay/skepsis) | biblioteca / V2 | Validación y auditoría estadística de backtests; candidato reciente. | Apache-2.0 | 63 / Investigar más |
| `quant-dsr-paper` [The Deflated Sharpe Ratio](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf) | paper / V1 | Corrección por selección de ensayos y no normalidad del Sharpe. | No verificada | sin puntuación / Extraer una técnica |
| `quant-pbo-paper` [The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf) | paper / V1 | CSCV para cuantificar deterioro de selección dentro/fuera de muestra. | No verificada | sin puntuación / Extraer una técnica |
| `AI-gift-eval` [GIFT-Eval](https://github.com/SalesforceAIResearch/gift-eval) | benchmark/repositorio de investigación / V2 | Reutilizar protocolo de evaluación y separación pretrain/test | Apache-2.0 | 70 / Investigar más |
| `AI-fev` [Forecast Evaluation (fev)](https://github.com/autogluon/fev) · [revisión](03_DEEP_TECHNICAL_REVIEWS/ai_fev.md) | biblioteca/framework / V3 | Definir tareas con cortes, covariables y fingerprints reproducibles | Apache-2.0 | 86 / Adoptar biblioteca |
| `AI-PAPER-2606-27100` [Pretrained Time-Series Foundation Models for Financial Return Forecasting](https://arxiv.org/abs/2606.27100v1) | paper / línea de investigación / V1 | Comparación rolling-origin en cinco acciones; mejoras frente random walk pequeñas/poco generalizadas según autores. | No verificada | sin puntuación / Investigar más |
| `AI-PAPER-2510-13654` [Rethinking Evaluation in the Era of Time Series Foundation Models: (Un)known Information Leakage Challenges](https://arxiv.org/abs/2510.13654v3) | paper / línea de investigación / V1 | Distingue solapamiento de muestras y solapamiento temporal de series correlacionadas. | No verificada | sin puntuación / Investigar más |
| `AI-PAPER-2608-03259` [FinVerse: Toward More Realistic Evaluation for Financial Time-Series Forecasting](https://arxiv.org/abs/2608.03259v3) | paper / línea de investigación / V1 | Evaluación financiera por significado económico, ranking transversal y cartera; orden de modelos varía frente benchmark genérico. | No verificada | sin puntuación / Investigar más |
## H — IA y modelos

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `AI-chronos` [Chronos forecasting library](https://github.com/amazon-science/chronos-forecasting) · [revisión](03_DEEP_TECHNICAL_REVIEWS/ai_chronos.md) | biblioteca/framework / V3 | Forecast probabilístico con covariables y comparación zero-shot | Apache-2.0 | 78 / Investigar más |
| `AI-timesfm` [TimesFM library](https://github.com/google-research/timesfm) · [revisión](03_DEEP_TECHNICAL_REVIEWS/ai_timesfm.md) | biblioteca/framework / V3 | Estudiar forecasting multivariable y comparar generaciones de modelos | Apache-2.0 | 63 / Investigar más |
| `AI-uni2ts` [Uni2TS / Moirai](https://github.com/SalesforceAIResearch/uni2ts) · [revisión](03_DEEP_TECHNICAL_REVIEWS/ai_uni2ts.md) | biblioteca/framework / V3 | Aprovechar tratamiento de máscaras y adaptación de horizontes | Apache-2.0 | 62 / Investigar más |
| `AI-autogluon` [AutoGluon](https://github.com/autogluon/autogluon) | biblioteca/framework / V2 | Comparar modelos tabulares y temporales dentro de un experimento | Apache-2.0 | 67 / Investigar más |
| `AI-gluonts` [GluonTS](https://github.com/awslabs/gluonts) | biblioteca/framework / V2 | Modelos probabilísticos y representaciones de forecasts | Apache-2.0 | 66 / Investigar más |
| `AI-statsforecast` [StatsForecast](https://github.com/Nixtla/statsforecast) | biblioteca/framework / V2 | Baselines ARIMA/ETS/Theta y naive económicos en CPU | Apache-2.0 | 81 / Adoptar biblioteca |
| `AI-mlforecast` [MLForecast](https://github.com/Nixtla/mlforecast) · [revisión](03_DEEP_TECHNICAL_REVIEWS/ai_mlforecast.md) | biblioteca/framework / V3 | Lags y boosting con validación temporal reproducible | Apache-2.0 | 84 / Adoptar biblioteca |
| `AI-neuralforecast` [NeuralForecast](https://github.com/Nixtla/neuralforecast) | biblioteca/framework / V2 | Comparación de NBEATS/NHITS/TFT y otras arquitecturas | Apache-2.0 | 64 / Investigar más |
| `AI-darts` [Darts](https://github.com/unit8co/darts) | biblioteca/framework / V2 | Interfaz común para forecasting, backtesting y anomalías | Apache-2.0 | 70 / Investigar más |
| `AI-sktime` [sktime](https://github.com/sktime/sktime) | biblioteca/framework / V2 | Pipelines y validación temporal con múltiples estimadores | BSD-3-Clause | 68 / Investigar más |
| `AI-pytorch-forecasting` [PyTorch Forecasting](https://github.com/sktime/pytorch-forecasting) | biblioteca/framework / V2 | TFT y redes con interfaces de entrenamiento | MIT | 60 / Investigar más |
| `AI-timeseries-library` [Time-Series-Library](https://github.com/thuml/Time-Series-Library) | biblioteca/framework / V2 | Extraer implementaciones comparables de modelos académicos | MIT | 55 / Investigar más |
| `AI-lag-llama` [Lag-Llama](https://github.com/time-series-foundation-models/lag-llama) | biblioteca/framework / V2 | Estudiar pronósticos probabilísticos con lags | Apache-2.0 | 55 / Investigar más |
| `AI-moment` [MOMENT](https://github.com/moment-timeseries-foundation-model/moment) | biblioteca/framework / V2 | Explorar representación general para clasificación/anomalías | MIT | 62 / Investigar más |
| `AI-granite-tsfm` [IBM Granite TSFM](https://github.com/ibm-granite/granite-tsfm) | biblioteca/framework / V2 | Explorar forecasters compactos y ajuste ligero | Apache-2.0 | 69 / Investigar más |
| `AI-tirex` [TiRex](https://github.com/NX-AI/tirex) | biblioteca/framework / V2 | Referencia xLSTM de forecasting | NXAI Community License | 59 / Investigar más |
| `AI-tabpfn` [TabPFN](https://github.com/PriorLabs/TabPFN) | biblioteca/framework / V2 | Baseline para pequeños paneles de características | Apache-2.0 | 61 / Investigar más |
| `AI-lightgbm` [LightGBM](https://github.com/lightgbm-org/LightGBM) | biblioteca/framework / V2 | Baseline de árboles para factores y clasificación de escenarios | MIT | 77 / Investigar más |
| `AI-catboost` [CatBoost](https://github.com/catboost/catboost) | biblioteca/framework / V2 | Comparar árboles con variables categóricas de protocolos | Apache-2.0 | 73 / Investigar más |
| `AI-xgboost` [XGBoost](https://github.com/dmlc/xgboost) | biblioteca/framework / V2 | Baseline de boosting ampliamente reutilizable | Apache-2.0 | 73 / Investigar más |
| `AI-river` [River](https://github.com/online-ml/river) · [revisión](03_DEEP_TECHNICAL_REVIEWS/ai_river.md) | biblioteca/framework / V3 | Detectar drift en residuos y métricas de calidad de datos | BSD-3-Clause | 84 / Adoptar biblioteca |
| `AI-pyod` [PyOD](https://github.com/yzhao062/pyod) | biblioteca/framework / V2 | Comparar detectores de anomalías multivariadas | BSD-2-Clause | 74 / Investigar más |
| `AI-merlion` [Merlion](https://github.com/salesforce/Merlion) | biblioteca/framework / V2 | Extraer arquitectura de ensembles de anomalías | BSD-3-Clause | 57 / Conservar como referencia |
| `AI-adtk` [ADTK](https://github.com/arundo/adtk) | biblioteca/framework / V2 | Detectores interpretables basados en reglas y agregadores | MPL-2.0 | 66 / Investigar más |
| `AI-alibi-detect` [Alibi Detect](https://github.com/SeldonIO/alibi-detect) | biblioteca/framework / V2 | Referencia de drift multivariable y pruebas de distribución | BUSL-1.1 | 61 / Investigar más |
| `AI-evidently` [Evidently](https://github.com/evidentlyai/evidently) | biblioteca/framework / V2 | Informes de calidad y drift de entradas/salidas | Apache-2.0 | 74 / Investigar más |
| `AI-finbert` [FinBERT code](https://github.com/ProsusAI/finBERT) · [revisión](03_DEEP_TECHNICAL_REVIEWS/ai_finbert.md) | biblioteca/framework / V3 | Baseline de sentimiento y estudio de truncado/calibración | Apache-2.0 | 60 / Investigar más |
| `AI-finqa` [FinQA code / benchmark repository](https://github.com/czyssrs/FinQA) | benchmark/repositorio de investigación / V2 | Evaluar aritmética verificable sobre informes | MIT | 65 / Investigar más |
| `AI-tatqa` [TAT-QA](https://github.com/NExTplusplus/TAT-QA) | benchmark/repositorio de investigación / V2 | Evaluar combinación de tabla y texto financiero | MIT | 64 / Investigar más |
| `AI-financebench` [FinanceBench repository](https://github.com/patronus-ai/financebench) | benchmark/repositorio de investigación / V1 | Referencia de preguntas con evidencias documentales | No verificada | 58 / Investigar más |
| `AI-convfinqa` [ConvFinQA](https://github.com/czyssrs/ConvFinQA) | benchmark/repositorio de investigación / V2 | Pruebas de razonamiento numérico conversacional | MIT | 60 / Investigar más |
| `AI-tsfel` [TSFEL](https://github.com/fraunhoferportugal/tsfel) | biblioteca/framework / V2 | Features estadísticas/temporales/espectrales de bajo coste | BSD-3-Clause | 74 / Investigar más |
| `AI-tsfresh` [TSFresh](https://github.com/blue-yonder/tsfresh) | biblioteca/framework / V2 | Extracción y selección estadística de features | MIT | 69 / Investigar más |
| `AI-aeon` [aeon](https://github.com/aeon-toolkit/aeon) | biblioteca/framework / V2 | Clasificación, clustering y anomalías de series con interfaces comunes | BSD-3-Clause | 67 / Investigar más |
| `AI-tirex2` [TiRex-2](https://github.com/NX-AI/tirex-2) | biblioteca/framework / V2 | Alternativa actual multivariable al TiRex original | Apache-2.0 | 68 / Investigar más |
| `AI-model-amazon-chronos-2` [amazon/chronos-2](https://huggingface.co/amazon/chronos-2) | model / V2 | Modelo 120M para forecasting multivariable con covariables y cuantiles. | apache-2.0 | 67 / Investigar más |
| `AI-model-amazon-chronos-bolt-small` [amazon/chronos-bolt-small](https://huggingface.co/amazon/chronos-bolt-small) | model / V2 | Baseline compacto de forecasting univariado por patches. | apache-2.0 | 67 / Investigar más |
| `AI-model-google-timesfm-3-0-pytorch` [google/timesfm-3.0-pytorch](https://huggingface.co/google/timesfm-3.0-pytorch) | model / V2 | Pesos multivariables TimesFM3, licencia no comercial/no producción. | TimesFM Non-Commercial License v1.0 | 62 / Investigar más |
| `AI-model-google-timesfm-2-5-200m-pytorch` [google/timesfm-2.5-200m-pytorch](https://huggingface.co/google/timesfm-2.5-200m-pytorch) | model / V2 | Checkpoint200M anterior con declaración Apache2.0. | apache-2.0 | 67 / Investigar más |
| `AI-model-salesforce-moirai-2-0-r-small` [Salesforce/moirai-2.0-R-small](https://huggingface.co/Salesforce/moirai-2.0-R-small) | model / V2 | Modelo 11.4M, cuantiles, máscaras de observación; CC-BY-NC. | cc-by-nc-4.0 | 62 / Investigar más |
| `AI-model-salesforce-moirai-1-1-r-small` [Salesforce/moirai-1.1-R-small](https://huggingface.co/Salesforce/moirai-1.1-R-small) | model / V2 | Checkpoint Moirai anterior útil como comparación; CC-BY-NC. | cc-by-nc-4.0 | 62 / Investigar más |
| `AI-model-prosusai-finbert` [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) | model / V2 | Pesos de sentimiento financiero inglés; CC-BY-NC-SA4.0. | cc-by-nc-sa-4.0 | 62 / Investigar más |
| `AI-model-baai-bge-m3` [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) | model / V2 | Recuperación multilingüe densa, sparse y multivector. | mit | 67 / Investigar más |
| `AI-model-baai-bge-small-en-v1-5` [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) | model / V2 | Embeddings compactos para documentos en inglés. | mit | 67 / Investigar más |
| `AI-model-ibm-granite-granite-timeseries-ttm-r2` [ibm-granite/granite-timeseries-ttm-r2](https://huggingface.co/ibm-granite/granite-timeseries-ttm-r2) | model / V2 | Familia compacta TinyTimeMixer; variante por frecuencia/horizonte. | apache-2.0 | 67 / Investigar más |
| `AI-model-nx-ai-tirex` [NX-AI/TiRex](https://huggingface.co/NX-AI/TiRex) | model / V1 | Pesos35M xLSTM con licencia comunitaria. | NXAI Community License | 62 / Investigar más |
| `AI-dataset-patronusai-financebench` [PatronusAI/financebench](https://huggingface.co/datasets/PatronusAI/financebench) | dataset / V1 | Muestra pública150 casos QA con evidencia; CC-BY-NC4.0. | cc-by-nc-4.0 | 62 / Investigar más |
| `AI-dataset-takala-financial-phrasebank` [takala/financial_phrasebank](https://huggingface.co/datasets/takala/financial_phrasebank) | dataset / V1 | Frases financieras inglesas con etiquetas de sentimiento y acuerdo. | cc-by-nc-sa-3.0 | 62 / Investigar más |
| `AI-dataset-ibm-finqa` [ibm/finqa](https://huggingface.co/datasets/ibm/finqa) | dataset / V1 | Distribución HF de preguntas aritméticas financieras; declarar origen/versiones. | cc-by-4.0 | 62 / Investigar más |
| `AI-dataset-salesforce-gifteval` [Salesforce/GiftEval](https://huggingface.co/datasets/Salesforce/GiftEval) | dataset / V1 | Benchmark heterogéneo de forecasting; validar permisos por componente. | apache-2.0 | 67 / Investigar más |
| `AI-dataset-salesforce-giftevalpretrain` [Salesforce/GiftEvalPretrain](https://huggingface.co/datasets/Salesforce/GiftEvalPretrain) | dataset / V1 | Colección de preentrenamiento de gran tamaño; no descargar para este fin. | apache-2.0 | 67 / Investigar más |
| `AI-dataset-autogluon-chronos-datasets` [autogluon/chronos_datasets](https://huggingface.co/datasets/autogluon/chronos_datasets) | dataset / V1 | Colección multi-origen con licencias por configuración. | other | 62 / Investigar más |
| `AI-dataset-autogluon-fev-datasets` [autogluon/fev_datasets](https://huggingface.co/datasets/autogluon/fev_datasets) | dataset / V1 | Colección para tareas de forecasting con condiciones por subdataset. | other | 62 / Investigar más |
## I — Agentes

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `AI-fingpt` [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) · [revisión](03_DEEP_TECHNICAL_REVIEWS/ai_fingpt.md) | biblioteca/framework / V3 | Extraer tareas financieras y estudiar errores de diseño temporal | MIT | 51 / Investigar más |
| `AI-finrobot` [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) | biblioteca/framework / V2 | Referencia de organización de herramientas y análisis financiero | Apache-2.0 | 58 / Investigar más |
| `AI-tradingagents` [TradingAgents](https://github.com/TauricResearch/TradingAgents) · [revisión](03_DEEP_TECHNICAL_REVIEWS/ai_tradingagents.md) | biblioteca/framework / V3 | Extraer controles as-of, abstención y registro de contexto | Apache-2.0 | 68 / Investigar más |
| `AI-ai-hedge-fund` [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund) | biblioteca/framework / V2 | Referencia educativa de análisis por agentes | MIT | 52 / Investigar más |
| `AI-docling` [Docling](https://github.com/docling-project/docling) · [revisión](03_DEEP_TECHNICAL_REVIEWS/ai_docling.md) | biblioteca/framework / V3 | Extraer tablas y contenido con estados de fallo para citar fuentes | MIT | 83 / Adoptar biblioteca |
| `AI-unstructured` [Unstructured library](https://github.com/Unstructured-IO/unstructured) | biblioteca/framework / V2 | Particionar documentos en elementos | Apache-2.0 | 69 / Investigar más |
| `AI-marker` [Marker](https://github.com/datalab-to/marker) | biblioteca/framework / V2 | Conversión PDF a formato procesable | Apache-2.0 | 66 / Investigar más |
| `AI-trafilatura` [Trafilatura](https://github.com/adbar/trafilatura) | biblioteca/framework / V2 | Extracción ligera de texto y metadatos web | Apache-2.0 | 82 / Adoptar biblioteca |
| `AI-sentence-transformers` [Sentence Transformers](https://github.com/huggingface/sentence-transformers) | biblioteca/framework / V2 | Embeddings y rerankers para recuperar evidencia | Apache-2.0 | 73 / Investigar más |
| `AI-flagembedding` [FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) | biblioteca/framework / V2 | Recuperación híbrida/multilingüe BGE | MIT | 72 / Investigar más |
| `AI-haystack` [Haystack](https://github.com/deepset-ai/haystack) | biblioteca/framework / V2 | Pipelines de recuperación y composición verificable | Apache-2.0 | 66 / Investigar más |
| `AI-llamaindex` [LlamaIndex framework](https://github.com/run-llama/llama_index) | biblioteca/framework / V2 | Conectores y herramientas de documentos | MIT | 64 / Investigar más |
| `AI-langgraph` [LangGraph](https://github.com/langchain-ai/langgraph) | biblioteca/framework / V2 | Estado durable y pasos explícitos de investigación | MIT | 66 / Investigar más |
| `AI-pydantic-ai` [Pydantic AI](https://github.com/pydantic/pydantic-ai) | biblioteca/framework / V2 | Esquemas de salida, herramientas tipadas y validación | MIT | 74 / Investigar más |
| `AI-dspy` [DSPy](https://github.com/stanfordnlp/dspy) | biblioteca/framework / V2 | Optimizar prompts/pipelines contra tareas medibles | MIT | 64 / Investigar más |
| `AI-ragas` [Ragas](https://github.com/vibrantlabsai/ragas) | biblioteca/framework / V2 | Medir aspectos de recuperación y respuesta | Apache-2.0 | 67 / Investigar más |
| `AI-inspect-ai` [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | biblioteca/framework / V2 | Evaluaciones reproducibles de LLM y tool use | MIT | 72 / Investigar más |
| `AI-garak` [garak](https://github.com/NVIDIA/garak) | biblioteca/framework / V2 | Ensayar resistencia a fallos e inyección en entorno controlado | Apache-2.0 | 63 / Investigar más |
| `AI-pyrit` [PyRIT (repositorio observado)](https://github.com/Azure/PyRIT) | biblioteca/framework / V2 | Referencia histórica de evaluación de riesgo | MIT | 51 / Conservar como referencia |
| `AI-promptfoo` [Promptfoo](https://github.com/promptfoo/promptfoo) | biblioteca/framework / V2 | Comparar prompts y automatizar evaluaciones | MIT | 71 / Investigar más |
| `AI-llm-guard` [LLM Guard](https://github.com/protectai/llm-guard) | biblioteca/framework / V2 | Referencia de scanners de contenido | MIT | 52 / Conservar como referencia |
| `AI-finllm-eval` [Tencent finLLM-Eval](https://github.com/Tencent/finLLM-Eval) | benchmark/repositorio de investigación / V1 | Separar hechos, cadenas lógicas y tripletas activo-fecha-métrica | No verificada | 47 / Investigar más |
## J — Noticias y eventos

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `quant-dowhy` [DoWhy](https://github.com/py-why/dowhy) | biblioteca / V2 | Identificación, estimación y refutación causal. | MIT | 63 / Investigar más |
| `quant-econml` [EconML](https://github.com/py-why/EconML) | biblioteca / V2 | Estimación de efectos heterogéneos con ML. | MIT; componentes econml.tree/econml.grf derivados bajo BSD-3-Clause | 63 / Investigar más |
| `quant-eventstudy` [eventstudy](https://github.com/LemaireJean-Baptiste/eventstudy) | biblioteca / V2 | Estudios de eventos con retornos anormales. | GPL-3.0 | 60 / Investigar más |
| `quant-pyfixest` [PyFixest](https://github.com/py-econometrics/pyfixest) | biblioteca / V2 | Efectos fijos, inferencia y diferencias en diferencias. | MIT | 63 / Investigar más |
| `quant-bsts-paper` [Inferring causal impact using Bayesian structural time-series models](https://arxiv.org/abs/1506.00356) | paper / V1 | Contrafactual mediante modelo estructural bayesiano de series. | No verificada | sin puntuación / Extraer una técnica |
| `AI-causal-learn` [causal-learn](https://github.com/py-why/causal-learn) | biblioteca/framework / V2 | Descubrimiento causal como generador de hipótesis | MIT | 60 / Investigar más |
## K — Cartera y riesgo

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `quant-quantstats` [QuantStats](https://github.com/ranaroussi/quantstats) | biblioteca / V2 | Métricas de rentabilidad, riesgo y reportes. | Apache-2.0 | 63 / Investigar más |
| `quant-pyportfolioopt` [PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt) · [revisión](03_DEEP_TECHNICAL_REVIEWS/quant_pyportfolioopt.md) | biblioteca / V3 | Optimización de cartera, covariance shrinkage, Black-Litterman y HRP. | MIT | 83 / Adoptar biblioteca |
| `quant-riskfolio-lib` [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | biblioteca / V2 | Optimización de carteras con medidas de riesgo alternativas. | BSD-3-Clause | 63 / Investigar más |
| `quant-pyfolio-reloaded` [Pyfolio-reloaded](https://github.com/stefan-jansen/pyfolio-reloaded) | fork/continuación; mantenimiento no auditado / V2 | Continuación de reportes de rendimiento de Pyfolio. | Apache-2.0 | 63 / Investigar más |
| `quant-empyrical-reloaded` [Empyrical-reloaded](https://github.com/stefan-jansen/empyrical-reloaded) | fork/continuación; mantenimiento no auditado / V2 | Métricas financieras reutilizables. | Apache-2.0 | 63 / Investigar más |
| `quant-empyrical` [Empyrical original](https://github.com/quantopian/empyrical) | biblioteca / V2 | Origen de métricas financieras; contrastar mantenimiento. | Apache-2.0 | 63 / Investigar más |
| `quant-ffn` [ffn](https://github.com/pmorissette/ffn) | biblioteca / V2 | Funciones de análisis de activos y carteras. | MIT | 63 / Investigar más |
| `quant-rugarch` [rugarch](https://github.com/alexiosg/rugarch) | biblioteca / V2 | Modelos GARCH en R. | GPL-3 (declaración DESCRIPTION) | 60 / Investigar más |
| `quant-performanceanalytics` [PerformanceAnalytics](https://github.com/braverock/PerformanceAnalytics) | biblioteca / V2 | Analítica de rentabilidad y riesgo en R. | GPL-2 / GPL-3 (declaración DESCRIPTION) | 60 / Investigar más |
| `quant-portfolioanalytics` [PortfolioAnalytics](https://github.com/braverock/PortfolioAnalytics) | biblioteca / V2 | Especificación y optimización de carteras en R. | GPL-3 (declaración DESCRIPTION) | 60 / Investigar más |
| `quant-cvxportfolio` [cvxportfolio](https://github.com/cvxgrp/cvxportfolio) | biblioteca / V2 | Optimización de cartera y simulación considerando costes. | GPL-3.0 | 60 / Investigar más |
| `quant-cvxpy` [CVXPY](https://github.com/cvxpy/cvxpy) | biblioteca / V2 | Modelado de optimización convexa como componente matemático. | Apache-2.0 | 63 / Investigar más |
## L — Visualización

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `infra-datasette` [datasette](https://github.com/simonw/datasette) | herramienta funcional / V2 | Exploración y publicación controlada de tablas SQLite. | Apache-2.0 | 66 / Investigar más |
| `infra-streamlit` [streamlit](https://github.com/streamlit/streamlit) | biblioteca / V2 | Dashboards interactivos Python; distinguir framework y hosting. | Apache-2.0 | 66 / Investigar más |
| `infra-marimo` [marimo](https://github.com/marimo-team/marimo) · [revisión](03_DEEP_TECHNICAL_REVIEWS/infra_marimo.md) | herramienta funcional / V3 | Cuadernos reactivos reproducibles guardados como Python. | Apache-2.0 | 87 / Adoptar biblioteca |
| `infra-panel` [panel](https://github.com/holoviz/panel) | biblioteca / V2 | Aplicaciones de datos sobre Bokeh y ecosistema HoloViz. | BSD-3-Clause | 66 / Investigar más |
| `infra-voila` [voila](https://github.com/voila-dashboards/voila) | biblioteca / V2 | Convierte notebooks en interfaces; evaluar estado oculto. | BSD (texto consultado; variante no resuelta) | 66 / Investigar más |
| `infra-plotly` [plotly.py](https://github.com/plotly/plotly.py) | biblioteca / V2 | Gráficos interactivos exportables. | MIT | 76 / Adoptar biblioteca |
| `infra-altair` [altair](https://github.com/vega/altair) | biblioteca / V2 | Gráficos declarativos basados en Vega-Lite. | BSD-3-Clause | 76 / Adoptar biblioteca |
| `infra-echarts` [echarts](https://github.com/apache/echarts) | biblioteca / V2 | Gráficos interactivos web de propósito general. | Apache-2.0 | 66 / Investigar más |
| `infra-lightweight-charts` [lightweight-charts](https://github.com/tradingview/lightweight-charts) | biblioteca / V2 | Gráficos financieros web; revisar atribución de interfaz. | Apache-2.0 | 66 / Investigar más |
| `infra-perspective` [perspective](https://github.com/finos/perspective) | biblioteca / V2 | Visor analítico con pivotes, filtros y motor WebAssembly. | Apache-2.0 | 66 / Investigar más |
| `infra-hvplot` [hvplot](https://github.com/holoviz/hvplot) | biblioteca / V2 | Visualización declarativa desde dataframes. | BSD-3-Clause | 66 / Investigar más |
| `infra-bokeh` [bokeh](https://github.com/bokeh/bokeh) | biblioteca / V2 | Visualización interactiva web desde Python. | BSD-3-Clause | 66 / Investigar más |
| `infra-cytoscapejs` [cytoscape.js](https://github.com/cytoscape/cytoscape.js) | biblioteca / V2 | Visualización y manipulación de grafos en navegador. | MIT | 66 / Investigar más |
| `infra-graphistry` [pygraphistry](https://github.com/graphistry/pygraphistry) | biblioteca / V2 | Cliente de análisis visual de grafos; backend/servicios separados. | BSD-3-Clause | 66 / Investigar más |
| `infra-pyvis` [pyvis](https://github.com/WestHealth/pyvis) | biblioteca / V1 | Visualización ligera de redes desde Python. | No verificada | 58 / Investigar más |
| `infra-visidata` [visidata](https://github.com/saulpw/visidata) | herramienta funcional / V2 | Exploración de tablas desde terminal. | GPL-3.0 | 66 / Investigar más |
| `infra-evidence` [evidence](https://github.com/evidence-dev/evidence) | herramienta funcional / V2 | Informes de datos con SQL y Markdown. | MIT | 66 / Investigar más |
| `infra-observable-framework` [framework](https://github.com/observablehq/framework) | herramienta funcional / V2 | Aplicaciones e informes de datos estáticos interactivos. | ISC | 66 / Investigar más |
## M — Datos e infraestructura

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `infra-duckdb` [duckdb](https://github.com/duckdb/duckdb) · [revisión](03_DEEP_TECHNICAL_REVIEWS/infra_duckdb.md) | biblioteca / V3 | Motor SQL embebido para consultar Parquet y unir series; candidato base de almacenamiento analítico. | MIT | 90 / Adoptar biblioteca |
| `infra-polars` [polars](https://github.com/pola-rs/polars) · [revisión](03_DEEP_TECHNICAL_REVIEWS/infra_polars.md) | biblioteca / V3 | Dataframes columnares con ejecución lazy y joins temporales. | MIT | 88 / Adoptar biblioteca |
| `infra-arrow` [arrow](https://github.com/apache/arrow) | biblioteca / V2 | Formato y bibliotecas de intercambio columnar; evitar conversiones innecesarias. | Apache-2.0 | 66 / Investigar más |
| `infra-pandas` [pandas](https://github.com/pandas-dev/pandas) | biblioteca / V2 | Dataframes para investigación y compatibilidad con bibliotecas cuantitativas. | BSD-3-Clause | 66 / Investigar más |
| `infra-ibis` [ibis](https://github.com/ibis-project/ibis) | biblioteca / V2 | Expresiones analíticas portables entre motores; evaluar coste de abstracción. | Apache-2.0 | 66 / Investigar más |
| `infra-dbt-duckdb` [dbt-duckdb](https://github.com/duckdb/dbt-duckdb) | biblioteca / V2 | Adaptador dbt para transformaciones SQL y pruebas sobre DuckDB. | Apache-2.0 | 66 / Investigar más |
| `infra-sqlglot` [sqlglot](https://github.com/tobymao/sqlglot) | biblioteca / V2 | Parser/transpilador SQL; extracción de linaje limitada a semántica SQL. | MIT | 66 / Investigar más |
| `infra-dlt` [dlt](https://github.com/dlt-hub/dlt) · [revisión](03_DEEP_TECHNICAL_REVIEWS/infra_dlt.md) | biblioteca / V3 | Ingesta incremental declarativa con estado y destinos analíticos. | Apache-2.0 | 81 / Investigar más |
| `infra-ingestr` [ingestr](https://github.com/bruin-data/ingestr) | biblioteca / V2 | Traslado incremental entre fuentes y destinos; dependencia de conectores. | FSL-1.1-ALv2 | 61 / Investigar más |
| `infra-meltano` [meltano](https://github.com/meltano/meltano) | biblioteca / V2 | Orquestación de conectores Singer; evaluar coste operativo personal. | MIT | 53 / Conservar como referencia |
| `infra-ducklake` [ducklake](https://github.com/duckdb/ducklake) | biblioteca / V2 | Catálogo transaccional de datos Parquet; más complejidad que ficheros simples. | MIT | 66 / Investigar más |
| `infra-delta-rs` [delta-rs](https://github.com/delta-io/delta-rs) | biblioteca / V2 | Lectura/escritura de tablas Delta en Rust y Python. | Apache-2.0 | 66 / Investigar más |
| `infra-datafusion` [datafusion](https://github.com/apache/datafusion) | biblioteca / V2 | Motor SQL embebible en Rust; alternativa de ingeniería a DuckDB. | Apache-2.0 | 66 / Investigar más |
| `infra-questdb` [questdb](https://github.com/questdb/questdb) | biblioteca / V2 | Base de series temporales con ingestión y consultas temporales. | Apache-2.0 | 66 / Investigar más |
| `infra-clickhouse` [ClickHouse](https://github.com/ClickHouse/ClickHouse) | biblioteca / V2 | Motor analítico columnar servidor para volúmenes superiores al uso personal inicial. | Apache-2.0 | 53 / Conservar como referencia |
| `infra-timescaledb` [timescaledb](https://github.com/timescale/timescaledb) | biblioteca / V2 | Extensión temporal PostgreSQL; revisar capas de licencias. | Apache-2.0 + Timescale License por directorio | 48 / Conservar como referencia |
| `infra-sqlite` [sqlite](https://github.com/sqlite/sqlite) | mirror oficial; motor / V2 | Mirror de SQLite; metadatos locales y catálogos pequeños. | Dominio público en componentes identificados; revisar terceros | 76 / Adoptar biblioteca |
| `infra-sqlite-utils` [sqlite-utils](https://github.com/simonw/sqlite-utils) | biblioteca / V2 | Utilidades para carga y mantenimiento de tablas SQLite. | Apache-2.0 | 66 / Investigar más |
| `infra-frictionless` [frictionless-py](https://github.com/frictionlessdata/frictionless-py) | biblioteca / V2 | Esquemas y validación de paquetes de datos intercambiables. | MIT | 76 / Adoptar biblioteca |
| `infra-pandera` [pandera](https://github.com/unionai-oss/pandera) · [revisión](03_DEEP_TECHNICAL_REVIEWS/infra_pandera.md) | biblioteca / V3 | Validación de esquemas y restricciones de tablas. | MIT | 84 / Adoptar biblioteca |
| `infra-great-expectations` [great_expectations](https://github.com/great-expectations/great_expectations) | biblioteca / V2 | Framework de expectativas y documentación de calidad; evaluar complejidad. | Apache-2.0 | 66 / Investigar más |
| `infra-soda-core` [soda-core](https://github.com/sodadata/soda-core) | biblioteca / V2 | Comprobaciones declarativas de datos; distinguir núcleo y oferta comercial. | Elastic-2.0 | 61 / Investigar más |
| `infra-pydantic` [pydantic](https://github.com/pydantic/pydantic) | biblioteca / V2 | Validación de tipos en contratos de entrada/salida. | MIT | 76 / Adoptar biblioteca |
| `infra-patito` [patito](https://github.com/JakobGM/patito) · [revisión](03_DEEP_TECHNICAL_REVIEWS/infra_patito.md) | biblioteca / V3 | Esquemas sobre Polars con modelos Pydantic. | MIT | 80 / Investigar más |
| `infra-tenacity` [tenacity](https://github.com/jd/tenacity) | biblioteca / V2 | Reintentos programables; no sustituyen límites del proveedor. | Apache-2.0 | 66 / Investigar más |
| `infra-requests-cache` [requests-cache](https://github.com/requests-cache/requests-cache) · [revisión](03_DEEP_TECHNICAL_REVIEWS/infra_requests-cache.md) | biblioteca / V3 | Caché HTTP persistente con políticas de expiración. | BSD-2-Clause | 84 / Adoptar biblioteca |
| `infra-hishel` [hishel](https://github.com/karpetrosyan/hishel) | biblioteca / V2 | Caché HTTP respetuosa de semántica HTTP para clientes modernos. | BSD-3-Clause | 66 / Investigar más |
| `infra-httpx` [httpx](https://github.com/encode/httpx) | biblioteca / V2 | Cliente HTTP síncrono/asíncrono; núcleo de conectores pequeños. | BSD-3-Clause | 76 / Adoptar biblioteca |
| `infra-fsspec` [filesystem_spec](https://github.com/fsspec/filesystem_spec) | biblioteca / V2 | Interfaz homogénea a sistemas de ficheros locales/remotos. | BSD-3-Clause | 66 / Investigar más |
| `infra-intake` [intake](https://github.com/intake/intake) | biblioteca / V2 | Catálogos declarativos de fuentes y acceso a datos. | BSD-2-Clause | 66 / Investigar más |
| `infra-dvc` [dvc](https://github.com/iterative/dvc) | biblioteca / V2 | Versionado de datos y procesos con almacén externo. | Apache-2.0 | 66 / Investigar más |
| `infra-lakefs` [lakeFS](https://github.com/treeverse/lakeFS) | biblioteca / V2 | Versionado tipo Git sobre almacenamiento de objetos. | BUSL-1.1; Additional Use Grant limitado | 48 / Conservar como referencia |
| `infra-openlineage` [OpenLineage](https://github.com/OpenLineage/OpenLineage) | biblioteca / V2 | Especificación y clientes de eventos de linaje. | Apache-2.0 | 53 / Conservar como referencia |
| `infra-datahub` [datahub](https://github.com/datahub-project/datahub) | biblioteca / V2 | Catálogo de metadatos empresarial; referencia más que componente inicial. | Apache-2.0 | 53 / Conservar como referencia |
| `infra-dagster` [dagster](https://github.com/dagster-io/dagster) | biblioteca / V2 | Orquestación basada en activos y estado de materializaciones. | Apache-2.0 | 53 / Conservar como referencia |
| `infra-prefect` [prefect](https://github.com/PrefectHQ/prefect) | biblioteca / V2 | Orquestación Python con reintentos y observabilidad. | Apache-2.0 | 53 / Conservar como referencia |
| `infra-luigi` [luigi](https://github.com/spotify/luigi) | biblioteca / V2 | Dependencias de tareas batch y objetivos persistentes. | Apache-2.0 | 66 / Investigar más |
| `infra-apscheduler` [apscheduler](https://github.com/agronholm/apscheduler) | biblioteca / V2 | Planificación local de trabajos periódicos. | MIT | 66 / Investigar más |
| `infra-joblib` [joblib](https://github.com/joblib/joblib) | biblioteca / V2 | Caché de cálculos y paralelismo local. | BSD-3-Clause | 66 / Investigar más |
| `infra-diskcache` [python-diskcache](https://github.com/grantjenks/python-diskcache) | biblioteca / V2 | Caché local persistente sobre disco. | Apache-2.0 | 66 / Investigar más |
| `infra-orjson` [orjson](https://github.com/ijl/orjson) | biblioteca / V1 | Serialización JSON rápida; atención a timestamps y números. | No verificada | 58 / Investigar más |
| `infra-xtdb` [xtdb](https://github.com/xtdb/xtdb) | biblioteca / V2 | Base bitemporal SQL con tiempos válido/sistema. | MPL-2.0 | 53 / Conservar como referencia |
| `infra-sirix` [sirix](https://github.com/sirixdb/sirix) | biblioteca / V2 | Historial inmutable bitemporal y snapshots estructuralmente compartidos. | BSD-3-Clause | 53 / Conservar como referencia |
| `infra-narwhals` [narwhals](https://github.com/narwhals-dev/narwhals) | biblioteca / V2 | Compatibilidad entre bibliotecas de dataframes. | MIT | 66 / Investigar más |
| `infra-ydata-profiling` [ydata-profiling](https://github.com/ydataai/ydata-profiling) | biblioteca / V2 | Perfilado exploratorio; no confundir descriptivos con integridad temporal. | MIT | 66 / Investigar más |
| `infra-data-diff` [data-diff](https://github.com/datafold/data-diff) | biblioteca / V2 | Comparación de tablas; comprobar mantenimiento y transición a comercial. | MIT | 66 / Conservar como referencia |
| `infra-datacompy` [datacompy](https://github.com/capitalone/datacompy) · [revisión](03_DEEP_TECHNICAL_REVIEWS/infra_datacompy.md) | biblioteca / V3 | Comparación tabular para detectar revisiones de series. | Apache-2.0 | 84 / Adoptar biblioteca |
| `infra-qfs` [quant-feature-store](https://github.com/sophie-nguyenthuthuy/quant-feature-store) · [revisión](03_DEEP_TECHNICAL_REVIEWS/infra_qfs.md) | prototipo / V3 | Prototipo bitemporal pequeño de prevención de leakage descubierto en búsqueda. | No verificada | 60 / Extraer una técnica |
| `infra-point-in-time-datawarehouse` [point-in-time-datawarehouse](https://github.com/winstongarth/point-in-time-datawarehouse) | prototipo / V1 | Ejemplo de restricciones bitemporales y reconciliación de proveedores. | No verificada | 45 / Conservar como referencia |
| `infra-alpha-lake` [alpha-lake](https://github.com/mblaauw/alpha-lake) | prototipo / V2 | Lakehouse de investigación tritemporal; extraer patrones sin adoptar plataforma. | Apache-2.0 | 53 / Conservar como referencia |
| `infra-ptdata-methodology` [ptdata-methodology](https://github.com/ptdata-io/ptdata-methodology) | especificación de servicio; documentación abierta / V2 | Especificación pública de servicio de datos point-in-time; no confundir con implementación abierta. | CC-BY-4.0 para documentación | 66 / Investigar más |
| `infra-row-level-prov` [row-level-prov](https://github.com/stevenblough/row-level-prov) | prototipo / V2 | Prototipo de linaje por fila/campo con restricciones de uso comercial. | PolyForm-Noncommercial-1.0.0 | 61 / Investigar más |
## N — Fuentes alternativas

| ID / recurso | Tipo / nivel | Uso y límite de selección | Licencia observada | Puntos / decisión |
|---|---|---|---|---|
| `infra-provider-polymarket-api` [Polymarket: API de datos](https://docs.polymarket.com/api-reference/predictions/overview) | proveedor/API o servicio comercial de referencia / V1 | Datos de eventos, mercados, precios e historial; no se invocaron operaciones. | Términos del servicio/dataset pendientes de caso concreto | sin puntuación / Conservar como referencia |

Las fichas completas —commit, dependencias, fuentes, riesgos, confianza, limitaciones y puntos por criterio— están en [projects.json](inventories/projects.json) y [projects.csv](inventories/projects.csv). Para reproducir una afirmación, seguir evidence_ids → evidence → source_id → sources. No usar la tabla abreviada como autorización de adopción.
