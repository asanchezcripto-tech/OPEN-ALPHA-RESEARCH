"""Write the documentary stage register and polish prose; stdlib, offline."""
import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
I = ROOT / 'inventories'
stages = [
    ('A', 'Descubrimiento amplio',
     'Catorce áreas A–N; organizaciones, índices, documentación, repositorios y cards.',
     '79 consultas registradas y aperturas originales con trazabilidad de acceso.',
     'Resultados genéricos o comerciales sin evidencia primaria suficiente como prueba técnica.',
     'Cobertura menor de GitLab/Codeberg/SourceHut y ausencia de barrido sistemático de varias fuentes académicas/comunitarias.',
     'Reconciliación de datos, revisiones temporales y mecanismos de captura de valor.',
     ['search_log.json', 'sources.json', '../01_SEARCH_COVERAGE.md']),
    ('B', 'Catalogación',
     '288 recursos diferenciados, clasificados por tipo, utilidad, nivel, permisos y bloqueantes.',
     'IDs, URL canónica, fecha/versión disponibles y fichas con alcance explícito.',
     'Interpretar cada card, SDK o servicio como una aplicación independiente lista para usar.',
     'Campos nulos: idioma, release, issues, pruebas o hardware que no se auditaron en todas las fichas.',
     '22 componentes útiles como bibliotecas, técnicas o referencias, con bloqueantes separados.',
     ['projects.json', 'selected_components.json', '../02_PROJECT_CATALOG.md']),
    ('C', 'Depuración y eliminación de duplicados',
     'Solapamientos entre áreas, recursos originales/forks/mirrors y sucesores oficiales.',
     'Dos entradas duplicadas de repositorio consolidadas: DoWhy y EconML; FRED-MD/QD diferenciados por dataset.',
     'Sumar vistas especializadas al total y recomendar los SDK Polymarket anteriores como opción vigente.',
     'Diff completo y mantenimiento longitudinal de todos los forks.',
     'Migración documentada al SDK unificado de Polymarket.',
     ['deduplication.json', 'relations.json', '../03_DEEP_TECHNICAL_REVIEWS/crypto_polymarket_sdk.md']),
    ('D', 'Verificación de recursos',
     'Documentación original, licencias, cards y archivos técnicos de candidatos.',
     '285 recursos con consulta suficiente para su nivel: 38 V1, 208 V2 y 39 V3.',
     'Dar por verificados ECB API, Treasury API y emissions-adapters con evidencia insuficiente; quedan D0.',
     'Corte exacto al 3-nov y recursos que no permitieron lectura; condiciones completas de algunos datos/servicios.',
     'Separar permiso de código, pesos, datasets, servicio y contratos de una misma marca.',
     ['sources.json', 'evidence.json', 'licenses.json']),
    ('E', 'Análisis técnico profundo',
     '39 rutas críticas: 10 quant, 10 crypto, 10 IA y 9 infraestructura.',
     'Comportamiento estático documentado, manifiestos y tests seleccionados cuando fueron accesibles.',
     'Equiparar lectura de tests con ejecución, cobertura o seguridad integral.',
     'Ejecución aislada, rendimiento, dependencias transitivas, cobertura real y comportamiento en producción.',
     'Controles de vintages, stale cache, nulos, OI/funding y soporte documental.',
     ['../03_DEEP_TECHNICAL_REVIEWS/README.md', 'evidence.json']),
    ('F', 'Evaluación de algoritmos y modelos',
     '32 métodos, 11 modelos, 22 fichas de datasets y 8 papers/líneas de investigación.',
     'Supuestos, fallos, licencias observadas, función del benchmark y alcance de lectura.',
     'Derivar rentabilidad cripto de forecasting general, sentimiento o resultados de autores no reproducidos.',
     'Inferencia local, calibración prospectiva, rendimiento por régimen y auditoría completa de los papers.',
     'Bases estadísticas antes de foundation models; IA acotada para extracción y cambios.',
     ['algorithms.json', 'models.json', 'datasets.json', 'papers.json']),
    ('G', 'Comparación',
     '22 comparaciones por escenario entre bibliotecas, servicios y métodos.',
     'Tradeoffs de complejidad, alcance temporal, fuente, licencia y operación personal.',
     'Ranking universal por popularidad o puntuación total sin comprobar bloqueantes.',
     'Benchmarks comparables de tiempo, coste y precisión sobre datos propios.',
     'Almacén local, ficha manual y baseline simple como alternativas evaluables.',
     ['comparisons.json', '../08_TECHNOLOGY_COMPARISONS.md']),
    ('H', 'Descubrimiento de oportunidades',
     '16 conceptos autónomos y 12 combinaciones de técnicas con hipótesis comprobables.',
     'Problema, datos, arquitectura mínima, resultado visible, coste estimado y métrica de utilidad.',
     'Construcción de una plataforma global, HFT o superagente de inversión durante este mandato.',
     'Demanda real, ahorro de tiempo y reducción de errores aún no medidos.',
     'Monitor de revisiones, trazabilidad de tesis y puentes de captura de valor.',
     ['opportunities.json', '../09_HIDDEN_GEMS.md', '../10_NOVEL_COMBINATIONS.md']),
    ('I', 'Diseño preliminar',
     'Protocol Value, Thesis Tracker, Regime Navigator, Derivatives Stress y Event Lab.',
     'Flujos, entradas/salidas, alternativa gratuita limitada, abstención y experimentos mínimos.',
     'Implementar productos o prometer históricos completos y plazos sin comprobar fuentes.',
     'Elección final de protocolo/venues, permisos por fuente y criterios empíricos del futuro piloto.',
     'Una primera capacidad útil por herramienta sin depender de CIE.',
     ['../12_TOP_FIVE_BLUEPRINTS/README.md', 'opportunities.json']),
    ('J', 'Revisión crítica',
     'Revisión cruzada por tres áreas y comprobación de afirmaciones decisivas del coordinador.',
     'Correcciones incorporadas de supply, cobertura, temporalidad, citas, permisos, OI/funding, CAR y dependencia.',
     'Cero fallos en muestras pequeñas como garantía de producción; diagnóstico contemporáneo como predicción.',
     'Auditoría externa y validación económica; los revisores pertenecen al mismo equipo de investigación.',
     'Criterios de aceptación más precisos y control de información futura a lo largo de toda la canalización.',
     ['../QUALITY_REVIEW.md', '../workstreams/quant/critical_review.md', '../workstreams/crypto/critical_review.md', '../workstreams/ai/critical_review.md']),
    ('K', 'Consolidación final',
     'Informes, inventarios CSV/JSON, navegación, manifiesto y paquete local.',
     'Integridad comprobada por auxiliar propio; consultar resultado exacto de quality_checks.json.',
     'Cachés de texto externo, bytecode y cualquier publicación remota del paquete.',
     'No se revisitaron todas las URLs en esta pasada; los resultados documentales no son pruebas de software.',
     'Continuar por ID y afirmación sin repetir el barrido completo.',
     ['README.md', 'quality_checks.json', '../README.md', '../FILE_MANIFEST.json']),
]
rows = []
for code, name, examined, verified, discarded, pending, opportunities, reusable in stages:
    rows.append(dict(id='stage-'+code, name=name, closed_at='2026-11-04',
                     status='Cerrada dentro del alcance documental; límites explícitos.',
                     examined=examined, verified=verified, discarded=discarded,
                     unchecked=pending, opportunities=opportunities, reusable_artifacts=reusable,
                     confidence='Documental; consultar el alcance de cada registro.',
                     maintenance_status='Registro de cierre; no etapa de desarrollo de producto.'))
