> **📝 MIS NOTAS** · Encuentro 3 · Pruebas que detectan · 23 nov 2026
> Este bloque lo escribí yo para estudiar. Debajo de la línea está el material original del profesor, sin cambios.

## 📝 ¿De qué trata este curso? (explicado para alguien nuevo)

Cuando usas una app (pedir un domicilio, reservar una cita, comprar en línea) ves botones y pantallas. Eso es el **frontend**. Detrás hay un programa que recibe tus pedidos, decide si se pueden hacer y guarda la información. Eso es el **backend**, y es lo que aprendemos a construir en este curso, usando **Python**.

Al final del curso cada persona tiene **su propio proyecto**: una API pequeña con **reglas de negocio**, **pruebas automáticas**, **integración continua** y una **base de datos** (MongoDB), ordenada en capas que puedas explicar.

## 📝 ¿Qué enseña este Encuentro 3?

**La pregunta del día:** *¿tu prueba detecta un error de la regla, o solo repite lo que hace el código?*

En el Encuentro 1 **escribimos** la regla. En el Encuentro 2 la **protegimos** (`@property`). Ahora escribimos **pruebas automáticas**: pequeños programas que revisan solos que la regla se cumpla, cada vez que cambias el código.

🏪 **Analogía:** una prueba es como la persona que hace el **arqueo de caja** al final del día. Si solo copia lo que dice el sistema ("el sistema dice 7, anoto 7"), nunca va a descubrir un error. Una prueba útil **cuenta por su cuenta** lo que *debería* haber según el caso ("vendí 3 de 10, deben quedar 7") y lo compara con lo que dice el sistema.

| Idea | Qué significa | Archivo |
|---|---|---|
| 🔁 **Prueba eco** vs. 🎯 **prueba del caso** | La eco compara el código consigo mismo y siempre pasa. La del caso espera un número que sale del negocio. | `test_eco.py` |
| 🧱 **Arrange – Act – Assert** | Preparar → hacer la acción → afirmar el resultado. | `test_producto.py` |
| 🚫 **`pytest.raises(..., match=...)`** | Probar que algo se **rechaza**, y por el motivo correcto. | `test_producto.py`, `test_turno_rechazo.py` |
| 🧰 **Fixture** (con `yield` y `scope`) | Preparación reutilizable. Por defecto se crea **nueva para cada prueba**. | `test_caja.py`, `test_orden.py` |
| 🔢 **`parametrize`** | La misma prueba con varios datos (por ejemplo, el borde 3 y 4). | `test_producto.py` |
| 🎭 **Mock** e **inyección** | Reemplazar al proveedor real (que usa internet) por un "doble" que controlamos. | `reabastecimiento.py`, `test_reabastecimiento.py`, `test_proveedor_cae.py` |
| 🧟 **Mutantes** | Copias del código con un error escondido. Si tus pruebas no fallan, el mutante **sobrevive**: a tus pruebas les falta algo. | `mutantes/`, `cazar_mutantes.py` |

Ideas para llevarse:

- 🎯 **El esperado sale del caso, no del código.** Si copias el resultado del código en la prueba, la prueba solo confirma que el código hace lo que hace (con errores incluidos).
- 🚫 **Prueba también el rechazo.** Una regla tiene dos caras: lo que acepta y lo que rechaza. Y después del rechazo, revisa que el estado **no cambió**.
- 🧰 **Cada prueba debe arrancar limpia.** Si dos pruebas comparten un objeto que se modifica, el resultado depende del orden en que corren (`test_orden.py`).
- 🎭 **No dependas de internet en tus pruebas.** Inyecta lo externo (el proveedor) para poder reemplazarlo por un mock, y prueba también **qué pasa cuando falla**.
- 🧟 **Una prueba vale por los errores que detecta.** Que todo esté en verde no basta; romper el código a propósito te dice si tus pruebas sirven.

## 📝 Ruta sugerida por los archivos

