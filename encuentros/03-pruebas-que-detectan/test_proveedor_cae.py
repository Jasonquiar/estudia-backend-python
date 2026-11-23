from unittest.mock import Mock
import pytest
from producto import Producto
from reabastecimiento import ProveedorHTTP, Reabastecimiento


def test_proveedor_cae():
    proveedor = Mock(spec=ProveedorHTTP)
    panela = Producto("panela-1kg", "Panela de Barbosa 1 kg", 2)
    # 1. Haz que proveedor.pedir falle con TimeoutError (side_effect).
    # 2. Comprueba que revisar(panela) devuelve "pendiente".
    pytest.fail("Completa esta prueba")
