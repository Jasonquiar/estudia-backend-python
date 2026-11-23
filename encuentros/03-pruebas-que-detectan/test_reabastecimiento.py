from unittest.mock import Mock
from urllib.error import URLError
import pytest
from producto import Producto
import reabastecimiento
from reabastecimiento import ProveedorHTTP, Reabastecimiento


@pytest.fixture
def proveedor():
    return Mock(spec=ProveedorHTTP)


def test_pide_con_poco_stock(proveedor):
    proveedor.pedir.return_value = "MED-2048"
    cafe = Producto("cafe-500g", "Café de Santa Elena", 2)
    assert Reabastecimiento(proveedor).revisar(cafe) == "MED-2048"
    proveedor.pedir.assert_called_once_with("cafe-500g", 12)


def test_no_pide_con_stock(proveedor):
    cafe = Producto("cafe-500g", "Café de Santa Elena", 10)
    assert Reabastecimiento(proveedor).revisar(cafe) is None
    proveedor.pedir.assert_not_called()


def test_adaptador_sin_red_queda_pendiente(monkeypatch):
    def sin_red(*args, **kwargs):
        raise URLError("Sin conexión")
    monkeypatch.setattr(reabastecimiento, "urlopen", sin_red)
    cafe = Producto("cafe-500g", "Café de Santa Elena", 2)
    assert Reabastecimiento(ProveedorHTTP()).revisar(cafe) == "pendiente"


@pytest.mark.integracion
@pytest.mark.skip(reason="Requiere URL real, autorización y red del proveedor")
def test_proveedor_real():
    orden = ProveedorHTTP().pedir("cafe-500g", 12)
    assert isinstance(orden, str) and orden
