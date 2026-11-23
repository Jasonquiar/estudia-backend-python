"""Ejecuta un archivo de pruebas contra el Producto original y contra cada mutante.

Un mutante MUERE cuando alguna prueba falla al ejecutarse (pytest termina con código 1). Casi siempre es una
aserción que no se cumple; si en cambio la prueba termina por otro error (por ejemplo un RuntimeError), el
script lo avisa: el mutante murió, pero no porque la prueba comprobara el resultado. Cualquier otra cosa
(error al importar o preparar las pruebas, argumentos inválidos, cero pruebas) no demuestra nada sobre las
pruebas: se muestra como ERROR con el diagnóstico y el script termina con código 2.
"""
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


def ejecutar(candidato):
    entorno = os.environ.copy()
    entorno.pop("PRODUCTO", None)
    if candidato:
        entorno["PRODUCTO"] = str(candidato.relative_to(carpeta))
    return subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "--tb=line", "-rfE", "-p", "no:cacheprovider", pruebas],
        cwd=carpeta, env=entorno, capture_output=True, text=True,
    )


def error(nombre, resultado, motivo=None):
    print(f"{nombre}: ERROR, no se puede concluir: {motivo or PORQUE.get(resultado.returncode, 'código ' + str(resultado.returncode))}")
    print("\n".join((resultado.stdout + resultado.stderr).strip().splitlines()[-8:]))
    sys.exit(2)


original = ejecutar(None)
if original.returncode != 0:  # sin el original en verde, un "MUERE" no significaría nada
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
            print(f"{candidato.stem}: MUERE, pero por un error inesperado ({', '.join(otros)}), no por una aserción")
        else:
            print(f"{candidato.stem}: MUERE")
    else:
        error(candidato.stem, resultado)
