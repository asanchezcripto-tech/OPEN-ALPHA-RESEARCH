# Cobertura y metodología

Referencia solicitada: 2026-11-03. Observación efectiva: 2026-11-04. No se retrofechó ninguna verificación. Se fijaron commits/cards cuando fue posible; no se reconstruyó sistemáticamente qué commit estaba disponible al cierre del día 3. Las conclusiones sobre estado actual se refieren al contenido observado el 4.

## Resultado contado y límites de cada nivel

| Magnitud | Resultado |
|---|---:|
| Recursos diferenciados en catálogo principal |288|
| Consulta original suficiente para el nivel declarado |285|
| V3: revisiones técnicas estáticas de rutas críticas |39|
| V2: documentación más licencia o archivo técnico |208|
| V1: existencia/alcance/card/abstract |38|
| D0: comprobación insuficiente |3|
| Registros de fuentes, incluidos fallos |1081|
| URLs de fuente distintas |1072|
| Evidencias registradas |686|
| Consultas de búsqueda registradas |79|
| Métodos / comparaciones |32 / 22|
| Componentes seleccionados |22|
| Conceptos / diseños preliminares |16 /5|

La meta orientativa de 250–500 candidatos, 100 recursos verificados y 30–50 revisiones se alcanza **bajo estas definiciones**. No significa auditar 288 proyectos completos: muchos son bibliotecas de apoyo, cards, datasets, servicios o referencias académicas. Los inventarios especializados son vistas o fichas complementarias; no deben sumarse como recursos nuevos. FRED-MD/FRED-QD comparten URL pero son datasets distintos. Dos duplicados de repositorio —DoWhy/EconML— se consolidaron, conservando fuentes de ambas áreas. Las licencias/capas de pesos y código se mantienen separadas.

Los registros de fuentes incluyen archivos distintos del mismo proyecto y rutas fallidas. Hay 982 registros con estado 200/consultado; el resto son fallos/lecturas insuficientes. Ese conteo no son 982 proyectos ni 982 afirmaciones verificadas. El hash identifica contenido, no certifica veracidad. V3 tampoco implica ejecutar tests, medir cobertura, auditar todas las dependencias o probar una estrategia.

## Cobertura por categoría

Un recurso puede pertenecer a varias categorías: estas filas no deben sumarse. V3 indica lectura estática de rutas seleccionadas, no una auditoría completa del área.

| Área | Recursos | V3 |
|---|---:|---:|
| A — Macro | 31 | 3 |
| B — Mercado cripto | 26 | 8 |
| C — Derivados | 18 | 6 |
| D — On-chain | 50 | 5 |
| E — Fundamentales y valoración | 27 | 3 |
| F — Oportunidades | 11 | 2 |
| G — Validación cuantitativa | 70 | 12 |
| H — IA y modelos | 75 | 9 |
| I — Agentes | 29 | 3 |
| J — Noticias y eventos | 20 | 4 |
| K — Cartera y riesgo | 20 | 5 |
| L — Visualización | 22 | 1 |
| M — Datos e infraestructura | 106 | 19 |
| N — Fuentes alternativas | 19 | 3 |

## Pasadas realizadas

**A — Cartografía.** Puntos de partida del mandato, consultas especializadas, organizaciones de protocolos, documentación, repositorios y cards. Búsquedas en inglés, español, chino y una consulta alemana; amplitud lingüística limitada. Priorización de horizonte 3–18 meses y preguntas económicas, no de funcionalidades de trading.

**B — Relaciones.** Seguir manifiestos, módulos, tests, referencias, SDK→servicio, código→pesos→datos y sucesores oficiales. No se descargaron dependencias ni se clonó masivamente. Se conserva un grafo con aristas tipadas en [relations](inventories/relations.json).

**C — Contracorriente.** Bibliotecas de reconciliación, contratos, monitorización y benchmarks; prototipos bitemporales y recursos macro. Se valoran por el error que pueden evitar, no por estrellas. Algunos prototipos se conservan solo como técnicas por carecer de licencia verificada.

**D — Comparación y depuración.** Separar SDK, protocolo, mirror, fork, herramienta, servicio cerrado, paper y modelo. Comprobar las dos migraciones del SDK Polymarket, continuidades/forks quant y marcas de archivo. No se auditó exhaustivamente el diff de cada fork ni su sostenibilidad. Las URLs incorrectas y cambios de canonical se registran; un 404 no implica inexistencia del proyecto.

