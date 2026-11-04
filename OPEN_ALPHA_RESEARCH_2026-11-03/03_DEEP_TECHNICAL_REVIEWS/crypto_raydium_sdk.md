# Raydium SDK V2 — revisión técnica estática

Observado: 2026-11-04. Referencia del mandato: 2026-11-03. Commit examinado: `f3fa7cbfd649fa5bfd20c9e693cfbf3b7ce69966`. La fecha de este commit no se obtuvo; la instantánea observada el día 4 no se presenta como reconstrucción certificada del día 3. Nivel V3: inspección de rutas concretas; no se ejecutó, instaló ni importó software externo.

El SDK sirve para leer la estructura real de pools Solana y calcular con enteros grandes. Su mejor uso inicial es interpretar cuentas y cotizaciones, con cuidado de distinguir CLMM, CPMM y AMMv4. No se necesita firmar swaps para analizar fundamentales.

## Rutas examinadas

[src/raydium/clmm/layout.ts](https://github.com/raydium-io/raydium-sdk-V2/blob/f3fa7cbfd649fa5bfd20c9e693cfbf3b7ce69966/src/raydium/clmm/layout.ts) expone layouts con `protocolFeeRate`, `tradeFeeRate`, `fundFeeRate`, acumuladores de fees, rewards y campos de fee dinámica. Se inspeccionaron también rutas de [src/raydium/clmm/clmm.ts](https://github.com/raydium-io/raydium-sdk-V2/blob/f3fa7cbfd649fa5bfd20c9e693cfbf3b7ce69966/src/raydium/clmm/clmm.ts), [src/raydium/cpmm/cpmm.ts](https://github.com/raydium-io/raydium-sdk-V2/blob/f3fa7cbfd649fa5bfd20c9e693cfbf3b7ce69966/src/raydium/cpmm/cpmm.ts) y el test [test/cpmmSwapQuote.test.js](https://github.com/raydium-io/raydium-sdk-V2/blob/f3fa7cbfd649fa5bfd20c9e693cfbf3b7ce69966/test/cpmmSwapQuote.test.js). El [package.json](https://github.com/raydium-io/raydium-sdk-V2/blob/f3fa7cbfd649fa5bfd20c9e693cfbf3b7ce69966/package.json) declara 0.2.81-alpha en el commit observado, y dependencias Solana web3/SPL, BN, decimal.js y axios. Licencia raíz [GPL3](https://github.com/raydium-io/raydium-sdk-V2/blob/f3fa7cbfd649fa5bfd20c9e693cfbf3b7ce69966/LICENSE).

## Arquitectura y precisión

El SDK organiza módulos por producto: cuenta, token, CLMM, CPMM y rutas, entre otros. Los layouts convierten datos binarios de cuentas en campos financieros. Los acumuladores de fees y liquidez deben interpretarse con decimales y escalas de punto fijo; convertir directamente a float puede perder precisión.

Una cuota de reparto documentada no identifica por sí sola los pagos efectivos a tokenholders. Los campos de configuración proporcionan la base técnica para preguntar qué fee se aplicó a qué pool y cuándo. Es necesario unir instrucciones/events, configuración y transferencia final para comprobar buybacks. Las fees de LP no deben atribuirse a RAY.

La ruta antigua de protocol fees devolvió 404. Se localizó y abrió la [ruta canónica actual](https://docs.raydium.io/ray/protocol-fees): documenta reparto LP/buyback/tesorería de 84/12/4 para CLMM y CPMM, y 88/12 para AMM v4. Son porcentajes de la fee, no del volumen. Las escalas de configuración difieren: 10.000 para AMM v4 y 1.000.000 para CLMM/CPMM. Esta es evidencia documental, sin lectura independiente del estado desplegado.

La página de [buybacks](https://docs.raydium.io/ray/ray-buybacks) indica que el RAY recomprado permanece en una dirección del protocolo. Acumulación en esa cuenta no equivale a burn ni a distribución de caja a tenedores. La [comparación de fees](https://docs.raydium.io/reference/fee-comparison) describe configuraciones y cambios de septiembre de 2026, incluidos campos de creator fee. Un monitor debe fijar pool, programa, slot y versión de configuración; los datos agregados no bastan para certificar el destino de cada importe.

## Qué se comprobó en tests

`cpmmSwapQuote.test.js` construye fixtures que sustituyen peticiones de cuenta, reutiliza una cotización y comprueba que construir dos transacciones no muta la cotización ni altera límites. Incluye variantes exact-in/exact-out y financiación máxima de SOL nativo. Es una prueba significativa del contrato de cálculo/construcción, aunque no cubre todo el mercado. Se leyó, no se ejecutó; no hay porcentaje de cobertura medido ni prueba de rentabilidad de LP.

## Riesgos de interpretación

Token2022 puede añadir fees de transferencia; la cantidad enviada, recibida y contabilizada no tiene por qué coincidir. Liquidez concentrada fuera de rango no equivale a profundidad ejecutable. Un evento de swap puede ser una pierna de una ruta más larga; sumar todas las piernas como usuarios nuevos o capital nuevo sobreestima actividad.

Los datos agregados de API y el estado RPC deben guardar timestamps/slots y consistencia. Los porcentajes de crecimiento sin corrección de bots, incentivos y composición de pools no demuestran actividad orgánica. Este SDK no resuelve por sí solo esa identificación causal.

## Adopción y experimento

GPL exige evaluar obligaciones al combinar o distribuir; programas Raydium CLMM/CPMM poseen licencias propias que se comprobaron por separado. Para un análisis privado acotado, estudiar layouts o usar una lectura RPC mínima puede reducir superficie de dependencias. La biblioteca completa aporta comodidad cuando se necesitan varios productos.

Muestra propuesta: cinco pools por tipo, siete días, lecturas de configuración y 10 swaps contrastados por pool. Aceptación: importes exactos reconciliados; fees separadas por destino; programa/slot/versiones guardados; sin extrapolar porcentajes globales no verificados. CPU doméstica y pocos GB deberían bastar para esta muestra —estimación—; un archivo completo de Solana requiere infraestructura muy diferente. Valor añadido esperado: detectar crecimiento aparente explicado por mix de pools o cambios de fees.


## Decisión y puntuación

Investigar actividad por tipo de pool y fee vigente. Adoptar biblioteca. Puntuación editorial: **68/100**; utility 19, evidence 12, data 10, ease 6, license 6, maintenance 4, usability 5, differentiation 6. Los puntos expresan encaje para este inversor y fuerza de la evidencia estática, no fiabilidad absoluta ni rentabilidad.

Condiciones pendientes: validación operacional y permisos de datos; las obligaciones de licencia dependen del modo de integración y distribución.
