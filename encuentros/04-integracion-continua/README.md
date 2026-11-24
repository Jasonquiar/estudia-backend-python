> **📝 MIS NOTAS** · Encuentro 4 · Integración continua, calidad y regresión · 25 nov 2026
> Este bloque lo escribí yo para estudiar. Debajo de la línea está el material original del profesor, sin cambios.

## 📝 ¿De qué trata este curso? (explicado para alguien nuevo)

Cuando usas una app (pedir un domicilio, reservar una cita, comprar en línea) ves botones y pantallas. Eso es el **frontend**. Detrás hay un programa que recibe tus pedidos, decide si se pueden hacer y guarda la información. Eso es el **backend**, y es lo que aprendemos a construir en este curso, usando **Python**.

Al final del curso cada persona tiene **su propio proyecto**: una API pequeña con **reglas de negocio**, **pruebas automáticas**, **integración continua** y una **base de datos** (MongoDB), ordenada en capas que puedas explicar.

## 📝 ¿Qué enseña este Encuentro 4?

**La pregunta del día:** *cuando el pipeline dice verde, ¿qué se ejecutó de verdad?*

En el Encuentro 3 escribimos **pruebas que detectan**. Ahora hacemos que esas pruebas corran **solas, en un computador limpio**, cada vez que alguien hace `git push`. Eso es la **integración continua (CI)**. Y aprendemos a no creerle ciegamente al ✅ verde.

🏪 **Analogía:** la CI es como el **inspector de sanidad** que visita la tienda cada vez que llega mercancía nueva. No le importa que "en mi casa la nevera funciona": revisa con **sus** instrumentos, en **su** visita. Pero si el inspector firma el acta sin abrir la nevera (cero pruebas), la firma no vale nada. Por eso hay que **leer el acta** (el log) y ver cuántas cosas revisó.

| Idea | Qué significa | Carpeta |
|---|---|---|
| 🧼 **Entorno limpio** | GitHub instala **solo** lo que dice `requirements.txt`. Lo que tienes instalado "de casualidad" en tu computador allá no existe. | `ci_inventario/` |
| ⚙️ **Workflow** (`.github/workflows/ci.yml`) | La receta que sigue GitHub: traer el código, preparar Python, instalar, probar. | `ci_inventario/`, `plantilla_ci/` |
| 🤥 **Verde mentiroso** | El job sale verde aunque no corrió ninguna prueba (archivo mal nombrado + `| tee` sin `pipefail`). | `ci_cero_pruebas/` |
| 🔢 **Código de salida** | El número que deja un comando al terminar: `0` = éxito; otro = algo pasó. GitHub decide verde/rojo **solo** con ese número. | `ci_cero_pruebas/` |
| 🧹 **Linter (Ruff)** | Lee el código **sin ejecutarlo** y encuentra errores: imports sin usar, variables olvidadas, funciones duplicadas, funciones muy complejas. | `hallazgo_ruff/`, `hallazgo_ruff_gemelo/` |
| 📊 **Cobertura** | Qué líneas y ramas se **ejecutaron** durante las pruebas. Dice qué NO se probó, pero no si lo que sí se ejecutó se comprobó bien. | `cobertura_y_aserciones/` |
| 🧟 **Mutantes** (otra vez) | Medir si las pruebas **detectan**: 100 % de cobertura y aun así los mutantes sobreviven. | `cobertura_y_aserciones/` |
| 🌳 **Complejidad ciclomática** (`C901`) | Cuántos caminos distintos tiene una función. Muchos caminos = difícil de leer y de probar. | `practica_domicilios/` |

Ideas para llevarse:

- 🧼 **"En mi computador sí funciona" no es prueba.** Si una librería no está en `requirements.txt`, en el entorno limpio no existe.
- 🔎 **Verde no significa "se probó".** En el log, busca siempre la línea con **cuántas pruebas pasaron** (`7 passed`). Si dice `no tests ran`, el verde es mentira.
- 🔢 **GitHub solo mira el código de salida del último comando del pipe.** `pytest | tee` deja el código de `tee` (0). Con `shell: bash` o `set -o pipefail` el error de pytest no se esconde.
- 🛠️ **Tres herramientas, tres preguntas distintas:**
  - **Ruff:** ¿hay errores que se ven *sin ejecutar*?
  - **Cobertura:** ¿qué partes *se ejecutaron*?
  - **Aserciones / mutantes:** ¿las pruebas *comprueban* el resultado del negocio?
