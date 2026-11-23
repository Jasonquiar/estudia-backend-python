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


def pytest_addoption(parser):
    parser.addoption("--producto-defecto", action="store_true")


def pytest_configure(config):
    if config.getoption("--producto-defecto"):
        import producto_con_defecto
        sys.modules["producto"] = producto_con_defecto
