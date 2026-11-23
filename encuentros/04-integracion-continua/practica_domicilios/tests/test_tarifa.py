import pytest
from tarifa import FueraDeCobertura, calcular_tarifa


def test_distancia_no_positiva():
    with pytest.raises(ValueError, match="Debe ser positiva"):
        calcular_tarifa(0, "Robledo", 10, "regular")


def test_fuera_de_cobertura():
    with pytest.raises(FueraDeCobertura, match="fuera de cobertura"):
        calcular_tarifa(26, "Robledo", 10, "regular")


@pytest.mark.parametrize("distancia, esperado", [(1.5, 4000), (4, 6000), (8, 9000)])
def test_tramos_de_distancia(distancia, esperado):
    assert calcular_tarifa(distancia, "Robledo", 10, "regular") == esperado


def test_recargo_el_poblado():
    assert calcular_tarifa(3, "El Poblado", 10, "regular") == 7500


def test_hora_pico_del_almuerzo():
    assert calcular_tarifa(3, "Robledo", 12, "regular") == 6600


def test_cliente_frecuente():
    assert calcular_tarifa(3, "Robledo", 10, "frecuente") == 5400


def test_cliente_nuevo_cerca_no_paga():
    assert calcular_tarifa(1.5, "Robledo", 10, "nuevo") == 0