- 📊 **Más cobertura no es mejor si las pruebas no afirman nada.** Una prueba que recorre todo sin `assert` da 100 % y no detecta ningún mutante.
- 🌳 **Refactorizar = cambiar la forma sin cambiar el comportamiento.** Las pruebas son las que te avisan si lo cambiaste sin querer.

## 📝 Ruta sugerida por las carpetas

| Orden | Carpeta / archivo | Qué vas a ver |
|---|---|---|
| 0 | Preparar el entorno (`.venv` + `requirements-dev.txt`) | Instala pytest, pytest-cov, Ruff y unidecode. |
| 1 | `ci_inventario/` | Un proyecto "de verdad": `src/`, `tests/`, `pytest.ini`, `requirements.txt` y el workflow. 7 pruebas en verde. |
| 2 | `ci_inventario/` en un venv **limpio** | Falla porque falta `unidecode`. Y si quitas `pytest.ini`, no encuentra `producto`. |
| 3 | `ci_cero_pruebas/` | 🤥 Verde con cero pruebas: `prueba_producto.py` no empieza por `test_` y `| tee` esconde el código 5. |
| 4 | `hallazgo_ruff/` + `hallazgo_ruff_gemelo/` | 🫵 Sé el linter: 3 hallazgos en cada uno (F401, F841, F811). |
| 5 | `cobertura_y_aserciones/` | 📊 100 % de cobertura que no detecta nada vs. 94 % que mata a los dos mutantes. |
| 6 | `practica_domicilios/` | 🫵 Práctica: la tarifa de un domicilio, 75 % de cobertura y complejidad 17 (> 10). |
| 7 | `plantilla_ci/` | `ci.yml` para tu proyecto; `ci_reto.yml` y `pre-commit` para el nivel reto. |

Cada archivo tiene comentarios `# 📝` con la explicación, la salida esperada y preguntas de repaso al final. En los `.yml`, `.ini`, `.toml` y `requirements` las notas también van con `#` (es el comentario en esos formatos), así que **no cambian lo que hacen**.

## 📝 Salidas esperadas (verificadas con Python 3.12, pytest 9.2 y Ruff 0.17.6)

| Dónde | Comando | Resultado |
|---|---|---|
| `ci_inventario/` | `python -m pytest -v` | `7 passed` |
| `ci_inventario/` (venv solo con pytest) | `python -m pytest -v` | `ModuleNotFoundError: No module named 'unidecode'` → `Interrupted: 1 error during collection` |
| copia de `ci_inventario/` **sin** `pytest.ini` | `python -m pytest` | `No module named 'producto'` → `2 errors during collection` |
| `ci_cero_pruebas/` | `python -m pytest -v; echo $?` | `no tests ran` · código **5** |
| `ci_cero_pruebas/` | `python -m pytest -v \| tee salida_pytest.txt; echo $?` | `no tests ran` · código **0** 🤥 |
| `hallazgo_ruff/` | `ruff check .` | `Found 3 errors.` (F401 `os`, F841 `codigo`, F811 `test_salida_valida`) |
| `hallazgo_ruff_gemelo/` | `ruff check .` | `Found 3 errors.` (F401 `sys`, F841 `minimo`, F811 `alerta`) |
| `cobertura_y_aserciones/` | `pytest tests/test_recorre_todo.py --cov...` | `1 passed` · **100 %** · mutante_1 y mutante_2 **SOBREVIVEN** |
| `cobertura_y_aserciones/` | `pytest tests/test_con_aserciones.py --cov...` | `7 passed` · **94 %** (faltan `__repr__` y `__str__`) · mutante_1 y mutante_2 **MUEREN** |
| `practica_domicilios/` | `python -m pytest -v` | `9 passed` |
| `practica_domicilios/` | `pytest --cov=tarifa --cov-branch ...` | **75 %** con ramas sin cubrir |
| `practica_domicilios/` | `ruff check .` | `C901 calcular_tarifa is too complex (17 > 10)` |

💡 Los números de línea que salen en los reportes de cobertura y de Ruff cambian un poco por mis comentarios `# 📝` (las notas agregan líneas). Las notas de cada archivo dicen los números de **esta** copia.

💡 Para que no se llene la carpeta de archivos sueltos: `.pytest_cache/`, `.coverage` y `.ruff_cache/` ya están en el `.gitignore` de la raíz.

## 📝 Palabras clave

