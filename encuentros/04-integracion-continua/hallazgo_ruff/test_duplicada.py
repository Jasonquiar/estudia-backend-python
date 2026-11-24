"""
📝 MIS NOTAS (Encuentro 4 · Tres herramientas, tres preguntas · 23 nov 2026)

🫵 Mira las dos funciones con calma antes de correr Ruff. ¿Qué tienen de raro?
⚠️ SPOILER al final del archivo.
"""
from producto import Producto


def test_salida_valida():
    cafe = Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    assert cafe.registrar_salida(3) == 7


def test_salida_valida():
    cafe = Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    assert cafe.registrar_salida(10) == 0




























# 📝 ⚠️ SPOILER ─────────────────────────────────────────────────────────────
#
# F811 Redefinition of unused `test_salida_valida` from line 10  → test_duplicada.py:15
#
# 🎯 Las dos funciones se llaman IGUAL. En Python, el segundo "def" reemplaza al primero
#    (como escribir dos veces x = ...: queda el último). pytest solo ve UNA prueba.
#    → La prueba de "sacar 3 de 10 deja 7" NUNCA corre, y nadie se entera:
#      la salida dice "1 passed" y todo se ve verde.
#
# 🔧 Corrección: darle a cada una un nombre propio que diga qué caso prueba, por ejemplo
#    test_salida_parcial (3 de 10 → 7) y test_salida_de_todo_el_stock (10 de 10 → 0).
#
# 💡 Este archivo no está pensado para correr con pytest aquí (no hay producto.py en esta
#    carpeta): es para que Ruff lo lea. Ruff no necesita ejecutar nada para encontrar el error.
#
# ❓ PREGUNTAS DE REPASO
# 1. Si corrieras este archivo con pytest, ¿cuántas pruebas reportaría? ¿Cuál se pierde?
# 2. ¿Por qué este error es más peligroso que un import sin usar?
