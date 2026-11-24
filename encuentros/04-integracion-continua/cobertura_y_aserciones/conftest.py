"""
📝 MIS NOTAS (Encuentro 4 · Cobertura y aserciones · 23 nov 2026)

🎯 Igual que el conftest.py del Encuentro 3, pero más corto: solo cambia "producto".
   Si existe la variable de entorno PRODUCTO (por ejemplo PRODUCTO=mutantes/mutante_1.py),
   carga ese archivo y lo registra como el módulo "producto". Las pruebas hacen
   "from producto import Producto" y reciben el mutante sin saberlo.

💡 Quien pone esa variable es cazar_mutantes.py. Infraestructura del curso:
   lo importante es saber QUÉ hace.
"""
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
