"""
📝 MIS NOTAS (Encuentro 4 · Cobertura y aserciones · 23 nov 2026)

🎯 Idea central:
   UNA prueba que pasa por todo el código del Producto pero casi no comprueba
   resultados. Es la "trampa" de la cobertura: el reporte dice 100 %, y aun así
   no detecta ningún mutante.

🏪 Analogía: un vigilante que recorre TODOS los pasillos de la tienda… con los ojos cerrados.
   El registro dice "pasó por todo"; nadie dice que haya visto algo.

▶️ python -m pytest tests/test_recorre_todo.py -v --cov=producto --cov-branch --cov-report=term-missing
     1 passed
     src/producto.py      Stmts 29  Miss 0  Branch 6  BrPart 0  Cover 100%
   python cazar_mutantes.py tests/test_recorre_todo.py
     Producto original: pruebas pasan
     mutante_1: SOBREVIVE
     mutante_2: SOBREVIVE

🫵 Haz tú el mutante (README): en una copia de src/producto.py borra
   "self.existencias -= cantidad" → esta prueba sigue pasando (sobrevive).
   Cambia cafe.registrar_salida(3) por assert cafe.registrar_salida(3) == 7 → ahora falla (muere).
   Y después RESTAURA el original.
"""
import pytest
from producto import Producto


def test_recorre_todo():
    cafe = Producto("cafe-500g", "Café de Santa Elena 500 g", 10)
    cafe.registrar_salida(3)
    # 📝 ⚠️ Se ejecuta, pero no hay assert: si devolviera 10 (sin descontar), nadie se entera.
    with pytest.raises(Exception):
        cafe.registrar_salida(0)
    # 📝 ⚠️ pytest.raises(Exception) es DEMASIADO general: cualquier error lo satisface
    #    (incluso un TypeError por un error de programación). Y no tiene match=...
    #    🆚 Lo correcto: pytest.raises(ValueError, match="Debe ser positiva").
    with pytest.raises(Exception):
        cafe.registrar_salida(50)
    with pytest.raises(Exception):
        Producto("panela-1kg", "Panela de Barbosa 1 kg", -1)
    cafe.necesita_pedido()
    repr(cafe)
    str(cafe)
    # 📝 ⚠️ Se llaman y se descarta el resultado. Cuentan para la cobertura, no comprueban nada.
    #    Por eso mutante_2 (cambia <= por <) sobrevive: nadie mira qué devolvió necesita_pedido().

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Cómo puede una prueba dar 100 % de cobertura y no detectar ningún mutante?
# 2. ¿Qué pregunta responde la cobertura? ¿Qué pregunta NO responde?
# 3. ¿Qué tendrías que agregar a esta prueba para matar a mutante_1? ¿Y a mutante_2?
