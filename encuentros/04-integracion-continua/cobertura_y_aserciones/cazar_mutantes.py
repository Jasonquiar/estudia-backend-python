"""Ejecuta un archivo de pruebas contra el Producto original y contra cada mutante.

Un mutante MUERE cuando alguna prueba falla al ejecutarse (pytest termina con código 1). Casi siempre es una
aserción que no se cumple; si en cambio la prueba termina por otro error (por ejemplo un RuntimeError), el
script lo avisa: el mutante murió, pero no porque la prueba comprobara el resultado. Cualquier otra cosa
(error al importar o preparar las pruebas, argumentos inválidos, cero pruebas) no demuestra nada sobre las
pruebas: se muestra como ERROR con el diagnóstico y el script termina con código 2.
"""
# 📝 MIS NOTAS (Encuentro 4 · Cobertura y aserciones · 23 nov 2026)
#
# 🎯 Idea central:
#    El cazador del Encuentro 3, mejorado. Ahora recibe el archivo de pruebas como
#    argumento y es más estricto: distingue un mutante que MUERE por una aserción de
#    uno que "muere" por cualquier otro error (que no prueba nada).
#
# ▶️ python cazar_mutantes.py tests/test_recorre_todo.py    → mutante_1 y mutante_2 SOBREVIVEN
#    python cazar_mutantes.py tests/test_con_aserciones.py  → mutante_1 y mutante_2 MUEREN
#    ⚠️ El argumento es obligatorio: sin él, sys.argv[1] lanza IndexError.
#
# 🔢 Códigos de salida de pytest que usa (los mismos que en ci_cero_pruebas/):
#    0 = todas pasaron → el mutante SOBREVIVE
#    1 = alguna falló  → el mutante MUERE (si fue por un assert o un pytest.raises que no se cumplió)
#    2, 3, 4, 5        → ERROR: no se puede concluir nada (el script termina con código 2)
#
# 💡 No hace falta entender cada línea: es una herramienta del curso.
import os
import re
import subprocess
import sys
from pathlib import Path

carpeta = Path(__file__).resolve().parent
pruebas = sys.argv[1]
PORQUE = {2: "la ejecución fue interrumpida (error al importar o recoger las pruebas)",
          3: "error interno de pytest", 4: "argumentos inválidos", 5: "no se encontró ninguna prueba"}
COMPARACION = {"AssertionError", "Failed"}  # una aserción o un pytest.raises que no se cumplió
# 📝 "Failed" es lo que lanza pytest.raises cuando el error esperado NO ocurre ("DID NOT RAISE").


def ejecutar(candidato):
    entorno = os.environ.copy()
    entorno.pop("PRODUCTO", None)
    # 📝 Se borra por si quedó puesta en tu terminal: el original debe correr con src/producto.py.
    if candidato:
        entorno["PRODUCTO"] = str(candidato.relative_to(carpeta))
    return subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "--tb=line", "-rfE", "-p", "no:cacheprovider", pruebas],
        # 📝 --tb=line: una línea por fallo (de ahí saca el tipo de error con la regex).
        #    -p no:cacheprovider: no crea .pytest_cache.
        cwd=carpeta, env=entorno, capture_output=True, text=True,
    )


def error(nombre, resultado, motivo=None):
    print(f"{nombre}: ERROR, no se puede concluir: {motivo or PORQUE.get(resultado.returncode, 'código ' + str(resultado.returncode))}")
    print("\n".join((resultado.stdout + resultado.stderr).strip().splitlines()[-8:]))
    sys.exit(2)


original = ejecutar(None)
if original.returncode != 0:  # sin el original en verde, un "MUERE" no significaría nada
    # 📝 Si tus pruebas fallan con el código BUENO, el problema es la prueba, no el código.
    error("Producto original", original)
print("Producto original: pruebas pasan")
for candidato in sorted((carpeta / "mutantes").glob("mutante_*.py")):
    resultado = ejecutar(candidato)
    if resultado.returncode == 0:
        print(f"{candidato.stem}: SOBREVIVE")
    elif resultado.returncode == 1:
        if re.search(r"^ERROR ", resultado.stdout, re.M):  # falló al preparar una prueba (fixture, conftest)
            error(candidato.stem, resultado, "una prueba no pudo prepararse (error, no fallo)")
        tipos = set(re.findall(r":\d+: (\w+)", resultado.stdout)) - {""}
        otros = sorted(t for t in tipos if t not in COMPARACION)
        if otros:
            # 📝 Ejemplo: un TypeError. El mutante murió, pero la prueba no "comprobó" nada:
            #    el código simplemente explotó. Por eso el aviso.
            print(f"{candidato.stem}: MUERE, pero por un error inesperado ({', '.join(otros)}), no por una aserción")
        else:
            print(f"{candidato.stem}: MUERE")
    else:
        error(candidato.stem, resultado)

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué el cazador corre primero las pruebas contra el Producto original?
# 2. ¿Qué diferencia hay entre "MUERE" y "MUERE, pero por un error inesperado"?
# 3. Si pytest sale con código 5 contra un mutante, ¿el mutante murió? ¿Por qué el script dice ERROR?
