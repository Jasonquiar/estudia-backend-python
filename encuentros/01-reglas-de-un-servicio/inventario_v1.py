"""E01 · Demo v1: registra salidas de inventario SIN regla de negocio.

Antes de ejecutar: ¿qué imprime la segunda línea?
"""
"""
📝 MIS NOTAS (Encuentro 1 · Reglas de un servicio · 11 nov 2026)

🎯 Idea central:
   Un servicio que hace la cuenta sin hacerse preguntas termina guardando datos
   imposibles, por ejemplo -2 cafés en la bodega.

🏪 Analogía:
   Una tienda sin portero ni bodeguero. Cualquiera entra, pide 6 cafés y alguien
   tacha 6 en el cuaderno, aunque en el estante solo queden 4. El cuaderno dice -2,
   pero en la vida real no existen los "cafés negativos".

🔗 Viene de / lleva a:
   ⬅️ Viene de diagnostico.py (calentamiento: predecir la salida antes de ejecutar).
   ➡️ Lleva a inventario_v2.py, donde la regla "nunca quedar con stock negativo"
      ya existe y RECHAZA la segunda solicitud.

🔮 Antes de ejecutar (eso pide el profe): ¿qué imprime la segunda línea?
   Escribe tu predicción y después compárala con la salida real que anoté abajo.
"""

inventario = {"cafe-500g": 10, "panela-1kg": 4}
# 📝 Un diccionario hace de "bodega": la llave es el SKU (código del producto)
#    y el valor es cuántas unidades hay. Al empezar: 10 cafés y 4 panelas.


def registrar_salida(inventario, sku, cantidad):
    # 📝 Solo resta y devuelve lo que queda. No pregunta nada antes.
    #    ❌ No revisa si HAY suficiente (no hay regla de negocio).
    #    ❌ No revisa si la cantidad tiene sentido (0, -3…): no valida el dato.
    #    Ejemplo → 4 cafés y piden 6 → 4 - 6 = -2, y lo guarda sin quejarse.
    inventario[sku] = inventario[sku] - cantidad
    return inventario[sku]


solicitudes = [
    ("Tienda Doña Rosa", "cafe-500g", 6),  # se espera ACEPTAR
    ("Tienda El Paisa", "cafe-500g", 6),   # se espera RECHAZAR: solo quedan 4
]
# 📝 Cada solicitud es una tupla (tienda, sku, cantidad).
#    Los comentarios del profe dicen lo que el NEGOCIO espera:
#    ✅ Doña Rosa: hay 10 y pide 6 → se acepta, quedan 4.
#    ❌ El Paisa: hay 4 y pide 6 → debería rechazarse... pero el código no lo sabe.

for tienda, sku, cantidad in solicitudes:
    # 📝 "Desempaqueta" cada tupla en tres variables y registra la salida.
    #    Fíjate que no hay if ni try/except: TODAS las solicitudes pasan.
    quedan = registrar_salida(inventario, sku, cantidad)
    print(f"{tienda} retira {cantidad} de {sku} -> quedan {quedan}")
    # 📝 → Tienda Doña Rosa retira 6 de cafe-500g -> quedan 4
    # 📝 → Tienda El Paisa retira 6 de cafe-500g -> quedan -2   ⚠️ ¡el bug!

# 📝 CONCLUSIÓN: el programa no "falla" (no sale ningún error), y eso es lo peligroso.
#    Lo que está mal es el DATO: -2 cafés. Un servicio backend debe IMPEDIR esto,
#    no solo hacer la resta. ¿Dónde se pone esa regla? → mira inventario_v2.py.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Qué imprime la segunda línea y por qué el programa no lanza ningún error?
# 2. ¿Qué regla de negocio falta en registrar_salida? Escríbela en una sola frase.
# 3. Si alguien llama registrar_salida(inventario, "cafe-500g", -3), ¿qué pasa con
#    las existencias? ¿Eso es romper una regla de negocio o mandar un dato inválido?
# 4. Si quisieras agregar la regla, ¿la pondrías en el for de abajo o dentro de
#    registrar_salida? ¿Por qué? (Pista: ¿quién más podría llamar a la función?)
