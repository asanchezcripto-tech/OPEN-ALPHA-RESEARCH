# GraphSense lib — revisión técnica estática

Observado: 2026-11-04. Referencia del mandato: 2026-11-03. Commit examinado: `cb54f2a4b768258abc2d408ca79e6fee5ebbb215`. La fecha de este commit no se obtuvo; la instantánea observada el día 4 no se presenta como reconstrucción certificada del día 3. Nivel V3: inspección de rutas concretas; no se ejecutó, instaló ni importó software externo.

La oportunidad menos obvia es reutilizar el esquema de atribución y sus controles, no desplegar toda la plataforma forense. Una etiqueta con fuente, confianza y fecha mejora el análisis de capital mucho más que llamar “smart money” a una lista de wallets sin provenance.

## Migración y rutas inspeccionadas

El repositorio histórico [graphsense-tagpack-tool](https://github.com/graphsense/graphsense-tagpack-tool) declara migración y archivo. El código actual examinado está en GraphSense lib: [src/graphsenselib/tagpack/confidence.py](https://github.com/graphsense/graphsense-lib/blob/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/src/graphsenselib/tagpack/confidence.py), [src/graphsenselib/tagpack/tagpack_schema.py](https://github.com/graphsense/graphsense-lib/blob/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/src/graphsenselib/tagpack/tagpack_schema.py), [src/graphsenselib/tagpack/schema.py](https://github.com/graphsense/graphsense-lib/blob/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/src/graphsenselib/tagpack/schema.py) y [src/graphsenselib/tagpack/conf/tagpack_schema.yaml](https://github.com/graphsense/graphsense-lib/blob/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/src/graphsenselib/tagpack/conf/tagpack_schema.yaml). Se revisaron además [tests/tagpack/test_tagpack_schema.py](https://github.com/graphsense/graphsense-lib/blob/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/tests/tagpack/test_tagpack_schema.py) y [tests/tagpack/test_cluster_staleness.py](https://github.com/graphsense/graphsense-lib/blob/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/tests/tagpack/test_cluster_staleness.py). Licencia [MIT](https://github.com/graphsense/graphsense-lib/blob/cb54f2a4b768258abc2d408ca79e6fee5ebbb215/LICENSE).

## Modelo de información

El esquema exige campos de fuente, moneda, red, etiqueta y confianza; contempla actor, dirección, tx_hash, contexto, clasificación, fecha y marcadores de clusters. La clase de confianza carga categorías definidas localmente; su `level` no es una probabilidad calibrada de identidad. Una interfaz debe mostrar la categoría y fundamento, sin convertirla artificialmente en porcentaje de certeza.

El validador usa tipos, campos obligatorios y taxonomías. La existencia de una fuente no demuestra que la atribución sea cierta, pero permite revisarla. `lastmod` opcional no resuelve por sí solo historial bitemporal: una herramienta de investigación necesita añadir cuándo se conoció la atribución y para qué periodo era válida.

Los [TagPacks públicos](https://github.com/graphsense/graphsense-tagpacks) requieren origen público y enlaces de respaldo. La licencia del contenedor no prueba todos los derechos de las fuentes originales ni su actualidad. La revisión debe dar prioridad a direcciones de protocolos/tesorerías verificables, evitando inferencias personales innecesarias.

## Pruebas y límites

Los tests de esquema comprueban propiedades y campos obligatorios. El test de stale mappings crea un TagStore y backend falsos para contrastar asignaciones de clusters guardadas con las actuales. Es un mecanismo interesante: una etiqueta no debería seguir vinculada silenciosamente a un cluster que cambió al actualizar el análisis. Se leyó código de prueba; no se ejecutó ni se auditó la totalidad del motor de clustering.

Dirección, cuenta, cluster y entidad deben permanecer separados. En UTXO, heurísticas de co-input pueden fallar con CoinJoin; en EVM, contratos, routers, multisigs y smart wallets añaden relaciones diferentes. Un grafo bonito puede hacer que una atribución débil parezca demostrada. La salida correcta puede ser un intervalo de flujo atribuible, no una cifra puntual.

## Proporcionalidad y coste

El README del servicio completo describe Cassandra para blockchain y Postgres para TagStore. Es mucho para una primera herramienta personal. Extraer el patrón de esquema —o usar una pequeña parte compatible del código— permite un CSV/JSON versionado con 20–100 direcciones de interés, fuentes y revisión humana. CPU ordinaria sin GPU basta para ese diccionario; el coste de plataforma completa no se extrapola a esta pieza.

Alternativa: tabla manual de entidades y direcciones con reglas explícitas; BlockSci queda como referencia académica porque su README dice que no se mantiene activamente desde 2020. No usar un fork con actividad como sustituto automático sin examinar cambios sustanciales.

## Experimento propuesto

Anotar30 direcciones públicas de tesorerías/protocolos, cada una con evidencia y nivel, y revisar10 atribuciones con una segunda fuente. Calcular flujo bajo tres supuestos: sólo confirmadas, confirmadas+probables y todas. Aceptación: 100% de etiquetas trazables, conflicto explícito sin sobrescritura y diferencia entre escenarios visible. Hipótesis de valor: descartar narrativas de acumulación que dependen de una atribución frágil. No se realizó identificación de personas privadas.


## Decisión y puntuación

Extraer esquema de etiquetas con fuente y confianza. Adoptar biblioteca. Puntuación editorial: **73/100**; utility 21, evidence 12, data 8, ease 6, license 10, maintenance 4, usability 5, differentiation 7. Los puntos expresan encaje para este inversor y fuerza de la evidencia estática, no fiabilidad absoluta ni rentabilidad.

Condiciones pendientes: validación operacional y permisos de datos; las obligaciones de licencia dependen del modo de integración y distribución.
