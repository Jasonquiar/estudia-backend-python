"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   🫵 PRÁCTICA EN SALA. Escribir dos pruebas del Taller:
   ✅ una inscripción que se acepta, y ❌ una que se rechaza porque no hay cupo.
   Después, correr el cazador de mutantes para ver si esas pruebas DETECTAN errores.

📋 Pasos (del README):
   1. Completar las dos pruebas → python -m pytest test_taller_practica.py -v
   2. Cazar → python cazar_mutantes.py   (¿cuáles mutantes sobreviven?)
   3. Escribir la prueba que mata al que sobrevivió y volver a cazar.
   📦 Entregable: cuántos mutantes sobrevivieron al principio y qué prueba lo mató.

⚠️ OJO: las notas no la resuelven: la práctica es mía. Solo dejo pistas.
"""
import pytest
from taller import InscripcionRechazada, Taller
# 📝 Con el cazador, conftest.py hace que "taller" sea un mutante en vez de taller.py.
#    Por eso tus pruebas no se cambian: el import es el mismo.


@pytest.fixture
def guitarra():
    return Taller("Guitarra en la Casa de la Cultura de Manrique", cupo=2)
    # 📝 Cada prueba recibe un taller NUEVO, vacío, con cupo 2.
    #    💡 Cupo 2 es pequeño a propósito: se llena con solo 2 inscripciones.


def test_inscripcion_valida(guitarra):
    pytest.fail("Completa esta prueba")
    # 📝 Pistas (no es la solución):
    #    - Act: inscribe a una persona.
    #    - Assert: ¿qué DEBE devolver según el caso (cupo 2, 1 inscrita)? Calcúlalo tú,
    #      no lo copies del código (¡acuérdate de test_eco.py!).
    #    - Assert extra: ¿la persona quedó en guitarra.inscritos?


def test_inscripcion_invalida(guitarra):
    pytest.fail("Completa esta prueba")
    # 📝 Pistas (no es la solución):
    #    - Arrange: llena el taller (¿cuántas personas hacen falta con cupo 2?).
    #    - Act + Assert: la siguiente inscripción, dentro de pytest.raises(..., match=...).
    #      El texto del mensaje está en taller.py.
    #    - Después del with: ¿cuántos inscritos debe haber? (el rechazo no cambia el estado)

# 📝 🧟 Pistas para el paso 3 (después de cazar):
#    - Con solo estas dos pruebas, ¿qué reglas de taller.py NO estás vigilando?
#      Repasa las 3 reglas en las notas de taller.py.
#    - Cada mutante que sobrevive rompe una regla que ninguna prueba revisa.
#      Escribe una prueba nueva (test_...) para esa regla.
#    - Recuerda: el cazador primero exige que TODAS tus pruebas pasen contra taller.py.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué la fixture usa cupo=2 y no cupo=30?
# 2. En la prueba inválida, ¿por qué vale la pena revisar len(guitarra.inscritos) después del rechazo?
# 3. Si un mutante sobrevive, ¿quiere decir que el código está bien? ¿Qué quiere decir?
