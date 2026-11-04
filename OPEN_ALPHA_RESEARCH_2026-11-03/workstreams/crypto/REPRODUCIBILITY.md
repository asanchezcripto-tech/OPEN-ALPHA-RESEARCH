# Reproducibilidad y límites de la investigación crypto

Se conservan inventarios JSON, URLs exactas, commits y SHA256 del texto recuperado, notas propias y diez revisiones estáticas. Las páginas web que no permiten fijar versión se identifican por URL y fecha de observación. No se mantiene copia de código externo en la entrega.

Los scripts `.py` de esta carpeta son auxiliares propios de investigación. No son una herramienta financiera ni importan librerías de los repositorios analizados. Se usaron Python estándar, HTTP de lectura y `git ls-remote` para identificar referencias; no se clonaron entornos, instalaron dependencias, ejecutaron tests externos, importaron módulos descargados ni conectaron wallets o cuentas.

`collect_sources.py`, `probe.py` e `inspect_code.py` documentan el proceso de descubrimiento y lectura. Repetir un descubrimiento de HEAD capturaría una versión nueva: para repetir exactamente una comprobación, usar la URL raw fijada por commit en `sources.json` y contrastar el hash. El hash prueba identidad del contenido recuperado, no su corrección ni su disponibilidad anterior. Los datos de mercado y benchmarks no fueron descargados o reproducidos.

`build_inventory.py`, `read_sections.py` y `write_reviews.py` utilizaban caches temporales de inspección. Esos caches de texto de terceros se retiraron de la entrega; los scripts no deben ejecutarse esperando que estén presentes. Los documentos finales incorporan correcciones editoriales posteriores al generador. `finalize_inventory.py` aplica las anotaciones a los inventarios existentes y no requiere esos caches.

Fuentes y evidencias tienen identificadores separados. Los intentos HTTP fallidos se preservan como límites de acceso, sin interpretarlos como prueba de inexistencia. Un V3 sólo cubre las rutas enumeradas; no representa una auditoría integral o un benchmark. Los tests descritos se leyeron, nunca se ejecutaron.

Fecha de referencia del mandato: 2026-11-03. Fecha de observación: 2026-11-04. La fecha de commit no se recuperó sistemáticamente. Para una investigación point-in-time posterior haría falta fijar además fecha de disponibilidad de cada versión, fuente y etiqueta; no se atribuye automáticamente al día 3 lo leído el día 4.
