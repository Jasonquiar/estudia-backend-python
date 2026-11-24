"""
📝 MIS NOTAS (Encuentro 4 · Práctica: una función con muchas ramas · 23 nov 2026)

🎯 Idea central:
   Las 9 pruebas que ya existen (7 funciones; tramos_de_distancia cuenta como 3).
   Todas pasan, pero dejan reglas sin ejecutar. Tu trabajo: agregar las que faltan.

▶️ python -m pytest -v                                               → 9 passed
   python -m pytest --cov=tarifa --cov-branch --cov-report=term-missing
     src/tarifa.py   Stmts 36  Miss 8  Branch 32  BrPart 7  Cover 75%
     (la columna Missing te dice QUÉ líneas de tarifa.py no se ejecutan: léela en tu terminal)

🔎 Reglas que ninguna prueba ejecuta todavía (pistas, sin los números esperados):
   - distancia de MÁS de 10 km              - comunas Santa Elena y Belén
   - lluvia (llueve=True)                   - hora de la noche (22 h a 6 h)
   - cliente "empresa" (cerca y lejos)      - cliente "nuevo" a más de 2 km

⚠️ OJO: las notas no la resuelven: la práctica es mía. Calcula cada esperado A MANO
   con las reglas del encabezado de src/tarifa.py.
"""
import pytest
from tarifa import FueraDeCobertura, calcular_tarifa


def test_distancia_no_positiva():
    with pytest.raises(ValueError, match="Debe ser positiva"):
        calcular_tarifa(0, "Robledo", 10, "regular")


def test_fuera_de_cobertura():
    with pytest.raises(FueraDeCobertura, match="fuera de cobertura"):
        calcular_tarifa(26, "Robledo", 10, "regular")
    # 📝 26 porque es el primer entero FUERA del límite (25). ¿Y 25 justo? Debe atenderse.


@pytest.mark.parametrize("distancia, esperado", [(1.5, 4000), (4, 6000), (8, 9000)])
def test_tramos_de_distancia(distancia, esperado):
    assert calcular_tarifa(distancia, "Robledo", 10, "regular") == esperado
    # 📝 "Robledo", 10 h, "regular": la combinación NEUTRA (sin recargos ni descuentos).
    #    Así cada prueba aísla UNA regla: aquí solo cambia la distancia.
    #    💡 Ojo: 1,5 / 4 / 8 están en la MITAD de cada tramo. Los bordes (2, 5, 10) no se prueban.


def test_recargo_el_poblado():
    assert calcular_tarifa(3, "El Poblado", 10, "regular") == 7500


def test_hora_pico_del_almuerzo():
    assert calcular_tarifa(3, "Robledo", 12, "regular") == 6600
    # 📝 6.000 × 1,10 = 6.600. Solo cambia la hora (12 h = pico del almuerzo).


def test_cliente_frecuente():
    assert calcular_tarifa(3, "Robledo", 10, "frecuente") == 5400
    # 📝 6.000 × 0,90 = 5.400.


def test_cliente_nuevo_cerca_no_paga():
    assert calcular_tarifa(1.5, "Robledo", 10, "nuevo") == 0

# 📝 🫵 Aquí abajo van tus pruebas nuevas (una por regla, con nombre que diga el caso).

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué casi todas las pruebas usan "Robledo", 10 h y "regular"?
# 2. ¿Qué prueba agregarías para el borde exacto de 2 km? ¿Y para 25 km?
# 3. Después de tu refactor, ¿cuál de estas pruebas te avisaría si rompiste el recargo de El Poblado?
