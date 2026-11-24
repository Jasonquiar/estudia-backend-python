"""
📝 MIS NOTAS (Encuentro 4 · Integración continua · 23 nov 2026)

🎯 Idea central:
   Las 2 pruebas que dependen de unidecode. Son las que fallan en un entorno
   limpio si requirements.txt está incompleto.

▶️ python -m pytest tests/test_etiquetas.py -v   → 2 passed
   En un venv que solo tiene pytest:
     E   ModuleNotFoundError: No module named 'unidecode'
     ERROR tests/test_etiquetas.py
     Interrupted: 1 error during collection
   💡 OJO: es un ERROR al RECOGER (importar) las pruebas, no un FAILED de una prueba.
      pytest no llega a correr NINGUNA, ni siquiera las de test_producto.py (código de salida 2).
"""
from etiquetas import etiqueta, slug
from producto import Producto
# 📝 Estos import funcionan porque pytest.ini dice pythonpath = src.


def test_slug_quita_tildes_y_espacios():
    assert slug("  Café de Santa Elena ") == "cafe-de-santa-elena"
    # 📝 El esperado sale del caso: espacios en los bordes, tilde y mayúsculas.


def test_etiqueta_une_sku_y_nombre():
    panela = Producto("panela-1kg", "Panela de Barbosa 1 kg", 8)
    assert etiqueta(panela) == "panela-1kg-panela-de-barbosa-1-kg"

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. Si falta unidecode, ¿por qué tampoco corren las pruebas de test_producto.py?
# 2. ¿Qué diferencia hay entre "1 error" y "1 failed" en la salida de pytest?
