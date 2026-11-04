# Licencias, restricciones y riesgos de adopción

Esta matriz es una evaluación técnica de compatibilidad potencial, no un dictamen jurídico. Se refiere al commit/card observado; no hereda licencias de otra versión o componente. **Código, pesos, datos, documentación y servicios son capas distintas.** El inventario completo está en [licenses.csv](inventories/licenses.csv) y [JSON](inventories/licenses.json), con fuentes, confianza y bloqueantes.

Clases: REUTILIZACIÓN POTENCIALMENTE COMPATIBLE; COMPATIBLE CON OBLIGACIONES; SOLO INVESTIGACIÓN / RESTRICCIONES; LICENCIA NO VERIFICADA; NO RECOMENDADO PARA EL USO PREVISTO. Una licencia no verificada bloquea copia/adaptación, no la lectura crítica de documentación pública. La clase con restricciones no significa que todo uso personal esté prohibido: exige evaluar el caso concreto.

## Casos que cambian la decisión

| Recurso/capa | Licencia observada | Clasificación | Fuente exacta |
|---|---|---|---|
| duckdb | MIT | REUTILIZACIÓN POTENCIALMENTE COMPATIBLE | [texto/card](https://raw.githubusercontent.com/duckdb/duckdb/6bb57d29dbc1f9032005816e6bb08763bd1a8fb2/LICENSE) |
| pandera | MIT | REUTILIZACIÓN POTENCIALMENTE COMPATIBLE | [texto/card](https://raw.githubusercontent.com/unionai-oss/pandera/7ad5f3948d9d1810217d5a25070e6b65e9154059/LICENSE.txt) |
| quant-feature-store | No verificada | LICENCIA NO VERIFICADA | [repositorio y búsqueda de permiso](https://github.com/sophie-nguyenthuthuy/quant-feature-store) |
| ingestr | FSL-1.1-ALv2 | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/bruin-data/ingestr/f5ffc5db8e1165647fe9f336f0272dd70c4e84d9/LICENSE) |
| lakeFS | BUSL-1.1; Additional Use Grant limitado | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/treeverse/lakeFS/a247a81d32f05aca22ced14536ca0e6cfdaa1794/LICENSE) |
| soda-core | Elastic-2.0 | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/sodadata/soda-core/b1cb7f20446a76961b3b5be6900751a4ac967fc7/LICENSE) |
| timescaledb | Apache-2.0 + Timescale License por directorio | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/timescale/timescaledb/dc2de5b5b095d45834eaa87743379445c0427bfe/LICENSE) |
| vectorbt | Apache-2.0 WITH Commons-Clause | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/polakowo/vectorbt/c923f74c9e4d1e07e626ae9002f7382cd8264833/LICENSE.md) |
| OpenBB / OpenBQ | Apache-2.0 | REUTILIZACIÓN POTENCIALMENTE COMPATIBLE | [texto/card](https://raw.githubusercontent.com/openbq-org/OpenBB/2a392e890f6eb1f0f4e3a71742720af8f056333a/LICENSE) |
| MLFinLab | Acuerdo propietario Hudson & Thames; referencias internas ambiguas a ArbitrageLab | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/hudson-and-thames/mlfinlab/79dcc7120ec84110578f75b025a75850eb72fc73/LICENSE.txt) |
| RQAlpha | Apache-2.0 modificado: uso comercial sujeto a autorización | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/ricequant/rqalpha/0bf04946e8250b457e30c3c81d338a6b925da0bb/LICENSE) |
| pykalman | BSD modificado: restricciones de canales de distribución | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/pykalman/pykalman/d62e60be00bd028ecc7eea6a8bea02f583910428/LICENSE) |
| DefiLlama dimension adapters | No inferida de la licencia del cliente; revisar fuentes y condiciones por dataset | LICENCIA NO VERIFICADA | [repositorio y búsqueda de permiso](https://github.com/DefiLlama/dimension-adapters) |
| Polymarket unified Python SDK | MIT | REUTILIZACIÓN POTENCIALMENTE COMPATIBLE | [texto/card](https://raw.githubusercontent.com/Polymarket/py-sdk/aa94ec431e3d4946576fb7c0d079fe1c14fcf676/LICENSE) |
| Polymarket CTF Exchange V2 | BUSL-1.1; sin Additional Use Grant; Change Date 2030-03-27 a MIT en texto examinado | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/Polymarket/ctf-exchange-v2/ccc0596074f4dfd62c944fbca4de252893b82b4b/LICENSE.md) |
| Uniswap v3 core | BUSL-1.1; Change License GPL-2.0-or-later desde 2023-04-01 para texto examinado | COMPATIBLE CON OBLIGACIONES | [texto/card](https://raw.githubusercontent.com/Uniswap/v3-core/5ea68a77cb541c6b3812df783be71ba8c081e25f/LICENSE) |
| Uniswap v4 core | BUSL-1.1; Change Date 2027-06-15 a MIT, con posibles modificaciones ENS; revisar versión | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/Uniswap/v4-core/bea7f6d1c11cd5dc4f0d5151ffa37a1c239feee6/licenses/BUSL_LICENSE) |
| GMX Synthetics | BUSL-1.1; Change License GPL-2.0-or-later desde 2026-08-31 para texto examinado | COMPATIBLE CON OBLIGACIONES | [texto/card](https://raw.githubusercontent.com/gmx-io/gmx-synthetics/a85ea3491c19c93bb4b5a002d9b358fb769b7849/LICENSE) |
| Dune Spellbook | BUSL-1.1; Change Date 2027-03-03 a GPL-3.0-or-later; restricción de Data/Analytics Platform | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/duneanalytics/spellbook/a8deb6ccfd44d1255aaca2592e40fbc80e03f242/LICENSE) |
| Cryptofeed | AGPL-3.0-or-later + atribución adicional | COMPATIBLE CON OBLIGACIONES | [texto/card](https://raw.githubusercontent.com/bmoscon/cryptofeed/3128a3bed0c06812751b528d35f89debb22a5202/LICENSE) |
| Raydium SDK V2 | GPL-3.0 (ver texto/versiones por archivo) | COMPATIBLE CON OBLIGACIONES | [texto/card](https://raw.githubusercontent.com/raydium-io/raydium-sdk-V2/f3fa7cbfd649fa5bfd20c9e693cfbf3b7ce69966/LICENSE) |
| Coin Metrics Community Data | CC-BY-NC-4.0 | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/coinmetrics/data/f1a36afb962731c387bb03982758ab0103063da5/LICENSE) |
| TimesFM library | Apache-2.0 | REUTILIZACIÓN POTENCIALMENTE COMPATIBLE | [texto/card](https://raw.githubusercontent.com/google-research/timesfm/e51928e27119cb17bebc005be2696b75e0a9e688/LICENSE) |
| google/timesfm-3.0-pytorch | TimesFM Non-Commercial License v1.0 | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://huggingface.co/google/timesfm-3.0-pytorch/resolve/43046b85ec22d584a13f8098c2ed39c889e129c2/LICENSE) |
| FinBERT code | Apache-2.0 | REUTILIZACIÓN POTENCIALMENTE COMPATIBLE | [texto/card](https://raw.githubusercontent.com/ProsusAI/finBERT/3b4bfed383a8bb6b013db2f1ce9c766ff5100d24/LICENSE) |
| ProsusAI/finbert | cc-by-nc-sa-4.0 | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://huggingface.co/ProsusAI/finbert/resolve/0bc2ac10dda6929bcb1f77ccc43c7ec5c424f031/README.md) |
| Salesforce/moirai-2.0-R-small | cc-by-nc-4.0 | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://huggingface.co/Salesforce/moirai-2.0-R-small/resolve/30f43ff08c8494f4943ae1521e9d4e94a0fbb389/README.md) |
| Alibi Detect | BUSL-1.1 | SOLO INVESTIGACIÓN / RESTRICCIONES | [texto/card](https://raw.githubusercontent.com/SeldonIO/alibi-detect/c2fd0e05c648d353467bdb15fd6149a103b3a981/LICENSE) |

Las fechas de cambio de BUSL se interpretan respecto al texto de la versión concreta: no basta etiquetar todo como BUSL ni suponer que cualquier versión futura ya se convirtió. Términos ENS, excepciones por archivo, activos y dependencias pueden cambiar el alcance. La restricción de pykalman afecta canales de redistribución y contiene excepciones: no presentarla como prohibición general para usuarios finales.

Un SDK MIT puede convivir con contratos BUSL; un programa Raydium Apache puede convivir con SDK GPL. Code y checkpoint TimesFM/FinBERT tienen permisos distintos. Coin Metrics Community Data no hereda MIT de su cliente. Las cards declaran permisos, pero no auditan por sí solas todos los derechos del corpus de entrenamiento.

## Riesgos que prevalecen sobre el score

| Riesgo | Consecuencia | Respuesta proporcional |
|---|---|---|
| Sin licencia aplicable | Copia/adaptación no autorizada por ser público | Referencia conceptual o alternativa con permiso verificado |
| Historial sin vintage | Sesgo de conocimiento futuro | Prospectivo o reconstrucción etiquetada; no backtest causal |
| SDK deprecado | Compatibilidad y correcciones inciertas | Sucesor oficial revisado, sin asumir que fork activo basta |
| Servicio comercial detrás de código | Reproducción/coste/retención no garantizados | Alcance pequeño, alternativa manual y condiciones del endpoint |
| Payload o notebook no confiable | Ejecución/supply chain | Solo lectura aquí; futuro aislamiento y revisión antes de ejecutar |
| Datos/citas sin soporte semántico | Informe convincente pero incorrecto | Revisión humana, cálculos reproducibles y abstención |
| Caché caducada o feed parcial | Falsa calma o alerta errónea | Estado de frescura, cobertura y suspensión de conclusiones |
| Confusión de beneficiario/unidad | Valoración sin sentido económico | Reconciliar cantidades, mecanismos y elegibilidad |

No se hizo auditoría integral de vulnerabilidades ni dependencias transitivas. No se certifica seguridad por ausencia de incidencias observadas. No se recomiendan claves de exchange/wallet para ejecutar código no auditado. No se generaron operaciones, contratación, publicación remota ni cambios en CIE.

## Preparación del paquete

La entrega contiene notas propias, URLs, identificadores, metadatos y hashes. El ZIP excluye cachés de texto/código de terceros, pesos y datasets; no incorpora librerías ajenas. `.gitignore` protege cachés de trabajo y secretos comunes. No se creó repositorio remoto. Antes de una publicación futura, revisar también permisos de cualquier dato/documento añadido después de esta investigación.
