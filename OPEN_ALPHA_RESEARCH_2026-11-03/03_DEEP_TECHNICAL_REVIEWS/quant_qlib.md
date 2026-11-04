# Qlib: conservar el diseño point-in-time antes que adoptar toda la plataforma

Candidato `quant-qlib` · observación 2026-11-04 · nivel V3 (estático). Commit `54355232463878d2eebb91fe0ee5fa7fa1f5976c`.

La instantánea corresponde a la consulta del 4 de noviembre; no se probó que ese árbol completo estuviera disponible al cierre del día 3. La existencia de tests no demuestra que pasen. Ningún código externo se ejecutó.

## Capacidad y alcance

La capa de datos separa proveedores de calendario, instrumentos, features, expresiones y PIT. El operador P colapsa una serie por periodos a cada fecha de observación: invoca la carga de la feature con cur_time y conserva el último valor disponible. PRef fija el periodo contable. Esta separación sirve para fundamentación DeFi revisada, aunque los recolectores de referencia son de acciones.

**Entradas:** Panel de instrumentos y features, calendarios, fecha del periodo contable y fecha de disponibilidad de cada revisión.

**Salidas:** Features consultables en el momento de observación, datasets de entrenamiento y evaluación de señales.

## Evidencia técnica y límites

En qlib/data/pit.py se rechaza una ventana que refiera a un periodo futuro; la ausencia de fichero produce warning y serie vacía. En tests/test_pit.py hay fixtures de publicaciones revisadas, pruebas de consultas, expresiones y datos inexistentes. Se leyó también la interfaz PITProvider y la documentación de datos. El test de normalización con fecha ausente introduce una fecha por regla: un dato imputado no debe convertirse en fecha de publicación comprobada.

El motor solo puede respetar la disponibilidad que recibe. Un historical dump reconstruido hoy, un universo que excluya tokens muertos o una fecha de publicación imputada pueden seguir introduciendo sesgo. El PIT de Qlib no convierte por sí solo una API actual de revenue en un archivo histórico de conocimiento.

## Adopción proporcional

Para 3–18 meses aporta disciplina de experimentos y features; desplegar toda la plataforma solo para diez métricas es excesivo. Priorizar una tabla append-only con event_time, available_at y acquired_at; considerar Qlib cuando existan muchos factores y un universo point-in-time.

**Dependencias observadas:** pandas>=1.1, mlflow<3.13, filelock>=3.16.0,<3.30, LightGBM, CVXPY, PyArrow.

Estimación editorial para datos diarios de decenas de activos: CPU y 8–16 GB RAM; GPU innecesaria para la capa PIT o un baseline lineal. MLflow/Redis y extensiones de compilación aumentan superficie operativa. No se midió uso real.

**Licencia del código:** MIT. Clasificación: REUTILIZACIÓN POTENCIALMENTE COMPATIBLE. Código, datos y servicios se evalúan por separado. No se emitió dictamen jurídico definitivo.

## Experimento de aceptación propuesto, no ejecutado

Construir en un entorno futuro autorizado un fixture con dos revisiones de revenue, un token retirado y una fecha desconocida. Exigir que la consulta t no cambie al añadir una revisión disponible después de t; lo desconocido debe generar abstención o rango, no una fecha exacta inventada.

## Veredicto

Extraer el patrón temporal y la interfaz de features; investigar más antes de adoptar el framework completo. Alternativa proporcional: DuckDB/Parquet más as-of explícito y un registro de experimentos. Qlib no acredita alpha cripto por contener modelos o integrar RD-Agent.

Puntuación editorial 76/100: utilidad 22/25; evidencia 13/15; datos 9/15; facilidad 6/12; licencia 10/10; mantenimiento 5/8; uso diario 5/8; diferenciación 6/7. La puntuación describe utilidad de investigación, no retorno financiero. No se auditó exhaustivamente el historial de releases o issues.

## Fuentes exactas

- [qlib/data/pit.py](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/pit.py)
- [qlib/data/data.py](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/data.py)
- [tests/test_pit.py](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/tests/test_pit.py)
- [docs/component/data.rst](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/docs/component/data.rst)
- [pyproject.toml](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/pyproject.toml)
- [LICENSE](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/LICENSE)
