from producto import Producto


def test_salida_valida():
    cafe = Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    assert cafe.registrar_salida(3) == 7


def test_salida_valida():
    cafe = Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    assert cafe.registrar_salida(10) == 0
