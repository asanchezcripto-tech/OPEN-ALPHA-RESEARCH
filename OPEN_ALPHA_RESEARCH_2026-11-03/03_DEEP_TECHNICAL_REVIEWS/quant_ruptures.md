# ruptures: segmentación útil, con obligación de medir el retraso de detección

Candidato `quant-ruptures` · observación 2026-11-04 · nivel V3 (estático). Commit `ee1c8ff8a548d54c641b2bb471562165931f31c7`.

La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.

## Capacidad y alcance

La interfaz BaseEstimator separa fit/predict de funciones de coste. Pelt acumula el error de cada segmento más penalización y poda candidatos. CostL2 suma varianzas por feature multiplicadas por longitud del tramo; por ello unidades y escalado afectan directamente al resultado.

**Entradas:** Serie univariable o matriz temporal de variables escaladas; penalización, coste y segmento mínimo.

**Salidas:** Índices de ruptura de una segmentación retrospectiva, no probabilidades de un régimen económico.

## Evidencia técnica y límites

Pelt usa por defecto model=l2, min_size=2 y jump=5. predict comprueba que la segmentación sea posible. fit almacena toda la señal; la recursión evalúa particiones hasta el final recibido. tests/test_detection.py existe y fue leído a nivel de estructura; no se ejecutó ni se midió cobertura.

Aplicar una vez PELT a toda la historia y usar retrospectivamente sus rupturas como alertas produce conocimiento futuro. Para evaluar utilidad operativa, recalcular con prefijos de datos y guardar cuándo apareció cada alerta, cuánto se movió y si desapareció al llegar nuevos puntos.

## Adopción proporcional

Una pequeña librería de costes es más proporcional que entrenar un transformer para detectar cambios de nivel, volatilidad o correlación. No identifica automáticamente bull/bear ni causalidad macro. La elección de coste, ventana y penalización determina qué cambio puede verse.

**Dependencias observadas:** NumPy, SciPy; Cython para ciertas rutas compiladas.

CPU y 4–8 GB RAM estimados para paneles diarios pequeños; el coste depende del algoritmo y de candidatos conservados. No afirmar complejidad lineal universal. GPU innecesaria. Estandarización debe estimarse solo con datos disponibles.

**Licencia del código:** BSD-2-Clause. Clasificación: REUTILIZACIÓN POTENCIALMENTE COMPATIBLE. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.

## Experimento de aceptación propuesto, no ejecutado

Crear un replay semanal de funding, volatilidad realizada y crecimiento de stablecoins. Comparar PELT con CUSUM o umbrales robustos, bajo presupuesto fijo de falsas alarmas. Aceptar si reduce retraso o trabajo de revisión sin multiplicar alarmas, medido sobre periodos retenidos.

## Veredicto

Adoptar para exploración y extraer técnica para Market Regime Navigator; no vender sus rupturas retrospectivas como anticipación. BSD-2-Clause revisada. strucchange ofrece monitorización y tests econométricos alternativos; HMM añade estados latentes a costa de más supuestos.

Puntuación editorial 88/100: utilidad 23/25; evidencia 13/15; datos 13/15; facilidad 11/12; licencia 10/10; mantenimiento 5/8; uso diario 7/8; diferenciación 6/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.

## Fuentes exactas

- [src/ruptures/detection/pelt.py](https://github.com/deepcharles/ruptures/blob/ee1c8ff8a548d54c641b2bb471562165931f31c7/src/ruptures/detection/pelt.py)
- [src/ruptures/costs/costl2.py](https://github.com/deepcharles/ruptures/blob/ee1c8ff8a548d54c641b2bb471562165931f31c7/src/ruptures/costs/costl2.py)
- [tests/test_detection.py](https://github.com/deepcharles/ruptures/blob/ee1c8ff8a548d54c641b2bb471562165931f31c7/tests/test_detection.py)
- [LICENSE](https://github.com/deepcharles/ruptures/blob/ee1c8ff8a548d54c641b2bb471562165931f31c7/LICENSE)
