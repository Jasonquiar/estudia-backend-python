"""E02 · La regla vive en el objeto: una property protege las existencias."""
"""
📝 MIS NOTAS (Encuentro 4 · Cobertura y aserciones · 23 nov 2026)

⚠️ SPOILER: aquí está marcado el error escondido. Si quieres cazar "a ciegas",
   corre primero python cazar_mutantes.py tests/test_recorre_todo.py y lee esto después.

🧟 Mutante 1: falta UNA línea en registrar_salida.
🔍 Comparar con src/producto.py, línea por línea, para encontrarlo.
"""


class MovimientoInvalido(Exception):
    """Rechazo de negocio: el movimiento dejaría el inventario en un estado no permitido."""


class Producto:
    alerta_stock = 3  # atributo de CLASE: el mismo para todos los productos

    def __init__(self, sku, nombre, existencias):
        self.sku = sku            # atributos de INSTANCIA: propios de cada producto
        self.nombre = nombre
        self.existencias = existencias  # pasa por el setter: la regla se aplica desde el inicio

    @property
    def existencias(self):
        return self._existencias

    @existencias.setter
    def existencias(self, valor):
        if valor < 0:  # REGLA: nunca quedar con stock negativo
            raise MovimientoInvalido(f"Existencias inválidas: {valor}")
        self._existencias = valor

    def registrar_salida(self, cantidad):
        if cantidad <= 0:
            raise ValueError(f"Cantidad inválida: {cantidad}. Debe ser positiva")
        if cantidad > self.existencias:
            raise MovimientoInvalido(f"Stock insuficiente: hay {self.existencias}, se piden {cantidad}")
        return self.existencias
        # 📝 🧟 EL ERROR: falta "self.existencias -= cantidad" justo antes de este return.
        #    registrar_salida(3) con 10 devuelve 10 y el stock no baja.
        #    🎯 Lo mata: assert cafe.registrar_salida(3) == 7 (o assert cafe.existencias == 7).
        #    Es el mismo defecto de producto_con_defecto.py del Encuentro 3.

    def necesita_pedido(self):
        return self.existencias <= self.alerta_stock

    def __repr__(self):  # para quien programa: sin ambigüedad
        return f"Producto(sku={self.sku!r}, existencias={self.existencias})"

    def __str__(self):   # para quien usa el sistema: legible
        return f"{self.nombre}: {self.existencias} unidades"
