"""
📝 MIS NOTAS (Encuentro 4 · Tres herramientas, tres preguntas · 23 nov 2026)

🫵 El "gemelo": repetir el ejercicio de hallazgo_ruff/ con datos nuevos.
   Encuentra a ojo los 3 defectos (son de los mismos tipos) y luego: ruff check .
⚠️ SPOILER al final del archivo.
"""
import sys


def alerta(producto):
    minimo = 3
    return producto.existencias <= producto.alerta_stock


def alerta(producto, margen=0):
    return producto.existencias <= producto.alerta_stock + margen




























# 📝 ⚠️ SPOILER ─────────────────────────────────────────────────────────────
#
# ▶️ ruff check .   (desde hallazgo_ruff_gemelo/)   → Found 3 errors.
#
# 1. F401 `sys` imported but unused  → línea 8. Se importa y no se usa.
#
# 2. F841 Local variable `minimo` is assigned to but never used  → línea 12.
#    🤔 ¿Qué pretendía el autor? Tal vez comparar contra minimo en vez de alerta_stock,
#       o es un resto de una versión vieja. Ruff no lo sabe: decide una persona.
#
# 3. F811 Redefinition of unused `alerta` from line 11  → línea 16.
#    La segunda alerta() reemplaza a la primera. Aquí no es una prueba que se pierde,
#    sino una FUNCIÓN: quien llame alerta(p) usa la versión con margen=0 (mismo resultado),
#    y la primera versión (con su "minimo") es código muerto.
#    🔧 Quedarse con UNA (la de margen, que cubre los dos casos) y borrar la otra.
#
# 🆚 Mismos códigos que en hallazgo_ruff/ (F401, F841, F811), en otro contexto:
#    por eso sirve para comprobar que aprendiste a reconocerlos, no a memorizarlos.
#
# ❓ PREGUNTAS DE REPASO
# 1. Después de corregir, ¿cuántas definiciones de alerta deberían quedar?
# 2. ¿Qué devuelve alerta(p, margen=2) para un producto con 5 existencias y alerta_stock 3?
