> **📝 MIS NOTAS** · Encuentro 1 · Reglas de un servicio · 11 nov 2026
> Este bloque lo escribí yo para estudiar. Debajo de la línea está el material original del profesor, sin cambios.

## 📝 ¿De qué trata este curso? (explicado para alguien nuevo)

Cuando usas una app (pedir un domicilio, reservar una cita, comprar en línea) ves botones y pantallas. Eso es el **frontend**. Detrás hay un programa que recibe tus pedidos, decide si se pueden hacer y guarda la información. Eso es el **backend**, y es lo que aprendemos a construir en este curso, usando **Python**.

🏪 **Analogía:** el frontend es el mostrador de una tienda; el backend es la bodega con su bodeguero. Tú pides en el mostrador, pero quien revisa si hay producto, lo anota en el cuaderno y dice "sí" o "no" es el bodeguero.

Al final del curso cada persona tiene **su propio proyecto**: una API pequeña (un programa al que otras apps le hacen pedidos) que:

1. **Cumple reglas de negocio:** no deja hacer cosas que el negocio no permite *(Encuentros 1 y 2)*.
2. **Tiene pruebas automáticas:** código que revisa que esas reglas funcionen *(Encuentro 3)*.
3. **Se revisa solo cada vez que subes cambios**, con integración continua *(Encuentro 4)*.
4. **Guarda los datos** en una base de datos (MongoDB) y está **ordenado en capas** que puedes explicar.

## 📝 ¿Qué enseña este Encuentro 1?

**La pregunta del día:** *¿qué debe impedir un servicio backend, y cómo demostramos que lo impide?*

Un backend no es solo "hacer la cuenta". También debe **decir que no** cuando algo no tiene sentido. Hay dos tipos de "no":

| Tipo de rechazo | Qué significa | Ejemplo | En Python |
|---|---|---|---|
| ❌ **Dato inválido** | La solicitud está mal escrita y no tiene sentido. | Sacar **-3** cafés · reservar de **21 a 20** | `ValueError` |
| ❌ **Regla de negocio** | La solicitud está bien escrita, pero el negocio no la permite. | Sacar 6 cafés cuando solo hay **4** · reservar una hora **ya ocupada** | Una excepción propia: `MovimientoInvalido`, `ReservaRechazada` |

Tres ideas para llevarse:

- 🔮 **Predecir antes de ejecutar.** Escribe qué crees que va a imprimir el programa *antes* de correrlo. Si te equivocas, encontraste algo que aún no entiendes.
- 👮 **La regla vive en un solo lugar:** dentro de la operación que cambia el dato (por ejemplo, `Producto.registrar_salida`). Así nadie se la puede saltar.
- ⚠️ **"No dio error" no significa "está bien".** En `inventario_v1.py` el programa termina sin errores… y deja **-2 cafés** en la bodega.

## 📝 Ruta sugerida por los archivos

| Orden | Archivo | Qué vas a ver |
|---|---|---|
| 1 | `diagnostico.py` | Calentamiento: predecir la salida. Python deja el café en -2 sin quejarse. |
| 2 | `inventario_v1.py` | Un inventario **sin reglas**: la segunda tienda deja el stock en -2. |
| 3 | `inventario_v2.py` | El mismo inventario **con reglas**: rechaza por dato inválido y por regla de negocio. |
| 4 | `reservas_practica.py` | Práctica: aplicar el mismo patrón a las reservas de una sala. |

Cada archivo `.py` tiene comentarios `# 📝` con la explicación, la salida esperada y preguntas de repaso al final.

## 📝 Palabras clave

- **Servicio / backend:** el programa "de atrás" que recibe pedidos, aplica reglas y guarda datos.
- **Regla de negocio:** algo que el servicio *nunca debe permitir* o *siempre debe cumplir* (ej.: "el stock nunca queda negativo").
- **Excepción (`raise`):** la forma en que Python dice "me detengo, esto no se puede". Se atrapa con `try / except`.
- **Entidad:** una clase que guarda sus datos *y* las reglas que los protegen (ej.: `Producto`, `Sala`).

---

# Encuentro 1 · Reglas de un servicio

**Pregunta del día:** ¿qué debe impedir un servicio backend, y cómo demostramos que lo impide?

| Archivo | Qué es |
|---|---|
| `diagnostico.py` | Calentamiento: predice la salida antes de ejecutar |
| `inventario_v1.py` | Un inventario que registra salidas… ¿qué podría salir mal? |
| `inventario_v2.py` | Una entidad con una operación que **rechaza** un cambio inválido |
| `reservas_practica.py` | Práctica: completa `reservar()` |

```bash
python3 diagnostico.py
python3 inventario_v1.py
python3 inventario_v2.py
python3 reservas_practica.py
```

## Práctica: reservas de una sala de ensayo

Sala de ensayo de una casa de la cultura. Ya hay una reserva de **18 a 19**. Llegan dos solicitudes: **A)** 19 a 20 · **B)** 18 a 20.

1. Para A y B escribe: **entrada · resultado esperado (acepta/rechaza) · motivo**.
2. Completa los `TODO` de `reservar()` en `reservas_practica.py`.
3. **Antes de ejecutar**, escribe qué esperas que imprima. Ejecuta y compara.

**Reto:** agrega el caso C) 21 a 20. ¿Se rechaza por una regla de negocio o por un dato inválido? ¿Por qué 19–20 **no** choca con 18–19?

## Para tu proyecto

En la ficha de tu proyecto, deja escritas:
- 2 necesidades (qué hay que registrar, consultar o modificar, y quién lo usa),
- 1 regla de negocio (algo que el servicio nunca debe permitir o siempre debe cumplir),
- 1 caso que se acepta y 1 caso que se rechaza.

**Para pensar antes del próximo encuentro:** ¿tu regla vive mejor en una función o en un método de una clase? Trae una razón.