## Fuentes, acceso y sesgos

GitHub/raw, documentación oficial, Hugging Face, bancos centrales/organismos y autores académicos fueron las fuentes principales. PyPI/Conda e índices ayudan a descubrir/migrar nombres; no se usan como prueba suficiente de capacidades. Las fuentes sociales solo orientaron descubrimiento, no conclusiones técnicas. No se consultaron cuentas privadas ni se solicitaron credenciales.

GitLab produjo resultados escasos/no pertinentes; Codeberg/SourceHut tuvieron bloqueos del motor y cobertura insuficiente. El mirror CRAN de strucchange permite identificar su procedencia, pero no sustituye una auditoría del original. Kaggle, Hugging Face Spaces, SSRN, Semantic Scholar, Docker Hub, repositorios universitarios no anglófonos y forks fuera de GitHub **no recibieron un barrido directo sistemático**. No se presenta cobertura completa de esas fuentes. Las cotizaciones ETF, opciones históricas, macro asiática y etiquetas on-chain son lagunas relevantes.

No se eludieron robots, autenticación, restricciones ni límites. No se contrataron APIs. ECB API/Treasury API y la pista emissions-adapters quedan D0. En Raydium la URL antigua falló y se localizó la canonical; se conserva esa corrección sin afirmar configuración desplegada universal.

## Protocolo de evidencia y seguridad

Se hizo lectura estática de código, tests, manifests y licencias. Las conclusiones distinguen código observado, declaración de autores, resultado externo no reproducido e inferencia/diseño propio. El texto externo se trató como datos; no se siguieron instrucciones incrustadas. Los auxiliares propios solo consultan fuentes y generan documentos/inventarios. No se importó ni ejecutó código de terceros.

La coordinación revisó afirmaciones decisivas de fredapi, skfolio, TimesFM3, Polymarket y fuentes de protocolos, además de las revisiones de infraestructura. Hubo revisión independiente cruzada de los cinco blueprints; se incorporaron correcciones sobre oferta, denominador de cobertura, OI/funding, frecuencia, CAR, clusters, soporte de citas y permisos. [Registro de revisión](QUALITY_REVIEW.md).

## Puntuación y decisiones

| Criterio | Máximo |
|---|---:|
| Utilidad para análisis e inversión personal |25|
| Calidad técnica y evidencia |15|
| Datos disponibles/verificables |15|
| Facilidad de reutilización |12|
| Licencia/compatibilidad |10|
| Mantenimiento/sostenibilidad |8|
| Uso diario |8|
| Diferenciación |7|
| **Total** |**100**|

Son enteros editoriales, no mediciones de producción. D0 no recibe score consolidado. Fuentes/papers/servicios con evidencia insuficiente para comparar pueden quedar sin puntuación. No ordenar automáticamente todas las categorías juntas: una base de datos y un paper no resuelven la misma pregunta.

La confianza y los bloqueantes se publican aparte. Mantenimiento se valoró de forma provisional porque no se auditó una cronología completa de issues/releases; «no archivado» no demuestra sostenibilidad. Variaciones pequeñas de puntuación no justifican decisiones distintas. Antes de adoptar: resolver permiso y datos, fijar alcance y comparar contra alternativa simple. La lista de 22 componentes incluye referencias/técnicas con copia bloqueada; no es una lista de instalación.

## Consultas y continuidad

Las consultas exactas, fechas y resultados se conservan en [search_log.csv](inventories/search_log.csv) y JSON. Las aperturas directas y lecturas HTTP adicionales están en [sources](inventories/sources.json), no se confunden con consultas de búsqueda. El protocolo común y los scripts auxiliares explican reproducción de la catalogación; los commits/hashes fijan lo observado aunque la web futura cambie.

Persisten límites: historia de mantenimiento, auditoría transitiva, contratos desplegados, derechos completos de datasets, latencia real, integridad de históricos y todos los ensayos empíricos. Los experimentos se han diseñado, no ejecutado. Ver [backlog](13_RESEARCH_BACKLOG.md) y [estado por etapas](inventories/stage_log.json).
