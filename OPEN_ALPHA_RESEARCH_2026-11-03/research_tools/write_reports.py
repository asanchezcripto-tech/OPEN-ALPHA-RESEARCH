"""Render narrative research registers from the normalized, reviewed inventories."""
import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(n):return json.loads((ROOT/'inventories'/(n+'.json')).read_text(encoding='utf-8'))
projects=read('projects');lookup={r['id']:r for r in projects};sources={r['id']:r for r in read('sources')}
def val(x):
    if isinstance(x,list):return '; '.join(str(i) for i in x)
    if isinstance(x,dict):return '; '.join(f'{k}: {v}' for k,v in x.items())
    return str(x) if x is not None else 'No comprobado.'
def links(ids):return ', '.join(f"[{lookup[i]['name']}]({lookup[i]['url']})" if i in lookup else f'`{i}`' for i in ids)
def source_links(ids,maxn=4):return ', '.join(f"[{sources[i]['title']}]({sources[i]['url']})" for i in ids[:maxn] if i in sources)
intro='''# Algoritmos y métodos transferibles

El conocimiento reutilizable es más amplio que los repositorios. Estas fichas separan problema, supuestos, datos, validación, fallos y situaciones de abstención. Las propuestas cripto se apoyan en implementación/documentación inspeccionada, pero no se han calculado ni probado sobre una cartera real.

## Orden de trabajo recomendado

Primero identidad, unidad y fecha de conocimiento; después una base sencilla; finalmente modelos más complejos si mejoran una tarea predefinida. Para horizontes de3–18meses, retornos de un año calculados cada día se solapan: no son cientos de observaciones independientes. La longitud efectiva de la muestra y el número de regímenes limitan cualquier inferencia.

La validación temporal abarca todo el pipeline: universo, limpieza, escalado, selección de variables, ajuste, embeddings/memoria y ranking. Añadir información futura no debe cambiar una salida pasada. Purga/embargo deben corresponder al intervalo de las etiquetas, no solo al número de filas; CPCV no sustituye seguimiento prospectivo. Un modelo de lenguaje puede recordar hechos posteriores aunque sus herramientas respeten el corte.

Para regímenes, distinguir probabilidades filtradas de suavizadas y detección online de segmentación offline. Para causalidad, definir tratamiento, cronología, controles y supuestos; una correlación rezagada o una biblioteca causal no establece identificación. Para tests múltiples, registrar todos los ensayos: ningún ajuste rescata un historial selectivo de resultados.

En riesgo, expected shortfall es pérdida media de cola bajo una distribución estimada, no límite de pérdida. VaR puede infravalorar liquidez, gaps y contraparte. En cripto, documentar calendario24/7, convención de anualización, tipos de contratos y exposición a stablecoins. No trasladar por defecto252sesiones o frecuencia de funding de otro mercado.

En valoración, el puente de fees a captura es un registro de mecanismos, no una identidad universal revenue=beneficio del token. Un unlock no siempre crea tokens; mint entre cadenas puede compensar burn en otra. En grafos, evaluar qué cambia al retirar etiquetas inciertas antes de atribuir flujos a entidades.

## Fichas de técnicas

'''
text=intro
labels=[('problem','Problema'),('assumptions','Supuestos'),('data_frequency','Datos y frecuencia'),('validation','Cómo validar'),('common_failures','Fallos habituales'),('simple_implementation','Implementación sencilla o reutilización'),('crypto_value','Valor para cripto'),('do_not_use_when','Cuándo abstenerse')]
for m in read('algorithms'):
    text+=f"### {m['id']} — {m['name']}\n\n"
    for k,label in labels:text+=f"**{label}:** {val(m.get(k))}\n\n"
    text+='**Implementaciones/candidatos:** '+links(m.get('implementations',[]))+'.\n\n'
    text+='**Fuentes:** '+(source_links(m.get('source_ids',[])) or f"[Referencia]({m.get('url')})")+'. La ficha es una síntesis; consultar el alcance de lectura de cada fuente.\n\n'
text+='## Papers y grado de lectura\n\n'
for p in read('papers'):
    text+=f"- [{p.get('name') or p.get('title')}]({p.get('url')}) — {val(p.get('version_or_commit') or p.get('publication'))}. {val(p.get('reading_scope') or p.get('limitations'))}\n"
