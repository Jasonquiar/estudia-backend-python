"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   Dos pruebas que, cada una sola, están bien… pero juntas una falla.
   El culpable es scope="module": las dos comparten EL MISMO café.
   Este es el "quinto fallo" que el README dice que se descubre en clase.

🏪 Analogía:
   Dos personas hacen inventario usando la MISMA caja. La primera saca 3 cafés
   para su prueba y no los devuelve. La segunda abre la caja esperando 10… y hay 7.

▶️ Salidas reales:
   python -m pytest test_orden.py -v
     → test_salida PASSED
     → test_inventario_inicial FAILED   (AssertionError: assert 7 == 10)
   python -m pytest test_orden.py::test_salida -v              → 1 passed
   python -m pytest test_orden.py::test_inventario_inicial -v  → 1 passed  ⚠️ ¡sola sí pasa!
"""
import pytest
from producto import Producto


@pytest.fixture(scope="module")
def cafe():
    return Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    # 📝 scope="module" → se crea UNA sola vez para todo el archivo y se REUSA.
    #    (En test_caja.py el scope era el de por defecto, "function": uno nuevo por prueba.)
    #    Aquí no hay yield: con return también funciona, solo que no hay "después".


def test_salida(cafe):
    assert cafe.registrar_salida(3) == 7
    # 📝 Corre primero: 10 - 3 = 7 ✅. Pero deja el café compartido en 7.


def test_inventario_inicial(cafe):
    assert cafe.existencias == 10
    # 📝 Recibe el MISMO objeto, que ya quedó en 7 → assert 7 == 10 ❌
    #    Sola (::test_inventario_inicial) pasa, porque nadie descontó antes.
    #    ⚠️ Una prueba cuyo resultado depende del ORDEN o de cuáles corres es una
    #    prueba frágil: no puedes confiar ni en su verde ni en su rojo.
    #
    # 📝 Cómo se arregla (idea): que cada prueba reciba su propio café
    #    (quitar scope="module"). Usa scope más amplio solo para cosas que
    #    las pruebas NO modifican (por ejemplo, una conexión de solo lectura).

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué test_inventario_inicial falla con el archivo completo pero pasa sola?
# 2. ¿Qué cambia entre scope="function" (por defecto) y scope="module"?
# 3. ¿Cuándo sí tendría sentido compartir una fixture entre pruebas?
# 4. El README pide "escribe su alcance" para la fixture de tu proyecto: ¿cuál pondrías y por qué?
