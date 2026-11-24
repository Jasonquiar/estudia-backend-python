"""Etiqueta legible para el estante: sin tildes ni espacios."""
# 📝 MIS NOTAS (Encuentro 4 · Integración continua · 23 nov 2026)
#
# 🎯 Idea central:
#    Un módulo NUEVO que existe para enseñar una cosa: depende de una librería
#    EXTERNA (unidecode) que no viene con Python. Si no está en requirements.txt,
#    en el entorno limpio de GitHub este import falla.
#
# 🔗 Lo usa tests/test_etiquetas.py.
#
# 📋 Ejemplos:
#    slug("  Café de Santa Elena ")  → "cafe-de-santa-elena"
#    etiqueta(Producto("panela-1kg", "Panela de Barbosa 1 kg", 8))
#                                    → "panela-1kg-panela-de-barbosa-1-kg"
from unidecode import unidecode
# 📝 ⭐ La línea que rompe el entorno limpio si falta "unidecode" en requirements.txt.


def slug(nombre):
    texto = unidecode(nombre).lower().strip()
    # 📝 unidecode quita tildes ("Café" → "Cafe"), lower pasa a minúsculas,
    #    strip quita los espacios de los bordes.
    return "-".join(texto.split())
    # 📝 split() parte por espacios (y se salta los repetidos); "-".join los une con guiones.


def etiqueta(producto):
    return f"{producto.sku}-{slug(producto.nombre)}"

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué este archivo es el que hace fallar la CI si requirements.txt solo dice "pytest"?
# 2. ¿Qué devuelve slug("Ñame de Urabá")? Predice y luego compruébalo en la terminal.