text+='\nLos inventarios [algorithms.json](inventories/algorithms.json) y [papers.json](inventories/papers.json) conservan IDs y fuentes. No todos los trabajos se leyeron completos: los abstracts y pistas de investigación se identifican expresamente, y ningún benchmark fue reproducido.\n'
(ROOT/'04_ALGORITHMS_AND_METHODS.md').write_text(text,encoding='utf-8')
text='''# Modelos, datasets y benchmarks

La recomendación inicial es separar tareas. Forecasting de volumen/fees/volatilidad, anomalías, extracción documental, clasificación de texto y pronóstico de retorno son problemas distintos. El primer piloto debe comparar una base naive/estacional, una regresión o boosting sencillo y como máximo un foundation model. El coste de limpiar y fechar datos puede superar al de inferencia.

## Selección técnica

StatsForecast y MLForecast ofrecen bases de comparación; fev ayuda a fijar tarea/cortes. Chronos2 merece un experimento acotado por sus cuantiles y covariables, sin asumir alpha. River sirve para vigilar errores/cambios de datos. Docling/Trafilatura son útiles para localizar evidencia, con revisión de tablas, unidades y fechas. No es necesario un sistema de debate multiagente para estas capacidades.

TimesFM3 existe, pero los términos observados de sus pesos incluyen restricciones no comerciales y de producción: no heredan automáticamente Apache del repositorio de código. FinBERT también separa código y pesos; Moirai exige revisar cada checkpoint. Alibi Detect actual tiene BSL; no clasificarlo por una licencia antigua. Ver las revisiones y [matriz de riesgos](07_LICENSE_AND_RISK_MATRIX.md).

## Pesos examinados

La verificación de card/licencia es documental; no se descargaron pesos ni se hizo inferencia. Los datos de preentrenamiento no quedan autorizados por la licencia del checkpoint.

| Recurso | Capacidad declarada | Licencia de pesos/card | Decisión y límites |
|---|---|---|---|
'''
for m in read('models'):
    text+=f"| [{m['name']}]({m['url']}) | {val(m.get('description')).replace('|','/')} | {val(m.get('license_weights') or m.get('license_code'))} | {val(m.get('adoption_mode'))}; {val(m.get('blockers') or m.get('limitations')).replace('|','/')} |\n"
text+='''
## Evaluación de benchmarks

fev y GIFT-Eval estandarizan parte de la comparación, pero sus equipos también desarrollan modelos. Un leaderboard no es un estudio independiente ciego ni demuestra capacidad de anticipar rendimientos. Fijar versión, cortes, frecuencias, horizontes, covariables conocidas y ponderación por dataset; comprobar solapamiento de muestras y de shocks temporales entre series correlacionadas.

FinQA, TAT-QA y FinanceBench evalúan capacidades relevantes de lectura/cálculo, no constituyen por sí solos un benchmark DeFi. FinanceBench ofrece una muestra pública de150casos; el tamaño descrito del conjunto mayor no implica que todo esté disponible. La corrección histórica de leakage de formato en FinQA refuerza la necesidad de fijar versión. Los tres preprints IA recientes se revisaron solo a nivel de abstract/historial; sus conclusiones no son resultados propios ni pruebas específicas en BTC/ETH/HYPE. [Detalle de fuentes y limitaciones](workstreams/ai/findings.md).

Métricas propuestas: MASE/WIS/pinball y cobertura por horizonte para forecasts; Brier/log loss y calibración para probabilidades; precisión de soporte de citas, error numérico y abstención para documentos. Rentabilidad neta, turnover, drawdown y estabilidad por régimen requerirían una pregunta económica y validación separadas. No inferir ganancias de menor error de precio.

## Datasets y fuentes de datos

Este inventario mezcla datasets descargables, colecciones de vintages y superficies de datos de servicios. Esa clase debe leerse junto al acceso y permisos; ninguno se descargó de forma completa ni se midió su integridad.

| Recurso | Alcance | Permiso/capa observada | Límite principal |
|---|---|---|---|
'''
for d in read('datasets'):
    text+=f"| [{d['name']}]({d.get('url')}) | {val(d.get('coverage') or d.get('description')).replace('|','/')} | {val(d.get('license') or d.get('license_data') or d.get('license_status')).replace('|','/')} | {val(d.get('temporal_risk') or d.get('limitations')).replace('|','/')} |\n"
