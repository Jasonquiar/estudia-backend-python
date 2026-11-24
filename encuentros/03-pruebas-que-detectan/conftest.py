"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   conftest.py es un archivo especial: pytest lo carga SOLO, antes de las pruebas
   de esta carpeta. Aquí se usa para "cambiar el código por debajo" sin tocar
   los import de las pruebas:
   - --producto-defecto → "producto" pasa a ser producto_con_defecto.py (test_eco.py).
   - Variable TALLER     → "taller" pasa a ser un mutante (lo usa cazar_mutantes.py).

📄 Y pytest.ini (el otro archivo de configuración) declara la etiqueta
   "integracion" que usa test_reabastecimiento.py (@pytest.mark.integracion).

💡 No hace falta entender cada línea: es infraestructura del curso. Lo importante
   es saber QUÉ hace, para que no te sorprenda.
"""
import importlib.util
import os
from pathlib import Path
import sys

# Sustituir el módulo conserva los mismos imports en todas las pruebas.
for nombre, variable in [("producto", "PRODUCTO"), ("taller", "TALLER")]:
    ruta = os.environ.get(variable)
    if ruta:
        archivo = Path(__file__).parent / ruta
        ficha = importlib.util.spec_from_file_location(nombre, archivo)
        modulo = importlib.util.module_from_spec(ficha)
        sys.modules[nombre] = modulo
        ficha.loader.exec_module(modulo)
# 📝 Si existe la variable TALLER (o PRODUCTO), carga ese archivo y lo registra en
#    sys.modules con el nombre "taller". Así, cuando una prueba hace
#    "from taller import Taller", Python le entrega el mutante sin saberlo.


def pytest_addoption(parser):
    parser.addoption("--producto-defecto", action="store_true")
    # 📝 Agrega a pytest una opción nueva de línea de comandos: --producto-defecto.


def pytest_configure(config):
    if config.getoption("--producto-defecto"):
        import producto_con_defecto
        sys.modules["producto"] = producto_con_defecto
        # 📝 Si usaste la opción, "producto" pasa a ser el Producto que no descuenta.
