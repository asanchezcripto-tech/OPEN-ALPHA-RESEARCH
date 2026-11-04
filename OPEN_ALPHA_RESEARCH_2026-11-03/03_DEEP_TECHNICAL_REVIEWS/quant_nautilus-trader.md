# NautilusTrader: referencia de relojes y eventos, adopción completa aplazada

Candidato `quant-nautilus-trader` · observación 2026-11-04 · nivel V3 (estático). Commit `66479c13eda08f75c95c65c815a43a5674c08ed2`.

La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.

## Capacidad y alcance

El núcleo Rust BacktestEngine coordina un kernel, reloj virtual, iterador de datos, venues simulados y callbacks. add_data puede ordenar por ts_init; la separación de tiempo del evento y de inicialización resulta valiosa para un laboratorio con disponibilidad diferida. No debe confundirse ts_init importado con fecha histórica de conocimiento verificada.

**Entradas:** Instrumentos, eventos de mercado con timestamps, venues, saldos iniciales, estrategias y modelos de ejecución.

**Salidas:** Eventos de órdenes/fills, estados de cartera y resultados de una simulación configurable.

## Evidencia técnica y límites

run revisa errores previos de callbacks, funding y balances, y aborta en estados inválidos. Se leyeron tests dentro de engine.rs sobre secuencias de modificaciones, fills, timers, cambios de instrumentos y restauración. FillModel permite un libro sintético y rutas probabilísticas; la existencia de una interfaz realista no garantiza una calibración realista.

La reproducción ordenada sigue necesitando feeds completos, precisión de timestamps y políticas de latencia. Una configuración de liquidez ilimitada o fill dentro del spread puede fabricar una ejecución favorable si no se documenta. No se verificó equivalencia de datos históricos y feed en vivo.

## Adopción proporcional

Valioso cuando una hipótesis swing depende de orden de eventos, funding y fills multivenue. Para valoración de protocolos a seis meses es más complejo que lo necesario. Extraer diseño de reloj e identidad de instrumento antes de montar un motor de trading.

**Dependencias observadas:** Rust; crates nautilus-common/model/execution/system; bindings Python; modelos de fill y fees.

Estimación: 16–32 GB RAM y SSD para replay intradía; datos diarios requieren mucho menos. Rust y bindings implican más mantenimiento. No se descargaron wheels, compiladores ni histórico, y no se midió rendimiento.

**Licencia del código:** LGPL-3.0. Clasificación: COMPATIBLE CON OBLIGACIONES. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.

## Experimento de aceptación propuesto, no ejecutado

Si una hipótesis futura depende de ejecución, usar un caso pequeño con orden retrasada, funding, cambio de instrumento y hueco de feed. Exigir coincidencia con ledger manual, error explícito ante inconsistencias y sensibilidad al doble de spread/latencia. Comparar con simulación por barras para demostrar necesidad del motor.

## Veredicto

Conservar como referencia y adoptar solo bajo necesidad demostrada. LGPL-3.0 revisada con obligaciones a evaluar según distribución/enlace. No atribuir beneficios o fidelidad empírica al calificativo production-grade.

Puntuación editorial 66/100: utilidad 17/25; evidencia 14/15; datos 8/15; facilidad 4/12; licencia 8/10; mantenimiento 5/8; uso diario 4/8; diferenciación 6/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.

## Fuentes exactas

- [crates/backtest/src/engine.rs](https://github.com/nautechsystems/nautilus_trader/blob/66479c13eda08f75c95c65c815a43a5674c08ed2/crates/backtest/src/engine.rs)
- [crates/execution/src/models/fill.rs](https://github.com/nautechsystems/nautilus_trader/blob/66479c13eda08f75c95c65c815a43a5674c08ed2/crates/execution/src/models/fill.rs)
- [crates/backtest/Cargo.toml](https://github.com/nautechsystems/nautilus_trader/blob/66479c13eda08f75c95c65c815a43a5674c08ed2/crates/backtest/Cargo.toml)
- [LICENSE](https://github.com/nautechsystems/nautilus_trader/blob/66479c13eda08f75c95c65c815a43a5674c08ed2/LICENSE)