- **Integración continua (CI):** que un servidor (aquí, GitHub Actions) instale y pruebe tu código **automáticamente** en cada `push` o pull request.
- **Pipeline / workflow / job / step:** el workflow es el archivo `.yml`; adentro hay *jobs* (trabajos, como `pruebas`), y cada job tiene *steps* (pasos) que se ejecutan en orden.
- **`runs-on: ubuntu-latest`:** el computador limpio (Linux) donde corre el job. Se crea nuevo en cada ejecución y se borra al final.
- **`uses:` vs `run:`:** `uses` usa una acción ya hecha (`actions/checkout` trae el código, `actions/setup-python` instala Python); `run` ejecuta un comando de terminal.
- **`requirements.txt`:** la lista de librerías que necesita el proyecto. `requirements-dev.txt` agrega las de desarrollo (cobertura, Ruff) e incluye la otra con `-r requirements.txt`.
- **`pytest.ini`:** configuración de pytest. `pythonpath = src` → los `import` encuentran el código en `src/`; `testpaths = tests` → busca pruebas en `tests/`.
- **Código de salida (exit code):** `0` éxito. En pytest: `1` alguna prueba falló, `2` interrumpido (por ejemplo, error al importar), `5` no encontró ninguna prueba. Se ve con `echo $?` (PowerShell: `$LASTEXITCODE`).
- **Pipe (`|`) y `tee`:** `|` pasa la salida de un comando al siguiente; `tee` la muestra **y** la guarda en un archivo. El código que queda es el del **último** comando.
- **`pipefail`:** opción de bash que hace que el pipe falle si **cualquiera** de sus comandos falla.
- **Linter:** herramienta que revisa el código sin ejecutarlo. **Ruff** es un linter muy rápido para Python. Códigos: `F401` import sin usar, `F841` variable asignada y nunca usada, `F811` algo redefinido sin haber usado lo anterior, `C901` función demasiado compleja, `E…` estilo (pycodestyle).
- **Cobertura (`pytest-cov`):** `--cov=modulo` mide ese módulo; `--cov-branch` también mide **ramas** (el "sí" y el "no" de cada `if`); `--cov-report=term-missing` muestra qué líneas faltan.
- **Rama parcial (`58->61`):** el `if` de la línea 58 nunca tomó el camino que salta a la 61 (nunca fue falso).
- **Complejidad ciclomática:** 1 + cada decisión (`if`, `elif`, `and`, `or`, bucles…). Ruff la mide con la regla `C901` y avisa si pasa de `max-complexity`.
- **Regresión:** algo que funcionaba y deja de funcionar después de un cambio. La CI existe para atraparla antes de que llegue a producción.
- **Refactorizar:** mejorar la forma del código (más legible, menos complejo) **sin** cambiar lo que hace.
- **Matriz (`strategy.matrix`):** correr el mismo job con varias versiones (por ejemplo Python 3.11 y 3.14).
- **`--cov-fail-under=80`:** hace que el pipeline falle si la cobertura baja de 80 %.
- **pre-commit:** herramienta que corre revisiones (aquí Ruff) **en tu computador** antes de cada `git commit`.

---

# Encuentro 4 · Integración continua, calidad y regresión

**Pregunta del día:** cuando el pipeline dice verde, ¿qué se ejecutó de verdad?

También puedes ver el material en el navegador, con las salidas preparadas: https://live.maikoldiaz.dev/backend-python/04/material/

Continuamos con el Producto del encuentro 3. Python 3.11 o posterior.

| Carpeta | Uso |
| --- | --- |
| `ci_inventario/` | Un proyecto pequeño con pruebas, `requirements.txt`, `pytest.ini` y un workflow en `.github/workflows/ci.yml` |
| `ci_cero_pruebas/` | El mismo proyecto con un workflow que sale verde sin ejecutar ninguna prueba: ¿por qué? |
| `cobertura_y_aserciones/` | Dos archivos de pruebas del Producto, y mutantes para comparar qué detecta cada uno |
| `hallazgo_ruff/` | Código con tres hallazgos de Ruff |
| `hallazgo_ruff_gemelo/` | Otro archivo con tres hallazgos, para repetir el ejercicio con datos nuevos |
| `practica_domicilios/` | La práctica: una función con muchas ramas, sus pruebas y el reporte de cobertura |
| `plantilla_ci/` | `ci.yml` para copiar a tu repositorio, una versión de nivel reto y una configuración de pre-commit |

Cada carpeta funciona sola. Los comandos de abajo se ejecutan **desde dentro de la carpeta** que se indica.

## Preparar el entorno

