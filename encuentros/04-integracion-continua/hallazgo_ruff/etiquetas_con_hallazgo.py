"""
📝 MIS NOTAS (Encuentro 4 · Tres herramientas, tres preguntas · 23 nov 2026)

🫵 Sé el linter: en 2 minutos, encuentra a ojo los defectos de este archivo y de
   test_duplicada.py (3 en total) y anótalos con su línea. Después: ruff check .

⚠️ SPOILER al final del archivo. No bajes hasta haberlo intentado.
"""
import os
from unidecode import unidecode


def etiqueta(producto):
    nombre = unidecode(producto.nombre).lower()
    codigo = producto.sku.upper()
    return f"{producto.sku}-{nombre}"




























# 📝 ⚠️ SPOILER ─────────────────────────────────────────────────────────────
#
# ▶️ ruff check .   (desde hallazgo_ruff/)   → Found 3 errors.  (código de salida 1)
#
# 1. F401 `os` imported but unused  → etiquetas_con_hallazgo.py:9
#    Se importa os y nunca se usa. No rompe nada, pero confunde ("¿para qué está?")
#    y hace más lento el import. Ruff lo puede arreglar solo: ruff check . --fix
#
# 2. F841 Local variable `codigo` is assigned to but never used  → etiquetas_con_hallazgo.py:15
#    🤔 ¿Qué pretendía el autor? Seguramente usar el SKU en mayúsculas en la etiqueta:
#       return f"{codigo}-{nombre}". Calculó el valor y se le olvidó usarlo.
#    ⚠️ Ruff NO lo arregla solo con --fix (es un "unsafe fix"): no puede saber la intención.
#       Decidir si se borra la línea o se usa la variable es trabajo de una persona.
#
# 3. F811 Redefinition of unused `test_salida_valida`  → test_duplicada.py (ver sus notas).
#
# 💡 Ruff responde UNA pregunta: ¿hay errores que se ven SIN ejecutar el código?
#    No dice si la etiqueta es correcta para el negocio: eso lo dicen las pruebas.
#
# ❓ PREGUNTAS DE REPASO
# 1. ¿Cuál de los 3 hallazgos puede esconder un error de negocio y cuál es solo "basura"?
# 2. ¿Por qué Ruff no se atreve a arreglar solo el F841?
