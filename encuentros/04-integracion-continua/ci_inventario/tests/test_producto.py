"""
📝 MIS NOTAS (Encuentro 4 · Integración continua · 23 nov 2026)

🎯 Idea central:
   Las pruebas del Producto del Encuentro 3, ahora dentro de tests/.
   Son las mismas ideas: camino feliz, rechazos con raises + match y el borde con parametrize.

▶️ python -m pytest -v   (desde ci_inventario/)   → 7 passed
   5 de este archivo (test_alerta cuenta como 2) + 2 de test_etiquetas.py.
   🔎 Ese "7 passed" es lo que hay que buscar en el log de GitHub Actions.
"""
import pytest
from producto import MovimientoInvalido, Producto


@pytest.fixture
def cafe():
    return Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    # 📝 Fixture con return (sin yield): no hace falta "limpiar" nada al final.


def test_salida_valida(cafe):
    assert cafe.registrar_salida(3) == 7
    assert cafe.existencias == 7


def test_salida_rechazada(cafe):
    with pytest.raises(MovimientoInvalido, match="Stock insuficiente"):
        cafe.registrar_salida(11)
    assert cafe.existencias == 10
    # 📝 Después del rechazo el stock no cambia (fuera del with).


def test_cantidad_cero(cafe):
    with pytest.raises(ValueError, match="Debe ser positiva"):
        cafe.registrar_salida(0)


@pytest.mark.parametrize("existencias, esperado", [(3, True), (4, False)])
def test_alerta(existencias, esperado):
    panela = Producto("panela-1kg", "Panela de Barbosa 1 kg", existencias)
    assert panela.necesita_pedido() is esperado

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué pytest encuentra este archivo? (Pista: su nombre y testpaths en pytest.ini.)
# 2. Si en GitHub el log dijera "5 passed" en vez de "7 passed", ¿qué sospecharías?
