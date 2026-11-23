import pytest
from taller import InscripcionRechazada, Taller


@pytest.fixture
def guitarra():
    return Taller("Guitarra en la Casa de la Cultura de Manrique", cupo=2)


def test_inscripcion_valida(guitarra):
    pytest.fail("Completa esta prueba")


def test_inscripcion_invalida(guitarra):
    pytest.fail("Completa esta prueba")
