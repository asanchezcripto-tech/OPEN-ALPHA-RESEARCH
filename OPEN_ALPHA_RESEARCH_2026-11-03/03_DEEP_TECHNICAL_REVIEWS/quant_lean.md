# LEAN: un buen motor multiactivo no incluye por sí mismo buenos históricos

Candidato `quant-lean` · observación 2026-11-04 · nivel V3 (estático). Commit `9ecfed98339c27849a2a708edc03455caf151e91`.

La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.

## Capacidad y alcance

AlgorithmManager recorre slices de datos y coordina warmup, algoritmo, transacciones, resultados y reloj. Los fill models son componentes intercambiables. Se inspeccionó EquityFillModel como ejemplo concreto; no se extrapolan sus reglas a perpetuos cripto.

**Entradas:** Suscripciones e instrumentos, slices temporales, estrategia, universo y modelos de comisiones/slippage/fill.

**Salidas:** Simulación por eventos, órdenes, posiciones y reportes.

## Evidencia técnica y límites

MarketFill obtiene bid/ask según tipos de datos realmente suscritos y añade slippage. La ruta stop-limit examinada rechaza barras cuyo cierre no sea posterior a la orden. Los tests comprueban datos obsoletos, precio bid/ask, horas de mercado y órdenes antes de la barra. Esto es mejor evidencia de implementación que una lista comercial de activos soportados.

Un motor con controles no corrige un universo creado con información futura ni una base ajustada retrospectivamente mal documentada. Horarios de acciones, splits y ajustes no se trasladan directamente a mercados 24/7. La prueba examinada es de equity; funding/liquidación de cripto exige revisión separada.

## Adopción proporcional

Aporta más valor para investigaciones multiactivo que mezclen renta variable, futuros y cripto. La nube QuantConnect, datasets y paquetes de datos tienen condiciones separadas del motor. No presupuestar cero porque el repositorio sea Apache.

**Dependencias observadas:** .NET/C#, integración Python, proveedores y modelos de brokerage/datos.

CPU, 8–16 GB RAM y entorno .NET estimados para backtests modestos; almacenamiento depende de resolución. Mantener motor completo tiene más coste técnico que una biblioteca de métricas o cartera. No ejecución ni instalación.

**Licencia del código:** Apache-2.0. Clasificación: REUTILIZACIÓN POTENCIALMENTE COMPATIBLE. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.

## Experimento de aceptación propuesto, no ejecutado

Reproducir una estrategia de asignación mensual con ledger independiente, precios sin ajustes y ajustados, activo deslistado y retraso de publicación. Antes de preferir LEAN, demostrar un fallo material que un backtest simple no pueda representar. Verificar datos y permisos fuera del motor.

## Veredicto

Conservar como referencia; adoptar para una necesidad multiactivo definida. Apache-2.0 revisada. Para el mandato inicial priorizar skfolio/PyPortfolioOpt y métodos de inferencia; construir motor propio no se justifica.

Puntuación editorial 69/100: utilidad 18/25; evidencia 14/15; datos 8/15; facilidad 5/12; licencia 10/10; mantenimiento 5/8; uso diario 5/8; diferenciación 4/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.

## Fuentes exactas

- [Engine/AlgorithmManager.cs](https://github.com/QuantConnect/Lean/blob/9ecfed98339c27849a2a708edc03455caf151e91/Engine/AlgorithmManager.cs)
- [Common/Orders/Fills/EquityFillModel.cs](https://github.com/QuantConnect/Lean/blob/9ecfed98339c27849a2a708edc03455caf151e91/Common/Orders/Fills/EquityFillModel.cs)
- [Tests/Common/Orders/Fills/EquityFillModelTests.cs](https://github.com/QuantConnect/Lean/blob/9ecfed98339c27849a2a708edc03455caf151e91/Tests/Common/Orders/Fills/EquityFillModelTests.cs)
- [LICENSE](https://github.com/QuantConnect/Lean/blob/9ecfed98339c27849a2a708edc03455caf151e91/LICENSE)
