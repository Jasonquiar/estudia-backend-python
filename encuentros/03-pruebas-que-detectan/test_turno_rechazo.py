import pytest
from producto import MovimientoInvalido, Producto


def test_existencias_negativas():
    # Un producto no puede nacer con existencias negativas.
    # Prepara el caso, actúa y afirma el rechazo con pytest.raises(..., match=...).
    pytest.fail("Escribe esta prueba")
