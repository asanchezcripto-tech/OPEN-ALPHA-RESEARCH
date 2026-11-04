# Hallazgos quant, macro y riesgo

Observación: 4 de noviembre de 2026; referencia solicitada: 3 de noviembre. La rama consultada el día 4 no se reconstruyó como cierre histórico del día 3. Esta entrega es revisión de fuentes y código, sin instalar/importar/ejecutar software externo ni reproducir benchmarks.

La mayor mejora posible para este mandato es **conservar cuándo se conocía cada dato y someter hipótesis a comparaciones sencillas**, antes de ampliar el número de modelos. Hay componentes maduros para ello, pero una biblioteca estadística no subsana un histórico reconstruido con conocimiento futuro.

## Cobertura real

Se descubrieron y documentaron 65 recursos: 51 repositorios y 14 fuentes macro, datasets o papers. 63 tienen comprobación directa suficiente para su nivel: 10 V3, 43 V2 y 10 V1. ECB API y Treasury API permanecen D0 por 503/403 en documentación específica; sí existen referencias oficiales complementarias. Se registran33 consultas de descubrimiento y seguimiento, 18 métodos y 6 comparaciones. V2 suele significar README más licencia/manifiesto; solo V3 implica rutas críticas y tests inspeccionados. No se auditó exhaustivamente actividad, issues ni releases de todo el catálogo.

La cobertura tiene sesgo Python/GitHub/inglés y bancos centrales estadounidenses/europeos. Se investigó el ecosistema chino mediante consultas chinas y RQAlpha/vn.py. GitLab y Codeberg tuvieron cobertura menor; strucchange se identificó como paquete original en Codeberg a través de un mirror CRAN, y no se contó el mirror como proyecto adicional. SourceHut, macro asiática, feeds de flujos ETF y datos de opciones detallados requieren continuidad. ETFs diarios necesitan distinguir creación/redención de cambios de AUM por precio; no se validó una fuente gratuita completa.

## Seis comprobaciones que cambian decisiones

