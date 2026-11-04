# Algoritmos y métodos transferibles

El conocimiento reutilizable es más amplio que los repositorios. Estas fichas separan problema, supuestos, datos, validación, fallos y situaciones de abstención. Las propuestas cripto se apoyan en implementación/documentación inspeccionada, pero no se han calculado ni probado sobre una cartera real.

## Orden de trabajo recomendado

Primero identidad, unidad y fecha de conocimiento; después una base sencilla; finalmente modelos más complejos si mejoran una tarea predefinida. Para horizontes de 3–18 meses, retornos de un año calculados cada día se solapan: no son cientos de observaciones independientes. La longitud efectiva de la muestra y el número de regímenes limitan cualquier inferencia.

La validación temporal abarca todo el pipeline: universo, limpieza, escalado, selección de variables, ajuste, embeddings/memoria y ranking. Añadir información futura no debe cambiar una salida pasada. Purga/embargo deben corresponder al intervalo de las etiquetas, no solo al número de filas; CPCV no sustituye seguimiento prospectivo. Un modelo de lenguaje puede recordar hechos posteriores aunque sus herramientas respeten el corte.

Para regímenes, distinguir probabilidades filtradas de suavizadas y detección online de segmentación offline. Para causalidad, definir tratamiento, cronología, controles y supuestos; una correlación rezagada o una biblioteca causal no establece identificación. Para tests múltiples, registrar todos los ensayos: ningún ajuste rescata un historial selectivo de resultados.

En riesgo, expected shortfall es pérdida media de cola bajo una distribución estimada, no límite de pérdida. VaR puede infravalorar liquidez, gaps y contraparte. En cripto, documentar calendario24/7, convención de anualización, tipos de contratos y exposición a stablecoins. No trasladar por defecto252sesiones o frecuencia de funding de otro mercado.

En valoración, el puente de fees a captura es un registro de mecanismos, no una identidad universal revenue=beneficio del token. Un unlock no siempre crea tokens; mint entre cadenas puede compensar burn en otra. En grafos, evaluar qué cambia al retirar etiquetas inciertas antes de atribuir flujos a entidades.

## Fichas de técnicas

### method-infra-bitemporal-join — Selección bitemporal por ventanas

**Problema:** Elegir datos conocidos sin usar revisiones posteriores.

**Supuestos:** Identidad y tiempos de evento/conocimiento distintos.

**Datos y frecuencia:** Según métrica; diario/semanal en el alcance inicial.

**Cómo validar:** Invariancia de consultas pasadas al añadir futuro.

**Fallos habituales:** ASOF por fecha económica; empates no resueltos; eventos futuros conocidos excluidos.

**Implementación sencilla o reutilización:** Consultar diseño y revisión del componente; no se implementó aquí.

**Valor para cripto:** Hace auditables fundamentales y macro.

**Cuándo abstenerse:** No inventar fecha de publicación; si falta, marcar reconstrucción.

