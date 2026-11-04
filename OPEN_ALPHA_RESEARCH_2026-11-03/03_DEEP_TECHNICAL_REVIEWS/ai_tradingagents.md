# TradingAgents — revisión técnica estática

ID: `AI-tradingagents`. Verificado: 2026-11-04. Referencia estratégica: 2026-11-03; snapshot observado, no reconstrucción garantizada al cierre.

Commit: `c4544913a14ed3df5f1ed7b9e8483270ce20682a`. [Repositorio](https://github.com/TauricResearch/TradingAgents). [Licencia de código](https://raw.githubusercontent.com/TauricResearch/TradingAgents/c4544913a14ed3df5f1ed7b9e8483270ce20682a/LICENSE). Nivel V3 limitado a rutas citadas; sin instalación ni ejecución.

Puntuación editorial: **68/100**. Desglose: utility=18, evidence=11, data=8, ease=6, license=9, maintenance=6, usability=5, differentiation=5. Confianza: media-alta sobre rutas observadas; no sobre eficacia financiera. Los bloqueos de licencia/datos prevalecen.

## Veredicto

El repositorio actual contiene controles temporales concretos que merecen extraerse; descartarlo solo por ser multiagente ignoraría trabajo útil. Tampoco sus debates constituyen evidencia de ventaja de mercado. Priorizar controles as-of, abstención y estado de investigación; mantener el sistema completo como referencia hasta medir coste y exactitud frente a un flujo sencillo. Código Apache 2.0 inspeccionado; proveedores de datos/LLM son contratos separados.

## Arquitectura y controles observados

[trading_graph.py](https://github.com/TauricResearch/TradingAgents/blob/c4544913a14ed3df5f1ed7b9e8483270ce20682a/tradingagents/graph/trading_graph.py) coordina configuración de agentes, identidad del instrumento, memoria, checkpoints y reportes; observa `asset_type` crypto y estado de cartera. La firma de ejecución incluye parámetros que cambian el análisis, evitando reutilizar un checkpoint bajo otra configuración. `_memory_as_of` impone un corte a lecciones históricas; para ejecución del día el filtro cambia. Estos detalles son útiles para Thesis Tracker porque el pasado de una tesis no debe enriquecerse silenciosamente con lecciones posteriores.

[date_window.py](https://github.com/TauricResearch/TradingAgents/blob/c4544913a14ed3df5f1ed7b9e8483270ce20682a/tradingagents/dataflows/date_window.py) limita la fecha solicitada por una herramienta a la fecha del análisis, canonicaliza fechas y valida ventanas. También retiene perfiles live-only sin vintage e información de operaciones sin fecha de divulgación en análisis históricos. Esto reconoce que timestamp del evento y del conocimiento son distintos. No garantiza que todos los proveedores estén completos ni que un LLM no recuerde hechos posteriores por preentrenamiento.

## Evidencia de pruebas y límites

[test_tool_date_enforcement.py](https://github.com/TauricResearch/TradingAgents/blob/c4544913a14ed3df5f1ed7b9e8483270ce20682a/tests/test_tool_date_enforcement.py) comprueba fechas futuras, identidad del instrumento, fechas omitidas y ventanas inválidas. [test_fundamentals_lookahead.py](https://github.com/TauricResearch/TradingAgents/blob/c4544913a14ed3df5f1ed7b9e8483270ce20682a/tests/test_fundamentals_lookahead.py) exige retirar perfiles actuales en retrospectiva, incluso no realizar la llamada. Son verificaciones estáticas de diseño de tests, sin ejecución ni cobertura cuantificada. No es correcto afirmar que «no existe control de leakage» para este commit; sí es correcto que lo observado no resuelve contaminación del modelo ni todos los datos revisados.

## Riesgos prácticos

LangGraph y clientes LLM amplían superficie de dependencias. Noticias y documentos son entradas no confiables: una cita no debe convertirse en instrucción de herramientas. Permisos de lectura sola, destinos permitidos, límite de gasto y salida con referencias son controles a añadir/verificar para un producto futuro. No se probó aislamiento frente a prompt injection. El precio depende de tokens, número de agentes, rondas y proveedores: no se proporciona una tarifa inventada. CPU local 8–16 GB puede alojar orquestación, pero no implica capacidad de inferencia local del modelo elegido.

## Experimento propuesto

Veinte preguntas sobre cambios de tesis, cada una con fuentes congeladas y respuesta humana. Comparar flujo determinista + un modelo frente a debate de múltiples agentes usando el mismo corpus y presupuesto. Puntuar exactitud de citas, cifras recalculadas, contradicciones detectadas, abstención y minutos de revisión. Incluir documentos adversariales y futuras publicaciones que deben excluirse. Adoptar pasos extra solo si mejoran resultados fuera del conjunto usado para ajustar prompts.

Aprovechar controles temporales y trazabilidad; evitar tomar rating final, consenso narrativo o backtest con conocimiento retrospectivo como recomendación de inversión.
