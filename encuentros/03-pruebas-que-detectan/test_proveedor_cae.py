"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   🫵 Tu turno. Probar el "camino triste": el proveedor se cae (TimeoutError)
   y el servicio, en vez de romperse, devuelve "pendiente".

🎭 Herramienta nueva: side_effect
   - return_value = "cuando te llamen, DEVUELVE esto".
   - side_effect  = "cuando te llamen, HAZ esto". Si le das una excepción,
     el mock la LANZA (finge que el proveedor se cayó).

⚠️ OJO: las notas no la resuelven: la práctica es mía. Solo dejo pistas.

▶️ python -m pytest test_proveedor_cae.py -v
   Ahora: FAILED (Failed: Completa esta prueba). Cuando la escribas: PASSED.
"""
from unittest.mock import Mock
import pytest
from producto import Producto
from reabastecimiento import ProveedorHTTP, Reabastecimiento


def test_proveedor_cae():
    proveedor = Mock(spec=ProveedorHTTP)
    panela = Producto("panela-1kg", "Panela de Barbosa 1 kg", 2)
    # 📝 2 unidades → necesita_pedido() es True → revisar() SÍ va a llamar al proveedor.
    #    (Si tuviera 10, nunca llamaría y la prueba no probaría la caída.)
    # 1. Haz que proveedor.pedir falle con TimeoutError (side_effect).
    # 2. Comprueba que revisar(panela) devuelve "pendiente".
    pytest.fail("Completa esta prueba")
    # 📝 Borra el pytest.fail cuando escribas tus líneas.
    #
    # 📝 Pistas (no es la solución):
    #    - Mira test_pide_con_poco_stock: allá se configura proveedor.pedir.return_value.
    #      Aquí se configura el otro atributo, side_effect, con la excepción.
    #    - Para el paso 2, crea el servicio inyectando el mock, como en test_reabastecimiento.py.
    #    - Extra: ¿también deberías comprobar que el mock SÍ fue llamado?

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Qué diferencia hay entre return_value y side_effect?
# 2. ¿Por qué el producto de esta prueba tiene 2 unidades y no 10?
# 3. Si borras TimeoutError del except en reabastecimiento.py, ¿tu prueba falla? (¡pruébalo y restaura!)
