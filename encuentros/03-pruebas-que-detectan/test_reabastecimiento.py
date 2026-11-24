"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   Probar el servicio Reabastecimiento SIN internet, de tres formas:
   1) 🎭 Mock del proveedor completo (pruebas 1 y 2).
   2) 🐒 monkeypatch de urlopen, para probar el adaptador real sin red (prueba 3).
   3) 🌐 Prueba de integración contra el proveedor real… omitida (prueba 4).

🏪 Analogía:
   Ensayo de teatro: en vez del proveedor de verdad, un actor (Mock) dice el
   libreto que le damos ("tu número de orden es MED-2048"). Al final le
   preguntamos al actor: "¿te llamaron? ¿una vez? ¿con qué palabras?".

▶️ python -m pytest test_reabastecimiento.py -v   → 3 passed, 1 skipped
"""
from unittest.mock import Mock
from urllib.error import URLError
import pytest
from producto import Producto
import reabastecimiento
from reabastecimiento import ProveedorHTTP, Reabastecimiento


@pytest.fixture
def proveedor():
    return Mock(spec=ProveedorHTTP)
    # 📝 Mock = objeto "doble" que finge ser un ProveedorHTTP.
    #    spec=ProveedorHTTP → solo acepta los métodos que el real tiene (pedir).
    #    Si escribes proveedor.pedri(...) (mal escrito), falla en vez de aceptarlo en silencio.


def test_pide_con_poco_stock(proveedor):
    proveedor.pedir.return_value = "MED-2048"
    # 📝 return_value → "cuando te llamen pedir(...), responde MED-2048".
    cafe = Producto("cafe-500g", "Café de Santa Elena", 2)
    # 📝 2 <= 3 → necesita pedido.
    assert Reabastecimiento(proveedor).revisar(cafe) == "MED-2048"
    # 📝 El servicio devuelve lo que respondió el proveedor.
    proveedor.pedir.assert_called_once_with("cafe-500g", 12)
    # 📝 Le pregunto al mock: ¿te llamaron UNA vez, con el sku y la cantidad 12?
    #    Esto prueba que el servicio pide lo CORRECTO, no solo que devuelve algo.


def test_no_pide_con_stock(proveedor):
    cafe = Producto("cafe-500g", "Café de Santa Elena", 10)
    # 📝 10 > 3 → no necesita pedido.
    assert Reabastecimiento(proveedor).revisar(cafe) is None
    proveedor.pedir.assert_not_called()
    # 📝 Y además: ¡no molestó al proveedor! (un pedido innecesario cuesta plata).


def test_adaptador_sin_red_queda_pendiente(monkeypatch):
    def sin_red(*args, **kwargs):
        raise URLError("Sin conexión")
    # 📝 Una función falsa que siempre "se queda sin internet".
    monkeypatch.setattr(reabastecimiento, "urlopen", sin_red)
    # 📝 🐒 monkeypatch reemplaza, SOLO durante esta prueba, el urlopen que usa
    #    reabastecimiento.py por sin_red. Al terminar la prueba lo deja como estaba.
    #    Aquí sí se usa el ProveedorHTTP REAL: se prueba que el adaptador + el
    #    servicio juntos reaccionan bien cuando no hay red.
    cafe = Producto("cafe-500g", "Café de Santa Elena", 2)
    assert Reabastecimiento(ProveedorHTTP()).revisar(cafe) == "pendiente"
    # 📝 URLError → el except de revisar() lo atrapa → "pendiente".


@pytest.mark.integracion
@pytest.mark.skip(reason="Requiere URL real, autorización y red del proveedor")
def test_proveedor_real():
    orden = ProveedorHTTP().pedir("cafe-500g", 12)
    assert isinstance(orden, str) and orden
    # 📝 🌐 PRUEBA DE INTEGRACIÓN: habla con el proveedor DE VERDAD.
    #    - @pytest.mark.integracion → etiqueta declarada en pytest.ini.
    #    - @pytest.mark.skip → no se ejecuta (aparece como SKIPPED).
    #    ⚠️ Los mocks prueban cómo reacciona MI código al contrato que SUPONGO
    #    ({"orden": ...}). Solo una prueba de integración comprueba que el
    #    proveedor real cumple ese contrato. No quitar el skip "solo para ver verde".

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Para qué sirve return_value? ¿Y assert_called_once_with?
# 2. ¿Qué gana test_no_pide_con_stock con la línea assert_not_called()?
# 3. ¿En qué se diferencia la prueba 3 (monkeypatch) de las pruebas 1 y 2 (Mock)?
# 4. Si el proveedor real cambia su respuesta a {"numero": ...}, ¿qué prueba lo detectaría?
