# vectorbt: exploración rápida con costes explícitos y licencia restringida

Candidato `quant-vectorbt` · observación 2026-11-04 · nivel V3 (estático). Commit `c923f74c9e4d1e07e626ae9002f7382cd8264833`.

La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.

## Capacidad y alcance

Portfolio.from_orders y from_signals normalizan y difunden arrays antes de pasarlos a kernels. Las rutas Numba leídas implementan ejecución con estado, cash compartido y resolución de señales. El manifiesto actual añade engine y backend Rust opcional: no se verificó paridad de ambos backends.

**Entradas:** Precios/barras, señales u órdenes, tamaño, costes, deslizamiento, agrupación y capital inicial.

**Salidas:** Registros de órdenes, cash, posiciones, métricas y comparaciones de muchas variantes.

## Evidencia técnica y límites

buy_nb aplica precio multiplicado por 1 +slippage y sell_nb por 1-slippage; ambos consideran fees, límites de tamaño y cash. simulate_from_signal_func_nb tiene costes por defecto cero y configuración de stops. tests/test_portfolio.py contiene casos concretos de fees, slippage, partial fills, cash sharing y call sequence; se inspeccionaron nombres y fragmentos, no se ejecutó la suite.

El usuario controla cuándo la señal conoce el cierre y cuándo opera. El motor no audita automáticamente disponibilidad de fundamentales ni garantiza orden intrabar de high/low. La simultaneidad entre columnas y cash sharing exige revisar la secuencia de órdenes.

## Adopción proporcional

Adecuado para comparar reglas semanales y escenarios de coste. Su rapidez abarata también el sobreajuste: cada intento debe registrarse, incluidos resultados descartados. Comparar con bt para asignación de activos y con un motor por eventos únicamente cuando el orden temporal cambie la conclusión.

**Dependencias observadas:** NumPy>=2.4.6, pandas>=3.0.3,<4.0, Numba>=0.66, SciPy, Plotly, vectorbt-rust opcional.

CPU y 8–16 GB RAM para paneles diarios modestos, estimación editorial. Una matriz T×N×P crece con todas las variantes; limitar lotes. El commit requiere Python>=3.11,<3.15 y nuevas versiones NumPy/pandas; no asumir compatibilidad con notebooks históricos.

**Licencia del código:** Apache-2.0 WITH Commons-Clause. Clasificación: SOLO INVESTIGACIÓN / RESTRICCIONES. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.

## Experimento de aceptación propuesto, no ejecutado

Tomar una regla semanal simple y un ledger manual de diez operaciones. Comparar comisiones dobles, spread, señal retrasada una barra y secuencia de rebalanceo. Aceptar solo coincidencia contable y robustez de conclusiones ante esos cambios; no seleccionar la variante de Sharpe máximo sin ajuste por búsqueda.

## Veredicto

Uso personal exploratorio condicionado. LICENSE.md declara Apache 2.0 con Commons Clause: no es Apache permisiva sin restricciones. Antes de vender un producto/servicio derivado hace falta revisión del alcance. El módulo PRO comercial es otro recurso; sus capacidades no se atribuyen a este repositorio.

Puntuación editorial 73/100: utilidad 20/25; evidencia 13/15; datos 10/15; facilidad 9/12; licencia 4/10; mantenimiento 5/8; uso diario 7/8; diferenciación 5/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.

## Fuentes exactas

- [vectorbt/portfolio/base.py](https://github.com/polakowo/vectorbt/blob/c923f74c9e4d1e07e626ae9002f7382cd8264833/vectorbt/portfolio/base.py)
- [vectorbt/portfolio/nb.py](https://github.com/polakowo/vectorbt/blob/c923f74c9e4d1e07e626ae9002f7382cd8264833/vectorbt/portfolio/nb.py)
- [tests/test_portfolio.py](https://github.com/polakowo/vectorbt/blob/c923f74c9e4d1e07e626ae9002f7382cd8264833/tests/test_portfolio.py)
- [pyproject.toml](https://github.com/polakowo/vectorbt/blob/c923f74c9e4d1e07e626ae9002f7382cd8264833/pyproject.toml)
- [LICENSE.md](https://github.com/polakowo/vectorbt/blob/c923f74c9e4d1e07e626ae9002f7382cd8264833/LICENSE.md)