| Orden | Archivo | Qué vas a ver |
|---|---|---|
| 0 | `pytest.ini`, `conftest.py` | Configuración (no hace falta entenderla para empezar). Permite `--producto-defecto` y los mutantes. |
| 1 | `producto.py` / `producto_con_defecto.py` | El Producto del Encuentro 2 y una copia rota que **no descuenta**. |
| 2 | `test_eco.py` | La prueba eco (no detecta el defecto) vs. la prueba del caso (sí lo detecta). |
| 3 | `test_producto.py` | Arrange–Act–Assert, `raises` + `match`, fixture con `yield`, `parametrize`. |
| 4 | `test_turno_rechazo.py` | 🫵 Tu turno: probar que un producto no nace con existencias negativas. |
| 5 | `test_caja.py` | 🫵 Tu turno: predecir cuántas veces se imprime «Abrir caja de panela». |
| 6 | `test_orden.py` | Una fixture compartida (`scope="module"`) hace que una prueba falle según el orden. |
| 7 | `reabastecimiento.py` | Un servicio que llama a un proveedor externo (inyectado). |
| 8 | `test_reabastecimiento.py` | Mock, `assert_called_once_with`, `monkeypatch` y una prueba de integración omitida. |
| 9 | `test_proveedor_cae.py` | 🫵 Tu turno: simular que el proveedor se cae con `side_effect`. |
| 10 | `taller.py` + `test_taller_practica.py` | 🫵 Práctica en sala: dos pruebas del Taller. |
| 11 | `cazar_mutantes.py` + `mutantes/` | Correr tus pruebas contra 3 Talleres con errores escondidos. |

Cada archivo `.py` tiene comentarios `# 📝` con la explicación, la salida esperada y preguntas de repaso al final.

## 📝 Salida esperada al correr todo (`python -m pytest -v`)

```
5 failed, 16 passed, 1 skipped
```

| Falla | ¿Por qué? |
|---|---|
| `test_turno_rechazo.py::test_existencias_negativas` | Te toca escribirla (tiene `pytest.fail`). |
| `test_proveedor_cae.py::test_proveedor_cae` | Te toca escribirla. |
| `test_taller_practica.py` (2 pruebas) | Práctica en sala. |
| `test_orden.py::test_inventario_inicial` | `assert 7 == 10`: la fixture es compartida y la prueba anterior ya descontó 3. |

La omitida (`skipped`) es `test_proveedor_real`: necesita internet y un proveedor de verdad.

## 📝 Palabras clave

- **pytest:** la herramienta que busca archivos `test_*.py`, ejecuta las funciones `test_*` y te dice cuáles pasan (PASSED) y cuáles fallan (FAILED).
- **`assert`:** "afirmo que esto es verdad". Si no lo es, la prueba falla.
- **Prueba eco:** compara el resultado del código con… el mismo código. Siempre pasa, así que no detecta nada.
- **Arrange – Act – Assert (AAA):** preparar, actuar, afirmar. Las tres partes de una prueba ordenada.
- **`pytest.raises(Error, match="texto")`:** la prueba pasa **solo si** se lanza ese error con ese mensaje.
- **Fixture:** función con `@pytest.fixture` que prepara algo para las pruebas. Con `yield`, lo que va después se ejecuta al terminar (como "cerrar la caja").
- **`scope`:** cada cuánto se crea la fixture. `function` (por defecto) = una por prueba; `module` = una para todo el archivo.
- **`parametrize`:** correr la misma prueba con varias filas de datos.
- **Inyección de dependencias:** el servicio recibe al proveedor desde afuera (`Reabastecimiento(proveedor)`) en lugar de crearlo adentro. Así se puede cambiar por un mock.
- **Mock:** objeto "doble" que finge ser el real. Puedes decirle qué devolver (`return_value`), qué error lanzar (`side_effect`) y preguntarle cómo lo llamaron (`assert_called_once_with`).
- **`monkeypatch`:** reemplaza algo temporalmente durante una prueba (aquí, `urlopen`, para no usar internet).
- **Prueba de integración:** prueba contra el servicio real. Comprueba el contrato de verdad, pero es lenta y depende de la red.
- **Mutante:** copia del código con un error pequeño puesto a propósito. **Muere** si alguna prueba falla; **sobrevive** si todas pasan.

---

# Encuentro 3 · Pruebas que detectan

**Pregunta del día:** ¿tu prueba detecta un error de la regla o solo repite lo que hace el código?

También puedes ver el material en el navegador, con las salidas preparadas: https://live.maikoldiaz.dev/backend-python/03/material/

Continuamos con el Producto y el Taller del encuentro 2. Python 3.11 o posterior.

