from producto import Producto


def test_eco():
    cafe = Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    assert cafe.registrar_salida(3) == cafe.existencias


def test_resultado_del_caso():
    cafe = Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    assert cafe.registrar_salida(3) == 7
