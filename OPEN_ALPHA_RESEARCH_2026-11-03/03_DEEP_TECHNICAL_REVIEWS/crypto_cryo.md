# Cryo — revisión técnica estática

Observado: 2026-11-04. Referencia del mandato: 2026-11-03. Commit examinado: `80eedf5355ca7b141d48123126515e6c9dd7d290`. La fecha de este commit no se obtuvo; la instantánea observada el día 4 no se presenta como reconstrucción certificada del día 3. Nivel V3: inspección de rutas concretas; no se ejecutó, instaló ni importó software externo.

Cryo es una opción especialmente proporcionada para conseguir muestras EVM en Parquet y comprobar una hipótesis, sin levantar una plataforma de indexación. Su README declara estado temprano y advierte que los valores por defecto pueden sobrecargar un RPC de terceros; no debe recomendarse su ejecución ciega.

## Evidencia de arquitectura

Se inspeccionaron [crates/freeze/src/freeze.rs](https://github.com/paradigmxyz/cryo/blob/80eedf5355ca7b141d48123126515e6c9dd7d290/crates/freeze/src/freeze.rs), [crates/freeze/src/types/sources.rs](https://github.com/paradigmxyz/cryo/blob/80eedf5355ca7b141d48123126515e6c9dd7d290/crates/freeze/src/types/sources.rs), [crates/freeze/src/types/schemas.rs](https://github.com/paradigmxyz/cryo/blob/80eedf5355ca7b141d48123126515e6c9dd7d290/crates/freeze/src/types/schemas.rs) y [Cargo.toml](https://github.com/paradigmxyz/cryo/blob/80eedf5355ca7b141d48123126515e6c9dd7d290/Cargo.toml). Licencia dual [MIT](https://github.com/paradigmxyz/cryo/blob/80eedf5355ca7b141d48123126515e6c9dd7d290/LICENSE-MIT) o [Apache2](https://github.com/paradigmxyz/cryo/blob/80eedf5355ca7b141d48123126515e6c9dd7d290/LICENSE-APACHE). El workspace declara 0.3.2; incluye CLI, freeze, conversión a dataframes y bindings Python.

El motor divide consultas en particiones y tipos de dataset. `freeze` prepara trabajos, comprueba dry run, omite archivos existentes cuando no se permite sobrescribir y produce resumen con completados, errores y omitidos. La colección usa semáforos de chunks y escribe dataframes; esto facilita reanudar, pero saltarse un archivo no verifica que su contenido siga siendo canónico tras una reorg o revisión de la fuente.

El manifest actual usa Alloy y Polars. Parte del README aún describe ethers.rs; esta diferencia es razón para preferir la implementación fijada al explicar arquitectura, sin concluir por ello que todo el README sea inválido.

## Control de datos y límites

`Source` contiene chain_id, RPC, control de concurrencia y campos de rate limiter. El constructor inspeccionado no activa por sí solo todos esos controles; algunos valores son etiquetas descriptivas. Por tanto no se dedujo que un número visible como100 solicitudes concurrentes pruebe limitación efectiva de tráfico en cualquier ruta. Antes de ejecutar habría que revisar el parsing CLI y configuración concreta. Esta revisión no ejecutó Cryo ni verificó tasas reales.

Para `eth_getBlockReceipts` existe fallback a recibos por transacción. Un mismo rango de bloques puede costar muchas más peticiones según las capacidades del RPC. Traces, state diffs y estados históricos requieren proveedores con métodos y retención adecuados. “Open source” no implica RPC archival gratis.

Los esquemas admiten conversiones de U256 y chain_id. Para cantidades monetarias conviene conservar integer/string/binary exacto y aplicar decimales después; float sólo para visualización o estadísticas con tolerancia declarada. Guardar hash de bloque y ventana finalizada es responsabilidad del flujo analítico; Parquet por sí solo no garantiza provenance.

## Pruebas y coste

Se inspeccionó el motor y esquema, pero no un conjunto completo de pruebas de regresión de datasets. No hay resultados de rendimiento propios. El tamaño de muestra manda: extracción de algunos contratos/días probablemente cabe en 8–16 GB RAM y CPU doméstica, mientras trazas de toda una cadena exigen mucho más. Son estimaciones operativas y deben sustituirse por medición futura autorizada en un entorno aislado.

Ethereum ETL es una alternativa Python simple si CSV basta. Ponder resulta preferible para servicio continuo y rollback de reorg. SQD puede reducir extracción multichain, con dependencia adicional de su red. No hace falta seleccionar una sola tecnología para todos los casos.

## Experimento propuesto

Obtener en el futuro una ventana finalizada pequeña de logs de un contrato y repetirla con otro RPC autorizado. Comparar recuentos, clave `(chain_id,block_hash,tx_hash,log_index)`, cantidades exactas y checksums del resultado. Aceptación: cero huecos sin explicación; fallos visibles en resumen; reanudación idempotente; límites de tráfico respetados; coste por mil bloques registrado. Hipótesis: una muestra bien fijada reduce tiempo de falsar métricas frente a depender sólo del dashboard agregado.


## Decisión y puntuación

Obtener evidencia pequeña, reproducible y portable. Adoptar biblioteca. Puntuación editorial: **77/100**; utility 22, evidence 12, data 10, ease 8, license 10, maintenance 3, usability 6, differentiation 6. Los puntos expresan encaje para este inversor y fuerza de la evidencia estática, no fiabilidad absoluta ni rentabilidad.

Condiciones pendientes: validación operacional y permisos de datos; las obligaciones de licencia dependen del modo de integración y distribución.
