# Dictamen estratégico final

El mundo ya ha desarrollado casi todas las piezas técnicas necesarias para un laboratorio personal de investigación financiera. Lo que falta no es otro motor de cálculo: es una disciplina de evidencia que conecte fechas, definiciones económicas, incertidumbre y decisiones del analista. La oportunidad consiste en hacer esa conexión pequeña, transparente y útil cada semana.

## Qué cambia la forma de investigar

Los adaptadores públicos permiten leer cómo se construye una métrica y localizar dónde depende de una API, un contrato o una regla histórica. Los archivos de vintages permiten preguntar qué se sabía entonces. Los motores locales y formatos columnares hacen razonable trabajar con datos seleccionados sin una plataforma empresarial. Los modelos de extracción y forecasting pueden reducir trabajo preparatorio, siempre que su aporte se mida contra una base simple. [Comparaciones](08_TECHNOLOGY_COMPARISONS.md).

La investigación también muestra por qué esas capacidades no se deben combinar de forma automática. Un adaptador puede usar un upstream privado; un SDK puede normalizar campos y perder semántica; una función as-of puede conservar varias revisiones; una caché puede devolver una respuesta caducada con 200. Son detalles pequeños con consecuencias grandes para una tesis. Las revisiones técnicas señalan las rutas concretas, no defectos atribuidos indiscriminadamente a proyectos enteros.

## Ventaja funcional que sí puede defenderse

Una herramienta aporta una mejora verificable si permite reconstruir una cifra, detectar una revisión, distinguir devengo de transferencia, reducir una omisión o abstenerse cuando faltan datos. Estas mejoras se pueden probar con muestras, fixtures y revisión humana. Son diferentes de demostrar que una estrategia gana dinero.

Para este usuario, las capacidades con mejor relación utilidad/esfuerzo son: puentes de captura de valor, registro de tesis, contexto con vintages, normalización contractual de derivados y cronologías de eventos. No requieren inicialmente GPU, ejecución de órdenes, una organización de agentes o indexar todas las cadenas. Los requisitos domésticos expuestos son presupuestos orientativos; no se hicieron benchmarks locales.

## Dónde está la distancia entre promesa y evidencia

Los agentes financieros pueden redactar análisis convincentes y aun usar perfiles actuales en experimentos históricos. Otros proyectos ya incorporan mejores controles temporales: conviene extraerlos y comprobarlos, sin asumir que el debate entre agentes añade información. Un LLM también puede conocer hechos posteriores desde su entrenamiento. [FinGPT](03_DEEP_TECHNICAL_REVIEWS/ai_fingpt.md), [TradingAgents](03_DEEP_TECHNICAL_REVIEWS/ai_tradingagents.md).

Los foundation models pueden mejorar forecasts de ciertas magnitudes, pero resultados de benchmarks generales no se trasladan a retornos cripto. Un leaderboard puede compartir datasets o autores con los modelos evaluados. El permiso de los pesos puede impedir el uso imaginado incluso cuando el runtime es abierto. Estas son razones para ensayos pequeños, no para declarar inútil toda IA. [Evaluación de modelos](05_MODELS_AND_DATASETS.md).

Los dashboards de «smart money» y mapas de liquidaciones pueden ocultar la incertidumbre de etiquetas, posiciones no observadas, muestreo y definición de usuarios. No hay censo universal de intención económica en una blockchain. Un registro de transferencias no observa automáticamente compras internas en un CEX, ni un mint de stablecoin prueba entrada fiat: puede corresponder a una migración intercadena. [Hallazgos crypto](workstreams/crypto/findings.md).

Las listas de software suelen exagerar adoptabilidad. Esta revisión localizó deprecaciones, cambios de licencia, fechas futuras de conversión de BUSL y condiciones distintas entre código, contratos, pesos y datos. La etiqueta «public» o el nombre de una organización no resuelve esos permisos. [Licencias y riesgos](07_LICENSE_AND_RISK_MATRIX.md).

## Qué construir progresivamente

Investigar primero **Protocol Value & Dilution Analyzer** porque responde a la pregunta central sobre actividad sostenible y captura por token. Empezar con un protocolo y reconciliar cantidades antes de emitir ratios. Después, **Thesis Tracker**, para que un resultado tenga hipótesis, alternativas y una condición de revisión. Ambas pueden ser útiles con mucha curación manual.

La tercera capacidad es **Market Regime & Liquidity Navigator**, con bloques separados y fechas de conocimiento visibles. La cuarta, **Derivatives Stress Monitor**, debe diagnosticar presión con su frecuencia real de observación, sin dibujar liquidaciones futuras como hechos. La quinta, **Event Impact Research Lab**, aporta una manera de cuestionar catalizadores y conservar resultados negativos; su valor depende de cronologías y muestras comparables.

La selección reúne capacidades complementarias. El monitor de revisiones obtiene un score alto y se propone como función transversal. Un panel de cartera puede resolverse antes con componentes existentes. La evaluación de oportunidades explicita estas diferencias. [Diseños](12_TOP_FIVE_BLUEPRINTS/README.md).

## Innovaciones que merecen experimento

Comparar rankings usando la versión de métrica conocida entonces frente a la versión actual. Explicar una divergencia por precio, cantidades, incentivo, destinatario o cambio de cobertura. Medir cuánto cambia un mapa de flujos al retirar etiquetas dudosas. Vincular una predicción prospectiva a condiciones de resolución y evaluar calibración. Detectar cambios en la latencia del dato antes de emitir una alerta financiera.

Ninguna propuesta necesita ser inédita mundialmente para tener valor personal. La hipótesis es que estas combinaciones reducen errores concretos y carga de revisión. Si no superan una ficha manual o regla simple, se descartan o simplifican. [Combinaciones y experimentos](10_NOVEL_COMBINATIONS.md).

## Camino hacia utilidad diaria

1. Elegir una pregunta y un protocolo; redactar definición, fuentes y qué invalidaría la respuesta.
2. Conservar snapshots y fechas, incluida incertidumbre de disponibilidad; verificar permisos del alcance concreto.
3. Producir una ficha manual reproducible y registrar cuánto tarda y qué errores aparecen.
4. Automatizar únicamente adquisición repetida, validación y diferencias; mantener revisión de interpretación.
5. Añadir un modelo o detector solo con un experimento predefinido y una alternativa simple.
6. Pasar a una lectura diaria de 10–20 minutos con acceso a evidencia, sin ocultar huecos ni convertir alertas en órdenes.

Estos son pasos de un posible mandato posterior. Esta entrega es investigación y diseño: no ejecutó los experimentos, no modificó CIE ni publicó repositorios. El barrido es amplio dentro de su cobertura declarada, con sesgos claros hacia GitHub, Python, Hugging Face y fuentes occidentales; no es un censo mundial exhaustivo. La continuación útil está priorizada en el [backlog](13_RESEARCH_BACKLOG.md), no escondida detrás de una afirmación de completitud absoluta.