**Implementaciones/candidatos:** [duckdb](https://github.com/duckdb/duckdb), [quant-feature-store](https://github.com/sophie-nguyenthuthuy/quant-feature-store).

**Fuentes:** [duckdb — repositorio](https://github.com/duckdb/duckdb), [duckdb/LICENSE](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/LICENSE), [duckdb/README.md](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/README.md), [duckdb/src/execution/operator/join/physical_asof_join.cpp](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/src/execution/operator/join/physical_asof_join.cpp). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-infra-reconciliation — Reconciliación y tolerancias por unidad

**Problema:** Distinguir cambios de proveedor de cambios económicos.

**Supuestos:** Misma definición, unidad, cobertura y claves.

**Datos y frecuencia:** Según métrica; diario/semanal en el alcance inicial.

**Cómo validar:** Cambios sintéticos materiales/no materiales y revisión humana.

**Fallos habituales:** Tolerancia global oculta cambios; referencia numérica asimétrica.

**Implementación sencilla o reutilización:** Consultar diseño y revisión del componente; no se implementó aquí.

**Valor para cripto:** Detecta artefactos de revenue/supply antes de rankear.

**Cuándo abstenerse:** No comparar métricas con beneficiarios o periodos distintos.

**Implementaciones/candidatos:** [datacompy](https://github.com/capitalone/datacompy), [pandera](https://github.com/unionai-oss/pandera).

**Fuentes:** [datacompy — repositorio](https://github.com/capitalone/datacompy), [datacompy/LICENSE](https://raw.githubusercontent.com/capitalone/datacompy/5a7a1eac257c2efdfa9a6f162647233c4ee7de9f/LICENSE), [datacompy/README.md](https://raw.githubusercontent.com/capitalone/datacompy/5a7a1eac257c2efdfa9a6f162647233c4ee7de9f/README.md), [datacompy/datacompy/core.py](https://raw.githubusercontent.com/capitalone/datacompy/5a7a1eac257c2efdfa9a6f162647233c4ee7de9f/datacompy/core.py). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-infra-freshness — Presupuesto de frescura y retraso

**Problema:** Evitar que fallos se interpreten como calma de mercado.

**Supuestos:** Timestamp original/acquisición y política por métrica.

**Datos y frecuencia:** Según métrica; diario/semanal en el alcance inicial.

**Cómo validar:** Cortes simulados, datos caducados y estado de abstención.

**Fallos habituales:** HTTP200 desde caché tratado como dato nuevo.

**Implementación sencilla o reutilización:** Consultar diseño y revisión del componente; no se implementó aquí.

**Valor para cripto:** Reduce alertas financieras basadas en feed congelado.

**Cuándo abstenerse:** No afirmar latencia exacta sin hora pública verificable.

**Implementaciones/candidatos:** [requests-cache](https://github.com/requests-cache/requests-cache), [dlt](https://github.com/dlt-hub/dlt).

**Fuentes:** [requests-cache — repositorio](https://github.com/requests-cache/requests-cache), [requests-cache/LICENSE](https://raw.githubusercontent.com/requests-cache/requests-cache/abe06a833cfb35a885f371d1b3db1199b3a968b5/LICENSE), [requests-cache/README.md](https://raw.githubusercontent.com/requests-cache/requests-cache/abe06a833cfb35a885f371d1b3db1199b3a968b5/README.md), [requests-cache/requests_cache/session.py](https://raw.githubusercontent.com/requests-cache/requests-cache/abe06a833cfb35a885f371d1b3db1199b3a968b5/requests_cache/session.py). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-infra-dependency-graph — Grafo de dependencias de cálculos

**Problema:** Recalcular solo lo afectado al cambiar supuestos.

**Supuestos:** Dependencias explícitas y entradas versionadas.

**Datos y frecuencia:** Según métrica; diario/semanal en el alcance inicial.

**Cómo validar:** Modificar un supuesto y cotejar descendientes/resultados.

**Fallos habituales:** Estado externo, llamada repetida o datos cambiantes fuera del grafo.

**Implementación sencilla o reutilización:** Consultar diseño y revisión del componente; no se implementó aquí.

**Valor para cripto:** Exploración reproducible de tesis y escenarios.

**Cuándo abstenerse:** No usar como sustituto de provenance de datos.

**Implementaciones/candidatos:** [marimo](https://github.com/marimo-team/marimo).

**Fuentes:** [marimo — repositorio](https://github.com/marimo-team/marimo), [marimo/LICENSE](https://raw.githubusercontent.com/marimo-team/marimo/54552ec3137df83992ac29aa73d1adf73eb252b1/LICENSE), [marimo/README.md](https://raw.githubusercontent.com/marimo-team/marimo/54552ec3137df83992ac29aa73d1adf73eb252b1/README.md), [marimo/marimo/_runtime/dataflow/graph.py](https://raw.githubusercontent.com/marimo-team/marimo/54552ec3137df83992ac29aa73d1adf73eb252b1/marimo/_runtime/dataflow/graph.py). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-point-in-time — Disponibilidad temporal y vintages

**Problema:** Reproducir lo que podía conocerse cuando se formuló una hipótesis.

**Supuestos:** Fechas de publicación/revisión reales; fuente y versión conservadas.

**Datos y frecuencia:** Periodos contables/macro y timestamps de disponibilidad; diario o semanal.

**Cómo validar:** Prueba de invariancia: añadir una revisión futura no altera ninguna consulta anterior.

**Fallos habituales:** Usar fecha del periodo como publicación; mezclar first-release con última vintage conocida.

**Implementación sencilla o reutilización:** Tabla append-only y selección última vintage por periodo con available_at<=t.

**Valor para cripto:** Evita que revenue revisado o PIB final mejore falsamente un screener.

**Cuándo abstenerse:** Si falta fecha de conocimiento, abstenerse o analizar escenarios de retraso; no backtest exacto.

**Implementaciones/candidatos:** [fredapi](https://github.com/mortada/fredapi), [Qlib](https://github.com/microsoft/qlib).

**Fuentes:** [FRED / ALFRED](https://alfred.stlouisfed.org/help). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-mixed-frequency — Factores dinámicos de frecuencia mixta

**Problema:** Resumir series macro publicadas de forma asíncrona.

**Supuestos:** Modelo de estados razonable, transformaciones y datos faltantes especificados.

**Datos y frecuencia:** Series mensuales/trimestrales con vintages y borde incompleto.

**Cómo validar:** Nowcast pseudo-real-time por fecha de publicación contra último valor/AR simple.

**Fallos habituales:** Forward-fill que simula información diaria, normalización global y smoothing retrospectivo.

**Implementación sencilla o reutilización:** DynamicFactorMQ o pocos indicadores normalizados con calendario de publicación.

**Valor para cripto:** Contexto de crecimiento/liquidez con incertidumbre, separado de retorno cripto.

**Cuándo abstenerse:** Cuando solo existen 2-3 series o no se dispone de vintages; preferir tablero transparente.

**Implementaciones/candidatos:** [statsmodels](https://github.com/statsmodels/statsmodels), [FRED-MD](https://www.stlouisfed.org/research/economists/mccracken/fred-databases), [FRED-QD](https://www.stlouisfed.org/research/economists/mccracken/fred-databases).

**Fuentes:** [dfm](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.dynamic_factor_mq.DynamicFactorMQ.html). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-pelt — PELT y costes de cambio estructural

**Problema:** Localizar rupturas en nivel, dispersión o composición multivariable.

**Supuestos:** Segmentos suficientemente largos, coste apropiado y penalización predefinida.

**Datos y frecuencia:** Diario/semanal; variables escaladas con información pasada.

**Cómo validar:** Replay de prefijos; medir retraso, falsas alarmas y desplazamiento de ruptura.

**Fallos habituales:** Etiquetas retrospectivas usadas como señales tempranas; seleccionar penalización por resultado de inversión.

**Implementación sencilla o reutilización:** PELT sobre un índice sencillo; comparar CUSUM.

**Valor para cripto:** Detectar cambios de revenue, financiación o amplitud que merecen investigación.

**Cuándo abstenerse:** No usar como prueba de régimen causal ni detector prospectivo sin replay.

**Implementaciones/candidatos:** [ruptures](https://github.com/deepcharles/ruptures).

**Fuentes:** [ruptures](https://github.com/deepcharles/ruptures). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-cusum — Monitorización CUSUM/MOSUM

**Problema:** Avisar cuando residuos o parámetros dejan de ser compatibles con una referencia.

**Supuestos:** Periodo de referencia estable y error definido.

**Datos y frecuencia:** Residuos de modelos sencillos o series estandarizadas; diario/semanal.

**Cómo validar:** Calibrar tasa de falsa alarma fuera de muestra y sensibilidad a outliers.

**Fallos habituales:** Confundir un outlier con ruptura persistente; recalibrar umbral tras observar el evento.

**Implementación sencilla o reutilización:** CUSUM sobre residuo robusto con umbral fijado.

**Valor para cripto:** Alerta ligera para cambios de régimen sin estados de caja negra.

**Cuándo abstenerse:** Referencia inestable o alertas múltiples sin control de falsos descubrimientos.

**Implementaciones/candidatos:** [strucchange (mirror CRAN)](https://github.com/cran/strucchange), [statsmodels](https://github.com/statsmodels/statsmodels).

**Fuentes:** [cusum](https://zeileis.codeberg.page/strucchange/man/mefp.html). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-markov-regime — Modelos de Markov/HMM con probabilidades filtradas

**Problema:** Representar estados latentes y transiciones inciertas.

**Supuestos:** Número de estados razonable, distribuciones y persistencia compatibles con datos.

**Datos y frecuencia:** Retornos/volatilidad/funding diario; suficiente duración por estado.

**Cómo validar:** Reajuste walk-forward; probabilidades filtradas, estabilidad de etiquetas y calibración.

**Fallos habituales:** Usar estados suavizados con datos futuros; múltiples óptimos e intercambio de etiquetas.

**Implementación sencilla o reutilización:** Dos estados y baseline umbral de volatilidad.

**Valor para cripto:** Resumen probabilístico de fragilidad; nunca orden de inversión directa.

**Cuándo abstenerse:** Pocas crisis independientes o estados que cambian por completo al mover la ventana.

**Implementaciones/candidatos:** [hmmlearn](https://github.com/hmmlearn/hmmlearn), [statsmodels](https://github.com/statsmodels/statsmodels).

**Fuentes:** [hmm](https://www.statsmodels.org/stable/generated/statsmodels.tsa.regime_switching.markov_regression.MarkovRegression.predict.html). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-purged-cv — Walk-forward, purga y embargo

**Problema:** Reducir contaminación entre muestras con etiquetas solapadas.

**Supuestos:** Horizonte de etiqueta/feature identificado y universo histórico correcto.

**Datos y frecuencia:** Panel de features con intervalos de resultado, no solo filas.

**Cómo validar:** Comprobar intersección de intervalos y pipeline ajustado solo en entrenamiento.

**Fallos habituales:** Purga cero por defecto, usar filas en tiempo irregular, normalizar antes del split.

**Implementación sencilla o reutilización:** WalkForward más eliminación explícita de intervalos superpuestos.

**Valor para cripto:** Auditar screeners a 3–18 meses; su tamaño efectivo puede ser mucho menor que filas diarias.

**Cuándo abstenerse:** CPCV no sustituye un periodo prospectivo ni resuelve cambios estructurales.

**Implementaciones/candidatos:** [skfolio](https://github.com/skfolio/skfolio).

**Fuentes:** [skfolio](https://github.com/skfolio/skfolio). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-block-bootstrap — Bootstrap temporal por bloques

**Problema:** Cuantificar dispersión preservando dependencia local.

**Supuestos:** Dependencia de corto alcance y cierta estabilidad local.

**Datos y frecuencia:** Retornos/pérdidas sincronizados de todas las variantes.

**Cómo validar:** Rango de longitudes de bloque, semillas registradas y sensibilidad por régimen.

**Fallos habituales:** Barajar puntos independientes, bloques demasiado cortos, creer que remuestreo crea información.

**Implementación sencilla o reutilización:** StationaryBootstrap con bloque justificado y varias longitudes.

**Valor para cripto:** Intervalos de ES, diferencias de métricas y estabilidad del ranking.

**Cuándo abstenerse:** Historial muy corto o único episodio que domina el resultado.

**Implementaciones/candidatos:** [arch](https://github.com/bashtage/arch).

**Fuentes:** [arch](https://github.com/bashtage/arch). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-spa-mcs — SPA, StepM y Model Confidence Set

**Problema:** Comparar muchas variantes contra baseline sin ignorar búsqueda múltiple.

**Supuestos:** Conjunto de intentos registrado, pérdidas homogéneas y dependencia controlable.

**Datos y frecuencia:** Matriz T×K de pérdidas sobre fechas idénticas.

**Cómo validar:** Baseline simple, bloques apropiados, todas las variantes incluidas.

**Fallos habituales:** Presentar solo ganadores; confundir p-value con probabilidad de beneficio.

**Implementación sencilla o reutilización:** SPA primero; MCS si interesa conjunto de modelos indistinguibles.

**Valor para cripto:** Evitar escoger señales de fundamentos por casualidad de backtest.

**Cuándo abstenerse:** Datos con leakage: corregirlos antes, la estadística no los detecta.

**Implementaciones/candidatos:** [arch](https://github.com/bashtage/arch).

**Fuentes:** [arch comparisons](https://bashtage.github.io/arch/multiple-comparison/multiple-comparisons.html). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-deflated-sharpe — Deflated Sharpe Ratio

**Problema:** Descontar inflación del Sharpe por múltiples ensayos y no normalidad.

**Supuestos:** Número efectivo de ensayos, duración, sesgo y curtosis estimados de modo honesto.

**Datos y frecuencia:** Retornos y registro completo de búsqueda; frecuencia coherente.

**Cómo validar:** Reproducir ejemplo del paper, escenarios para dependencia de ensayos y baseline nulo.

**Fallos habituales:** Contar solo estrategias publicadas; usar independencia ficticia; tratar DSR como certificado.

**Implementación sencilla o reutilización:** Implementación compatible auditada contra ejemplo; fórmula no ejecutada aquí.

**Valor para cripto:** Diagnóstico complementario al comparar muchas reglas de selección.

**Cuándo abstenerse:** Cuando no se conoce el proceso de búsqueda; reportar rango o abstención.

**Implementaciones/candidatos:** [skepsis](https://github.com/abhinay/skepsis).

**Fuentes:** [The Deflated Sharpe Ratio](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-pbo — Probabilidad de backtest overfitting / CSCV

**Problema:** Medir si ganador dentro de muestra pierde posición fuera de ella.

**Supuestos:** Familia de variantes comparable y particiones razonables.

**Datos y frecuencia:** Matriz de resultados de todas las estrategias sobre mismas fechas.

**Cómo validar:** Registrar proceso completo y comparar con holdout verdaderamente futuro.

**Fallos habituales:** Confundir CSCV con walk-forward; asumir que PBO bajo elimina leakage.

**Implementación sencilla o reutilización:** Técnica del paper; implementación candidata aún no auditada integralmente.

**Valor para cripto:** Advertir cuando una aparente ventaja depende de selección del mejor ensayo.

**Cuándo abstenerse:** Escasez de datos o enorme dependencia entre horizontes largos.

**Implementaciones/candidatos:** [skepsis](https://github.com/abhinay/skepsis).

**Fuentes:** [The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-event-study — Estudio de eventos con retornos anormales

**Problema:** Medir reacción asociada a un catalizador respecto a un modelo de mercado.

**Supuestos:** Fecha de anuncio conocida, ventana de estimación previa y benchmark razonable.

**Datos y frecuencia:** Precios/volumen intradía o diarios y registro de anuncios; mercado24/7.

**Cómo validar:** CAR con intervalos agrupados por evento/activo, placebo temporal y controles negativos.

**Fallos habituales:** Seleccionar retrospectivamente eventos ganadores, confundir anuncio/ejecución y eventos simultáneos.

**Implementación sencilla o reutilización:** AR=r-beta*benchmark; CAR=sum AR; comparar varias ventanas predefinidas.

**Valor para cripto:** Unlocks, cambios de fees y listados: reacción y dispersión, no causalidad automática.

**Cuándo abstenerse:** Si todos los activos comparten el shock o el evento se filtró antes.

**Implementaciones/candidatos:** [eventstudy](https://github.com/LemaireJean-Baptiste/eventstudy), [Financial Data Science](https://github.com/terence-lim/financial-data-science), [statsmodels](https://github.com/statsmodels/statsmodels).

**Fuentes:** [eventstudy](https://github.com/LemaireJean-Baptiste/eventstudy). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-bsts — Contrafactual con modelo estructural bayesiano

**Problema:** Estimar trayectoria sin intervención y su incertidumbre.

**Supuestos:** Controles no afectados por evento, relación estable y ausencia de otro shock concurrente.

**Datos y frecuencia:** Series objetivo/controles pre y post, fecha de disponibilidad.

**Cómo validar:** Placebos de fecha y activo, error preintervención, sensibilidad a controles.

**Fallos habituales:** Controles contaminados por contagio cripto; extrapolación de relación que cambió.

**Implementación sencilla o reutilización:** Baseline regresión/estado espacial antes de arquitectura causal compleja.

**Valor para cripto:** Analizar cambios de incentivos o comisiones de un protocolo.

**Cuándo abstenerse:** Shock sistémico o ausencia de controles plausibles; describir asociación.

**Implementaciones/candidatos:** [statsmodels](https://github.com/statsmodels/statsmodels).

**Fuentes:** [Inferring causal impact using Bayesian structural time-series models](https://arxiv.org/abs/1506.00356). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-did — Diferencias en diferencias y event-time moderno

**Problema:** Separar cambios relativos entre grupos tratados y controles.

**Supuestos:** Tendencias paralelas plausibles, no anticipación e interferencia limitada.

**Datos y frecuencia:** Panel protocolo/tiempo, calendario de adopción y variables de confusión.

**Cómo validar:** Pretrends como diagnóstico limitado, placebos, inferencia cluster y sensibilidad.

**Fallos habituales:** TWFE ingenuo con adopción escalonada y efectos heterogéneos; pocos clusters.

**Implementación sencilla o reutilización:** Diseño de grupos y calendario antes de escoger estimador.

**Valor para cripto:** Evaluar reducción de incentivos o cambios de parámetros comparables.

**Cuándo abstenerse:** Contagio generalizado, selección endógena muy fuerte o controles inexistentes.

**Implementaciones/candidatos:** [PyFixest](https://github.com/py-econometrics/pyfixest), [linearmodels](https://github.com/bashtage/linearmodels), [DoWhy](https://github.com/py-why/dowhy).

**Fuentes:** [did](https://arxiv.org/abs/2201.01194). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-covariance-shrinkage — Shrinkage y escenarios de covarianza

**Problema:** Estabilizar estimación de exposición y construcción de cartera.

**Supuestos:** Ventana representativa y precios/frecuencias alineados.

**Datos y frecuencia:** Retornos de activos y benchmark con faltantes tratados explícitamente.

**Cómo validar:** Walk-forward contra sample covariance y equal-weight; sensibilidad de pesos.

**Fallos habituales:** Confundir matriz PSD reparada con datos correctos; annualization252 en cripto365.

**Implementación sencilla o reutilización:** Ledoit-Wolf más límites de concentración.

**Valor para cripto:** Comparar dependencia de BTC, riesgo incremental de token y escenarios.

**Cuándo abstenerse:** No pronostica medias; no elegir max-Sharpe con expectativas inestables.

**Implementaciones/candidatos:** [PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt), [skfolio](https://github.com/skfolio/skfolio).

**Fuentes:** [PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-expected-shortfall — Expected shortfall, drawdown y escenarios

**Problema:** Cuantificar pérdidas extremas y trayectoria adversa.

**Supuestos:** Distribución histórica es solo escenario; cola estimable con incertidumbre.

**Datos y frecuencia:** Retornos, exposición, liquidez, stablecoin y contraparte.

**Cómo validar:** Bootstrap de cola, episodios retenidos y shocks hipotéticos explícitos.

**Fallos habituales:** VaR como peor pérdida máxima, ignorar liquidez/custodia o pocos puntos de cola.

**Implementación sencilla o reutilización:** ES histórico con rango y stress manual BTC/ETH/depeg.

**Valor para cripto:** Riesgo de cartera comprensible para decidir tamaño y liquidez.

**Cuándo abstenerse:** No usar una cifra puntual como límite garantizado de pérdidas.

**Implementaciones/candidatos:** [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib), [QuantStats](https://github.com/ranaroussi/quantstats), [skfolio](https://github.com/skfolio/skfolio).

**Fuentes:** [skfolio](https://github.com/skfolio/skfolio). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-factor-rank — Ranking transversal, IC y spreads por cuantiles

**Problema:** Comprobar relación entre factores y resultados futuros.

**Supuestos:** Universo point-in-time, datos comparables y etiquetas no contaminadas.

**Datos y frecuencia:** Panel mensual de tokens incluidos/excluidos y factores de valoración/crecimiento.

**Cómo validar:** IC por fecha, turnover, neutralización sectorial y prueba por régimen.

**Fallos habituales:** Survivorship, capitalización seleccionada hoy, doble conteo de señales correlacionadas.

**Implementación sencilla o reutilización:** Ranking robusto y distribución de retornos, no precio objetivo.

**Valor para cripto:** Screener de candidatos para investigar por qué fundamento/precio divergen.

**Cuándo abstenerse:** Cuando revenue o supply no son comparables entre protocolos.

**Implementaciones/candidatos:** [Alphalens-reloaded](https://github.com/stefan-jansen/alphalens-reloaded), [Qlib](https://github.com/microsoft/qlib).

**Fuentes:** [Alphalens-reloaded](https://github.com/stefan-jansen/alphalens-reloaded). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-cointegration — Cointegración y ajuste relativo

**Problema:** Estudiar relaciones de equilibrio de largo plazo entre series no estacionarias.

**Supuestos:** Integración compatible, estabilidad del vector y sentido económico.

**Datos y frecuencia:** Precios largos y sincronizados; cambios de especificación documentados.

**Cómo validar:** Tests con corrección múltiple, estabilidad y walk-forward de residuos.

**Fallos habituales:** Correlación confundida con cointegración; relación que desaparece por cambio de tokenomics.

**Implementación sencilla o reutilización:** Engle-Granger como diagnóstico, no ejecución automática.

**Valor para cripto:** Comparación relativa dentro de exposiciones económicamente vinculadas.

**Cuándo abstenerse:** No para cualquier par de tokens encontrado por barrido estadístico.

**Implementaciones/candidatos:** [arch](https://github.com/bashtage/arch), [ArbitrageLab](https://github.com/hudson-and-thames/arbitragelab), [statsmodels](https://github.com/statsmodels/statsmodels).

**Fuentes:** [arch](https://github.com/bashtage/arch). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### method-quant-garch — Volatilidad condicional y cobertura de intervalos

**Problema:** Describir heterocedasticidad y riesgo variable en el tiempo.

**Supuestos:** Innovaciones y especificación ajustadas, escalas consistentes.

**Datos y frecuencia:** Retornos diarios/intradía suficientemente extensos.

**Cómo validar:** Pérdida QLIKE/likelihood, cobertura de intervalos y comparación EWMA.

**Fallos habituales:** Usar menor error como alpha de retorno; cola mal especificada o escala incorrecta.

**Implementación sencilla o reutilización:** EWMA primero; GARCH si mejora calibración fuera de muestra.

**Valor para cripto:** Contexto para tamaño de riesgo y alertas de volatilidad.

**Cuándo abstenerse:** No predice dirección ni reemplaza escenario de salto/depeg.

**Implementaciones/candidatos:** [arch](https://github.com/bashtage/arch), [rugarch](https://github.com/alexiosg/rugarch).

**Fuentes:** [arch](https://github.com/bashtage/arch). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### crypto-method-value-bridge — Puente de captura por mecanismo

**Problema:** Evita atribuir al token actividad que corresponde a LP/creadores o ingresos todavía no convertidos

**Supuestos:** Definiciones, identidades y fechas verificables; no se validó empíricamente el método propuesto.

**Datos y frecuencia:** Fees, payouts, inventario, conversiones, buybacks, burn y supply

**Cómo validar:** Reconciliar balances/flujo en un protocolo y días seleccionados

**Fallos habituales:** Precio/FX, dobles conteos, mecanismos cambiantes o captura sin derecho contractual

**Implementación sencilla o reutilización:** Ledger o tabla pequeña; ver diseño y componentes enlazados.

**Valor para cripto:** Evita atribuir al token actividad que corresponde a LP/creadores o ingresos todavía no convertidos

**Cuándo abstenerse:** Sin cobertura, definiciones o supuestos verificables; registrar abstención.

**Implementaciones/candidatos:** [DefiLlama dimension adapters](https://github.com/DefiLlama/dimension-adapters), [Uniswap protocol fees](https://github.com/Uniswap/protocol-fees).

**Fuentes:** [DefiLlama/dimension-adapters / README.md](https://raw.githubusercontent.com/DefiLlama/dimension-adapters/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/README.md), [DefiLlama/dimension-adapters / LICENSE](https://raw.githubusercontent.com/DefiLlama/dimension-adapters/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/LICENSE), [DefiLlama/dimension-adapters / LICENSE.md](https://raw.githubusercontent.com/DefiLlama/dimension-adapters/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/LICENSE.md), [DefiLlama/dimension-adapters / LICENSE.txt](https://raw.githubusercontent.com/DefiLlama/dimension-adapters/c0bbb1a8a1fb5d1342d9d499daeb960d7f277ce9/LICENSE.txt). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### crypto-method-supply-ledger — Ledger de oferta y desbloqueos

**Problema:** Distingue dilución por creación de tokens de liberación de tokens preexistentes

**Supuestos:** Definiciones, identidades y fechas verificables; no se validó empíricamente el método propuesto.

**Datos y frecuencia:** Mint/burn, circulating/locked/treasury/bridge, cronología de anuncios

**Cómo validar:** Identidad de oferta y doble entrada de bridges

**Fallos habituales:** Múltiples representaciones del mismo activo y calendarios sin historial de revisiones

**Implementación sencilla o reutilización:** Ledger o tabla pequeña; ver diseño y componentes enlazados.

**Valor para cripto:** Distingue dilución por creación de tokens de liberación de tokens preexistentes

**Cuándo abstenerse:** Sin cobertura, definiciones o supuestos verificables; registrar abstención.

**Implementaciones/candidatos:** [DefiLlama pegged assets](https://github.com/DefiLlama/peggedassets-server).

**Fuentes:** [DefiLlama/peggedassets-server / README.md](https://raw.githubusercontent.com/DefiLlama/peggedassets-server/7772746c5164ce10bb0d646a2590c08a2e4059b3/README.md), [DefiLlama/peggedassets-server / LICENSE](https://raw.githubusercontent.com/DefiLlama/peggedassets-server/7772746c5164ce10bb0d646a2590c08a2e4059b3/LICENSE), [DefiLlama/peggedassets-server / LICENSE.md](https://raw.githubusercontent.com/DefiLlama/peggedassets-server/7772746c5164ce10bb0d646a2590c08a2e4059b3/LICENSE.md), [DefiLlama/peggedassets-server / LICENSE.txt](https://raw.githubusercontent.com/DefiLlama/peggedassets-server/7772746c5164ce10bb0d646a2590c08a2e4059b3/LICENSE.txt). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### crypto-method-derivative-normalization — Normalización contractual de derivados

**Problema:** Reduce falsas señales por precio, multiplicador o financiación de duración distinta

**Supuestos:** Definiciones, identidades y fechas verificables; no se validó empíricamente el método propuesto.

**Datos y frecuencia:** Instrumento, contractSize, settlement, OI, fase/intervalo/signo funding

**Cómo validar:** Casos de contrato inverso, intervalo cambiante y ausencia de datos

**Fallos habituales:** Instrumentos con especificación incompleta, APIs truncadas y doble conteo económico entre venues

**Implementación sencilla o reutilización:** Ledger o tabla pequeña; ver diseño y componentes enlazados.

**Valor para cripto:** Reduce falsas señales por precio, multiplicador o financiación de duración distinta

**Cuándo abstenerse:** Sin cobertura, definiciones o supuestos verificables; registrar abstención.

**Implementaciones/candidatos:** [CCXT](https://github.com/ccxt/ccxt), [Hyperliquid Python SDK](https://github.com/hyperliquid-dex/hyperliquid-python-sdk).

**Fuentes:** [ccxt/ccxt / README.md](https://raw.githubusercontent.com/ccxt/ccxt/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/README.md), [ccxt/ccxt / LICENSE](https://raw.githubusercontent.com/ccxt/ccxt/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/LICENSE), [ccxt/ccxt / LICENSE.md](https://raw.githubusercontent.com/ccxt/ccxt/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/LICENSE.md), [ccxt/ccxt / LICENSE.txt](https://raw.githubusercontent.com/ccxt/ccxt/28d9b2ca6e06173ce00f020cfd5bfac3275604d4/LICENSE.txt). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### crypto-method-flow-attribution — Flujos etiquetados con incertidumbre de entidad

**Problema:** Evita convertir movimiento entre wallets internas en entrada de capital de inversores

**Supuestos:** Definiciones, identidades y fechas verificables; no se validó empíricamente el método propuesto.

**Datos y frecuencia:** Transferencias, etiquetas, fuentes, timestamps y confianza

**Cómo validar:** Contrastar manualmente eventos y publicar discrepancias entre reglas de agrupación

**Fallos habituales:** Etiquetas retrospectivas, entidades con varias wallets, custodios/bridges y muestra incompleta

**Implementación sencilla o reutilización:** Ledger o tabla pequeña; ver diseño y componentes enlazados.

**Valor para cripto:** Evita convertir movimiento entre wallets internas en entrada de capital de inversores

**Cuándo abstenerse:** Sin cobertura, definiciones o supuestos verificables; registrar abstención.

**Implementaciones/candidatos:** [GraphSense lib](https://github.com/graphsense/graphsense-lib), [GraphSense TagPacks](https://github.com/graphsense/graphsense-tagpacks).

**Fuentes:** [graphsense/graphsense-lib / README.md](https://raw.githubusercontent.com/graphsense/graphsense-lib/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/README.md), [graphsense/graphsense-lib / LICENSE](https://raw.githubusercontent.com/graphsense/graphsense-lib/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/LICENSE), [graphsense/graphsense-lib / pyproject.toml](https://raw.githubusercontent.com/graphsense/graphsense-lib/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/pyproject.toml), [graphsense/graphsense-lib / src/graphsenselib/tagpack/confidence.py](https://raw.githubusercontent.com/graphsense/graphsense-lib/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/src/graphsenselib/tagpack/confidence.py). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### crypto-method-event-market-link — Mercados predictivos como evidencia de tesis

**Problema:** Aporta señal contextual; no trata precio como probabilidad objetiva

**Supuestos:** Definiciones, identidades y fechas verificables; no se validó empíricamente el método propuesto.

**Datos y frecuencia:** Reglas, resolución, precio, spread, profundidad y calendario de fuentes

**Cómo validar:** Muestra curada con revisión humana de equivalencia y fechas

**Fallos habituales:** Resoluciones distintas, sesgo de selección, falta de mercados cerrados y poca liquidez

**Implementación sencilla o reutilización:** Ledger o tabla pequeña; ver diseño y componentes enlazados.

**Valor para cripto:** Aporta señal contextual; no trata precio como probabilidad objetiva

**Cuándo abstenerse:** Sin cobertura, definiciones o supuestos verificables; registrar abstención.

**Implementaciones/candidatos:** [Polymarket unified Python SDK](https://github.com/Polymarket/py-sdk).

**Fuentes:** [Polymarket/py-sdk / README.md](https://raw.githubusercontent.com/Polymarket/py-sdk/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/README.md), [Polymarket/py-sdk / LICENSE](https://raw.githubusercontent.com/Polymarket/py-sdk/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/LICENSE), [Polymarket/py-sdk / pyproject.toml](https://raw.githubusercontent.com/Polymarket/py-sdk/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/pyproject.toml), [Polymarket/py-sdk / src/polymarket/clients/public.py](https://raw.githubusercontent.com/Polymarket/py-sdk/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/src/polymarket/clients/public.py). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### AI-METHOD-asof-covariates — Covariables con corte de conocimiento

**Problema:** Evitar que indicadores revisados o futuros contaminen forecasts.

**Supuestos:** Fecha de disponibilidad real y unidad identificadas

**Datos y frecuencia:** Diaria/semanal; fuente macro con vintages

**Cómo validar:** Casos negativos con publicaciones futuras; comparación de snapshots

**Fallos habituales:** Marcar M2 futuro como known-future; Cross-learning mezcla grupos con cortes distintos

**Implementación sencilla o reutilización:** Vista temporal antes de toda transformación y separación past/future

**Valor para cripto:** Comparar fundamentos sin conocimiento posterior

**Cuándo abstenerse:** No existe fecha de disponibilidad: abstenerse o marcar simulación retrospectiva.

**Implementaciones/candidatos:** [Forecast Evaluation (fev)](https://github.com/autogluon/fev), [Chronos forecasting library](https://github.com/amazon-science/chronos-forecasting), [TradingAgents](https://github.com/TauricResearch/TradingAgents).

**Fuentes:** [src/fev/task.py](https://raw.githubusercontent.com/autogluon/fev/13b1913881bb7c680d47262bbc32327304bb0571/src/fev/task.py), [Rethinking Evaluation in the Era of Time Series Foundation Models: (Un)known Information Leakage Challenges](https://arxiv.org/abs/2510.13654v3). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### AI-METHOD-prequential-drift — Evaluación prequential y drift sobre residuos

**Problema:** Distinguir degradación del modelo/cambio de datos.

**Supuestos:** Observaciones ordenadas; error calculado antes de actualizar; Dependencia temporal tratada en validación

**Datos y frecuencia:** Stream o diario

**Cómo validar:** Saltos sintéticos, periodos estables, demora y falsas alarmas/mes

**Fallos habituales:** Alarma por autocorrelación; Cambio de API interpretado como mercado

**Implementación sencilla o reutilización:** ADWIN sobre pérdida y calidad de datos

**Valor para cripto:** Detectar cambios de definición de fees y errores de ingesta

**Cuándo abstenerse:** No hay baseline estable o se pretende inferir dirección de precio.

**Implementaciones/candidatos:** [River](https://github.com/online-ml/river).

**Fuentes:** [river/drift/adwin.py](https://raw.githubusercontent.com/online-ml/river/4768de0579f977315e65cd23ee658534c1d62c26/river/drift/adwin.py). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### AI-METHOD-quantile-checks — Forecast cuantílico con calibración por régimen

**Problema:** Expresar incertidumbre en actividad y volatilidad.

**Supuestos:** Cortes limpios; Errores de calibración relevantes para periodo futuro

**Datos y frecuencia:** Diaria/semanal

**Cómo validar:** Pinball/WQL, cobertura, amplitud y scoring por régimen

**Fallos habituales:** Intervalos demasiado estrechos por calibración in-sample; Cobertura global oculta fallos en crisis

**Implementación sencilla o reutilización:** Un baseline y un TSFM; reservar periodo prospectivo

**Valor para cripto:** Priorizar sorpresas de fundamentales para investigación

**Cuándo abstenerse:** Se quiere deducir rentabilidad de un error pequeño en precio nominal.

**Implementaciones/candidatos:** [Chronos forecasting library](https://github.com/amazon-science/chronos-forecasting), [MLForecast](https://github.com/Nixtla/mlforecast), [Forecast Evaluation (fev)](https://github.com/autogluon/fev).

**Fuentes:** [src/chronos/chronos2/pipeline.py](https://raw.githubusercontent.com/amazon-science/chronos-forecasting/1224fafa91e1ecd6674f5204066b159e40b5e4a1/src/chronos/chronos2/pipeline.py), [mlforecast/forecast.py](https://raw.githubusercontent.com/Nixtla/mlforecast/74ba65e49cb39282e5f490c8dfd25e4bacacedaf/mlforecast/forecast.py). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### AI-METHOD-evidence-first-rag — Recuperación de evidencia con verificación numérica

**Problema:** Responder sobre protocolos preservando fuente, unidad y fecha.

**Supuestos:** Documentos permitidos y versionados; Cálculos separados del generador

**Datos y frecuencia:** Al aparecer documentos/eventos

**Cómo validar:** Gold set humano de citas y cifras; documentos adversariales

**Fallos habituales:** Cita existente que no implica afirmación; OCR pierde signo/escala; Documento malicioso actúa como instrucción

**Implementación sencilla o reutilización:** BM25 primero, extracción tipada y calculadora determinista

**Valor para cripto:** Comparar fees/revenue/captura de valor sin inventar mecanismo

**Cuándo abstenerse:** No puede localizarse la evidencia o resolver contradicción de unidades.

**Implementaciones/candidatos:** [Docling](https://github.com/docling-project/docling), [Trafilatura](https://github.com/adbar/trafilatura), [Pydantic AI](https://github.com/pydantic/pydantic-ai), [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3).

**Fuentes:** [docling/document_converter.py](https://raw.githubusercontent.com/docling-project/docling/0634e2f74561e5950d69b2cace67ef95400506ad/docling/document_converter.py), [Tencent finLLM-Eval readme](https://raw.githubusercontent.com/Tencent/finLLM-Eval/2747fb219d553dea0a183269554ce174aeb00531/README.md). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

### AI-METHOD-prospective-catalysts — Registro prospectivo de probabilidades de catalizadores

**Problema:** Evaluar calibración de hipótesis sin memoria retrospectiva del LLM.

**Supuestos:** Pregunta resoluble con regla previa; Fecha de forecast inmutable; Consenso de mercado conocido registrado

**Datos y frecuencia:** Evento; horizontes días a meses

**Cómo validar:** Brier/log loss, fiabilidad por bandas, comparación contra consenso

**Fallos habituales:** Cambiar regla después del resultado; Preguntas seleccionadas por éxito; Comparar modelos con preguntas diferentes

**Implementación sencilla o reutilización:** Tabla local de probabilidades y resoluciones

**Valor para cripto:** Thesis Tracker mide aprendizaje del analista y valor incremental

**Cuándo abstenerse:** Resolución ambigua o datos de mercado ilíquidos presentados como probabilidades precisas.

**Implementaciones/candidatos:** `ForecastBench como referencia conceptual`.

**Fuentes:** [ForecastBench metodología y equipo](https://www.forecastbench.org/about/). La ficha es una síntesis; consultar el alcance de lectura de cada fuente.

## Papers y grado de lectura

- [The Deflated Sharpe Ratio](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf) — 2014-07-31. Requiere registrar experimentos y estimar su dependencia; no corrige datos con leakage. Versión 31-jul-2014 consultada.
- [The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf) — 2015-02-27. PBO depende del conjunto de pruebas y de supuestos de partición; no sustituye test prospectivo. Versión 27-feb-2015 consultada.
- [Inferring causal impact using Bayesian structural time-series models](https://arxiv.org/abs/1506.00356) — arXiv: 1506.00356. Se leyó abstract/ficha y alcance, no se reprodujeron experimentos; exige controles no afectados y estabilidad pre/post.
- [BlockSci: Design and applications of a blockchain analysis platform](https://www.usenix.org/conference/usenixsecurity20/presentation/kalodner) — USENIX Security 2020; preprint de 2017 como versión anterior. Ficha original y abstract; no lectura completa de benchmarks ni reproducción
- [Price Trajectories, Impact and Sunshine Trading](https://raw.githubusercontent.com/0xBaro/hyperliquid/c4d3743c65923c6e921f731d753e580961d2328b/README.md) — Nota pública asociada a 0xBaro/hyperliquid; revisión/publicación formal no verificada. Documentación/repositorio; no revisión completa del estudio
- [Pretrained Time-Series Foundation Models for Financial Return Forecasting](https://arxiv.org/abs/2606.27100v1) — v1; 2026-06-25. No extrapolar a crypto o3-18 meses; Solo abstract e historial examinados; No auditoría de muestras, costes o pruebas estadísticas del texto completo
- [Rethinking Evaluation in the Era of Time Series Foundation Models: (Un)known Information Leakage Challenges](https://arxiv.org/abs/2510.13654v3) — v3; 2026-02-25. No reproducción; No demuestra contaminación de cada checkpoint del catálogo
- [FinVerse: Toward More Realistic Evaluation for Financial Time-Series Forecasting](https://arxiv.org/abs/2608.03259v3) — v3; 2026-10-23. Solo abstract e historial examinados; Código/datos/permiso/coste pendientes; No recomendar modelos por ranking sin reproducción

Los inventarios [algorithms.json](inventories/algorithms.json) y [papers.json](inventories/papers.json) conservan IDs y fuentes. No todos los trabajos se leyeron completos: los abstracts y pistas de investigación se identifican expresamente, y ningún benchmark fue reproducido.
