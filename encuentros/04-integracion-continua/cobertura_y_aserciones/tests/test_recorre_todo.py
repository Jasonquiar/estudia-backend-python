import pytest
from producto import Producto


def test_recorre_todo():
    cafe = Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    cafe.registrar_salida(3)
    with pytest.raises(Exception):
        cafe.registrar_salida(0)
    with pytest.raises(Exception):
        cafe.registrar_salida(50)
    with pytest.raises(Exception):
        Producto("panela-1kg", "Panela de Barbosa 1 kg", -1)
    cafe.necesita_pedido()
    repr(cafe)
    str(cafe)
