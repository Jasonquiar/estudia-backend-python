import pytest
from producto import Producto


@pytest.fixture
def panela():
    print("Abrir caja de panela")
    yield Producto("panela-1kg", "Panela de Barbosa 1 kg", 5)
    print("Cerrar caja de panela")


def test_salida_de_dos(panela):
    assert panela.registrar_salida(2) == 3


def test_salida_total(panela):
    assert panela.registrar_salida(5) == 0


def test_sin_alerta_con_cinco(panela):
    assert panela.necesita_pedido() is False


def test_alerta_con_dos():
    sal = Producto("sal-1kg", "Sal marina 1 kg", 2)
    assert sal.necesita_pedido() is True


def test_nombre(panela):
    assert str(panela) == "Panela de Barbosa 1 kg: 5 unidades"
