# requests-cache: disponibilidad y frescura son propiedades distintas

Recurso: [requests-cache](https://github.com/requests-cache/requests-cache). Commit observado: `abe06a833cfb35a885f371d1b3db1199b3a968b5`. Verificación: 2026-11-04; nivel V3, análisis estático.

**Decisión:** Adoptar biblioteca de forma limitada, con estado de frescura visible y políticas por endpoint. Puntuación editorial: **84/100**; riesgo bloqueante: ninguno identificado en esta ruta; no equivale a certificación.

## Arquitectura e implementación observada

CachedSession.send consulta el backend y decide entre respuesta guardada y red. _resend maneja errores de refresco; CacheActions permite reutilizar una respuesta caducada con stale_if_error, incluso sin límite temporal si se habilita con True. Se inspeccionaron estas rutas y sus pruebas.

## Qué aprovechar

Una caché reduce llamadas repetidas a documentación y endpoints lentos. Puede conservar lectura útil durante una caída, siempre que el panel indique fecha original, edad, estado caducado y última actualización fallida.

## Qué no asumir

Un HTTP 200 devuelto desde caché no prueba que la fuente siga disponible ni que el valor sea actual. No usar stale_if_error ilimitado para alertas de derivados. La caché es mutable y evictable: no sustituye al archivo de evidencia. Revisar claves de caché y separación por credenciales si algún desarrollo futuro incorpora fuentes autenticadas.

## Dependencias, pruebas y requisitos

Python >=3.8 y requests; backends/serializadores opcionales amplían dependencias. No se evaluaron todos los serializadores ni su seguridad.

test_stale_if_error__exception y test_stale_if_error__error_code comprueban devolución de respuesta antigua con from_cache e is_expired. Esa conducta es una característica deliberada, no un fallo de la biblioteca.

Estimación: CPU y disco local; volumen de caché acotado por TTL y cuota. No hay necesidad de GPU.

## Licencia y acceso

BSD-2-Clause. Clasificación: **REUTILIZACIÓN POTENCIALMENTE COMPATIBLE**. El permiso del código no se extiende a los datos ni a servicios alojados. No se investigó exhaustivamente cada dependencia o incidencia de seguridad.

## Alternativa y experimento mínimo propuesto

Hishel para un flujo basado en HTTPX y semántica HTTP. Para unos pocos snapshots diarios, guardar payload y hash sin caché adicional puede ser más transparente.

Interrumpir una fuente en un entorno futuro aislado y comprobar que el panel cambia a dato caducado, conserva retrieved_at original y suspende alertas al superar el umbral. Este experimento es un diseño, no una prueba realizada.

## Evidencias trazables

- [LICENSE](https://raw.githubusercontent.com/requests-cache/requests-cache/abe06a833cfb35a885f371d1b3db1199b3a968b5/LICENSE) — HTTP 200; SHA-256 `1aedf075663a232d425816b8b6c6c852e7e7976b5f98b968643162ec593d0b69`.
- [README.md](https://raw.githubusercontent.com/requests-cache/requests-cache/abe06a833cfb35a885f371d1b3db1199b3a968b5/README.md) — HTTP 200; SHA-256 `4c21c966f894a72aa06e0a59ebdb804bafc110783a6faf1ddcf3598e2c67b61d`.
- [requests_cache/session.py](https://raw.githubusercontent.com/requests-cache/requests-cache/abe06a833cfb35a885f371d1b3db1199b3a968b5/requests_cache/session.py) — fuente `infra-S0100`; inspección parcial de rutas descritas.
- [requests_cache/policy/actions.py](https://raw.githubusercontent.com/requests-cache/requests-cache/abe06a833cfb35a885f371d1b3db1199b3a968b5/requests_cache/policy/actions.py) — fuente `infra-S0101`; inspección parcial de rutas descritas.
- [tests/unit/test_session.py](https://raw.githubusercontent.com/requests-cache/requests-cache/abe06a833cfb35a885f371d1b3db1199b3a968b5/tests/unit/test_session.py) — fuente `infra-S0102`; inspección parcial de rutas descritas.
- [pyproject.toml](https://raw.githubusercontent.com/requests-cache/requests-cache/abe06a833cfb35a885f371d1b3db1199b3a968b5/pyproject.toml) — fuente `infra-S0103`; inspección parcial de rutas descritas.

Puntuación por criterio (máximos 25/15/15/12/10/8/8/7): utility=21, evidence=13, data=13, ease=11, license=9, maintenance=5, usability=7, differentiation=5. La disponibilidad y utilidad reciben peso alto; mantenimiento no obtiene puntuación máxima porque no se auditó su sostenibilidad.
