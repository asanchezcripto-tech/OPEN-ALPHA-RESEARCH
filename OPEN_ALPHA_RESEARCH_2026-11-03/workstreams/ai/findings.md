# IA, modelos, datasets y agentes: conclusiones para consolidación

Referencia estratégica: 3-nov-2026. Observación: 4-nov-2026. Se verificaron 80 recursos diferenciados —62 repositorios y 18 cards de modelos/datasets—, con 10 revisiones estáticas profundas, 60 V2 y 10 V1. Las versiones de repositorios y cards están fijadas por SHA; no se reconstruyó la disponibilidad exacta de cada commit al cierre del día 3. Los 80 no son 80 aplicaciones listas para utilizar: incluyen bibliotecas, benchmarks, pesos y colecciones de datos, cuyas relaciones están explícitas en `relations.json`.

No se instalaron/importaron/ejecutaron proyectos externos, no se descargaron pesos o datasets, no se usaron claves ni APIs de pago. Los scripts auxiliares son propios y sirven para leer metadatos/texto y generar esta investigación. Las observaciones locales conservan URLs, hashes y metadatos; se retirará el texto de terceros del paquete final. La revisión es estática, sin auditoría integral de dependencias ni reproducir benchmarks.

## Lo que priorizaría

| Componente | Utilidad inmediata para el diseño | Decisión |
|---|---|---|
| fev | Tareas con cortes, inputs conocidos y evaluación por ventana | Adoptar tras piloto aislado; primero congelar datos |
| MLForecast + StatsForecast | Baselines explicables de actividad/fees/volatilidad | Empezar en CPU con pocas variables |
| River/ADWIN | Detectar cambios en errores de modelos y definiciones de datos | Monitor de diagnóstico; no señal de compra |
| Docling + Trafilatura | Texto/tablas con evidencia localizable | Medir cifras y citas antes de añadir RAG |
| Chronos 2 | Comparador probabilístico con covariables | Experimento limitado frente a naive y boosting |
| TradingAgents: controles temporales | Abstención sobre perfiles live-only, fechas y memoria | Extraer patrón; evaluar coste de agentes por separado |

Las puntuaciones se encuentran desglosadas en cada ficha. Son una priorización editorial de utilidad personal y de evidencia observada; no una medición de calidad en producción ni rentabilidad. La cadencia de mantenimiento no se ha cuantificado y limita la confianza de ese criterio. Una cifra alta nunca elimina un bloqueo de licencia o de datos.

## Hallazgos que cambian decisiones

