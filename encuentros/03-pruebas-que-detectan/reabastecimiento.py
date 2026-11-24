"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   Un servicio que, si un producto tiene poco stock, le hace un pedido a un
   PROVEEDOR EXTERNO por internet. ¿Cómo se prueba algo que depende de internet
   sin usar internet? → Inyectando al proveedor, para poder cambiarlo por un mock.

🏪 Analogía:
   La tienda (Reabastecimiento) no sabe CÓMO se llama al proveedor: solo sabe
   que tiene "alguien a quien pedirle" (self.proveedor). En la vida real es el
   teléfono del proveedor (ProveedorHTTP). En las pruebas es un actor (Mock) que
   contesta lo que le digamos… o que finge que no hay señal.

🧩 Dos piezas:
   - ProveedorHTTP   → ADAPTADOR: sabe hablar HTTP/JSON con el proveedor real.
   - Reabastecimiento → SERVICIO: tiene la regla ("pido si necesita_pedido()")
     y decide qué hacer si el proveedor falla ("pendiente").

🔗 Viene de / lleva a:
   ⬅️ Usa Producto.necesita_pedido() de producto.py.
   ➡️ Lo prueban test_reabastecimiento.py y test_proveedor_cae.py.
"""
import json
from urllib.error import URLError
from urllib.request import Request, urlopen


class ProveedorHTTP:
    def pedir(self, sku, cantidad):
        datos = json.dumps({"sku": sku, "cantidad": cantidad}).encode("utf-8")
        # 📝 Convierte el pedido a JSON → b'{"sku": "cafe-500g", "cantidad": 12}'
        solicitud = Request(
            "https://proveedor-abastos.example/pedidos", data=datos,
            headers={"Content-Type": "application/json"}, method="POST",
        )
        # 📝 ⚠️ ".example" es un dominio RESERVADO: no existe de verdad. Es un
        #    ejemplo; en un proyecto real va la URL del proveedor.
        with urlopen(solicitud, timeout=5) as respuesta:
            return json.load(respuesta)["orden"]
            # 📝 Envía el POST (espera máximo 5 s) y del JSON de respuesta toma "orden".
            #    Ese es el CONTRATO que suponemos: el proveedor responde {"orden": "..."}.


class Reabastecimiento:
    def __init__(self, proveedor, cantidad_pedido=12):
        self.proveedor = proveedor
        # 📝 💉 INYECCIÓN DE DEPENDENCIAS: el proveedor llega desde AFUERA.
        #    Producción → Reabastecimiento(ProveedorHTTP())
        #    Pruebas    → Reabastecimiento(Mock(spec=ProveedorHTTP))
        #    Si aquí adentro escribiera self.proveedor = ProveedorHTTP(), no podría cambiarlo.
        self.cantidad_pedido = cantidad_pedido
        # 📝 Por defecto se piden 12 unidades.

    def revisar(self, producto):
        if not producto.necesita_pedido():
            return None
            # 📝 Hay stock suficiente (más de 3) → no pide nada y devuelve None.
        try:
            return self.proveedor.pedir(producto.sku, self.cantidad_pedido)
            # 📝 ✅ Poco stock → le pide al proveedor y devuelve el número de orden.
        except (TimeoutError, ConnectionError, URLError):
            return "pendiente"
            # 📝 ⚠️ Si el proveedor no contesta (tiempo agotado, sin conexión, error de URL),
            #    el servicio NO se cae: devuelve "pendiente" para reintentar después.
            #    Esta es otra regla del servicio, y también hay que probarla.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Qué devuelve revisar() en cada caso: mucho stock, poco stock, proveedor caído?
# 2. ¿Por qué el proveedor se pasa en el __init__ en lugar de crearlo adentro?
# 3. ¿Qué diferencia hay entre el "adaptador" (ProveedorHTTP) y el "servicio" (Reabastecimiento)?
# 4. Si el proveedor lanzara ValueError, ¿revisar() devolvería "pendiente"? ¿Por qué?
