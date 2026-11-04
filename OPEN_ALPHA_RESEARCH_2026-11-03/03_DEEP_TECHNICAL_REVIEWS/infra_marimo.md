# marimo: investigación reactiva con dependencias visibles

Recurso: [marimo](https://github.com/marimo-team/marimo). Commit observado: `54552ec3137df83992ac29aa73d1adf73eb252b1`. Verificación: 2026-11-04; nivel V3, análisis estático.

**Decisión:** Usar directamente como entorno de investigación después de una instalación autorizada y controlada; aquí solo se revisa. Puntuación editorial: **87/100**; riesgo bloqueante: ninguno identificado en esta ruta; no equivale a certificación.

## Arquitectura e implementación observada

DirectedGraph registra definiciones y dependencias de las celdas, actualiza aristas y detecta ciclos. El borrado de una celda afecta a sus descendientes. Es un control del flujo de cómputo, no un registro automático de procedencia financiera.

## Qué aprovechar

Sirve para comparar una tesis bajo distintas hipótesis de ingresos, dilución o riesgo sin mantener resultados de celdas ejecutadas en orden arbitrario. Una vista de 10–20 minutos puede mostrar cambios y acceso a las filas que los explican.

## Qué no asumir

La reactividad puede repetir llamadas o cálculos costosos si no se separan adquisición y análisis. Leer un notebook ajeno puede acabar ejecutando código; no abrirlo con ejecución automática. Un gráfico actualizado no demuestra que el dataset también esté actualizado ni que el modelo respete knowledge_time.

## Dependencias, pruebas y requisitos

El manifiesto requiere Python >=3.11. SQL y gráficos incorporan extras; las funciones de IA son opcionales y no necesarias para las propuestas.

Se leyó test_set_stale: una celda y sus descendientes quedan marcados, mientras una celda independiente no. También se inspeccionó la estructura de pruebas de ciclos/orden y dependencias SQL. No se ejecutaron.

Estimación: CPU, 8 GB o más para el alcance pequeño; requisitos reales dependen de lo ejecutado en las celdas, no del editor.

## Licencia y acceso

Apache-2.0. Clasificación: **REUTILIZACIÓN POTENCIALMENTE COMPATIBLE**. El permiso del código no se extiende a los datos ni a servicios alojados. No se investigó exhaustivamente cada dependencia o incidencia de seguridad.

## Alternativa y experimento mínimo propuesto

Jupyter/Voilà si ya hay notebooks fiables, Streamlit para un panel de uso recurrente o un informe HTML estático si no hace falta recalcular escenarios.

Modificar un supuesto y comprobar qué celdas cambian; usar snapshots fijos para que el resultado sea reproducible. Aceptar la interfaz si reduce tiempo de revisión sin perder citas ni unidades. Este experimento es un diseño, no una prueba realizada.

## Evidencias trazables

- [LICENSE](https://raw.githubusercontent.com/marimo-team/marimo/54552ec3137df83992ac29aa73d1adf73eb252b1/LICENSE) — HTTP 200; SHA-256 `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`.
- [README.md](https://raw.githubusercontent.com/marimo-team/marimo/54552ec3137df83992ac29aa73d1adf73eb252b1/README.md) — HTTP 200; SHA-256 `d017b1b939242ce844b38a20e9d53b7af277c48743cce6bcfca815634e760eca`.
- [marimo/_runtime/dataflow/graph.py](https://raw.githubusercontent.com/marimo-team/marimo/54552ec3137df83992ac29aa73d1adf73eb252b1/marimo/_runtime/dataflow/graph.py) — fuente `infra-S0155`; inspección parcial de rutas descritas.
- [tests/_runtime/test_dataflow.py](https://raw.githubusercontent.com/marimo-team/marimo/54552ec3137df83992ac29aa73d1adf73eb252b1/tests/_runtime/test_dataflow.py) — fuente `infra-S0157`; inspección parcial de rutas descritas.
- [pyproject.toml](https://raw.githubusercontent.com/marimo-team/marimo/54552ec3137df83992ac29aa73d1adf73eb252b1/pyproject.toml) — fuente `infra-S0158`; inspección parcial de rutas descritas.

Puntuación por criterio (máximos 25/15/15/12/10/8/8/7): utility=22, evidence=13, data=13, ease=10, license=10, maintenance=5, usability=8, differentiation=6. La disponibilidad y utilidad reciben peso alto; mantenimiento no obtiene puntuación máxima porque no se auditó su sostenibilidad.
