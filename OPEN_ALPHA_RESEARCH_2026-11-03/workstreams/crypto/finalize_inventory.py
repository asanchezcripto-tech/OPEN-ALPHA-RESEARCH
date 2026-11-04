"""Editorial annotations to the research catalogue. Own code; no external imports/execution.

Requires the generated inventory JSON, not the third-party inspection caches.
Idempotent: source and evidence IDs derive from exact URLs/claims.
"""
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
DATE = "2026-11-04"

def read(name):
    return json.loads((ROOT / (name + ".json")).read_text(encoding="utf8"))

def write(name, value):
    (ROOT / (name + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf8")

def ident(prefix, text):
    return prefix + hashlib.sha256(text.encode()).hexdigest()[:12]

candidates = read("candidates")
sources = {x["id"]: x for x in read("sources")}
evidence = {x["id"]: x for x in read("evidence")}
by_id = {x["id"]: x for x in candidates}

def source(url, title, kind="official_documentation", status="consultado", notes="Documentación pública consultada; sin ejecutar API de datos ni comprobar estado desplegado."):
    sid = ident("crypto-src-", url)
    sources[sid] = dict(id=sid, url=url, title=title, accessed_at=DATE, source_type=kind,
                        status=status, version_or_commit=None, notes=notes)
    return sid

def claim(candidate_id, sid, text, kind="documentary_observation", limitations="No demuestra exactitud de datos, ejecución local ni estado desplegado; conservar versión y alcance."):
    eid = ident("crypto-ev-detail-", candidate_id + sid + text)
    evidence[eid] = dict(id=eid, candidate_id=candidate_id, source_id=sid, claim=text,
                        evidence_type=kind, limitations=limitations)
    if candidate_id in by_id:
        c = by_id[candidate_id]
        c["source_ids"] = list(dict.fromkeys(c["source_ids"] + [sid]))
        c["evidence_ids"] = list(dict.fromkeys(c["evidence_ids"] + [eid]))
    return eid

def code_claim(repo, path, text, limitations="Inspección estática de esta ruta; no se ejecutaron tests ni se verificó comportamiento desplegado."):
    c = next(c for c in candidates if c["original_url"] == "https://github.com/" + repo)
    url = "https://raw.githubusercontent.com/" + repo + "/" + c["version_or_commit"] + "/" + path
    sid = ident("crypto-src-", url)
    assert sid in sources, url
    assert sources[sid]["status"] == "consultado", url
    return claim(c["id"], sid, text, "static_source_inspection", limitations)

docs = {}
docs["llama"] = source("https://docs.llama.fi/list-your-project/other-dashboards", "DefiLlama: other dashboards and financial metric definitions")
docs["llama_old"] = source("https://docs.llama.fi/list-your-project/other-dashboards/important-considerations", "DefiLlama: important considerations", notes="Página accesible que advierte estar desactualizada desde mayo de 2025; no prevalece sobre metodología actual.")
docs["hype_fees"] = source("https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees", "Hyperliquid: Fees")
docs["hype_info"] = source("https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint", "Hyperliquid: Info endpoint")
docs["hype_transfers"] = source("https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/hyperevm/hypercore-less-than-greater-than-hyperevm-transfers", "Hyperliquid: HyperCore and HyperEVM transfers", "official_search_result", notes="Contenido original servido por búsqueda; no se ejecutaron transferencias ni se comprobó fungibilidad de un activo concreto.")
docs["poly_api"] = source("https://docs.polymarket.com/api-reference/predictions/overview", "Polymarket: Predictions API overview")
docs["poly_limits"] = source("https://docs.polymarket.com/api-reference/rate-limits", "Polymarket: API rate limits")
docs["poly_v2_deprecated"] = source("https://github.com/Polymarket/py-clob-client-v2/releases/tag/v1.2.1", "Polymarket CLOB v2 release v1.2.1", "official_release", notes="Deprecación publicada en release; no se tomó como versión del SDK unificado.")
docs["ray_fees"] = source("https://docs.raydium.io/ray/protocol-fees", "Raydium: Protocol fees")
docs["ray_compare"] = source("https://docs.raydium.io/reference/fee-comparison", "Raydium: Fee comparison", notes="Documento incluye observación de configuraciones de septiembre de 2026; esas lecturas de cadena son reportadas por el documento, no reproducidas aquí.")
docs["ray_buybacks"] = source("https://docs.raydium.io/ray/ray-buybacks", "Raydium: Buybacks")
docs["ray_cpmm"] = source("https://docs.raydium.io/products/cpmm", "Raydium: CPMM")
docs["uni_tjar"] = source("https://blog.uniswap.org/how-tjar-works-uniswaps-onchain-fee-conversion-system", "Uniswap: How TJAR Works", "official_blog", notes="Publicado 2026-10-30. Anuncio/documentación de despliegue; no sustituye comprobación de bytecode, configuración y eventos.")
docs["uni_hooks"] = source("https://blog.uniswap.org/aggregator-hooks-are-now-live", "Uniswap: Aggregator Hooks Are Now Live", "official_search_result", notes="Resultado de búsqueda y enlace del artículo TJAR; fecha indicada 2026-10-22. No se inspeccionó implementación de estos hooks.")
docs["pump"] = source("https://pump.fun/pump-token", "Pump: PUMP token dashboard", notes="Advierte que custom pairs afectan cifras de revenue/buybacks; no usar importes mostrados como validados. Wallet data no disponible.")
docs["dune"] = source("https://docs.dune.com/api-reference/overview/introduction", "Dune: API introduction", notes="Servicio hospedado con cuentas/claves y condiciones propias; lectura documental, sin autenticación, consultas ni pago.")
docs["deribit"] = source("https://docs.deribit.com/api-reference/market-data/public-get_book_summary_by_currency", "Deribit: public/get_book_summary_by_currency")
docs["tt_home"] = source("https://tokenterminal.com/", "Token Terminal: product overview", "commercial_provider_documentation", notes="Producto analítico cerrado; sitio público no implica licencia abierta de datos ni reproducción de backend.")
docs["tt_metric"] = source("https://tokenterminal.com/explorer/metrics/tokenholder_revenue", "Token Terminal: tokenholder revenue methodology", "commercial_provider_documentation", notes="La propia página indica metodología textual generada automáticamente. Consultada como definición del proveedor, no como auditoría del cálculo.")
docs["tt_changelog"] = source("https://tokenterminal.com/resources/changelog?p=1", "Token Terminal: Changelog", "official_search_result", notes="Resultado original indexado; muestra revisiones de cobertura/métodos. No se descargó historial íntegro de versiones.")
docs["circle"] = source("https://developers.circle.com/cctp", "Circle: Cross-Chain Transfer Protocol")
docs["blocksci_paper"] = source("https://www.usenix.org/conference/usenixsecurity20/presentation/kalodner", "BlockSci: Design and applications of a blockchain analysis platform", "paper_original", notes="USENIX Security 2020; ficha/abstract consultados. No se reprodujeron benchmarks ni se reejecutó implementación.")
docs["blocksci_preprint"] = source("https://arxiv.org/abs/1709.02489", "BlockSci arXiv preprint", "paper_original", notes="Versión preliminar de 2017; se deduplica con publicación USENIX 2020 como una línea de investigación, no dos papers independientes.")

failed = [
    ("https://docs.raydium.io/raydium/protocol/protocol-fees", "Raydium: antigua ruta de protocol fees", "404; sustituida por /ray/protocol-fees; caché de búsqueda no prueba accesibilidad actual."),
    ("https://docs.polymarket.com/migrate/clob-sdk-to-unified-sdk", "Polymarket: antigua guía de migración", "No accesible en la investigación; READMEs y release oficial sí documentan migración."),
    ("https://tokenterminal.com/resources/knowledge-base/our-metrics", "Token Terminal: antigua ruta de métricas", "No accesible; se localizó /explorer/metrics/tokenholder_revenue."),
    ("https://hyperliquid.gitbook.io/hyperliquid-docs/hype/assistance-fund", "Hyperliquid: ruta candidata assistance fund", "Devuelve Page Not Found; mecanismo documentado en trading/fees."),
    ("https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams", "Binance: ruta histórica de liquidation streams", "Redirige a índice genérico; no valida supuesto de throttling 1 evento/s actual."),
]
for url, title, notes in failed:
    source(url, title, status="inaccesible_o_redireccion_sin_contenido_buscado", notes=notes)

claim("crypto-defillama-dimension-adapters", docs["llama"], "La metodología distingue fees, pagos al lado proveedor, revenue del protocolo y captura de holders; la etiqueta debe leerse por protocolo y versión.")
claim("crypto-hyperliquid-dex-hyperliquid-python-sdk", docs["hype_fees"], "La documentación describe conversión automática a HYPE del assistance fund y quema; HIP-3, spot, descuentos y deployers requieren ámbitos y bases separados.")
claim("crypto-hyperliquid-dex-hyperliquid-python-sdk", docs["hype_info"], "El endpoint Info documenta paginación y límites de resultados; una consulta temporal no equivale a descargar todo el historial disponible.")
claim("crypto-polymarket-py-sdk", docs["poly_limits"], "Los límites por IP y endpoint usan ventanas deslizantes y pueden retrasar peticiones; un HTTP exitoso no prueba frescura ni completitud.")
claim("crypto-polymarket-py-clob-client-v2", docs["poly_v2_deprecated"], "La release v1.2.1 documenta deprecación del cliente de transición V2 y remite al SDK unificado.")
claim("crypto-raydium-io-raydium-sdk-v2", docs["ray_fees"], "Documenta reparto 84/12/4 en CLMM/CPMM y 88/12 en AMM v4; porcentajes sobre fees y denominadores de configuración distintos.")
claim("crypto-raydium-io-raydium-sdk-v2", docs["ray_buybacks"], "El documento indica custodia del RAY recomprado en dirección del protocolo; no describe esa acumulación como burn.")
claim("crypto-uniswap-protocol-fees", docs["uni_tjar"], "TJAR es anunciado como infraestructura desplegada de conversión configurable; destino, threshold y propietario siguen siendo campos a verificar por despliegue.")
claim("crypto-pump-fun-pump-public-docs", docs["pump"], "El panel anuncia asignación de 50% a buyback/burn, pero advierte cobertura incorrecta de custom pairs y datos de wallets no disponibles.", limitations="Declaración del operador; cifras monetarias y transacciones no reconciliadas, no aptas como verdad validada.")
claim("crypto-duneanalytics-dune-client", docs["dune"], "Cliente abierto y documentación pública no equivalen a infraestructura hospedada ni resultados de consultas con licencia abierta.")
claim("crypto-defillama-peggedassets-server", docs["circle"], "Circle documenta transferencias USDC burn-and-mint entre cadenas: un mint local puede corresponder a migración de oferta, sin entrada fiat nueva.", limitations="Inferencia contable del mecanismo documentado; no se midieron flujos concretos ni se auditó CCTP.")
claim("crypto-citp-blocksci", docs["blocksci_paper"], "Publicación original de la plataforma BlockSci; aporta diseño analítico, no prueba mantenimiento vigente del repositorio.")

code_claim("DefiLlama/dimension-adapters", "helpers/hyperliquid.ts", "El helper modifica revenue shares por fecha (97/3 y luego 99/1) y contiene fallback a metaAndAssetCtxs actual cuando fallan snapshots recientes. No convertir ese fallback en dato point-in-time histórico.")
code_claim("DefiLlama/dimension-adapters", "fees/hyperliquid-hlp.ts", "El adaptador HLP asigna revenue cero, supply-side fees y doublecounted=true; sumar indiscriminadamente HLP y protocolo duplica conceptos.")
code_claim("hyperliquid-dex/hyperliquid-python-sdk", "hyperliquid/info.py", "Info inicia WebSocket por defecto salvo skip_ws; firmas retornan Any para diversos endpoints y una llamada de fundingHistory no garantiza paginación exhaustiva.")
code_claim("Polymarket/py-sdk", "src/polymarket/pagination.py", "Page mantiene has_more, next_cursor y limit_reached; llegar al máximo de profundidad no demuestra que se haya comprobado otra página.")
code_claim("Polymarket/py-sdk", "src/polymarket/clients/_transport.py", "El transporte interpreta Retry-After numérico/fecha y errores HTTP; no se verificó que todos los métodos reintenten de igual modo.")
code_claim("Uniswap/protocol-fees", "src/TokenJar.sol", "TokenJar restringe extracción al releaser, cuyo destino contractual puede cambiar el owner; no asumir inmutabilidad sin leer estado.")
code_claim("Uniswap/protocol-fees", "src/releasers/Firepit.sol", "Firepit configura el destinatario del recurso como 0xdead; transferencia a esa dirección no prueba por sí misma decremento de totalSupply del ERC20.")
code_claim("raydium-io/raydium-sdk-V2", "src/raydium/clmm/layout.ts", "Layouts incluyen tasas trade/protocol/fund y acumuladores; son claves para interpretar cuentas con escala y versión de programa.")
code_claim("raydium-io/raydium-sdk-V2", "test/cpmmSwapQuote.test.js", "Tests inspeccionados usan fixtures para exact-in/exact-out, financiación SOL y reutilización de cotización sin mutación; no ejecutados.")

# More specific licensing annotations, based on directly inspected licence text.
by_id["crypto-polymarket-ctf-exchange-v2"]["license_code"] = "BUSL-1.1; sin Additional Use Grant; Change Date 2030-03-27 a MIT en texto examinado"
by_id["crypto-uniswap-v4-core"]["license_code"] = "BUSL-1.1; Change Date 2027-06-15 a MIT, con posibles modificaciones ENS; revisar versión"
by_id["crypto-duneanalytics-spellbook"]["license_code"] = "BUSL-1.1; Change Date 2027-03-03 a GPL-3.0-or-later; restricción de Data/Analytics Platform"
by_id["crypto-hyperliquid-dex-node"]["license_code"] = "Apache-2.0 del repositorio examinado; disponibilidad/licencia del código del motor no comprobada"
by_id["crypto-aave-dao-aave-v3-origin"]["license_code"] = "BUSL-1.1; Change Date 2027-03-06 o fecha ENS anterior a MIT; Additional Use Grant restrictiva en texto examinado"
by_id["crypto-defillama-emissions-adapters"]["maintenance_status"] = "No comprobado; referencia documental indirecta y acceso directo fallido"
by_id["crypto-uniswap-protocol-fees"]["adoption_mode"] = "Extraer una técnica"
by_id["crypto-uniswap-protocol-fees"]["practical_use"] = "Interpretar etapas contables y eventos de fees; no es necesario desplegar ni bifurcar los contratos"

datasets = [
    dict(id="crypto-data-binance-public", candidate_id="crypto-binance-binance-public-data", name="Binance public data archives", access="Archivos públicos descargables; sin descarga masiva realizada", coverage="OHLCV/trades/aggTrades y productos documentados; no equiparar a histórico completo de OI/profundidad", temporal_risk="Spot usa microsegundos desde 2025-01-01 según README; publicación diaria posterior al día observado y revisiones posibles", license="No verificada para redistribución del dataset", free_alternative="Snapshots prospectivos de endpoints públicos con permiso de uso revisado"),
    dict(id="crypto-data-coinmetrics-community", candidate_id="crypto-coinmetrics-data", name="Coin Metrics community CSV", access="Repositorio público de CSV", coverage="Subconjunto de activos/métricas; archivos no descargados ni integridad medida", temporal_risk="Última versión puede incluir revisiones retrospectivas; fecha de archivo no equivale a disponibilidad original", license="CC-BY-NC-4.0 en dataset; cliente Python MIT separado", free_alternative="Métricas derivadas de fuentes originales con definición propia"),
    dict(id="crypto-data-graphsense-tagpacks", candidate_id="crypto-graphsense-graphsense-tagpacks", name="GraphSense tagpacks", access="Repositorio público; esquema y licencia inspeccionados", coverage="Etiquetas parciales de direcciones/servicios, no censo de titulares", temporal_risk="Etiquetas pueden conocerse después del evento; guardar observed_at, source y validez", license="MIT del repositorio inspeccionado; verificar condiciones de fuentes externas de cada etiqueta", free_alternative="Etiquetas documentadas manualmente y marcadas como hipótesis"),
    dict(id="crypto-data-defillama-dimensions", candidate_id="crypto-defillama-dimension-adapters", name="DefiLlama financial dimensions", access="Código público de adaptadores; disponibilidad de upstreams desigual", coverage="Protocolo/métrica/fecha/adaptador; no auditado el dataset completo", temporal_risk="Cambios de fórmulas y fallback a contextos actuales; historial del proveedor no necesariamente vintage", license="Licencia de copia del adaptador no localizada; derechos de servicio distintos", free_alternative="Muestra manual de eventos y contratos públicos"),
    dict(id="crypto-data-stablecoin-supply", candidate_id="crypto-defillama-peggedassets-server", name="Stablecoin balances and supply", access="Adaptadores públicos; frontend/API y permisos por revisar", coverage="Oferta por activo/cadena; no reservas bancarias ni entrada fiat observada", temporal_risk="Bridges, mint/burn, reclasificaciones de circulating supply y cambios de precios", license="No verificada", free_alternative="Balance/supply de contratos originales y documentos del emisor"),
    dict(id="crypto-data-hyperliquid-public", candidate_id="crypto-hyperliquid-dex-hyperliquid-python-sdk", name="Hyperliquid Info public market data", access="Documentación/API pública, sin necesidad de firmar para consultas de mercado", coverage="Mercados y cuentas conocidas; retención/paginación específicas", temporal_risk="Estado actual no sustituye archivo; muestras de wallets no son censo", license="MIT del SDK no concede derechos generales sobre servicio/datos", free_alternative="Snapshots prospectivos acotados"),
    dict(id="crypto-data-polymarket-public", candidate_id="crypto-polymarket-py-sdk", name="Polymarket public market and resolution data", access="SDK PublicClient y endpoints documentados", coverage="Mercados, precios, reglas, actividad; no se descargó universo histórico", temporal_risk="Mercados cerrados/retirados y revisiones de resolución; cursores y truncamiento", license="MIT del SDK; licencia/ToS de datos separadas", free_alternative="Cesta manual de mercados y snapshots de reglas"),
    dict(id="crypto-data-evm-events", candidate_id="crypto-paradigmxyz-cryo", name="Selected EVM logs/transactions", access="RPC público o propio con límites; cliente no garantiza archivo", coverage="Cadena/contratos/bloques seleccionados; depende del nodo", temporal_risk="Reorgs, finality, archive RPC y metadata que cambia; tx timestamp no equals acquisition", license="Código Cryo MIT OR Apache-2.0; términos del proveedor RPC separados", free_alternative="Explorador y muestras manuales para primer prototipo"),
]
for x in datasets:
    x["verified_at"] = DATE
    x["source_ids"] = by_id[x["candidate_id"]]["source_ids"]
    x["verification_scope"] = "Fuente y estructura documentales; no descarga, limpieza ni benchmark del dataset completo"

providers = [
    dict(id="crypto-provider-dune", name="Dune hosted analytics", category="Servicio cerrado con cliente y modelos públicos separados", source_ids=[docs["dune"]], use="Contraste de consultas y exploración de resultados", constraint="Cuenta/clave, cuotas y derechos de exportación/redistribución por revisar; Spellbook BUSL, cliente Apache-2.0", cost="No cotizado ni contratado", substitute="Cryo o Ponder + SQL propio sobre contratos acotados"),
    dict(id="crypto-provider-token-terminal", name="Token Terminal", category="Servicio analítico comercial cerrado", source_ids=[docs["tt_home"], docs["tt_metric"], docs["tt_changelog"]], use="Comparar definiciones, métricas y forma de presentar estados económicos", constraint="No se accedió a API autenticada, planes ni dataset íntegro; metodología textual generada automáticamente no prueba implementación", cost="No cotizado ni contratado", substitute="Adaptador revisado + eventos originales + reconciliación manual"),
    dict(id="crypto-provider-deribit", name="Deribit public market API", category="Mercado cerrado con documentación/API pública", source_ids=[docs["deribit"]], use="OI, mark/index, IV y funding de instrumentos específicos", constraint="Mark IV es magnitud modelada y específica del instrumento; no histórico integral por consultar snapshot", cost="No cotizado ni autenticado", substitute="Observación prospectiva limitada; API de otro venue con especificación comparable"),
    dict(id="crypto-provider-circle", name="Circle documentation and CCTP", category="Emisor/protocolo con documentación pública", source_ids=[docs["circle"]], use="Identificar migraciones de oferta y evitar contar mint intercadena como entrada fiat", constraint="Documentación no es prueba de reservas ni licencia de datos general", cost="No transacciones ni contratación", substitute="Eventos del contrato y reconciliación entre cadenas"),
]
for x in providers:
    x["verification_level"] = "V1"
    x["verified_at"] = DATE
    x["not_open_source_substitute"] = True

papers = [
    dict(id="crypto-paper-blocksci", title="BlockSci: Design and applications of a blockchain analysis platform", authors="Harry Kalodner, Malte Möser, Kevin Lee, Steven Goldfeder, Martin Plattner, Alishah Chator, Arvind Narayanan", publication="USENIX Security 2020; preprint de 2017 como versión anterior", source_ids=[docs["blocksci_paper"], docs["blocksci_preprint"]], candidate_id="crypto-citp-blocksci", reading_scope="Ficha original y abstract; no lectura completa de benchmarks ni reproducción", contribution="Arquitectura orientada a análisis blockchain y representación eficiente", limitations="Implementación sin desarrollo activo declarado desde 2020; no adoptar como stack vigente sin nuevo mantenimiento", reproducibility="Código asociado localizado; datasets y experimentos no reproducidos"),
    dict(id="crypto-paper-hyperliquid-paths", title="Price Trajectories, Impact and Sunshine Trading", authors="Davide Barone y Fabrizio Lillo según nota del repositorio", publication="Nota pública asociada a 0xBaro/hyperliquid; revisión/publicación formal no verificada", source_ids=by_id["crypto-0xbaro-hyperliquid"]["source_ids"], candidate_id="crypto-0xbaro-hyperliquid", reading_scope="Documentación/repositorio; no revisión completa del estudio", contribution="Pista para estudiar trayectoria de precios e impacto con datos de mercado públicos", limitations="Dataset, selección de eventos, vigencia y licencia no comprobados; no evidencia de alpha validada", reproducibility="Repositorio con src/scripts localizado, implementación no auditada ni ejecutada"),
]

methods = [
    dict(id="crypto-method-value-bridge", name="Puente de captura por mecanismo", inputs="Fees, payouts, inventario, conversiones, buybacks, burn y supply", output="Magnitudes separadas y residual explicado", hypothesis="Evita atribuir al token actividad que corresponde a LP/creadores o ingresos todavía no convertidos", failure="Precio/FX, dobles conteos, mecanismos cambiantes o captura sin derecho contractual", validation="Reconciliar balances/flujo en un protocolo y días seleccionados", evidence_type="Síntesis propuesta, sin experimento", supporting_ids=["crypto-defillama-dimension-adapters", "crypto-uniswap-protocol-fees"]),
    dict(id="crypto-method-supply-ledger", name="Ledger de oferta y desbloqueos", inputs="Mint/burn, circulating/locked/treasury/bridge, cronología de anuncios", output="Supply total vs circulante y escenarios de disponibilidad", hypothesis="Distingue dilución por creación de tokens de liberación de tokens preexistentes", failure="Múltiples representaciones del mismo activo y calendarios sin historial de revisiones", validation="Identidad de oferta y doble entrada de bridges", evidence_type="Método propuesto, sin cálculo de valoración", supporting_ids=["crypto-defillama-peggedassets-server"]),
    dict(id="crypto-method-derivative-normalization", name="Normalización contractual de derivados", inputs="Instrumento, contractSize, settlement, OI, fase/intervalo/signo funding", output="OI nativo y nocional con precio/timestamp; presión por venue", hypothesis="Reduce falsas señales por precio, multiplicador o financiación de duración distinta", failure="Instrumentos con especificación incompleta, APIs truncadas y doble conteo económico entre venues", validation="Casos de contrato inverso, intervalo cambiante y ausencia de datos", evidence_type="Diseño apoyado en rutas estáticas CCXT; no score validado", supporting_ids=["crypto-ccxt-ccxt", "crypto-hyperliquid-dex-hyperliquid-python-sdk"]),
    dict(id="crypto-method-flow-attribution", name="Flujos etiquetados con incertidumbre de entidad", inputs="Transferencias, etiquetas, fuentes, timestamps y confianza", output="Flujo bruto/neto por etiqueta y sensibilidad a agrupación", hypothesis="Evita convertir movimiento entre wallets internas en entrada de capital de inversores", failure="Etiquetas retrospectivas, entidades con varias wallets, custodios/bridges y muestra incompleta", validation="Contrastar manualmente eventos y publicar discrepancias entre reglas de agrupación", evidence_type="Técnica propuesta a partir del esquema GraphSense", supporting_ids=["crypto-graphsense-graphsense-lib", "crypto-graphsense-graphsense-tagpacks"]),
    dict(id="crypto-method-event-market-link", name="Mercados predictivos como evidencia de tesis", inputs="Reglas, resolución, precio, spread, profundidad y calendario de fuentes", output="Escenarios vinculados a tesis y cambios documentales", hypothesis="Aporta señal contextual; no trata precio como probabilidad objetiva", failure="Resoluciones distintas, sesgo de selección, falta de mercados cerrados y poca liquidez", validation="Muestra curada con revisión humana de equivalencia y fechas", evidence_type="Propuesta, sin backtest ni promesa de retornos", supporting_ids=["crypto-polymarket-py-sdk"]),
]

comparisons = [
    dict(id="crypto-compare-exchange-clients", candidates=["crypto-ccxt-ccxt", "crypto-bmoscon-cryptofeed", "crypto-hummingbot-hummingbot"], decision="CCXT para snapshots REST de lectura; Cryptofeed si hace falta streaming y se acepta AGPL+atribución; Hummingbot sólo referencia", reason="Horizonte inversor y coste operativo no justifican motor de ejecución", unmeasured="Latencia, cobertura real de endpoints y mantenimiento futuro"),
    dict(id="crypto-compare-indexers", candidates=["crypto-paradigmxyz-cryo", "crypto-ponder-sh-ponder", "crypto-graphprotocol-graph-node", "crypto-subsquid-squid-sdk"], decision="Cryo para extracción batch acotada; Ponder para índice continuo con reorgs; Graph Node/Subsquid cuando exista necesidad de servicio/archivo más amplio", reason="Elegir alcance de datos antes de infraestructura", unmeasured="Rendimiento, costes RPC y disponibilidad de historial"),
    dict(id="crypto-compare-prediction-sdk", candidates=["crypto-polymarket-py-sdk", "crypto-polymarket-py-clob-client", "crypto-polymarket-py-clob-client-v2"], decision="SDK unificado actual; repos legados sólo migración y referencia", reason="Fuentes oficiales documentan ambas deprecaciones", unmeasured="Compatibilidad local y estabilidad futura de API 0.x"),
    dict(id="crypto-compare-fundamentals", candidates=["crypto-defillama-dimension-adapters", "crypto-duneanalytics-spellbook"], provider_ids=["crypto-provider-token-terminal", "crypto-provider-dune"], decision="Fórmulas y eventos versionados para núcleo; proveedores como contraste de definiciones", reason="Adaptador público no garantiza upstream abierto; dashboard cerrado no prueba replicabilidad", unmeasured="Exactitud de importes e historial de revisiones de cada proveedor"),
]

search_groups = [
    ("Especialización y migraciones", ["site:github.com/Polymarket py-clob-client archived clob-client-v2 2026", "site:github.com/Polymarket \"polymarket-client\" Python unified", "site:github.com/graphsense graphsense-tagpack-tool archived successor"], "SDK unificado, deprecaciones y migraciones identificados; versiones verificadas contra README/release y archivos fijados por SHA"),
    ("Captura de valor y protocolo", ["site:hyperliquid.gitbook.io fees assistance fund HYPE burned", "site:docs.raydium.io protocol fees RAY buyback", "site:docs.uniswap.org protocol fee 2026 burn UNI", "site:blog.uniswap.org UNIfication fees burn 2026", "site:blog.uniswap.org protocol fees burn enabled December 2025 2026", "site:github.com/Uniswap \"protocol-fees\""], "Fuentes oficiales de fees, programa y anuncios; distinguir documentación de estado desplegado"),
    ("Adaptadores, stablecoins y licencias", ["site:github.com DefiLlama dimension-adapters fees hyperliquid index.ts", "site:github.com \"stablecoins\" DefiLlama", "site:github.com/DefiLlama \"stablecoins\" \"License\"", "site:github.com/DefiLlama \"emissions\" adapters", "DefiLlama stablecoins github peggedassets-server", "DefiLlama token unlocks github emissions adapters", "site:github.com/DefiLlama/dimension-adapters \"license\"", "site:github.com/DefiLlama/defillama-sdk \"license\""], "Ruta stablecoins corregida a peggedassets-server; emisiones no verificadas directamente; ausencia de licencia localizada no se convierte en permiso"),
    ("Infraestructura on-chain", ["site:github.com crypto onchain analytics open source sqd subsquid ethereum-etl cryo chainbase", "site:github.com paradigmxyz cryo README license", "site:github.com graphsense tagpacks confidence labels license", "site:github.com raydium-io raydium-sdk-V2 license", "site:github.com pump-fun pump-public-docs"], "Indexadores y esquemas comparados; rutas críticas inspeccionadas en diez proyectos"),
    ("Búsqueda internacional y fuera de GitHub", ["site:github.com 加密 链上 数据 分析 开源 Hyperliquid", "site:codeberg.org blockchain analytics cryptocurrency"], "No produjo candidatos adicionales suficientemente verificados; Codeberg limitado por acceso/robots. Cobertura internacional débil, no exhaustiva"),
    ("Retención, derivados y acceso", ["site:docs.polymarket.com api rate limits historical data", "site:docs.hyperliquid.xyz historical data candles snapshots retention", "site:docs.deribit.com public get_book_summary_by_currency mark_iv open_interest", "site:developers.binance.com liquidation order streams 1000ms all market", "site:developers.binance.com \"only the latest one liquidation\""], "Rate limits y snapshots documentados; no confirmación actual del supuesto Binance 1/s; no inventar retención completa"),
    ("Fuentes comerciales y definiciones", ["site:docs.tokenterminal.com financial metrics fees revenue tokenholder revenue", "site:docs.dune.com api pricing query credits data export", "site:tokenterminal.com \"Fees\" \"Tokenholder revenue\"", "site:tokenterminal.com \"Tokenholder revenue\" metrics", "site:tokenterminal.com \"Financial statements\" fees revenue"], "Dune/Token Terminal conservados como servicios cerrados; acceso documental, sin cuenta ni API pagada"),
    ("Contraejemplos de captura y oferta", ["site:docs.raydium.io \"12%\" buybacks fees", "site:hyperliquid.gitbook.io \"assistance fund\" \"burn\"", "site:hyperliquid.gitbook.io \"HYPE\" \"burned\"", "site:developers.circle.com CCTP burn mint USDC transfer supply"], "Nueva ruta Raydium consultada; RAY recomprado conservado en cuenta; CCTP aporta contraejemplo mint local versus entrada fiat"),
]
search_log = [dict(id="crypto-search-" + str(i + 1).zfill(2), date=DATE, engine="web.run public web search", purpose=g, queries=q, outcome=o, precision="Registro agrupado de consultas realizadas; no se inventan horas ni número de resultados") for i, (g, q, o) in enumerate(search_groups)]
search_log.append(dict(id="crypto-search-direct", date=DATE, engine="GitHub HTML, raw.githubusercontent.com, git ls-remote (sólo lectura)", purpose="Comprobación directa y fijación de versiones", queries=["HEAD y rutas README/licencia/manifest/rutas críticas de candidatos; URLs exactas en sources.json"], outcome="63 candidatos catalogados: 62 con lectura directa, 1 D0. Cinco URLs iniciales rechazadas/corregidas se conservan aparte. Diez revisiones estáticas V3", precision="HTTP status y SHA256 por ruta recuperada; fecha de commit no recuperada sistemáticamente"))
search_log.append(dict(id="crypto-search-canonical-docs", date=DATE, engine="Navegación directa de documentación oficial", purpose="Resolver enlaces rotos y leer mecanismos actuales", queries=["docs.raydium.io → reference/fee-comparison → ray/protocol-fees → ray/ray-buybacks", "docs.polymarket.com → api-reference/rate-limits", "developers.circle.com/cctp", "tokenterminal.com/explorer/metrics/tokenholder_revenue"], outcome="URLs canónicas recuperadas y límites documentales anotados; fallos originales preservados", precision="Sin autenticación, consultas a servicios de datos, contratos ni estado de wallets"))

write("candidates", candidates)
write("sources", list(sources.values()))
write("evidence", list(evidence.values()))
write("datasets", datasets)
write("providers", providers)
write("papers", papers)
write("methods", methods)
write("comparisons", comparisons)
write("search_log", search_log)
print(json.dumps(dict(candidates=len(candidates), sources=len(sources), evidence=len(evidence), datasets=len(datasets), providers=len(providers), papers=len(papers), methods=len(methods), comparisons=len(comparisons), search_groups=len(search_log))))
