import pytest
from producto import Producto


@pytest.fixture(scope="module")
def cafe():
    return Producto("cafe-500g", "Café de Santa Elena 500 g", 10)


def test_salida(cafe):
    assert cafe.registrar_salida(3) == 7


def test_inventario_inicial(cafe):
    assert cafe.existencias == 10
