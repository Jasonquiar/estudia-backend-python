"""
📝 MIS NOTAS (Encuentro 4 · Cobertura y aserciones · 23 nov 2026)

🎯 Idea central:
   Siete pruebas que SÍ afirman resultados del negocio. Tienen menos cobertura
   que test_recorre_todo.py (94 % vs. 100 %), pero matan a los dos mutantes.
   👉 Una prueba vale por lo que COMPRUEBA, no por las líneas que recorre.

▶️ python -m pytest tests/test_con_aserciones.py -v --cov=producto --cov-branch --cov-report=term-missing
     7 passed
     src/producto.py   Stmts 29  Miss 2  Branch 6  BrPart 0  Cover 94%   Missing 52, 55
     (52 y 55 = el return de __repr__ y de __str__: ninguna prueba los llama)
   python cazar_mutantes.py tests/test_con_aserciones.py
     Producto original: pruebas pasan
     mutante_1: MUERE
     mutante_2: MUERE
"""
import pytest
from producto import MovimientoInvalido, Producto


@pytest.fixture
def cafe():
    return Producto("cafe-500g", "Café de Santa Elena 500 g", 10)


def test_salida_descuenta(cafe):
    assert cafe.registrar_salida(3) == 7
    assert cafe.existencias == 7
    # 📝 🧟 Esta es la que mata a mutante_1 (el que no descuenta): esperaba 7 y recibe 10.


def test_salida_mayor_a_las_existencias(cafe):
    with pytest.raises(MovimientoInvalido, match="Stock insuficiente"):
        cafe.registrar_salida(11)


def test_cantidad_no_positiva(cafe):
    with pytest.raises(ValueError, match="Debe ser positiva"):
        cafe.registrar_salida(0)


def test_existencias_negativas():
    with pytest.raises(MovimientoInvalido, match="inválidas"):
        Producto("panela-1kg", "Panela de Barbosa 1 kg", -1)
    # 📝 Es la prueba que te tocaba escribir en el Encuentro 3 (test_turno_rechazo.py).


@pytest.mark.parametrize("existencias, esperado", [(2, True), (3, True), (4, False)])
def test_alerta_en_el_limite(existencias, esperado):
    panela = Producto("panela-1kg", "Panela de Barbosa 1 kg", existencias)
    assert panela.necesita_pedido() is esperado
    # 📝 🧟 El caso (3, True) mata a mutante_2: con "<", 3 < 3 es False.
    #    💡 (2, True) y (4, False) solos NO lo matarían: el mutante da lo mismo para 2 y para 4.
    #    Por eso se prueba justo EN el límite.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Cuál de estas pruebas mata a mutante_1? ¿Cuál a mutante_2?
# 2. Si borraras el caso (3, True) del parametrize, ¿qué mutante sobreviviría?
# 3. ¿Vale la pena subir al 100 % probando __repr__ y __str__? ¿Qué regla de negocio protegerías?
