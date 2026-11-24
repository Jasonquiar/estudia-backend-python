"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   Un "cazador" que corre TUS pruebas 4 veces: una contra el Taller bueno
   (taller.py) y una contra cada mutante. Así sabes si tus pruebas DETECTAN errores.

🧟 Cómo leer el resultado:
   - MUERE     → al menos una prueba falló contra el mutante. ✅ Tus pruebas lo detectaron.
   - SOBREVIVE → todas pasaron aunque el código está roto. ⚠️ Te falta una prueba.

🏪 Analogía:
   Un simulacro: alguien esconde a propósito un error en la caja. Si el arqueo
   (tus pruebas) no lo encuentra, el arqueo tiene un punto ciego.

▶️ python cazar_mutantes.py                    → usa test_taller_practica.py
   python cazar_mutantes.py otro_archivo.py    → usa las pruebas que le indiques

   Salida típica con solo las 2 pruebas de la práctica (verificado con unas pruebas de borrador):
     Taller original: pruebas pasan
     mutante_1: MUERE
     mutante_2: SOBREVIVE
     mutante_3: SOBREVIVE

⚠️ Matar todos los mutantes NO prueba que la regla esté 100% cubierta: solo que
   tus pruebas atrapan ESOS tres errores.

💡 No hace falta entender cada línea de este archivo: es una herramienta del curso.
"""
import os
from pathlib import Path
import subprocess
import sys
import tempfile


def cazar():
    carpeta = Path(__file__).resolve().parent
    pruebas = Path(sys.argv[1] if len(sys.argv) > 1 else "test_taller_practica.py").resolve()
    # 📝 Si no le pasas un archivo, usa test_taller_practica.py.
    # Copiar las pruebas aquí garantiza que se cargue nuestro conftest.
    with tempfile.TemporaryDirectory(prefix="pruebas_", dir=carpeta) as temporal:
        copia = Path(temporal) / "test_casos.py"
        copia.write_text(pruebas.read_text(encoding="utf-8"), encoding="utf-8")
        # 📝 Copia tus pruebas a una carpeta temporal (se borra sola al final).
        for candidato in [None, *sorted((carpeta / "mutantes").glob("mutante_*.py"))]:
            # 📝 Recorre: None (= el Taller original), mutante_1, mutante_2, mutante_3.
            entorno = os.environ.copy()
            entorno.pop("TALLER", None)
            entorno.pop("PRODUCTO", None)
            if candidato:
                entorno["TALLER"] = str(candidato)
                # 📝 La variable de entorno TALLER le dice a conftest.py:
                #    "cuando alguien haga import taller, dale este mutante".
            resultado = subprocess.run(
                [sys.executable, "-m", "pytest", "-q", str(copia)],
                cwd=carpeta, env=entorno, capture_output=True, text=True,
            )
            # 📝 Corre pytest en un proceso aparte. Código de salida de pytest:
            #    0 = todo pasó, 1 = alguna prueba falló, otro = error al ejecutar.
            if candidato is None:
                if resultado.returncode != 0:
                    print("Las pruebas deben pasar primero contra el Taller original.")
                    print(resultado.stdout)
                    return 2
                    # 📝 Si tus pruebas fallan con el código BUENO, la culpa es de la prueba
                    #    (o sigue el pytest.fail). No tiene sentido cazar todavía.
                print("Taller original: pruebas pasan")
            elif resultado.returncode in (0, 1):
                estado = "SOBREVIVE" if resultado.returncode == 0 else "MUERE"
                # 📝 Al revés de lo normal: aquí que pytest FALLE (1) es la buena noticia.
                print(f"{candidato.stem}: {estado}")
            else:
                print(f"{candidato.stem}: ERROR al ejecutar las pruebas")
                print(resultado.stdout, resultado.stderr)
                return 2
    return 0


if __name__ == "__main__":
    sys.exit(cazar())

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué el cazador corre primero las pruebas contra el Taller original?
# 2. ¿Por qué aquí que una prueba falle es una "buena noticia"?
# 3. Si los 3 mutantes mueren, ¿ya está probada toda la regla? ¿Por qué no necesariamente?
