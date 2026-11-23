import importlib.util
import os
import sys
from pathlib import Path

# Con PRODUCTO=mutantes/mutante_1.py las pruebas se ejecutan contra esa copia del Producto.
ruta = os.environ.get("PRODUCTO")
if ruta:
    ficha = importlib.util.spec_from_file_location("producto", Path(__file__).parent / ruta)
    modulo = importlib.util.module_from_spec(ficha)
    sys.modules["producto"] = modulo
    ficha.loader.exec_module(modulo)