Desde esta carpeta, crea y activa un entorno local:

```sh
python3 -m venv .venv
```

En macOS/Linux: `source .venv/bin/activate`. En PowerShell: `.venv\Scripts\Activate.ps1`
(si la política impide activarlo, usa `.venv\Scripts\python.exe` en lugar de `python`).
En Windows puedes crearlo con `py -3 -m venv .venv`.

```sh
python -m pip install -r ci_inventario/requirements-dev.txt
```

Eso instala pytest, pytest-cov, Ruff y unidecode. Los comandos con `$?` y `| tee` son de macOS/Linux o Git Bash; en PowerShell, el código de salida está en `$LASTEXITCODE`.

## 1. Pasa en mi computador, ¿por qué falla en uno limpio?

```sh
cd ci_inventario
python -m pytest -v
```

Pasan **7**. Ahora un entorno limpio, como el que crea GitHub en cada ejecución: solo lo que dice `requirements.txt`. El `requirements.txt` de esta carpeta ya está completo; para reproducir el problema **simulamos un archivo incompleto**, que solo dijera `pytest`, instalando solo esa línea:

```sh
python3 -m venv ../venv
../venv/bin/python -m pip install pytest
../venv/bin/python -m pytest -v
```

Antes de ejecutar, escribe qué esperas ver. Lee el log y escribe **la causa y la corrección exacta**. La corrección: el `requirements.txt` incompleto necesita la línea `unidecode` (aquí ya la tiene) y, en un entorno limpio, se vuelve a instalar y a correr lo mismo que el workflow:

```sh
python3 -m venv ../venv2
../venv2/bin/python -m pip install -r requirements.txt
../venv2/bin/python -m pytest -v
```

Segunda causa frecuente: sin `pytest.ini` con `pythonpath = src`, los `import` de las pruebas no encuentran el código. Compruébalo copiando la carpeta sin ese archivo y escribiendo de nuevo la causa y la corrección exacta.

## 2. Verde con cero pruebas

```sh
cd ../ci_cero_pruebas
python -m pytest -v; echo "código de salida: $?"
python -m pytest -v | tee salida_pytest.txt; echo "código de salida: $?"
```

Pytest sin pruebas termina con código **5**. Pero el workflow guarda la salida con `| tee`, y en este workflow, que no declara `shell`, GitHub ejecuta en Linux cada `run:` con `bash -e` (sin `pipefail`): el código que queda es el de `tee`, que es 0. Clasifica cada log (verde real, verde mentiroso, rojo porque no corrió ninguna prueba, rojo porque una prueba falló) y encuentra **la línea que lo prueba**. Después mira el archivo `tests/`: ¿por qué pytest no encontró nada? Propón dos cambios exactos y compara.

```sh
mv tests/prueba_producto.py tests/test_producto.py
python -m pytest -v | tee salida_pytest.txt
```

Eso hace que corran las pruebas. Para que un paso no esconda el código de pytest detrás de un pipe, declara `shell: bash` en el paso (GitHub lo ejecuta con `bash -eo pipefail`) o escribe `set -o pipefail;` antes del comando: así el verde con cero pruebas se pone rojo. `pipefail` evita que el job mienta, pero no hace que corran pruebas.

Otras formas de llegar a verde sin ejecutar pruebas: `python -m unittest discover` con pruebas escritas como funciones de pytest (en Python 3.11 termina con código 0 y «Ran 0 tests»; desde 3.12 termina con 5) o un `|| true` al final del comando. **En el log, busca siempre la línea con el número de pruebas que pasaron.**

## 3. Tres herramientas, tres preguntas

```sh
cd ../hallazgo_ruff
ruff check .
```

Antes de ejecutar Ruff, sé el linter: en 2 minutos, encuentra a ojo los defectos de los dos archivos y anótalos con su línea. Después compara con la salida real y repite el ejercicio con otro archivo (`hallazgo_ruff_gemelo/alertas_con_hallazgo.py`): encuentra a ojo los defectos y compáralos con `ruff check .` dentro de esa carpeta. Ruff dice si el código tiene errores que se ven sin ejecutarlo: un `import` sin usar, una variable que se calcula y nunca se usa (¿qué pretendía hacer el autor?) y una prueba que se define dos veces con el mismo nombre (la primera nunca corre).

