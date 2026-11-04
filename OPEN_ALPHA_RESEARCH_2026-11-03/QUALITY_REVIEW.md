# Revisión de calidad y alcance de las comprobaciones

La entrega documenta una investigación amplia con profundidad desigual. Se cerró el alcance documental del mandato: 288 recursos, 39 revisiones técnicas estáticas, 22 componentes seleccionados, 16 conceptos y cinco diseños. Las comprobaciones de integridad de archivos no prueban que el software analizado funcione ni que los diseños produzcan una ventaja de inversión.

Fecha de observación: 4 de noviembre de 2026. Referencia solicitada: 3 de noviembre. No se reconstruyó sistemáticamente la disponibilidad de cada versión al cierre del día 3. [Cobertura y lagunas](01_SEARCH_COVERAGE.md).

## Revisión cruzada y correcciones incorporadas

Tres investigadores por área revisaron los diseños del coordinador. Los informes originales se conservan: [crypto](workstreams/crypto/critical_review.md), [quant](workstreams/quant/critical_review.md) e [IA](workstreams/ai/critical_review.md). Son revisiones del mismo equipo de investigación, no auditorías externas independientes. Las recomendaciones prioritarias se incorporaron en los cinco diseños; los experimentos siguen pendientes.

| Diseño | Corrección incorporada | Implicación para su evaluación futura |
|---|---|---|
| [Protocol Value](12_TOP_FIVE_BLUEPRINTS/01_protocol_value.md) | Separar mint, unlock, inventario, recompra y burn; reconciliar cantidades antes de valorar; delimitar HyperCore/HyperEVM y mecanismos | No atribuir caja ni dilución al token sin identificar beneficiario, unidad y cobertura |
| Protocol Value | Denominador explícito del 95%; trazabilidad completa de eventos materiales en la muestra; estimación inicial para un protocolo | Un porcentaje de cobertura desconocido se retira; 90 días prospectivos exigen 90 días naturales |
| [Thesis Tracker](12_TOP_FIVE_BLUEPRINTS/02_thesis_tracker.md) | Comprobar que la cita respalda la afirmación; códigos de abstención; separar publicación y adquisición; confianza ordinal | Una URL real no garantiza soporte; cero fallos en un lote pequeño no estima fiabilidad de producción |
| Thesis Tracker | Generador sin shell, mensajes o escritura de tesis; pruebas con herramientas simuladas y presupuesto de llamadas | La seguridad depende de permisos y controles, además del prompt; el piloto no certifica inmunidad universal |
| [Regime Navigator](12_TOP_FIVE_BLUEPRINTS/03_regime_navigator.md) | Invariancia de toda la canalización al añadir información futura; vintages y disponibilidad desconocida explícitos | La selección temporal debe cubrir normalización, universo, parámetros y explicación |
| Regime Navigator | 24–36 meses como piloto técnico; rúbrica de explicaciones y detección sobre prefijos | No confundir buen funcionamiento técnico con estabilidad macro o anticipación económica |
| [Derivatives Stress](12_TOP_FIVE_BLUEPRINTS/04_derivatives_stress.md) | Fase e intervalo de funding; fórmulas específicas de OI; prima de perpetuo separada del basis a vencimiento | No sumar predicciones repetidas ni aplicar una conversión universal a contratos inversos |
| Derivatives Stress | Objetivo horario/diario, lados raw/normalizado, episodios y horizonte de evaluación | Datos horarios no validan avisos previos a cascadas intrahorarias; diagnóstico simultáneo no es predicción |
| [Event Lab](12_TOP_FIVE_BLUEPRINTS/05_event_lab.md) | Convención de CAR, dependencia entre activos/fechas, incertidumbre horaria y sorpresa del evento | CAR no equivale necesariamente a retorno compuesto ejecutable; no seleccionar la hora por su p-value |
| Event Lab | 20–40 eventos como curación, no potencia; fuente histórica y reconstrucción por segundo lector | Informar clusters y precisión; aceptar resultados nulos como resultado válido de investigación |

## Comprobación del coordinador

Se contrastaron afirmaciones decisivas con fuentes primarias y rutas concretas, además de leer las nueve revisiones de infraestructura y sus archivos críticos. El alcance de cada comprobación consta en las revisiones enlazadas:

- [fredapi](03_DEEP_TECHNICAL_REVIEWS/quant_fredapi.md): una consulta as-of puede conservar varias vintages anteriores; hace falta seleccionar la última por periodo.
- [skfolio](03_DEEP_TECHNICAL_REVIEWS/quant_skfolio.md): los valores por defecto de purga y embargo no acreditan por sí solos una separación temporal efectiva.
- [TimesFM](03_DEEP_TECHNICAL_REVIEWS/ai_timesfm.md): separar código y pesos, incluida la restricción de los pesos TimesFM 3 observados.
- [Polymarket](03_DEEP_TECHNICAL_REVIEWS/crypto_polymarket_sdk.md): comprobar el sucesor unificado y las dos etapas de deprecación; separar SDK, servicio y contratos.
- [DefiLlama](03_DEEP_TECHNICAL_REVIEWS/crypto_defillama_dimensions.md), [Uniswap](03_DEEP_TECHNICAL_REVIEWS/crypto_uniswap_protocol_fees.md) y [hallazgos crypto](workstreams/crypto/findings.md): distinguir fórmulas, documentación, activación y flujo económico observado; corregir la URL antigua de Raydium y conservar la advertencia de cobertura de Pump.
- [DuckDB](03_DEEP_TECHNICAL_REVIEWS/infra_duckdb.md), [requests-cache](03_DEEP_TECHNICAL_REVIEWS/infra_requests-cache.md), [Pandera](03_DEEP_TECHNICAL_REVIEWS/infra_pandera.md) y [DataComPy](03_DEEP_TECHNICAL_REVIEWS/infra_datacompy.md): revisar nulos, fechas, respuestas caducadas, filas descartadas y tolerancias antes de recomendar su uso.

No se volvieron a visitar todas las URLs durante la pasada final. Las fuentes preservan status, fecha, versión y hash cuando se obtuvo. Los intentos fallidos permanecen visibles. Las afirmaciones limitadas al abstract o a una card no se elevan a reproducción científica ni auditoría de derechos.

## Integridad de la entrega

El auxiliar propio [validate_delivery.py](research_tools/validate_delivery.py) comprueba IDs, referencias entre inventarios, correspondencia de celdas CSV/JSON, puntuaciones y límites, clasificación de licencias, niveles de verificación, rutas de revisiones/diseños, enlaces locales y recuentos. Su resultado exacto queda en [quality_checks.json](inventories/quality_checks.json). Se ejecuta con Python estándar y no importa ni ejecuta proyectos investigados.

Los recuentos se derivan de los inventarios. Se consolidaron DoWhy y EconML cuando aparecieron en dos áreas; se mantuvieron FRED-MD y FRED-QD como datasets distintos aunque compartan página. El inventario principal incorpora cinco referencias académicas complementarias de IA/crypto; los 80 recursos de la ficha original de IA son el alcance de esa área, no el total consolidado. Los inventarios especializados son vistas o fichas relacionadas y no se suman al total de 288.

Los D0 no reciben puntuación ni fecha de verificación afirmativa. Los campos no examinados quedan nulos o con una limitación explícita. Los bloqueantes prevalecen sobre el score; una referencia útil con licencia no verificada no se convierte en código adoptable.

El manifiesto de entrega registra tamaño y SHA-256 de los archivos incluidos. El ZIP excluye cachés de lectura y bytecode; contiene documentación, metadatos y auxiliares propios. No incluye pesos, datasets completos, código descargado de los proyectos ni credenciales. El manifiesto comprueba integridad, no veracidad de las fuentes.

## Límites que permanecen abiertos

No hubo ejecución de modelos, tests externos, benchmarks, backtests, transacciones ni instalación de dependencias investigadas. No se midieron rendimiento local, cobertura de tests, precisión predictiva, ahorro de tiempo ni coste real de servicios. Los ensayos y presupuestos de hardware son propuestas identificadas como tales.

Quedan pendientes la auditoría completa de mantenimiento y dependencias, derechos de cada dataset/modelo, reconstrucción exacta del corte, contratos efectivamente desplegados e históricos íntegros. GitHub/Python y fuentes anglófonas están sobrerrepresentados; otras plataformas tienen cobertura menor o insuficiente. El [backlog](13_RESEARCH_BACKLOG.md) prioriza estas limitaciones. Ninguna invalida el catálogo documental; sí limita la adopción y las conclusiones económicas.

CIE permaneció fuera del alcance. No se creó ni modificó un repositorio remoto. No se implementaron los productos propuestos.