text+='''
## Hardware y coste: presupuestos de piloto, no mediciones

| Familia | Presupuesto orientativo | Límite de la estimación |
|---|---|---|
| Baselines, fev, River | CPU,8–16GB RAM para panel pequeño | Depende de número/longitud de series y validaciones |
| Docling/OCR | CPU,16GB como partida | Modelos OCR/VLM y tablas pueden elevar recursos; permisos separados |
| Chronos2 |120M parámetros;≈0.48GB de tensores FP32 | Runtime, activaciones, lotes y contexto aumentan memoria; CPU soportada según autores |
| TimesFM3 |≈0.3B parámetros;≈1.2GB de tensores FP32 | Primero resolver licencia; no dimensionar RAM/GPU solo por pesos |
| Moirai2-small |11.4M parámetros;≈46MB de tensores FP32 | Runtime puede dominar; pesos con restricciones |
| Agentes con modelo alojado | CPU para orquestar; gasto por consumo | Nºllamadas×tokens×tarifa vigente más reintentos; no precio inventado |

Estas cuentas de tensores usan4bytes por parámetro y GB decimales; no son mínimos de ejecución ni hardware recomendado para comprar. No se conoce la RAM/GPU del usuario. River/Polars/marimo revisados requieren Python≥3.11; no se modificó el Python3.10 usado por los auxiliares propios.

Primero comprobar si la base simple basta. Solo ampliar modelos si la mejora se sostiene bajo el mismo presupuesto, datos y cortes. La licencia de código no cubre pesos, documentos, servicios ni datasets; un futuro piloto debe fijar esas capas en su propio manifest. [Inventario de modelos](inventories/models.json), [datasets](inventories/datasets.json) y [papers](inventories/papers.json).
'''
(ROOT/'05_MODELS_AND_DATASETS.md').write_text(text,encoding='utf-8')
text='''# Comparaciones tecnológicas por escenario

Son decisiones de ingeniería apoyadas en revisión estática, no benchmarks propios. No comparar un framework general y una función pequeña como si resolvieran el mismo alcance. Las preferencias se limitan al analista individual, horizonte de3–18meses y ausencia de ejecución automática.

La regla de adopción es: resolver primero la pregunta, después el contrato de datos y finalmente elegir el componente más pequeño suficiente. Un riesgo bloqueante de licencia o de histórico prevalece sobre el score.

'''
for c in read('comparisons'):
    text+=f"## {c['name']}\n\n**Alternativas:** {links(c.get('candidate_ids',[]))}.\n\n"
    pref=c.get('preferred') or c.get('winner_by_scenario') or c.get('decision')
    text+=f"**Elección por escenario:** {val(pref)}\n\n"
    text+=f"**Coste y límites:** {val(c.get('tradeoff') or c.get('limits') or c.get('reason'))}\n\n"
    if c.get('unmeasured'):text+=f"**No medido:** {c['unmeasured']}\n\n"
    text+='**Evidencia:** '+source_links(c.get('source_ids',[]),3)+'. Fuentes restantes y versiones en el inventario.\n\n'
text+='''## Qué usar directamente y qué requiere adaptación

Los paneles públicos de DefiLlama y las páginas oficiales de protocolos permiten comenzar una ficha manual, conservando sus límites. Dune/Token Terminal sirven como referencia funcional y contraste de definiciones; son servicios con condiciones propias. marimo, Datasette, VisiData u OpenBB/OpenBQ son candidatos de uso directo tras instalación/permiso y verificación de fuentes, no instalaciones realizadas aquí.

Bibliotecas como DuckDB, arch o Pandera exigen pequeñas integraciones; su licencia no entrega datos. SDKs actuales permiten lectura, pero también contienen superficies de ejecución que deben quedar fuera del producto propuesto. Los prototipos sin licencia y los agentes financieros completos son referencias o experimentos, no recomendaciones de despliegue inmediato.

No se recomienda construir desde cero un motor SQL, parser documental, cliente de exchange completo, motor genérico de backtesting ni un foundation model. Sí diseñar explícitamente el pequeño contrato temporal, las definiciones financieras, los criterios de abstención y los experimentos de utilidad que ninguna biblioteca decide por el usuario.
'''
(ROOT/'08_TECHNOLOGY_COMPARISONS.md').write_text(text,encoding='utf-8')
print('Wrote methods, models/datasets and comparisons reports.')
