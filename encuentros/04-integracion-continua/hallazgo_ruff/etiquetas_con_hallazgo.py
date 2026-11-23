import os
from unidecode import unidecode


def etiqueta(producto):
    nombre = unidecode(producto.nombre).lower()
    codigo = producto.sku.upper()
    return f"{producto.sku}-{nombre}"
