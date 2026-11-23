> **📝 MIS NOTAS** · Encuentro 2 · Dónde vive la regla · 18 nov 2026
> Este bloque lo escribí yo para estudiar. Debajo de la línea está el material original del profesor, sin cambios.

## 📝 ¿De qué trata este curso? (explicado para alguien nuevo)

Cuando usas una app (pedir un domicilio, reservar una cita, comprar en línea) ves botones y pantallas. Eso es el **frontend**. Detrás hay un programa que recibe tus pedidos, decide si se pueden hacer y guarda la información. Eso es el **backend**, y es lo que aprendemos a construir en este curso, usando **Python**.

Al final del curso cada persona tiene **su propio proyecto**: una API pequeña con **reglas de negocio**, **pruebas automáticas**, **integración continua** y una **base de datos** (MongoDB), ordenada en capas que puedas explicar.

## 📝 ¿Qué enseña este Encuentro 2?

**La pregunta del día:** *¿dónde vive la regla de tu servicio, y quién puede saltársela?*

En el Encuentro 1 aprendimos a **escribir** una regla de negocio (por ejemplo, "el stock nunca queda negativo"). Ahora la pregunta es **dónde ponerla** para que nadie se la salte.

🏪 **Analogía:** si el portero solo vigila la puerta principal, cualquiera puede entrar por la ventana. En código, la "ventana" es cambiar un dato directamente (`cafe.existencias = -5`) sin pasar por el método que revisa la regla.

| Dónde vive la regla | ¿Alguien se la puede saltar? | Archivo |
|---|---|---|
| Solo dentro de un **método** | ✅ Sí: basta con cambiar el atributo directo | `inventario_hueco.py`, `taller_practica.py` |
| En una **función** + un diccionario | ✅ Sí: cualquiera escribe en el diccionario | `taller_funcion.py` |
| En una **`@property`** (dentro del objeto, pegada al dato) | ❌ No por accidente (solo a propósito, con `_atributo`) | `inventario_property.py`, `solucion/taller_solucion.py` |

Ideas para llevarse:

- 👮 **Protege el dato, no solo la operación.** Con `@property`, *cualquier* cambio a `existencias` o a `cupo` pasa por el **setter**, que es el único lugar donde vive la regla.
- 🔢 **El orden importa.** En `__init__`, crea primero lo que el setter necesita revisar (por ejemplo, la lista de inscritos antes del cupo).
- 🧬 **Herencia ("ES UN") vs. 🧩 composición ("TIENE UN").** Un `ProductoPerecedero` *es* un producto con una regla extra. Un producto *tiene* una política de precio intercambiable.
- 📜 **No rompas el contrato.** Si una clase hija cambia lo que el padre prometía (por ejemplo, "rechazo cuando no hay cupo"), quien la use se lleva una sorpresa. A veces la composición es mejor opción que la herencia.
- 🤔 **¿Clase o función?** Si hay un *estado que cambia* y una *regla que lo protege*, la clase suele ganar. Si no, una función puede ser más simple.

## 📝 Ruta sugerida por los archivos

| Orden | Archivo | Qué vas a ver |
|---|---|---|
| 1 | `inventario_hueco.py` | El Producto del Encuentro 1 y su hueco: `cafe.existencias = -5` pasa sin control. |
| 2 | `inventario_property.py` | El hueco se tapa con `@property`. También atributos de clase/instancia y `__str__`/`__repr__`. |
| 3 | `estrategias.py` | Herencia con `super()`, override y composición con políticas de precio. |
| 4 | `taller_practica.py` | Práctica: el taller tiene el mismo hueco con el cupo. Te toca protegerlo. |
| 5 | `taller_funcion.py` | La misma práctica con una función y un diccionario: más simple, menos protegida. |
| 6 | `modelo_plantilla.py` | El molde para el `src/modelo.py` de tu propio proyecto. |
| 7 | `solucion/taller_solucion.py` | La solución del profesor, más el reto de la lista de espera. |

