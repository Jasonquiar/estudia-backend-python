"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   El "kit básico" para probar una regla: una prueba de lo que se ACEPTA, pruebas
   de lo que se RECHAZA (y que el estado no cambió), y los BORDES con parametrize.

🧱 Arrange – Act – Assert (AAA):
   1. Arrange (preparar): crear el café con 10 unidades.
   2. Act (actuar):       registrar_salida(3).
   3. Assert (afirmar):   quedan 7.

🧰 Herramientas nuevas:
   - @pytest.fixture con yield → preparación reutilizable con "antes" y "después".
   - pytest.raises(Error, match="texto") → probar un rechazo y su motivo.
   - @pytest.mark.parametrize → la misma prueba con varios datos.

▶️ python -m pytest test_producto.py -v   → 5 passed  (test_alerta cuenta como 2)
   Con -s además ves los print de la fixture.
"""
import pytest
from producto import MovimientoInvalido, Producto


@pytest.fixture
def cafe():
    print("Preparar café con 10 unidades")
    yield Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    print("Terminar el caso del café")
    # 📝 FIXTURE con yield:
    #    - Lo de ANTES del yield se ejecuta antes de la prueba (preparar).
    #    - Lo que va en el yield es lo que recibe la prueba en su parámetro "cafe".
    #    - Lo de DESPUÉS del yield se ejecuta al terminar la prueba (limpiar/cerrar).
    #    💡 Por defecto se crea un café NUEVO para cada prueba: ninguna afecta a otra.


def test_salida_valida(cafe):
    # 📝 pytest ve el parámetro "cafe" y busca una fixture con ese nombre.
    # Arrange: la fixture entrega el estado inicial.
    restantes = cafe.registrar_salida(3)  # Act
    assert restantes == 7  # Assert
    assert cafe.existencias == 7
    # 📝 ✅ CAMINO FELIZ. Dos asserts: lo que DEVUELVE el método y cómo QUEDA el objeto.
    #    Si el método devolviera 7 pero no guardara el cambio, el segundo assert lo atrapa.


def test_salida_rechazada(cafe):
    with pytest.raises(MovimientoInvalido, match="Stock insuficiente"):
        cafe.registrar_salida(11)
    # 📝 ❌ RECHAZO DE NEGOCIO: pedir 11 cuando hay 10.
    #    pytest.raises → la prueba PASA solo si adentro se lanza ese error.
    #    match="..."   → y además el mensaje debe contener ese texto.
    #    💡 Sin match, podría pasar por el motivo equivocado (otro MovimientoInvalido).
    assert cafe.existencias == 10
    # 📝 Muy importante: después del rechazo, el stock NO debe haber cambiado.
    #    Esta línea va FUERA del with: dentro, nunca se ejecutaría (el error corta el bloque).


def test_cantidad_cero(cafe):
    with pytest.raises(ValueError, match="Debe ser positiva"):
        cafe.registrar_salida(0)
    assert cafe.existencias == 10
    # 📝 ❌ DATO INVÁLIDO (0 no es una cantidad): ValueError, no MovimientoInvalido.
    #    Es el mismo patrón de la prueba anterior con otro tipo de error.


@pytest.mark.parametrize("existencias, esperado", [(3, True), (4, False)])
def test_alerta(existencias, esperado):
    panela = Producto("panela-1kg", "Panela de Barbosa 1 kg", existencias)
    assert panela.necesita_pedido() is esperado
    # 📝 PARAMETRIZE: pytest corre esta prueba 2 veces, una por cada tupla:
    #    → test_alerta[3-True]   (3 <= 3 → True)
    #    → test_alerta[4-False]  (4 <= 3 → False)
    #    💡 Se eligen 3 y 4 porque son el BORDE: si alguien cambia <= por <, el caso 3 falla.
    #    "is" en vez de "==" exige que devuelva exactamente True/False.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Qué parte del código es Arrange, cuál Act y cuál Assert en test_salida_valida?
# 2. ¿Por qué assert cafe.existencias == 10 va fuera del bloque with?
# 3. ¿Qué pasaría si en test_salida_rechazada quitaras match=...? ¿Seguiría siendo útil?
# 4. Si alguien cambia "<=" por "<" en necesita_pedido, ¿cuál de los dos casos falla?
# 5. Con --producto-defecto, ¿cuál de estas pruebas falla? Predice y luego corre:
#    python -m pytest test_producto.py --producto-defecto -v
