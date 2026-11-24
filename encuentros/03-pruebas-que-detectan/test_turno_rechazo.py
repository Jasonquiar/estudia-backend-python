"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   🫵 Tu turno. Probar OTRA regla del Producto: no puede NACER con existencias
   negativas. Esta regla vive en el setter (ver producto.py), y se activa en __init__.

⚠️ OJO: las notas no la resuelven: la práctica es mía. Solo dejo pistas.

▶️ python -m pytest test_turno_rechazo.py -v
   Ahora: FAILED (Failed: Escribe esta prueba). Cuando la escribas: PASSED.
"""
import pytest
from producto import MovimientoInvalido, Producto


def test_existencias_negativas():
    # Un producto no puede nacer con existencias negativas.
    # Prepara el caso, actúa y afirma el rechazo con pytest.raises(..., match=...).
    pytest.fail("Escribe esta prueba")
    # 📝 pytest.fail(...) hace fallar la prueba a propósito. Bórralo cuando escribas la tuya.
    #
    # 📝 Pistas (no es la solución):
    #    - Copia el patrón de test_salida_rechazada en test_producto.py.
    #    - Aquí el "Act" es CREAR el producto: esa línea tiene que ir DENTRO del with.
    #    - ¿Qué error lanza el setter y qué texto trae su mensaje? Míralo en producto.py.
    #    - Comprueba que tu prueba DETECTA: comenta temporalmente el if del setter
    #      en producto.py (las 2 líneas), corre la prueba (¿falla?) y restaura.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué aquí no hace falta un assert después del with para revisar el estado?
#    (Pista: si el producto no se pudo crear, ¿existe algún objeto que revisar?)
# 2. ¿Este rechazo es de regla de negocio o de dato inválido? ¿Qué error usa el código?
# 3. ¿Probarías también Producto(..., 0)? ¿Debe aceptarse o rechazarse según la regla?
