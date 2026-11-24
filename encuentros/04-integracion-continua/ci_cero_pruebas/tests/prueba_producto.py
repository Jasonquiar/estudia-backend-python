"""
📝 MIS NOTAS (Encuentro 4 · Verde con cero pruebas · 23 nov 2026)

🎯 Idea central:
   Las pruebas están BIEN escritas (son las de ci_inventario/tests/test_producto.py).
   El problema es el NOMBRE del archivo: pytest solo recoge archivos test_*.py.
   "prueba_producto.py" no empieza por "test_" → pytest ni lo abre.

▶️ python -m pytest -v; echo "código de salida: $?"
     collected 0 items
     ============ no tests ran in 0.01s ============
     código de salida: 5
   python -m pytest -v | tee salida_pytest.txt; echo "código de salida: $?"
     (la misma salida)
     código de salida: 0     🤥 el de tee

🔧 Después de renombrar:
   mv tests/prueba_producto.py tests/test_producto.py
   python -m pytest -v | tee salida_pytest.txt   → 5 passed
   (y vuelve a dejarlo como estaba si quieres repetir el ejercicio:
    mv tests/test_producto.py tests/prueba_producto.py)

⚠️ Las funciones SÍ empiezan por test_: no basta. pytest primero elige ARCHIVOS y luego funciones.
"""
import pytest
from producto import MovimientoInvalido, Producto


@pytest.fixture
def cafe():
    return Producto("cafe-500g", "Café de Santa Elena 500 g", 10)


def test_salida_valida(cafe):
    assert cafe.registrar_salida(3) == 7
    assert cafe.existencias == 7


def test_salida_rechazada(cafe):
    with pytest.raises(MovimientoInvalido, match="Stock insuficiente"):
        cafe.registrar_salida(11)
    assert cafe.existencias == 10


def test_cantidad_cero(cafe):
    with pytest.raises(ValueError, match="Debe ser positiva"):
        cafe.registrar_salida(0)


@pytest.mark.parametrize("existencias, esperado", [(3, True), (4, False)])
def test_alerta(existencias, esperado):
    panela = Producto("panela-1kg", "Panela de Barbosa 1 kg", existencias)
    assert panela.necesita_pedido() is esperado

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué pytest no corre estas pruebas si las funciones sí se llaman test_...?
# 2. Escribe las DOS correcciones exactas (archivo y workflow). ¿Qué arregla cada una?
# 3. En el log de GitHub, ¿qué línea buscarías para saber si el verde es real?
