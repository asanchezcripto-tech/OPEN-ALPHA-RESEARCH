# OP-03 — Market Regime & Liquidity Navigator

Diseño preliminar, no implementado. Prioridad estratégica 3. Propósito: contexto para decisiones de semanas/meses, sin predecir un punto de entrada exacto.

## Objetivo y capacidad inicial

Responder qué bloques del entorno apoyan o contradicen un escenario. Primera capacidad: BTC/ETH, volatilidad realizada, tendencia, fuerza relativa y tres series macro con calendario explícito. El usuario ve observaciones y antigüedad antes de una etiqueta de régimen.

Casos: distinguir deterioro amplio de una caída idiosincrática; comparar una expansión de stablecoins con entradas a venues observadas; estudiar si un cambio macro fue conocido antes o después de una reacción del mercado.

## Flujo y arquitectura

```mermaid
flowchart LR
 A[Precios y macro publicados] --> B[Snapshots y vintages]
 B --> C[Unidades, calendario y rezagos]
 C --> D[Indicadores por bloque]
 D --> E[Escenarios y contradicciones]
 E --> F[Panel diario de 5 minutos]
 D --> G[Replay de prefijos y sensibilidad]
```

Batch diario, Parquet/DuckDB, configuración pequeña de indicadores y un panel local. Un conjunto macro de baja frecuencia y otro de precios diarios; no rellenar publicaciones mensuales como si fueran nueva información diaria. No integrar necesariamente un modelo de forecasting.

Bibliotecas: fredapi, statsmodels, ruptures y River cuando aporten una pregunta adicional. Las revisiones [fredapi](../03_DEEP_TECHNICAL_REVIEWS/quant_fredapi.md), [ruptures](../03_DEEP_TECHNICAL_REVIEWS/quant_ruptures.md) y [DuckDB](../03_DEEP_TECHNICAL_REVIEWS/infra_duckdb.md) describen límites que el diseño debe controlar.

## Fuentes y alternativa sin pago

[ALFRED](https://alfred.stlouisfed.org/) y [documentación de tiempo real FRED](https://fred.stlouisfed.org/docs/api/fred/realtime_period.html) para vintages; ECB/BIS para series adecuadas a su frecuencia y condiciones; clientes oficiales/CCXT para precios. Stablecoin supply es un bloque separado. Flujos ETF requieren verificar fuente, publicación y licencia; no sustituirlos silenciosamente por variación de AUM, que incluye precio.

Una API gratuita puede exigir registro. Sin clave, la alternativa es descarga manual permitida y un universo reducido. Guardar la primera disponibilidad observada cuando el instante real de publicación no se conozca; no etiquetarla como hora exacta del mercado. No existe aquí una licencia universal para redistribuir series macro de terceros.

## Datos y algoritmos seleccionados

Cada punto lleva periodo económico, fecha de publicación/vintage, adquisición, divisa/unidad y metodología. En fredapi, seleccionar la última revisión por periodo dentro del corte; la revisión estática encontró que get_series_as_of_date puede devolver varias revisiones anteriores. No usar la ruta de OpenBB que descarta campos de vintage como archivo histórico de conocimiento.

Base: retornos logarítmicos, volatilidad realizada, percentiles robustos calculados solo con pasado, amplitud sobre universo conocido entonces y correlaciones móviles con intervalos. Estimar régimen mediante reglas simples primero. PELT es segmentación retrospectiva: en seguimiento, reestimar sobre cada prefijo y registrar cuándo detectó el cambio, sin asignarle retrospectivamente la fecha óptima completa.

Fijar la convención de anualización para precios cripto diarios; no heredar automáticamente 252 sesiones. Para macro/precios, definir transformaciones y rezagos antes del ensayo y evitar correlacionar niveles no estacionarios sin diagnóstico. BTC/ETH describen ese universo inicial; el bloque de amplitud global solo aparece al ampliar el universo con elegibilidad y deslistados por fecha.

Mantener separados liquidez monetaria, balance de bancos centrales, crédito, liquidez de mercado y stablecoins. Convertir M2 de distintos países a una moneda introduce efecto de cambio; mostrar resultados en moneda local o con una convención explícita y alternativa. El supuesto «más M2 implica BTC al alza con lag fijo» se trata como hipótesis y se contrasta contra explicaciones comunes, no como mecanismo demostrado.

Salida: 4 bloques —tendencia/amplitud, volatilidad, macro, liquidez cripto—, sin score compuesto hasta justificar sus pesos. Cada bloque muestra nivel, cambio, fecha conocida, cobertura y contradicciones.

## Validación, incertidumbre y aceptación

Comparar reglas base con un modelo más complejo usando cortes temporales predefinidos. Para etiquetas descriptivas, medir estabilidad, retraso de detección y frecuencia de cambios espurios; para forecasts, evaluar calibración y error fuera de muestra por separado. No juzgar una clasificación solo por acertar el nombre de un periodo después de verlo.

Experimento mínimo: 24–36 meses si la disponibilidad histórica lo permite y replay semanal; si no existen vintages de cripto, separar segmento reconstruido y piloto prospectivo. Fixtures con revisión macro, día festivo, series ausentes y delisting deben producir cero fuga temporal. Evaluar si la lectura del panel mejora una explicación escrita frente a tres indicadores simples.

Ese periodo sirve para un piloto técnico; no demuestra estabilidad a través de ciclos macro completos. Para validar el pipeline entero, añadir datos futuros a la entrada y exigir que no cambien las salidas ya emitidas para cortes anteriores: incluye normalización, universo, covarianzas, selección de variables y detector. Un fallo de invariancia invalida la evaluación temporal aunque los joins individuales sean correctos.

Comprobar mecánica y retraso con cambios sintéticos de fecha conocida. En datos reales, donde el régimen no es observable directamente, informar alertas por periodo, persistencia y revocaciones bajo reglas predefinidas; una revocación no prueba falsedad económica. Conservar tanto la fecha atribuida al cambio como la fecha en que se anunció. Clasificar disponibilidad histórica como conocida, acotada o desconocida; la primera descarga actual de un histórico no reconstruye su publicación pasada.

Evaluar las explicaciones con las mismas fechas y fuentes, ocultando al revisor el resultado posterior. La rúbrica cuenta afirmaciones sin soporte, errores de unidad/fecha, contradicciones detectadas y tiempo de lectura. Ninguna afirmación material puede pasar sin respaldo o marca de incertidumbre; la mejora respecto al baseline debe medirse, no decidirse a posteriori según el precio.

Abstenerse de etiqueta global cuando falte un bloque material o la clasificación sea sensible a pequeños cambios. Mostrar escenarios, no probabilidades precisas sin calibración.

## Incrementos y coste

BTC/ETH y tres indicadores → calendario/vintages → amplitud y stablecoins → detector de cambios → prueba contra base. Estimación: 6–10 jornadas y CPU/8–16 GB RAM; datos diarios de pocos activos, sin infraestructura de streaming. Evitar índices de «liquidez global» opacos, optimizar el lag macro sobre toda la muestra y mezclar balances mensuales con velas intradía.
