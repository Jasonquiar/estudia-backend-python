"""E01 · Demo v1: registra salidas de inventario SIN regla de negocio.

Antes de ejecutar: ¿qué imprime la segunda línea?
"""

inventario = {"cafe-500g": 10, "panela-1kg": 4}


def registrar_salida(inventario, sku, cantidad):
    inventario[sku] = inventario[sku] - cantidad
    return inventario[sku]


solicitudes = [
    ("Tienda Doña Rosa", "cafe-500g", 6),  # se espera ACEPTAR
    ("Tienda El Paisa", "cafe-500g", 6),   # se espera RECHAZAR: solo quedan 4
]

for tienda, sku, cantidad in solicitudes:
    quedan = registrar_salida(inventario, sku, cantidad)
    print(f"{tienda} retira {cantidad} de {sku} -> quedan {quedan}")
