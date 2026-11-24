"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   Dos pruebas del MISMO caso ("vendo 3 de 10"). Las dos pasan con el código bueno.
   Pero solo una DETECTA el error de producto_con_defecto.py.
   Esta es la respuesta a la pregunta del día.

🏪 Analogía:
   🔁 test_eco = el arqueo que copia lo que dice el sistema: "el sistema dice 10,
      anoto 10". Nunca encuentra un faltante.
   🎯 test_resultado_del_caso = el arqueo que cuenta por su cuenta: "vendí 3 de 10,
      deben quedar 7". Si el sistema dice 10, ¡alarma!

▶️ Cómo correrlo:
   python -m pytest test_eco.py -v                     → 2 passed
   python -m pytest test_eco.py --producto-defecto -v  → 1 passed, 1 failed
"""
from producto import Producto
# 📝 Con --producto-defecto, conftest.py cambia qué archivo es "producto" (este import no cambia).


def test_eco():
    cafe = Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    assert cafe.registrar_salida(3) == cafe.existencias
    # 📝 🔁 PRUEBA ECO: compara lo que devuelve el código con… el mismo código.
    #    Código bueno:    7 == 7   → PASSED
    #    Con el defecto: 10 == 10  → PASSED  ⚠️ ¡no detecta nada!
    #    El "esperado" no salió del caso, salió del propio código.


def test_resultado_del_caso():
    cafe = Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    assert cafe.registrar_salida(3) == 7
    # 📝 🎯 PRUEBA DEL CASO: el 7 lo calculé YO a partir del negocio (10 - 3).
    #    Código bueno:     7 == 7  → PASSED
    #    Con el defecto:  10 == 7  → FAILED ✅ ¡lo atrapó!
    #    → AssertionError: assert 10 == 7

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué test_eco pasa incluso con el código roto?
# 2. ¿De dónde debe salir el valor "esperado" de una prueba: del código o del caso?
# 3. Escribe en una frase la diferencia entre una prueba que "repite" y una que "detecta".
