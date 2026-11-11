"""E01 · Diagnóstico de Python (predicción antes de ejecutar)."""


def total_disponible(items):
    total = 0
    for nombre, cantidad in items.items():
        if cantidad > 0:
            total += cantidad
    return total


bodega = {"arepas": 12, "panela": 0, "cafe": 5}
bodega["cafe"] -= 7
print(total_disponible(bodega), bodega["cafe"])

# Pregunta 2 (chat): ¿qué pasa si descomentas la línea siguiente? ¿En qué línea lo dice el traceback?
# bodega["yuca"] -= 1