(I/'stage_log.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (I/'stage_log.csv').open('w',encoding='utf-8',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=rows[0].keys());writer.writeheader()
    for row in rows:
        writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v for k,v in row.items()})

# Protect code, hashes in inline code, and all URL/path targets. Only repair a
# closed vocabulary of number/unit joins in prose; never mutate evidence IDs.
protected = re.compile(r'```.*?```|`[^`\n]+`|https?://[^\s<>\)]+|\]\([^)]+\)', re.S)
units = ('meses|días|horas|minutos|jornadas|candidatos|recursos|revisiones|verificaciones|'
         'métodos|comparaciones|conceptos|diseños|aplicaciones|proyectos|registros|afirmaciones|'
         'consultas|componentes|casos|eventos|documentos|tesis|venues|tokens|fuentes|stablecoins|'
         'serie|técnicas|herramientas|utilidad|evidencia|datos|facilidad|licencia|mantenimiento|'
         'uso|diferenciación|GB|MB')
before = ('del|el|al|los|Los|de|y|con|para|hasta|entre|por|Hay|hay|día|estado|horizonte|'
          'documentan|auditar|son|ni|sum[ae]n|Prever|requiere|Modelo|Versión|versión|solo|'
          'alcanzar|heredar|superar|una|un|unas|unos|contiene|referencia|efectiva')
def polish_plain(text):
    text=re.sub(r'(?<=\d)(?=(?:'+units+r')\b)', ' ', text)
    text=re.sub(r'\b('+before+r')(?=\d)', r'\1 ', text)
    text=re.sub(r'(?<=[,;:])(?=\d)', ' ', text)
    text=re.sub(r'(?<=\d)%?(?=\+)',lambda m:m.group(0)+' ',text)
    text=re.sub(r'\+(?=\d)','+ ',text)
    text=text.replace('observado4-nov','observado 4-nov')
    return text
changed=0
for path in ROOT.rglob('*.md'):
    if '.working_cache' in path.parts:
        continue
    old=path.read_text(encoding='utf-8');pieces=[];position=0
    for match in protected.finditer(old):
        pieces.append(polish_plain(old[position:match.start()]));pieces.append(match.group())
        position=match.end()
    pieces.append(polish_plain(old[position:]));new=''.join(pieces)
    if new!=old:
        path.write_text(new,encoding='utf-8');changed+=1
print(f'Stage register written; prose spacing improved in {changed} Markdown files.')
