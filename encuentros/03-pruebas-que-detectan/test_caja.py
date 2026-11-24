"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   🫵 Tu turno: predecir cuántas veces se imprime «Abrir caja de panela».
   Sirve para entender CUÁNDO se ejecuta una fixture: una vez por cada prueba
   que la PIDE como parámetro (con el scope por defecto, "function").

🏪 Analogía:
   Cada cliente que pide panela recibe una caja nueva y sellada con 5 unidades.
   Se abre, se usa y se cierra. El cliente que pide sal no abre caja de panela.

▶️ python -m pytest test_caja.py -v -s
   El -s le dice a pytest que muestre los print (sin -s se los guarda).

✍️ Escribe tu predicción ANTES de leer la respuesta al final del archivo.
"""
import pytest
from producto import Producto


@pytest.fixture
def panela():
    print("Abrir caja de panela")
    yield Producto("panela-1kg", "Panela de Barbosa 1 kg", 5)
    print("Cerrar caja de panela")
    # 📝 Antes del yield = "abrir"; después del yield = "cerrar" (cuando la prueba termina).


def test_salida_de_dos(panela):
    assert panela.registrar_salida(2) == 3
    # 📝 Pide la fixture → caja nueva con 5. 5 - 2 = 3.


def test_salida_total(panela):
    assert panela.registrar_salida(5) == 0
    # 📝 Pide la fixture → OTRA caja nueva con 5 (no la que quedó en 3). 5 - 5 = 0.
    #    💡 Si la caja fuera compartida, esta prueba fallaría. Compara con test_orden.py.


def test_sin_alerta_con_cinco(panela):
    assert panela.necesita_pedido() is False
    # 📝 Caja nueva con 5 → 5 <= 3 es False.


def test_alerta_con_dos():
    sal = Producto("sal-1kg", "Sal marina 1 kg", 2)
    assert sal.necesita_pedido() is True
    # 📝 ⚠️ NO pide la fixture "panela" (no tiene parámetro) → aquí no se abre caja.


def test_nombre(panela):
    assert str(panela) == "Panela de Barbosa 1 kg: 5 unidades"
    # 📝 Usa __str__. Caja nueva con 5.

# 📝 ✅ RESPUESTA (lee solo después de predecir):
#    «Abrir caja de panela» se imprime 4 veces: una por cada prueba que tiene el
#    parámetro panela (todas menos test_alerta_con_dos). Salida real con -v -s:
#      test_caja.py::test_salida_de_dos Abrir caja de panela
#      PASSEDCerrar caja de panela
#      ... (igual para test_salida_total y test_sin_alerta_con_cinco)
#      test_caja.py::test_alerta_con_dos PASSED          ← sin abrir caja
#      test_caja.py::test_nombre Abrir caja de panela
#      PASSEDCerrar caja de panela
#      5 passed

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Qué decide si una prueba usa la fixture: el nombre del archivo o el parámetro?
# 2. ¿Por qué test_salida_total recibe 5 unidades y no 3, si test_salida_de_dos ya sacó 2?
# 3. ¿Qué pasaría con el conteo si la fixture tuviera scope="module"?
