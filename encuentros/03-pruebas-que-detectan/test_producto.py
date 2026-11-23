import pytest
from producto import MovimientoInvalido, Producto


@pytest.fixture
def cafe():
    print("Preparar café con 10 unidades")
    yield Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    print("Terminar el caso del café")


def test_salida_valida(cafe):
    # Arrange: la fixture entrega el estado inicial.
    restantes = cafe.registrar_salida(3)  # Act
    assert restantes == 7  # Assert
    assert cafe.existencias == 7


def test_salida_rechazada(cafe):
    with pytest.raises(MovimientoInvalido, match="Stock insuficiente"):
        cafe.registrar_salida(11)
    assert cafe.existencias == 10


def test_cantidad_cero(cafe):
    with pytest.raises(ValueError, match="Debe ser positiva"):
        cafe.registrar_salida(0)
    assert cafe.existencias == 10


@pytest.mark.parametrize("existencias, esperado", [(3, True), (4, False)])
def test_alerta(existencias, esperado):
    panela = Producto("panela-1kg", "Panela de Barbosa 1 kg", existencias)
    assert panela.necesita_pedido() is esperado