Cada archivo `.py` tiene comentarios `# 📝` con la explicación, la salida esperada y preguntas de repaso al final.

## 📝 Palabras clave

- **`@property` (getter y setter):** convierte un atributo en una "puerta con portero". El *getter* corre al **leer** el valor y el *setter* al **cambiarlo**.
- **`_atributo` (guion bajo):** convención de "privado, no lo toques". No es una cerradura: Python no lo impide.
- **Atributo de clase vs. de instancia:** el de clase es compartido por todos los objetos; el de instancia es propio de cada uno.
- **`__str__` vs. `__repr__`:** texto legible para el usuario vs. texto técnico para quien programa.
- **Herencia / `super()` / override:** una clase hija reutiliza al padre (`super()`) y puede reemplazar sus métodos (override).
- **Composición:** un objeto *tiene* otro objeto adentro y le delega trabajo.
- **Contrato:** lo que quien usa una clase espera que haga. Las clases hijas no deberían romperlo.

---

# Encuentro 2 · ¿Dónde vive la regla?

**Pregunta del día:** ¿dónde vive la regla de tu servicio, y quién puede saltársela?

También puedes ejecutar todo en el navegador, sin instalar Python: https://live.maikoldiaz.dev/material/py-02/

| Archivo | Qué es |
|---|---|
| `inventario_hueco.py` | El Producto del encuentro 1. ¿Qué pasa con el último ajuste? |
| `inventario_property.py` | La regla dentro del objeto con `@property`; atributos de clase e instancia; `__str__` y `__repr__` |
| `estrategias.py` | Herencia con `super()` y override; dos estrategias de precio por composición |
| `taller_practica.py` | Práctica: los talleres de la Casa de la Cultura |
| `taller_funcion.py` | La misma práctica con funciones y un diccionario |
| `modelo_plantilla.py` | Punto de partida para el `src/modelo.py` de tu repositorio |

```bash
python3 inventario_hueco.py
python3 inventario_property.py
python3 estrategias.py
python3 taller_practica.py
python3 taller_funcion.py
```

## Práctica: los talleres de la Casa de la Cultura

**Regla:** un taller nunca tiene más inscritos que cupos.

1. **Predecir.** Lee `taller_practica.py` y escribe qué imprimirá cada inscripción. Ejecuta y compara.
2. **Estado válido e inválido.** Al final, el cupo pasa a 5 (válido) y luego a 1 con 3 inscritos (inválido). ¿Qué pasó? Protege el cupo con una `@property` y vuelve a ejecutar. Cuidado con el orden en `__init__`.
3. **¿Clase o función?** Ejecuta `taller_funcion.py`. ¿Qué gana y qué pierde cada versión? ¿Cuál protege mejor la regla y cuál es más simple?

**Reto:** un taller con lista de espera. ¿Heredando de `Taller` o con composición? ¿Qué le pasaría a quien espera que `inscribir` rechace cuando no hay cupo?

## Para tu proyecto: tu repositorio

1. En https://github.com/new: nombre de tu servicio, **Public**, ✔ *Add a README file* → *Create repository*.
2. *Add file → Create new file* → `src/modelo.py` → pega tu modelo → *Commit changes*.
3. Copia en tu `README.md` la ficha de [`plantilla-proyecto/README.md`](../../plantilla-proyecto/README.md) con lo del encuentro 1.

Tu `modelo.py` lleva el brief en el docstring (actor, operación, recursos, regla, exclusiones, primer flujo), una entidad que protege su regla, un caso que se acepta, uno que se rechaza y por qué elegiste clase o función.

**Para pensar antes del próximo encuentro:** ¿qué caso, si fallara sin que nadie se diera cuenta, haría más daño? El lunes esos casos se vuelven pruebas en tu repositorio.

## Solución de referencia

[`solucion/taller_solucion.py`](solucion/taller_solucion.py): el taller con la regla dentro del objeto. No acepta inscripciones repetidas ni sin cupo, y no deja bajar el cupo por debajo de los inscritos. Ejecútalo y compara cada línea de la salida con lo que hace el tuyo.
