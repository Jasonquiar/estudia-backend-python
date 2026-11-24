"""E01 · Diagnóstico de Python (predicción antes de ejecutar)."""

"""
📝 MIS NOTAS (Encuentro 1 · Reglas de un servicio · 11 nov 2026)

🎯 Idea central:
   Antes de ejecutar, PREDICE la salida. Si tu predicción falla, ahí hay algo que
   todavía no entiendes del código (y ahí es donde se esconden los bugs).

🏪 Analogía:
   Un bodeguero hace el conteo del día. Si a la caja de café le sacan más de lo que
   había, en el cuaderno queda -2. El conteo de "lo que hay disponible" se salta
   esa caja negativa, así que el total parece normal y nadie se da cuenta.

🔗 Viene de / lleva a:
   ⬅️ Es el calentamiento: el primer archivo del encuentro.
   ➡️ Lleva a inventario_v1.py, donde el mismo problema (stock negativo) aparece
      en un "servicio" de inventario real.
"""


def total_disponible(items):
    # 📝 Suma SOLO las cantidades positivas del diccionario.
    #    .items() entrega pares (llave, valor) → ("arepas", 12), ("panela", 0)...
    #    `nombre` no se usa; solo importa `cantidad`.
    total = 0
    for nombre, cantidad in items.items():
        # 📝 El filtro: 0 y los negativos NO suman.
        #    ✅ 12 > 0 → suma   ❌ 0 > 0 es False → no suma   ❌ -2 > 0 → no suma
        if cantidad > 0:
            total += cantidad
    return total


bodega = {"arepas": 12, "panela": 0, "cafe": 5}
bodega["cafe"] -= 7
# 📝 Igual que bodega["cafe"] = bodega["cafe"] - 7 → 5 - 7 = -2.
#    Python NO protesta: no existe ninguna regla que impida el negativo.
#    Ahora la bodega es {"arepas": 12, "panela": 0, "cafe": -2}.
print(total_disponible(bodega), bodega["cafe"])
# 📝 → 12 -2
#    12 = solo arepas (panela es 0 y café es -2, ninguno suma).
#    -2 = el café quedó negativo. ⚠️ El total "se ve bien" y esconde el problema.

# Pregunta 2 (chat): ¿qué pasa si descomentas la línea siguiente? ¿En qué línea lo dice el traceback?
# bodega["yuca"] -= 1
# 📝 Respuesta: "yuca" NO es una llave del diccionario, así que no hay valor al
#    que restarle 1 → KeyError: 'yuca'.
#    El traceback señala la línea de bodega["yuca"] (en el archivo original del
#    profe era la línea 17; aquí cambió porque agregué notas).
#    💡 Diferencia con el café: con "cafe" Python SÍ deja quedar -2 (dato absurdo
#    pero sin error); con "yuca" Python sí se queja porque la llave no existe.
#    Python detecta errores de lenguaje, NO errores de negocio. Esos los ponemos nosotros.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Qué imprime el print y por qué el primer número es 12 y no 17 ni 10?
# 2. ¿Por qué bodega["cafe"] -= 7 no lanza error pero bodega["yuca"] -= 1 sí?
# 3. ¿Qué regla de negocio le falta a esta "bodega" para que el café nunca quede en -2?
# 4. ¿Qué tipo de error de Python sale con "yuca"? ¿Cómo lo encuentras en el traceback?
