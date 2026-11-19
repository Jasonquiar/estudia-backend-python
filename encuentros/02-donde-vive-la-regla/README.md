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
