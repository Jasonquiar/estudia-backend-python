import pytest
from producto import MovimientoInvalido, Producto


@pytest.fixture
def cafe():
    return Producto("cafe-500g", "Café de Santa Elena 500 g", 10)


def test_salida_descuenta(cafe):
    assert cafe.registrar_salida(3) == 7
    assert cafe.existencias == 7


def test_salida_mayor_a_las_existencias(cafe):
    with pytest.raises(MovimientoInvalido, match="Stock insuficiente"):
        cafe.registrar_salida(11)


def test_cantidad_no_positiva(cafe):
    with pytest.raises(ValueError, match="Debe ser positiva"):
        cafe.registrar_salida(0)


def test_existencias_negativas():
    with pytest.raises(MovimientoInvalido, match="inválidas"):
        Producto("panela-1kg", "Panela de Barbosa 1 kg", -1)


@pytest.mark.parametrize("existencias, esperado", [(2, True), (3, True), (4, False)])
def test_alerta_en_el_limite(existencias, esperado):
    panela = Producto("panela-1kg", "Panela de Barbosa 1 kg", existencias)
    assert panela.necesita_pedido() is esperado
