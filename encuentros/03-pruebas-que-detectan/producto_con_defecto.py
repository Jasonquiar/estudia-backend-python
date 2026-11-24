"""E02 · La regla vive en el objeto: una property protege las existencias."""
"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   Es el mismo Producto, pero con un DEFECTO puesto a propósito: registrar_salida
   ya no descuenta. Sirve para ver qué pruebas DETECTAN el error y cuáles no.

🏪 Analogía:
   El cajero cobra el café, te dice "listo, quedan…" y lee el cuaderno… pero
   se le olvidó tachar las 3 unidades. El cuaderno sigue diciendo 10.

🔗 Cómo se usa:
   No se importa directo. Con la opción --producto-defecto, conftest.py lo pone
   en lugar de producto.py:
       python -m pytest test_eco.py --producto-defecto -v
   ➡️ Mira test_eco.py para ver qué prueba lo atrapa.
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
        # 📝 ⚠️ EL DEFECTO: aquí falta  self.existencias -= cantidad
        #    Las validaciones siguen bien (los rechazos funcionan), pero la salida
        #    válida no baja el stock: con 10 y salida de 3 devuelve 10, no 7.
        return self.existencias

    def necesita_pedido(self):
        return self.existencias <= self.alerta_stock

    def __repr__(self):  # para quien programa: sin ambigüedad
        return f"Producto(sku={self.sku!r}, existencias={self.existencias})"

    def __str__(self):   # para quien usa el sistema: legible
        return f"{self.nombre}: {self.existencias} unidades"

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. Si corres test_producto.py con --producto-defecto, ¿cuáles pruebas crees que fallan
#    y cuáles pasan? (Pista: los rechazos no dependen de la línea que falta.)
# 2. ¿Por qué un defecto así podría llegar a producción si solo tuviéramos pruebas de rechazo?
