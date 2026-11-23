import json
from urllib.error import URLError
from urllib.request import Request, urlopen


class ProveedorHTTP:
    def pedir(self, sku, cantidad):
        datos = json.dumps({"sku": sku, "cantidad": cantidad}).encode("utf-8")
        solicitud = Request(
            "https://proveedor-abastos.example/pedidos", data=datos,
            headers={"Content-Type": "application/json"}, method="POST",
        )
        with urlopen(solicitud, timeout=5) as respuesta:
            return json.load(respuesta)["orden"]


class Reabastecimiento:
    def __init__(self, proveedor, cantidad_pedido=12):
        self.proveedor = proveedor
        self.cantidad_pedido = cantidad_pedido

    def revisar(self, producto):
        if not producto.necesita_pedido():
            return None
        try:
            return self.proveedor.pedir(producto.sku, self.cantidad_pedido)
        except (TimeoutError, ConnectionError, URLError):
            return "pendiente"
