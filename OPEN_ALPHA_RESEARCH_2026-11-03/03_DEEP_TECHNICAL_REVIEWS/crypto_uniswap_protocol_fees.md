# Uniswap protocol fees — revisión técnica estática

Observado: 2026-11-04. Referencia del mandato: 2026-11-03. Commit examinado: `00066e1cad8b5e78f768860e4169b39baf4b300c`. La fecha de este commit no se obtuvo; la instantánea observada el día 4 no se presenta como reconstrucción certificada del día 3. Nivel V3: inspección de rutas concretas; no se ejecutó, instaló ni importó software externo.

Este repositorio permite pasar de la etiqueta genérica “revenue de Uniswap” a una cadena verificable de derechos, conversiones y destinos. Es particularmente valioso para separar fees de LP, importes recolectados y tokens enviados a quema. No se verificaron transacciones o parámetros desplegados durante esta revisión.

## Implementación comprobada

| Ruta | Hallazgo estático |
|---|---|
| [src/TokenJar.sol](https://github.com/Uniswap/protocol-fees/blob/00066e1cad8b5e78f768860e4169b39baf4b300c/src/TokenJar.sol) | Sólo el releaser puede extraer; el owner puede cambiar el releaser. |
| [src/releasers/ExchangeReleaser.sol](https://github.com/Uniswap/protocol-fees/blob/00066e1cad8b5e78f768860e4169b39baf4b300c/src/releasers/ExchangeReleaser.sol) | Intercambia recursos por activos del Jar, controla nonce y limita número de activos. |
| [src/releasers/Firepit.sol](https://github.com/Uniswap/protocol-fees/blob/00066e1cad8b5e78f768860e4169b39baf4b300c/src/releasers/Firepit.sol) | Fija destinatario del recurso en `0xdead`. |
| [test/Firepit.t.sol](https://github.com/Uniswap/protocol-fees/blob/00066e1cad8b5e78f768860e4169b39baf4b300c/test/Firepit.t.sol) | Casos ERC20/nativo, saldo insuficiente y nonce inválido. |
| [foundry.toml](https://github.com/Uniswap/protocol-fees/blob/00066e1cad8b5e78f768860e4169b39baf4b300c/foundry.toml) | Configuración de compilación y pruebas; no ejecutada. |

Los archivos examinados contienen SPDX `AGPL-3.0-only`. El README declara esa licencia para el proyecto, pero las dependencias —incluido material de v4-core y Solmate— deben revisarse por archivo si se copia código. Para un monitor de lectura bastaría interpretar contratos/ABI; no es necesario desplegar ni bifurcar el protocolo.

## Flujo económico

Los adaptadores de fees alimentan un TokenJar. Un agente externo entrega el umbral del recurso elegido y recibe activos del Jar. `ExchangeReleaser` usa `safeTransferFrom` hacia el destinatario del recurso y emite `Released`. Firepit concreta la dirección de quema.

El código también comenta límites económicos: polvo que nunca resulta rentable retirar, costes de gas, cambios bruscos de precio y excedente para quien ejecuta la conversión. Por ello, valorar todos los activos acumulados como una recompra inmediata de UNI exageraría lo realizado. Hay que separar devengo de fee, transferencia al Jar, liberación y destino final.

Un envío a `0xdead` es evidencia de tokens retirados económicamente del uso; no debe afirmarse que el contrato ERC20 reduce `totalSupply` sin verificar su implementación. Y que el contrato exista en GitHub no prueba que cada pool lo utilice. El [README](https://github.com/Uniswap/protocol-fees/blob/00066e1cad8b5e78f768860e4169b39baf4b300c/README.md) enumera despliegues, pero no se contrastó bytecode ni estado de cada uno.

El [artículo oficial de TJAR del 30-10-2026](https://blog.uniswap.org/how-tjar-works-uniswaps-onchain-fee-conversion-system) describe despliegue y generalización del sistema. Es anuncio/documentación del operador; ofrece evidencia más reciente que una propuesta de 2025, pero no sustituye recibos y parámetros on-chain.

## Pruebas, riesgos y uso

Los tests inspeccionados cubren mecánica de transferencia y nonces. No prueban que el mecanismo maximice captura de valor, que un threshold sea adecuado o que no existan vulnerabilidades en el conjunto. Tampoco se revisaron informes de auditoría completos.

La capacidad útil para 3–18 meses sería un ledger semanal de fees cobradas, pendientes de conversión, UNI transferido a destino y cambios de política. Debe registrar chain_id, contrato, bloque, tx/log y etapa contable para evitar sumar L2→bridge→L1 como tres ingresos. Un watcher acotado no necesita GPU ni nodo propio; coste incierto del proveedor RPC y amplitud de historia. Es una estimación, sin benchmark.

## Experimento de valor añadido

Seleccionar un Jar y 30 días; reconciliar balances inicial/final, entradas y releases. Comparar una métrica ingenua de revenue con captura realizada y lag de conversión. Aceptación: cada release atribuible a evento; ninguna transferencia interna duplicada; diferencias contables explicadas; parámetros observados fechados; ausencia de actividad se representa como desconocida si falla la fuente. Resultado buscado: detectar falsas divergencias de valoración por desfases de conversión, sin afirmar que capturen retornos futuros.


## Decisión y puntuación

Auditar cadena fees→conversión→quema. Extraer una técnica contable y de lectura de eventos. Puntuación editorial: **75/100**; utility 25, evidence 14, data 9, ease 5, license 6, maintenance 4, usability 5, differentiation 7. Los puntos expresan encaje para este inversor y fuerza de la evidencia estática, no fiabilidad absoluta ni rentabilidad.

Condiciones pendientes: validación operacional y permisos de datos; las obligaciones de licencia dependen del modo de integración y distribución.