```sh
cd ../cobertura_y_aserciones
python -m pytest tests/test_recorre_todo.py -v --cov=producto --cov-branch --cov-report=term-missing
python cazar_mutantes.py tests/test_recorre_todo.py
python -m pytest tests/test_con_aserciones.py -v --cov=producto --cov-branch --cov-report=term-missing
python cazar_mutantes.py tests/test_con_aserciones.py
```

Antes de ejecutar: una sola prueba que recorre todo el código sin comprobar los resultados del negocio (y con `pytest.raises(Exception)`, demasiado general), ¿qué cobertura da? ¿Y las siete que sí afirman? ¿Cuál de las dos detecta un mutante? `cazar_mutantes.py` primero comprueba que el Producto original pase; un mutante «muere» cuando una prueba falla al ejecutarse (casi siempre una aserción; si fue otro error, el script lo avisa), y cualquier otro problema (importar, preparar las pruebas, argumentos, cero pruebas) se muestra como error, no como un mutante muerto.

Haz tú el mutante: en una copia de `src/producto.py`, borra la línea `self.existencias -= cantidad`, ejecuta `test_recorre_todo.py` (pasa: el mutante sobrevive), cambia `cafe.registrar_salida(3)` por `assert cafe.registrar_salida(3) == 7` (ahora falla: el mutante muere) y restaura el original. La complejidad ciclomática (cuántos caminos tiene una función) se mide en la práctica, con la regla `C901` de Ruff.

## Práctica: una función con muchas ramas

```sh
cd ../practica_domicilios
python -m pytest -v
python -m pytest --cov=tarifa --cov-branch --cov-report=term-missing
ruff check .
```

La tarifa de un domicilio en Medellín depende de la distancia, la comuna, la hora, la lluvia y el tipo de cliente; las reglas están al inicio de `src/tarifa.py`. Las pruebas actuales pasan, pero el reporte muestra ramas sin cubrir y Ruff marca la función como demasiado compleja.

1. Lean el reporte: ¿qué líneas de `tarifa.py` no se ejecutan? Elijan una rama y escriban la prueba que la cubre. **El esperado sale de las reglas, no de leer el código.**
2. Elijan **una** mejora: retornos tempranos, una tabla (diccionario) en lugar de `if`/`elif`, o extraer una función. Háganla sin cambiar el comportamiento.
   El redondeo también se conserva: Python redondea al par (7.650 → 7.600), como dice el encabezado de `tarifa.py`.
3. Repitan `python -m pytest --cov=tarifa --cov-branch --cov-report=term-missing` y `ruff check .`. Las pruebas deben seguir en verde.
4. Para ver la complejidad de cada función antes y después (con el umbral de 10, una función que baja a 5 ya no aparece en `ruff check .`), usen este comando; sale con código 1 a propósito, porque su trabajo es mostrar los números:

```sh
ruff check --isolated --select C901 --config 'lint.mccabe.max-complexity=1' --output-format concise src/tarifa.py
```

**Producto:** la complejidad antes y después, el porcentaje de cobertura antes y después, y qué prueba les habría avisado si la mejora hubiera cambiado el comportamiento.

La solución se publica después de la clase.

## Para tu proyecto

En tu repositorio:

1. Crea `requirements.txt` con lo que necesita tu proyecto (por ejemplo `pytest`) y comprueba que funciona en un entorno limpio: `python -m pip install -r requirements.txt`.
2. Copia `plantilla_ci/ci.yml` a `.github/workflows/ci.yml` y ajusta la versión de Python, las dependencias y el comando de pruebas.
3. Haz `git push`. En GitHub abre la pestaña **Actions** y entra a la ejecución.
4. **Comprueba en el log cuántas pruebas corrieron.** Debe ser más de cero y coincidir con tu ejecución local.
5. En tu `README.md`: el comando local con su salida, el comando del workflow, y el estado de cada parte (ejecutado, simulado o pendiente). Si no tienes acceso a Actions, conserva el YAML y tu salida local; **no los llames ejecución remota**.
6. Ejecuta `ruff check .` en tu proyecto. Elige **una** mejora de legibilidad o de complejidad, repite tus pruebas y escribe en el README qué cambiaste y por qué.

**Nivel reto:** `plantilla_ci/ci_reto.yml` (matriz de versiones de Python, Ruff y `--cov-fail-under` en el pipeline) y `plantilla_ci/pre-commit-config.yaml`. Más de cobertura no es mejor si las pruebas no afirman nada.

**Para pensar antes del próximo encuentro:** si tu proyecto guardara sus datos en documentos en vez de en la memoria, ¿qué parte de tu pipeline tendría que cambiar?
