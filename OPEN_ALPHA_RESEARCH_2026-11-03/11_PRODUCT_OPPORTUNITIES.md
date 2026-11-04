# Cartera de herramientas personales

16 conceptos, todos sin implementar. Las cinco primeras prioridades tienen diseños propios. El orden estratégico pondera el objetivo financiero y la complementariedad; no es una ordenación automática del score editorial. OP-13 puntúa alto como capacidad transversal y debe incluirse desde el primer piloto; OP-14 puede resolverse inicialmente con herramientas existentes. Ninguno obliga a construir una plataforma.

Los costes en jornadas son estimaciones de ingeniería para un alcance pequeño, no presupuestos cerrados ni plazos prometidos. El hardware no se midió. Una alternativa pública no implica datos ilimitados o redistribuibles.

| Prioridad | Concepto | Puntos | Primera pregunta |
|---|---|---|---|
| 1 | [Protocol Value & Dilution Analyzer](12_TOP_FIVE_BLUEPRINTS/01_protocol_value.md) | 84 | ¿Mejora el valor económico atribuible por token o solo la actividad del protocolo? |
| 2 | [Thesis Tracker con registro de evidencia](12_TOP_FIVE_BLUEPRINTS/02_thesis_tracker.md) | 87 | ¿Qué evidencia nueva cambia mi hipótesis y qué dato la refutaría? |
| 3 | [Market Regime & Liquidity Navigator](12_TOP_FIVE_BLUEPRINTS/03_regime_navigator.md) | 81 | ¿Qué escenarios favorecen las condiciones actuales y qué evidencia los contradice? |
| 4 | [Derivatives Stress Monitor](12_TOP_FIVE_BLUEPRINTS/04_derivatives_stress.md) | 77 | ¿Qué combinaciones de funding, OI, basis y liquidez sugieren fragilidad? |
| 5 | [Event Impact Research Lab](12_TOP_FIVE_BLUEPRINTS/05_event_lab.md) | 76 | ¿Cambió la reacción a un evento después de controlar mercado, filtración previa y régimen? |
| 6 | [Token Supply & Governance Change Monitor](#op-06) | 75 | ¿Qué cambio de oferta está confirmado, previsto o sujeto a decisión? |
| 7 | [On-Chain Capital Flow Explorer](#op-07) | 69 | ¿Qué movimiento de capital puede afirmarse con las etiquetas disponibles? |
| 8 | [Crypto Opportunity Screener](#op-08) | 71 | ¿Qué activos presentan discrepancias robustas que merecen lectura? |
| 9 | [Narrative & Sector Rotation Analyzer](#op-09) | 63 | ¿La atención coincide con crecimiento medible o solo con precio? |
| 10 | [Research Workbench con citas verificables](#op-10) | 70 | ¿Puedo reconstruir cada cifra y afirmación de un informe? |
| 11 | [Stablecoin Reserve & Liquidity Observatory](#op-11) | 71 | ¿Qué explica variaciones de stablecoin supply y quién captura el carry? |
| 12 | [Prediction Market Calibration Desk](#op-12) | 72 | ¿Cómo se calibran probabilidades comparables una vez considerados spreads y resolución? |
| 13 | [Data Revision & Source Disagreement Monitor](#op-13) | 88 | ¿Qué parte de la señal nace de una revisión del dato? |
| 14 | [Portfolio Thesis & Concentration Lens](#op-14) | 81 | ¿Parecen distintos mis tokens pero comparten el mismo riesgo? |
| 15 | [Forecast Utility Benchmark](#op-15) | 71 | ¿Mejora forecasting de volumen/volatilidad sobre una base simple y a qué coste? |
| 16 | [Organic Activity Quality Lens](#op-16) | 64 | ¿Persisten fees y usuarios cuando caen los incentivos? |

<a id="op-01"></a>

## OP-01 — Protocol Value & Dilution Analyzer

**Problema:** Comparar crecimiento económico, captura de valor y dilución con definiciones reconciliadas.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Mejora el valor económico atribuible por token o solo la actividad del protocolo?

**Datos:** Fees por tipo, revenue neto de pagos a LP/creadores, incentivos, recompras/burn, suministro y unlocks; HYPE/UNI/RAY/PUMP como casos; BTC/ETH como contexto.

**Bibliotecas:** DefiLlama dimension-adapters como referencia metodológica; SDKs oficiales; DuckDB, Pandera, DataComPy y marimo.

**Métodos:** Ledger contable por mecanismo/fecha, tasas normalizadas, escenarios de emisión, descomposición de cambios de ratios.

**Flujo:** Fuente→snapshot→reconciliación→mecanismo de captura→escenarios→ficha de discrepancias.

**Arquitectura mínima:** Un proceso batch semanal, Parquet y DuckDB; tabla de mecanismos revisada manualmente; informe local.

**Resultado:** Puente de fees a captura de token; escenarios y evidencia pendiente.

**Frecuencia:** Semanal; alertas por cambios de mecanismo

**Tiempo de consulta:** 5–8 minutos

**Limitaciones:** No es un DCF contractual; burn no es dividendo y supply circulante puede ser ambiguo.

**Coste técnico estimado:** 6–12 jornadas para un primer protocolo acotado; ampliar a tres e históricos completos requiere nueva estimación.

**Coste recurrente potencial:** Sin contratación: fuentes públicas permitidas; RPC/históricos completos pueden requerir pago, importe no cotizado.

**Riesgos:** Doble conteo, incentivos pagados en token, cambios retroactivos, límites de API.

**Cómo demostrar utilidad:** >=95% de cifras materiales trazadas; explicar toda divergencia material de definición; tiempo de revisión reducido20% en piloto.

**Incrementos:** Ficha manual1protocolo→comparador3→dilución y sensibilidad→alertas.

[Diseño preliminar completo](12_TOP_FIVE_BLUEPRINTS/01_protocol_value.md).

<a id="op-02"></a>

## OP-02 — Thesis Tracker con registro de evidencia

**Problema:** Evitar tesis que sobreviven a sus propios criterios de invalidación.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Qué evidencia nueva cambia mi hipótesis y qué dato la refutaría?

**Datos:** Documentos oficiales, eventos, métricas versionadas, tesis y criterios escritos por el usuario.

**Bibliotecas:** SQLite/DuckDB, Docling, Trafilatura, DataComPy; modelo de extracción opcional.

**Métodos:** Diff semántico con revisión, reglas deterministas, extracción estructurada con citas y abstención.

**Flujo:** Tesis→preguntas falsables→evidencias→cambio→revisión humana.

**Arquitectura mínima:** Una base local de tesis y evidencias; adquisición separada; lector de solo consulta.

**Resultado:** Resumen de cambios con fuente, contradicciones y decisión pendiente.

**Frecuencia:** Diaria o tras evento

**Tiempo de consulta:** 3–5 minutos

**Limitaciones:** No asignar confianza económica por número de documentos; fuentes correlacionadas no son evidencia independiente.

**Coste técnico estimado:** 4–8 jornadas para 3 tesis y 20 documentos

**Coste recurrente potencial:** Modo manual/local sin API de inferencia; inferencia alojada opcional no contratada.

**Riesgos:** Prompt injection, referencias inexistentes, falsa corroboración, extracción incorrecta.

**Cómo demostrar utilidad:** 100% de afirmaciones materiales con pasaje localizable; cero documentos tratados como instrucciones; menos contradicciones omitidas que checklist manual.

**Incrementos:** Plantilla manual→detección de cambios→extracción asistida→evaluación de abstención.

[Diseño preliminar completo](12_TOP_FIVE_BLUEPRINTS/02_thesis_tracker.md).

<a id="op-03"></a>

## OP-03 — Market Regime & Liquidity Navigator

**Problema:** Interpretar mercado y macro con sus ritmos y retrasos reales.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Qué escenarios favorecen las condiciones actuales y qué evidencia los contradice?

**Datos:** Precios/volumen diarios con universo histórico, stablecoin supply, ALFRED/FRED, ECB/BIS; ETF flujos solo si fuente/permiso/histórico son adecuados.

**Bibliotecas:** fredapi con selección explícita de vintage, statsmodels, ruptures, River, DuckDB.

**Métodos:** Percentiles robustos, momentum/amplitud, volatilidad/correlación, cambios de nivel en replay; escenario por bloques.

**Flujo:** Datos publicados→filtro temporal→indicadores simples→regímenes descriptivos→sensibilidad.

**Arquitectura mínima:** Batch diario; Parquet; configuración de indicadores y calendario de publicaciones.

**Resultado:** Mapa de escenario con indicadores, antigüedad y discrepancias.

**Frecuencia:** Diaria y revisión semanal

**Tiempo de consulta:** 3–5 minutos

**Limitaciones:** M2 global depende de divisas y calendario; stablecoin supply no equivale a poder comprador; régimen no es predicción.

**Coste técnico estimado:** 6–10 jornadas para un panel inicial

**Coste recurrente potencial:** Datos públicos; cobertura y condiciones varían, sin cuotas premium contratadas.

**Riesgos:** Revisiones macro, latencias, selección retrospectiva de regímenes, correlaciones espurias.

**Cómo demostrar utilidad:** Cero fuga temporal en fixtures; estabilidad fuera de muestra; mejora de comprensión evaluada frente a3indicadores base.

**Incrementos:** BTC/ETH+macro mínima→amplitud→stablecoins→comparación de regímenes.

[Diseño preliminar completo](12_TOP_FIVE_BLUEPRINTS/03_regime_navigator.md).

<a id="op-04"></a>

## OP-04 — Derivatives Stress Monitor

**Problema:** Separar apalancamiento observado de mapas de liquidación inferidos.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Qué combinaciones de funding, OI, basis y liquidez sugieren fragilidad?

**Datos:** Funding por intervalo/venue, OI y denominación, precios mark/index, profundidad observada, liquidaciones reportadas y disponibilidad.

**Bibliotecas:** CCXT y clientes oficiales de solo lectura; DuckDB, pandas/Polars, marimo.

**Métodos:** Normalización de contratos y frecuencias, percentiles por venue, escenarios de shocks, score explicable con abstención.

**Flujo:** Snapshots→unidades→comparación venues→señales observables→escenarios de estrés.

**Arquitectura mínima:** 2–3 venues, BTC/ETH/HYPE según cobertura, batch horario y resumen diario; sin motor de órdenes.

**Resultado:** Panel de presión y calidad con observaciones separadas de estimaciones.

**Frecuencia:** Diaria; intradía solo para investigación

**Tiempo de consulta:** 2–4 minutos

**Limitaciones:** No se conocen todas las posiciones ni liquidaciones futuras; feed puede estar muestreado.

**Coste técnico estimado:** 6–12 jornadas para 2 venues

**Coste recurrente potencial:** Endpoints públicos limitados; historial tick/profundidad probablemente requiere recolección prospectiva o pago.

**Riesgos:** Cambios de especificación, lag, posiciones agregadas, fallos de feed confundidos con calma.

**Cómo demostrar utilidad:** Detectar interrupciones y unidades erróneas; evaluar recall/precision de episodios con etiquetas predefinidas y tasa de alertas.

**Incrementos:** Funding+OI→basis→profundidad→replay de episodios.

[Diseño preliminar completo](12_TOP_FIVE_BLUEPRINTS/04_derivatives_stress.md).

<a id="op-05"></a>

## OP-05 — Event Impact Research Lab

**Problema:** Estudiar catalizadores sin seleccionar a posteriori solo ejemplos favorables.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Cambió la reacción a un evento después de controlar mercado, filtración previa y régimen?

**Datos:** Registro de anuncios con primer conocimiento, timestamps inciertos, retornos, controles y lista completa de eventos elegibles.

**Bibliotecas:** statsmodels, arch, SciPy; DuckDB y calendario de eventos propio.

**Métodos:** Retorno anormal, bootstrap por bloques/eventos, placebos, controles sintéticos cuando sean defendibles, FDR.

**Flujo:** Evento→cronología→ventanas predefinidas→controles→estimación→sensibilidad.

**Arquitectura mínima:** Dataset pequeño versionado, notebook de análisis y reporte estático.

**Resultado:** Distribución de efectos, solapamientos, placebos y explicaciones alternativas.

**Frecuencia:** Semanal o por lote de eventos

**Tiempo de consulta:** 10–20 minutos por estudio

**Limitaciones:** Identificación causal débil con eventos endógenos, muestra pequeña y noticias superpuestas.

**Coste técnico estimado:** 8–15 jornadas para 1familia de 20–40 eventos

**Coste recurrente potencial:** Fuentes públicas y curación manual; archivo de noticias histórico puede tener coste no cotizado.

**Riesgos:** Look-ahead en etiquetas, múltiples ensayos, horas de anuncio incorrectas, errores de independencia.

**Cómo demostrar utilidad:** Cronología auditada; todos los eventos elegibles registrados; intervalos y n publicados; resultado negativo aceptado.

**Incrementos:** Una familia retrospectiva→placebos→protocolo prospectivo→comparación por régimen.

[Diseño preliminar completo](12_TOP_FIVE_BLUEPRINTS/05_event_lab.md).

<a id="op-06"></a>

## OP-06 — Token Supply & Governance Change Monitor

**Problema:** Vincular emisiones y cambios de gobernanza a su conocimiento público.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Qué cambio de oferta está confirmado, previsto o sujeto a decisión?

**Datos:** Contratos de vesting, supply por bloque, propuestas/votos, burns y calendario anunciado.

**Bibliotecas:** SDKs blockchain, DuckDB, Pydantic y lectores oficiales.

**Métodos:** Estado por evento, incertidumbre por rango, net issuance, reconciliación de balance.

**Flujo:** Anuncio/contrato→verificación→fecha prevista/ejecutada→escenario.

**Arquitectura mínima:** Ficheros versionados y revisión semanal.

**Resultado:** Calendario con estado, magnitud y fuente.

**Frecuencia:** Semanal

**Tiempo de consulta:** 3 minutos

**Limitaciones:** Desbloqueo no implica venta; cambios de vesting pueden invalidar calendario.

**Coste técnico estimado:** 4–8 jornadas

**Coste recurrente potencial:** RPC público o lectura manual; históricos avanzados no presupuestados.

**Riesgos:** Direcciones equivocadas, bridges y custodios confundidos con supply nuevo.

**Cómo demostrar utilidad:** Conciliar cambios de supply y no etiquetar previsiones como ejecuciones.

**Incrementos:** 3 tokens→contratos→escenarios→integrar OP-01.


<a id="op-07"></a>

## OP-07 — On-Chain Capital Flow Explorer

**Problema:** Separar transferencias, puentes y cambios de tenencia de entradas netas económicas.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Qué movimiento de capital puede afirmarse con las etiquetas disponibles?

**Datos:** Logs, transferencias, bridges, etiquetas con procedencia/confianza, precios a la hora del flujo.

**Bibliotecas:** GraphSense, ethereum-etl/Subsquid/HyperSync como candidatos; NetworkX y DuckDB.

**Métodos:** Netting por entidad probabilística, graph cuts, conciliación de puentes, sensibilidad a etiquetas.

**Flujo:** Bloques→decodificación→etiquetas→deduplicación→flujos/intervalos.

**Arquitectura mínima:** Una cadena y universo de contratos limitado; no nodo/indexador global inicial.

**Resultado:** Grafo y bandas de flujo con transacciones de respaldo.

**Frecuencia:** Semanal

**Tiempo de consulta:** 5–10 minutos

**Limitaciones:** No identidad exacta ni intención de inversión; wrapping/bridge puede duplicar.

**Coste técnico estimado:** 10–20 jornadas

**Coste recurrente potencial:** RPC/indexador limitado; acceso archive puede ser pago.

**Riesgos:** Clustering falso, bots, reorg, cobertura incompleta.

**Cómo demostrar utilidad:** Fracción reconciliada y sensibilidad a quitar etiquetas dudosas.

**Incrementos:** Stablecoin+bridge1→DEX1→más redes solo si útil.


<a id="op-08"></a>

## OP-08 — Crypto Opportunity Screener

**Problema:** Reducir el universo a preguntas investigables.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Qué activos presentan discrepancias robustas que merecen lectura?

**Datos:** Universo point-in-time, liquidez, fundamentals, supply, momentum y calidad.

**Bibliotecas:** DuckDB, pandas/Polars, skfolio y funciones robustas.

**Métodos:** Ranking por bloques independientes, winsorización, neutralización por sector/tamaño y penalización por falta de datos.

**Flujo:** Universo→filtros→factores→ranking→ficha de hipótesis.

**Arquitectura mínima:** Batch semanal sobre datos ya curados, sin nuevo proveedor inicialmente.

**Resultado:** Lista corta explicada, sin botón de compra.

**Frecuencia:** Semanal

**Tiempo de consulta:** 5 minutos

**Limitaciones:** Peso del score arbitrario; universo incompleto y tokens desaparecidos sesgan.

**Coste técnico estimado:** 5–10 jornadas tras datos fiables

**Coste recurrente potencial:** Depende de OP-01/03/06; no contratar solo por cobertura.

**Riesgos:** Sobreajuste y falsa precisión.

**Cómo demostrar utilidad:** Estabilidad del ranking, carga de investigación útil, cobertura de desaparecidos.

**Incrementos:** Reglas simples→sensitivity→validación prospectiva.


<a id="op-09"></a>

## OP-09 — Narrative & Sector Rotation Analyzer

**Problema:** Contrastar popularidad narrativa con actividad económica.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿La atención coincide con crecimiento medible o solo con precio?

**Datos:** Noticias con timestamps, documentos, clasificación sectorial versionada y uso/revenue.

**Bibliotecas:** Embeddings con licencia revisada, clustering, River, pandas.

**Métodos:** Clustering temporal, deduplicación de noticias, amplitud sectorial y comparación de retrasos.

**Flujo:** Texto→deduplicación→temas→métricas→contradicciones.

**Arquitectura mínima:** Lote semanal de fuentes limitadas, extracción local opcional.

**Resultado:** Mapa de narrativas con evidencia de actividad.

**Frecuencia:** Semanal

**Tiempo de consulta:** 5 minutos

**Limitaciones:** Bots, cobertura idiomática y sector cambiante; sentimiento no es retorno.

**Coste técnico estimado:** 8–15 jornadas

**Coste recurrente potencial:** Archivo de noticias puede ser coste dominante.

**Riesgos:** Contaminación retrospectiva y copyright.

**Cómo demostrar utilidad:** Coherencia humana de clusters y mejora frente a conteo simple.

**Incrementos:** Una narrativa→2 fuentes→contraste on-chain.


<a id="op-10"></a>

## OP-10 — Research Workbench con citas verificables

**Problema:** Consultar datos y documentos sin perder procedencia.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Puedo reconstruir cada cifra y afirmación de un informe?

**Datos:** Snapshots, fuentes con permisos, tablas y fragmentos localizables.

**Bibliotecas:** Docling, DuckDB, marimo; Haystack/Pydantic AI opcionales.

**Métodos:** Recuperación híbrida, consultas permitidas, validación estructurada y abstención.

**Flujo:** Pregunta→fuentes→cálculo determinista→respuesta con evidencia.

**Arquitectura mínima:** Composición ligera de herramientas autónomas; sin superagente.

**Resultado:** Informe con enlaces a filas y documentos.

**Frecuencia:** Bajo demanda

**Tiempo de consulta:** 10 minutos

**Limitaciones:** Una respuesta citada aún puede interpretar mal; RAG no elimina inyección.

**Coste técnico estimado:** 10–20 jornadas después de OP-02

**Coste recurrente potencial:** Modelo alojado opcional; importe sujeto a uso y aprobación.

**Riesgos:** Coste inferencia, ejecución SQL peligrosa, fuga de datos.

**Cómo demostrar utilidad:** Exactitud de cifras, citas localizables, tasa de abstención y coste por pregunta.

**Incrementos:** Búsqueda manual→recuperación→síntesis asistida.


<a id="op-11"></a>

## OP-11 — Stablecoin Reserve & Liquidity Observatory

**Problema:** Separar emisión, respaldo, rentabilidad del emisor y liquidez negociable.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Qué explica variaciones de stablecoin supply y quién captura el carry?

**Datos:** Supply por red, reservas/atestaciones, T-bill rates, rescates, depeg, bridge supply.

**Bibliotecas:** Document extraction, DefiLlama stablecoins como referencia, DuckDB, series macro.

**Métodos:** Conciliación activos/pasivos por fecha, escenarios de tipos y rescates.

**Flujo:** Atestación→periodo→fecha conocida→supply→riesgos.

**Arquitectura mínima:** Informe mensual con alertas de depeg/calidad.

**Resultado:** Balance comparado y lag de atestaciones.

**Frecuencia:** Semanal/mensual

**Tiempo de consulta:** 5 minutos

**Limitaciones:** Atestación no auditoría continua; rendimiento reservas no pertenece al tenedor.

**Coste técnico estimado:** 8–12 jornadas

**Coste recurrente potencial:** Lectura pública; cobertura granular no garantizada.

**Riesgos:** Doble conteo bridged/canonical, reservas no transparentes.

**Cómo demostrar utilidad:** Conciliación supply y separación explícita de beneficiarios de rendimiento.

**Incrementos:** 2 stablecoins→redes→escenarios.


<a id="op-12"></a>

## OP-12 — Prediction Market Calibration Desk

**Problema:** Evaluar precios de probabilidad según reglas y liquidez.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Cómo se calibran probabilidades comparables una vez considerados spreads y resolución?

**Datos:** Mercados cerrados/abiertos, reglas versionadas, precios históricos, liquidez, cierre y resultado.

**Bibliotecas:** Polymarket PublicClient actual, DuckDB, métricas Brier/log loss.

**Métodos:** Calibración por horizon/bucket, bandas, resolución ambigua y sesgo de selección.

**Flujo:** Regla→cohorte→probabilidad elegible→resolución→evaluación.

**Arquitectura mínima:** Colección prospectiva reducida sin órdenes.

**Resultado:** Curvas de calibración y casos ambiguos.

**Frecuencia:** Semanal

**Tiempo de consulta:** 10 minutos

**Limitaciones:** Precio no probabilidad pura; fees/spread y selección de supervivientes.

**Coste técnico estimado:** 6–12 jornadas

**Coste recurrente potencial:** Endpoints públicos sujetos a límites; no operaciones.

**Riesgos:** Reglas modificadas, markets anulados, dependencia entre eventos.

**Cómo demostrar utilidad:** Cobertura de todos los mercados elegibles y calibración fuera de muestra.

**Incrementos:** Una categoría→reglas archivadas→cohortes.


<a id="op-13"></a>

## OP-13 — Data Revision & Source Disagreement Monitor

**Problema:** Detectar si cambió el mercado o cambió el proveedor.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Qué parte de la señal nace de una revisión del dato?

**Datos:** Dos snapshots de la misma serie, método/versión y fuente alternativa.

**Bibliotecas:** DataComPy, DuckDB, Pandera, hashes.

**Métodos:** Diff por clave, umbral material por unidad, separación precio/cantidad/coverage.

**Flujo:** Snapshot→diff→clasificación→recomputación marcada.

**Arquitectura mínima:** Pequeño módulo autónomo de archivos, sin servidor.

**Resultado:** Registro de revisiones y métricas afectadas.

**Frecuencia:** Diaria

**Tiempo de consulta:** 1–3 minutos

**Limitaciones:** Dos fuentes pueden compartir origen y errores.

**Coste técnico estimado:** 3–6 jornadas

**Coste recurrente potencial:** Fuentes existentes, almacenamiento local.

**Riesgos:** Tratar discrepancia como error sin conocer definiciones.

**Cómo demostrar utilidad:** Todas las revisiones materiales detectadas; no sobrescribir historia.

**Incrementos:** 1 serie→3 fuentes→avisos de metodología.


<a id="op-14"></a>

## OP-14 — Portfolio Thesis & Concentration Lens

**Problema:** Relacionar riesgo de cartera con tesis y dependencias comunes.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Parecen distintos mis tokens pero comparten el mismo riesgo?

**Datos:** Posiciones introducidas localmente, precios, stablecoins, cadenas, custodios y tesis.

**Bibliotecas:** PyPortfolioOpt/skfolio, Riskfolio-Lib, pandas.

**Métodos:** Exposiciones por bloques, correlación robusta, expected shortfall y shocks narrativos.

**Flujo:** Posición→mapa dependencias→escenarios→concentración.

**Arquitectura mínima:** Fichero local sin conexión a exchange; reporte semanal.

**Resultado:** Mapa de riesgos y escenarios de pérdidas.

**Frecuencia:** Semanal

**Tiempo de consulta:** 5 minutos

**Limitaciones:** Correlaciones cambian en crisis; riesgo contraparte no se deduce de retornos.

**Coste técnico estimado:** 4–8 jornadas

**Coste recurrente potencial:** Sin datos privados enviados ni API de trading.

**Riesgos:** Falsa precisión de VaR, rendimientos cortos, pesos faltantes.

**Cómo demostrar utilidad:** Reconstrucción exacta de exposición; sensibilidad bajo3shocks.

**Incrementos:** Cartera manual→factores→stress.


<a id="op-15"></a>

## OP-15 — Forecast Utility Benchmark

**Problema:** Comprobar si un modelo nuevo ayuda en una tarea concreta.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Mejora forecasting de volumen/volatilidad sobre una base simple y a qué coste?

**Datos:** Series con vintages, horizontes definidos, splits y coste de cómputo.

**Bibliotecas:** StatsForecast/MLForecast, Chronos2, fev; modelos con licencia compatible.

**Métodos:** Naive/estacional, boosting, cuantiles, WIS/MASE, calibración y ablations.

**Flujo:** Contrato de tarea→baselines→holdout→comparación→abstención.

**Arquitectura mínima:** Experimento aislado futuro, subset pequeño; sin modelos gigantes.

**Resultado:** Matriz de errores/coste y decisión de mantener o descartar.

**Frecuencia:** Por experimento

**Tiempo de consulta:** 20 minutos de revisión

**Limitaciones:** Benchmark general no prueba rentabilidad; pretraining cutoff incierto.

**Coste técnico estimado:** 5–10 jornadas sin afinar muchos modelos

**Coste recurrente potencial:** CPU primero; GPU/API solo tras presupuesto aprobado.

**Riesgos:** Contaminación de entrenamiento, covariables futuras, tuning repetido.

**Cómo demostrar utilidad:** Mejora robusta sobre base bajo mismo dataset y recursos.

**Incrementos:** Naive→boosting→un foundation model.


<a id="op-16"></a>

## OP-16 — Organic Activity Quality Lens

**Problema:** Distinguir crecimiento económico de actividad incentivada o circular.

**Usuario:** Analista e inversor particular, horizonte principal3–18 meses.

**Pregunta financiera:** ¿Persisten fees y usuarios cuando caen los incentivos?

**Datos:** Swaps/logs, incentivos, cohortes, fees pagadas y patrones de repetición.

**Bibliotecas:** Indexadores selectivos, NetworkX, Polars, métodos de cohortes.

**Métodos:** Retención por cohortes, sensibilidad a filtros de bots, flujos circulares y stress sin subvención.

**Flujo:** Actividad→cohortes→filtros transparentes→rangos→contraste.

**Arquitectura mínima:** Un protocolo/red; no clasificador universal de wallets.

**Resultado:** Bandas de crecimiento orgánico y casos dudosos.

**Frecuencia:** Mensual

**Tiempo de consulta:** 10 minutos

**Limitaciones:** Usuario no equivale a dirección; heurísticas pueden penalizar actividad legítima.

**Coste técnico estimado:** 10–20 jornadas

**Coste recurrente potencial:** Histórico de logs potencialmente costoso.

**Riesgos:** Etiquetas falsas y criterios post hoc.

**Cómo demostrar utilidad:** Estabilidad al variar filtros y validación manual de muestras.

**Incrementos:** Un programa incentivos→cohortes→event study.