1. **Un nombre de método no garantiza su semántica.** `fredapi.get_series_as_of_date` devuelve todas las filas con realtime_start anterior a la fecha; no reduce a la última vintage por periodo. El consumidor debe hacer esa selección explícita y conservar el historial. [Código examinado](https://github.com/mortada/fredapi/blob/d0a0ba3001ebbbceafdcbdd3eb23828f0537cdff/fredapi/fred.py).
2. **Una plataforma puede normalizar eliminando información necesaria.** La ruta FRED `models/series.py` de OpenBB elimina realtime_start/end y descarta faltantes antes de devolver series. Eso es útil para un gráfico actual, pero insuficiente para reconstruir vintages; no se extiende esta observación a todos los endpoints del proyecto. [Ruta examinada](https://github.com/openbq-org/OpenBB/blob/2a392e890f6eb1f0f4e3a71742720af8f056333a/openbb_platform/providers/fred/openbb_fred/models/series.py).
3. **PurgedCV puede no purgar.** En el commit revisado, skfolio fija purged_size=0 y embargo_size=0; se deben configurar. CPCV tampoco reemplaza walk-forward prospectivo. [Constructor y splitter](https://github.com/skfolio/skfolio/blob/0db206ed812622088cbd33af2e34a0f4762fa71e/src/skfolio/model_selection/_combinatorial.py).
4. **Offline no significa alerta temprana.** PELT en ruptures trabaja con toda la señal recibida. Solo un replay que guarde cuándo apareció la alerta permite medir anticipación, revisiones y falsas alarmas. [Implementación](https://github.com/deepcharles/ruptures/blob/ee1c8ff8a548d54c641b2bb471562165931f31c7/src/ruptures/detection/pelt.py).
5. **Licencias conocidas han cambiado o incluyen cláusulas adicionales.** vectorbt es Apache+Commons Clause; RQAlpha restringe uso comercial; pykalman incluye condiciones de redistribución por canales, con exención explícita de usuarios finales; MLFinLab presenta acuerdo propietario ambiguo. OpenBB actual, en cambio, pasó a Apache-2.0 y continuidad OpenBQ. Ver LICENSE enlazado en cada ficha; no heredar etiquetas de una lista antigua.
6. **Incluso una fuente oficial revisa el pasado.** OFR informa de una corrección del feed para cuatro días de mayo2026 y publica su índice con dos días hábiles de retraso. Un join por fecha de observación puede introducir información antes de su disponibilidad. [Fuente OFR](https://www.financialresearch.gov/financial-stress-index/).

## Componentes que priorizaría

| Componente | Capacidad aprovechable | Condición de uso |
|---|---|---|
| arch | Bootstrap por bloques, SPA, StepM, MCS | Registrar todas las variantes, pérdidas comparables y sensibilidad de bloque |
| skfolio | WalkForward y comparación de carteras | Configurar purga/embargo y convenciones cripto |
| PyPortfolioOpt | Shrinkage y escenarios de concentración | Tratar faltantes, annualización y medias con cautela |
| ruptures | Cambios estructurales en variables económicas | Replay de prefijos antes de usar como detector operativo |
| fredapi + ALFRED | Macro por vintage | Selección correcta de última revisión y permisos por serie |
| statsmodels | Baselines econométricos, estados espaciales | Filtrado frente a suavizado; evaluar contra métodos sencillos |
| sdmx1 | Metadatos y conectores de estadísticas oficiales | Verificar soporte y términos por organismo |
| Alphalens-reloaded | Evaluación de factores transversales | Universo point-in-time y adaptación del calendario |

Qlib merece conservarse por su patrón PIT y de experimentos; no empezaría adoptando toda su plataforma. Nautilus y LEAN son referencias técnicas útiles, con mayor coste que el necesario para ingresos y valoración de protocolos. Freqtrade tiene diagnósticos de look-ahead y recursividad aprovechables aunque la automatización de operaciones quede fuera del mandato. No se recomienda instalar ninguno durante esta fase.

## Hallazgos contracorriente

**arch** es conocido por GARCH, pero su módulo de comparación múltiple cubre una carencia más urgente: saber si alguno de muchos candidatos realmente mejora un benchmark. Sus tests verifican detalles de studentización y kernels. **strucchange** aporta monitorización econométrica y no solo segmentación retrospectiva. **Financial Data Science de Terence Lim** reúne lectores ALFRED y estudios de eventos en una base educativa inspeccionable, con derechos de datasets separados. **gingado**, del BIS, permite estudiar ML macro sin confundir innovación cripto con novedad del modelo. **skepsis** muestra un golden test de DSR vinculado al paper y puede ahorrar trabajo, pero su versión 0.1.0 y falta de auditoría integral impiden promoverlo a dependencia crítica.

“Poco obvio” describe aquí un componente o uso menos visible para este mandato, no una clasificación objetiva por estrellas. Las estrellas no se utilizaron como prueba de calidad.

## Oportunidades con hipótesis comprobable

- **Vintage-aware Macro Lens:** ALFRED+sdmx1 +tabla bitemporal+ruptures. Comparar conclusiones semanales usando datos conocidos entonces frente a series finales; medir cuántas falsas divergencias desaparecen. Primer resultado útil: cuatro indicadores con fecha de disponibilidad visible. No sumar M2 de países sin unidades/FX/solapamientos; GLI del BIS mide crédito, no dinero ni profundidad de mercado.
- **Research Robustness Auditor:** ledger de ensayos+arch+skfolio+estudios DSR/PBO. Hipótesis: reduce candidatos frágiles y tiempo de revisión respecto a ordenar Sharpe. Aceptación: detecta fixtures con leakage mediante reglas temporales y muestra cómo cambia ranking con costes/bloques; DSR no se usa como certificado.
- **Catalyst Cohort Lab:** registro prospectivo de eventos+eventstudy/PyFixest+arch. Hipótesis: separar anuncio, ejecución y eventos concurrentes cambia inferencias sobre unlocks o fee switches. Medir cobertura de timestamps y estabilidad del CAR bajo benchmarks, placebos y agrupación.
- **Portfolio Fragility Lens:** PyPortfolioOpt/skfolio+escenarios de BTC, depeg y liquidez. Hipótesis: revela concentraciones ocultas que no aparecen en pesos nominales. Aceptación: cada escenario es legible, puede reproducirse con ledger manual y no presenta VaR como pérdida máxima.
- **Protocol Factor Laboratory:** Alphalens-reloaded+PIT de fundamentos+bootstrap. Hipótesis: rankings de mejora económica ayudan a elegir temas de investigación incluso si no predicen rentabilidad. Medir calidad de cobertura, estabilidad de ranking y posterior confirmación/invalidación de hipótesis, además de retorno.

## Diseño mínimo común y costes

Una herramienta inicial puede consistir en archivos Parquet, consulta local, notebook parametrizado y un informe de 10–20 minutos. Separar observación, fecha disponible, adquisición, fuente, versión y estado de permiso. Para decenas de activos y frecuencia diaria, CPU y 8–16 GB son una estimación razonable de partida, no un benchmark; datos intradía multivenue y CPCV amplio cambian el presupuesto. No se ofrecen tarifas de proveedores no verificadas. Ningún diseño exige GPU ni ejecución automática.

La evaluación a3–18 meses tiene pocas observaciones independientes: cientos de retornos diarios solapados a un año no equivalen a cientos de apuestas independientes. Priorizar experimentos de calidad de datos y utilidad de investigación; cualquier afirmación de capacidad predictiva requiere periodos retenidos y seguimiento prospectivo.

## Licencias y límites de publicación

Código permisivo no cubre datos de FRED de terceros, API QuantConnect, fuentes de OpenBB ni datos de ejemplos. BIS exige atribución, evita afiliación implícita e impone condiciones adicionales de inclusión comercial. La clasificación es una valoración de compatibilidad potencial, no un dictamen jurídico. No publicar cachés ni copiar código de proyectos restringidos; el paquete conserva URLs, commits, hashes y notas propias.

## Pendientes y estado de etapas

A–D: barrido y lectura directa completados dentro de esta cobertura; corrección de URL DoWhy y canonicalización PyPortfolioOpt registradas. E–G: diez revisiones estáticas, métodos y comparaciones; ningún resultado empírico ejecutado. H–I: cinco combinaciones con experimentos mínimos propuestas para consolidación central. J: revisadas contradicciones código/docstrings/licencias; falta revisión por segundo lector y pruebas aisladas autorizadas si se decide desarrollar. K: JSON y notas listos para consolidar.

Pendientes concretos: fechas de commits respecto al corte3-nov, historial de releases/issues, riesgo transitivo de dependencias, licencias de datasets por serie, recuperación de documentación ECB/Treasury, forks comparados por diffs y no solo actividad, datos de flujos ETF, validación del reloj24/7 y ejecución en entorno desechable solo en un mandato posterior autorizado.
