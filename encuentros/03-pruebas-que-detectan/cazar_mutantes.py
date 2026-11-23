import os
from pathlib import Path
import subprocess
import sys
import tempfile


def cazar():
    carpeta = Path(__file__).resolve().parent
    pruebas = Path(sys.argv[1] if len(sys.argv) > 1 else "test_taller_practica.py").resolve()
    # Copiar las pruebas aquí garantiza que se cargue nuestro conftest.
    with tempfile.TemporaryDirectory(prefix="pruebas_", dir=carpeta) as temporal:
        copia = Path(temporal) / "test_casos.py"
        copia.write_text(pruebas.read_text(encoding="utf-8"), encoding="utf-8")
        for candidato in [None, *sorted((carpeta / "mutantes").glob("mutante_*.py"))]:
            entorno = os.environ.copy()
            entorno.pop("TALLER", None)
            entorno.pop("PRODUCTO", None)
            if candidato:
                entorno["TALLER"] = str(candidato)
            resultado = subprocess.run(
                [sys.executable, "-m", "pytest", "-q", str(copia)],
                cwd=carpeta, env=entorno, capture_output=True, text=True,
            )
            if candidato is None:
                if resultado.returncode != 0:
                    print("Las pruebas deben pasar primero contra el Taller original.")
                    print(resultado.stdout)
                    return 2
                print("Taller original: pruebas pasan")
            elif resultado.returncode in (0, 1):
                estado = "SOBREVIVE" if resultado.returncode == 0 else "MUERE"
                print(f"{candidato.stem}: {estado}")
            else:
                print(f"{candidato.stem}: ERROR al ejecutar las pruebas")
                print(resultado.stdout, resultado.stderr)
                return 2
    return 0


if __name__ == "__main__":
    sys.exit(cazar())