| Archivo | Uso |
| --- | --- |
| `producto.py` | El Producto del encuentro 2, importable |
| `producto_con_defecto.py` | El mismo Producto con un defecto: ya no descuenta |
| `test_eco.py` | Dos pruebas del mismo caso: una repite el código y otra espera lo que dice el caso |
| `test_producto.py` | Arrange–Act–Assert, `raises` con `match`, fixture con `yield` y `parametrize` |
| `test_turno_rechazo.py` | Tu turno: la prueba de rechazo de otra regla del Producto, por escribir |
| `test_caja.py` | Tu turno: una fixture con `yield`; cuántas veces se imprime «Abrir caja de panela» |
| `test_orden.py` | Dos pruebas que comparten una fixture |
| `reabastecimiento.py` | Servicio con proveedor inyectado y adaptador HTTP |
| `test_reabastecimiento.py` | Mock, llamadas, el adaptador sin red y una prueba de integración omitida |
| `test_proveedor_cae.py` | Tu turno: que el proveedor se caiga, con `side_effect`, por escribir |
| `taller.py` | El Taller del encuentro 2, importable |
| `test_taller_practica.py` | Fixture lista y dos pruebas por completar |
| `mutantes/mutante_1.py` … `mutante_3.py` | Tres copias del Taller con un error escondido |
| `cazar_mutantes.py` | Ejecuta tus pruebas contra el Taller y contra cada mutante |
| `conftest.py`, `pytest.ini` | Configuración de pytest para esta carpeta |

## Preparar el entorno

Desde esta carpeta, crea y activa un entorno local:

```sh
python3 -m venv .venv
```

En macOS/Linux: `source .venv/bin/activate`. En PowerShell: `.venv\Scripts\Activate.ps1`
(si la política impide activarlo, usa `.venv\Scripts\python.exe` en lugar de `python`).
En Windows puedes crearlo con `py -3 -m venv .venv`.

```sh
python -m pip install pytest
python -m pytest -v
```

El conjunto inicial falla a propósito: **16 pasan, 5 fallan y 1 se omite**. Cuatro fallos son pruebas que vas a escribir (las dos del Taller, la de rechazo y la del proveedor que cae); el quinto, en `test_orden.py`, lo descubrimos en clase.

Ejecuta por secciones, escribiendo antes qué esperas ver:

```sh
python -m pytest test_eco.py -v
python -m pytest test_eco.py --producto-defecto -v
python -m pytest test_producto.py -v
python -m pytest test_turno_rechazo.py -v
python -m pytest test_caja.py -v -s
python -m pytest test_orden.py -v
python -m pytest test_orden.py::test_salida -v
python -m pytest test_orden.py::test_inventario_inicial -v
python -m pytest test_reabastecimiento.py -v
python -m pytest test_proveedor_cae.py -v
```

## Práctica

En tu sala, abre `test_taller_practica.py`.

1. Completen las dos pruebas: una inscripción que se acepta y una que se rechaza cuando no hay cupo. Corran `python -m pytest test_taller_practica.py -v`.
2. Si escribieron la válida en el navegador, cópienla a su `test_taller_practica.py` local (el editor no guarda en tu computador y «Descargar» trae el original). Corran `python cazar_mutantes.py`. Cada mutante es una copia del Taller con un error escondido. ¿Cuáles sobreviven?
3. Escriban la prueba que mata al que sobrevivió. Vuelvan a cazar.

**Producto:** cuántos mutantes sobrevivieron al principio y cuál prueba lo mató.

El cazador exige que tus pruebas pasen primero contra el Taller original. Código de salida 2: las pruebas originales están incompletas o hubo un error de infraestructura; 0: la comparación se hizo, aunque sobrevivan mutantes. Que un mutante muera significa que al menos una prueba falló; no demuestra por sí solo que toda la regla esté cubierta.

La solución se publica después de la clase.

## Para tu proyecto

En tu repositorio:

1. Crea `pytest.ini` con dos líneas: `[pytest]` y `pythonpath = src`. Así `from modelo import …` funciona desde `tests/`.
2. Crea `tests/test_modelo.py` con una prueba de tu regla que se acepta y una que se rechaza. El esperado sale de tu caso, no de tu código.
3. Rompe tu regla a propósito (un `<` por `<=`, quita una validación). ¿Falló alguna prueba? Si no, tus pruebas todavía no detectan ese defecto: revisa el caso y las aserciones. Restaura.
4. Pasa la preparación a una fixture y escribe su alcance.
5. Si tu servicio llama algo externo (correo, pago, API, base de datos), reemplázalo con un mock y prueba qué pasa cuando falla.
6. En tu `README.md`: pega la salida de `python -m pytest -v` y escribe qué comportamiento externo aún no comprobaste.

El mock comprueba cómo reacciona tu código al contrato que supones; una prueba de integración comprueba ese contrato. La dirección `.example` de `reabastecimiento.py` está reservada: reemplázala antes de habilitar una prueba de integración y no quites el `skip` solo para ver verde.

**Para pensar antes del próximo encuentro:** ¿qué cambio en tu regla debería hacer fallar a tus pruebas? El miércoles esas pruebas corren solas en GitHub.