**TimesFM3 no debe heredarse de la licencia del código.** La [card oficial](https://huggingface.co/google/timesfm-3.0-pytorch/blob/43046b85ec22d584a13f8098c2ed39c889e129c2/README.md) y su [LICENSE](https://huggingface.co/google/timesfm-3.0-pytorch/blob/43046b85ec22d584a13f8098c2ed39c889e129c2/LICENSE) separan las restricciones de los pesos del código Apache. La licencia incluye producción y usos de resultados; investigar con ella no implica autorización para desplegar un analista de inversión. La alternativa anterior [TimesFM2.5](https://huggingface.co/google/timesfm-2.5-200m-pytorch/blob/1d952420fba87f3c6dee4f240de0f1a0fbc790e3/README.md) declara Apache y debe evaluarse como recurso distinto. No se emite dictamen jurídico definitivo sobre inversión personal.

**FinBERT también separa código, pesos y datos.** El aviso oficial del [repositorio](https://github.com/ProsusAI/finBERT/blob/3b4bfed383a8bb6b013db2f1ce9c766ff5100d24/README.md) de 12-oct-2026 aclara alcance del código Apache. Los [pesos](https://huggingface.co/ProsusAI/finbert/blob/0bc2ac10dda6929bcb1f77ccc43c7ec5c424f031/README.md) declaran CC-BY-NC-SA4.0; Financial PhraseBank tiene CC-BY-NC-SA3.0. El modelo aporta clasificación de tono en inglés, no captura de valor del token ni un pronóstico de precio.

**Hay cambios de licencia y abandono que las listas históricas no reflejan.** Alibi Detect tiene [BSL1.1 en el commit observado](https://github.com/SeldonIO/alibi-detect/blob/c2fd0e05c648d353467bdb15fd6149a103b3a981/LICENSE), con cambio futuro a Apache por versión; no asumir que el código actual es Apache. Merlion, Azure/PyRIT y ProtectAI/llm-guard aparecen archivados en la página original consultada. Los metadatos y hashes de páginas se conservan; no se verificó un sucesor oficial de esos tres. Un fork activo tampoco quedaría recomendado sin auditoría propia.

**El problema de FinGPT Forecaster es verificable en rutas concretas.** [prompt.py](https://github.com/AI4Finance-Foundation/FinGPT/blob/ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8/fingpt/FinGPT_Forecaster/prompt.py) construye introducciones con perfiles actuales y las incorpora a prompts retrospectivos. [data.py](https://github.com/AI4Finance-Foundation/FinGPT/blob/ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8/fingpt/FinGPT_Forecaster/data.py) convierte razonamientos de entrenamiento condicionados al movimiento conocido. Esto permite estudiar corpus y tareas, pero exige controles adicionales antes de interpretar un experimento predictivo. [basics.py](https://github.com/AI4Finance-Foundation/FinGPT/blob/ac5c5443fbeeafad801e7a3c188e4f24cfaad4d8/fingpt/FinGPT_Forecaster/basics.py) aplica un retraso supuesto de 45 días; una aproximación de disponibilidad no es una fecha de publicación verificada.

**TradingAgents actual sí incorpora controles temporales relevantes.** En [date_window.py](https://github.com/TauricResearch/TradingAgents/blob/c4544913a14ed3df5f1ed7b9e8483270ce20682a/tradingagents/dataflows/date_window.py) se observan límites as-of y abstención sobre datos live-only; existen [tests](https://github.com/TauricResearch/TradingAgents/blob/c4544913a14ed3df5f1ed7b9e8483270ce20682a/tests/test_tool_date_enforcement.py) de fechas, identidad e inputs inválidos. Su mérito está en controles comprobables, no en que varios personajes coincidan. Aun con herramientas temporalmente correctas, un modelo moderno puede recordar hechos futuros del backtest.

**Una advertencia antigua puede quedar resuelta.** La búsqueda encontró un issue histórico de TiRex 2 sobre `flashrnn` y licencia; el [pyproject actual](https://github.com/NX-AI/tirex-2/blob/b187b7cab3ea11a40909a01601ec9b4ada8769e0/pyproject.toml) ya no declara esa dependencia. No arrastrar el bloqueo sin revisar commit. El código actual declara Apache, mientras el [TiRex anterior](https://github.com/NX-AI/tirex/blob/6d882eafdef969dc1b6b28e99db5e9bbca536419/LICENSE) tiene licencia comunitaria. Pesos TiRex 2 no auditados aquí: backlog, no adopción automática.

## Benchmarks: evidencia y límites

fev y GIFT-Eval son buenos mecanismos para comparar tareas; sus equipos también desarrollan modelos. Un ranking cruzado entre proveedores mejora la información pero no equivale a evaluación independiente ciega. El orden de modelos depende de frecuencia, horizonte, variable, cortes y ponderación de datasets. Los conjuntos heredados pueden compartir shocks globales con preentrenamiento aunque una serie concreta sea nueva: el [trabajo de Meyer et al., v 3](https://arxiv.org/abs/2510.13654v3) distingue solapamiento de muestras y solapamiento temporal de series correlacionadas. Se consultó el abstract e historial, no se reprodujeron resultados.

Un [preprint financiero de junio 2026](https://arxiv.org/abs/2606.27100v1) evalúa varias TSFM en cinco acciones y encuentra mejoras sobre random walk pequeñas y poco generalizadas. Es evidencia externa útil para cuestionar extrapolaciones; cinco acciones y un estudio no permiten concluir cómo funcionarán BTC/ETH/HYPE. Tampoco demuestra que toda IA de forecasting sea inútil: reducir preparación de modelos puede tener valor sin generar alpha.

[FinVerse v 3](https://arxiv.org/abs/2608.03259v3), revisado en octubre 2026, propone evaluación por significado económico y resultados de ranking/cartera. Es una línea de investigación pertinente, no un benchmark auditado en este mandato: solo se leyeron abstract y metadatos, y no se verificaron código, datasets, permisos ni costes. Backlog prioritario por su alineación con la pregunta financiera. No trasladar números de su versión 1 al título/conclusiones de la versión 3.

[ForecastBench](https://www.forecastbench.org/about/) aporta otro patrón: pronosticar eventos antes de resolverse y puntuarlos después, en vez de pedir retrospectivas a un LLM que conoce la historia. Sus preguntas incluyen datos y mercados predictivos. La metodología merece reutilización conceptual en Thesis Tracker; para comparaciones con mercados hay que registrar si el modelo ve el consenso de mercado, y para humanos/modelos si responden las mismas preguntas. No se auditó aquí su código o permisos de cada origen.

FinanceBench ofrece una muestra pública 150 casos; la descripción de 10231 preguntas no implica disponibilidad del conjunto completo. La [card HF](https://huggingface.co/datasets/PatronusAI/financebench/blob/e04404e3a97f69f79c14d42f24981a1c9c3bcd18/README.md) declara CC-BY-NC4.0, mientras no se encontró LICENSE en rutas estándar del repo. No resolver esa diferencia con licencias citadas por terceros. [FinQA](https://github.com/czyssrs/FinQA/blob/0f16e2867befa6840783e58be38c9efb9229d742/README.md) documenta una corrección histórica de fuga por formato de filas: refuerza la necesidad de fijar versión, no basta con citar el nombre del benchmark.

## Hardware y costes para un particular

Son presupuestos propuestos para pilotos pequeños, no mínimos oficiales ni mediciones. No se conoce el hardware del usuario y no se propone comprar equipo.

| Familia | CPU/RAM orientativa | GPU | Almacenamiento y coste |
|---|---|---|---|
| fev, StatsForecast, MLForecast, River | CPU; 8–16 GB RAM para panel pequeño | No necesaria por diseño inicial | Parquet seleccionado; sin API obligatoria, tiempo de limpieza domina |
| Docling | CPU; 16 GB RAM como presupuesto de piloto | Opcional según OCR/VLM | Documentos y modelos elegidos; capacidad no medida |
| Chronos 2 |120 M parámetros;≈0.48 GB de pesos FP32, más runtime/activaciones | Opcional; CPU soportada por autores | No pesos descargados; coste local eléctrico no cuantificado |
| TimesFM3 |≈0.3 B parámetros;≈1.2 GB de pesos FP32 solamente | Depende de lote/backend | Restricción de licencia antes de coste; no tarifa comercial inferida |
| Moirai 2-small |11.4 M parámetros;≈46 MB de pesos FP32 solamente | No justificar compra por tamaño | Runtime pesa más que tensores; CC-BY-NC |
| FinBERT/BGE pequeño | CPU para lotes reducidos; 8 GB como presupuesto | Opcional | Fijar checkpoint y permisos; no convertir embeddings en «hechos» |
| Agentes con LLM remoto | CPU8–16 GB para orquestación | GPU del proveedor | Nºpreguntas × rondas × tokens × tarifas verificadas en el futuro; sin cifra inventada |

La versión River examinada requiere Python≥3.11; el Python 3.10 observado en la máquina no satisface esa versión. Se registra como incompatibilidad potencial para futuro piloto. No se modificó el entorno.

## Combinaciones con hipótesis comprobable

1. **Auditor de cambios de definición.** River sobre diferencias entre dos fuentes + registro de adaptador/versión. Hipótesis: reduce falsas alertas de fundamentales causadas por cambios de ingesta. Medir demora, falsos positivos y minutos de diagnóstico; no asumir que una discrepancia señala manipulación.
2. **Thesis Tracker con evidencia congelada.** Docling/Trafilatura + extracción tipada + cálculo determinista + controles as-of de TradingAgents. Hipótesis: localizar antes contradicciones y omisiones que una revisión manual sin registro. Medir precisión/cobertura de citas, errores numéricos y tiempo; almacenar hipótesis alternativas y abstenciones.
3. **Descomposición de sorpresa de fundamentales.** MLForecast/StatsForecast como baseline de actividad + Chronos 2 como contraste + fev. Hipótesis: distinguir crecimiento esperable de cambios persistentes en revenue/incentivos. Validar por regímenes y con datos conocidos; no construir directamente target price.
4. **Ensayo prospectivo de catalizadores.** Registro de probabilidades y fechas de resolución inspirado en ForecastBench + métricas Brier/log loss y actualizaciones justificadas. Hipótesis: mejorar calibración del investigador; separar exposición a consenso público de aportación incremental. Evitar comparar solamente aciertos finales.
5. **RAG de números con rechazo.** Recuperación BM25/BGE + tabla/unidad/fecha de Docling + funciones aritméticas. Hipótesis: menos errores graves que LLM sobre texto aplanado. Una respuesta sin fragmento exacto, moneda, escala o fecha no pasa al informe.

## Hallazgo contracorriente fuera del inglés

La consulta china encontró [Tencent finLLM-Eval](https://github.com/Tencent/finLLM-Eval/blob/2747fb219d553dea0a183269554ce174aeb00531/README.md). Es interesante por separar hechos, lógica y tripletas activo-fecha-métrica. Su propio README indica que la evaluación completa de exactitud de cifras usa una base financiera interna no publicada: la capacidad más atractiva anunciada no está completamente disponible. No se localizó licencia en las rutas estándar. Conservar la técnica, no adoptar el paquete como verificador universal.

## Seguridad, prioridades y backlog

Un sistema de investigación debe tratar fuentes como datos, mantener herramientas de lectura permitidas y separar los extractores del generador. Esquema validado≠hecho verdadero; citación existente≠cita que respalda la afirmación. Jueces LLM —Ragas, DSPy u otros— ayudan a seleccionar ejemplos, pero el conjunto de evaluación debe incluir fuentes y cálculos comprobados por una persona. Guardrails clasificadores no sustituyen aislamiento y permisos.

Primero medir extracción de hechos y valor de la evidencia diaria. Después comparar uno o dos modelos de forecasting; solo entonces considerar agentes adicionales o fine-tuning. Aplazar modelos enormes, RL para trading, entrenamiento de foundation models y ensembles masivos. Investigar más: FinVerse con código y permisos, evaluación multilingüe propia, sucesores de proyectos archivados, licencias de todos los checkpoints añadidos, benchmark de extracción de tablas de DeFi y reproducibilidad de temporalidad en fuentes reales.

Los fallos de rutas durante exploración son 404/ausencias de archivos, conservados en observaciones; no implican ausencia del proyecto. No se consultaron aquí GitLab/Codeberg/SourceHut: los cubre la coordinación con sus propias limitaciones. El sesgo del área sigue siendo GitHub/Hugging Face y documentación en inglés; la consulta china mejora descubrimiento sin convertirlo en cobertura mundial completa.
