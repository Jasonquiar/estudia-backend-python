"""E02 · La regla vive en el objeto: una property protege las existencias."""
"""
📝 MIS NOTAS (Encuentro 4 · Cobertura y aserciones · 23 nov 2026)

🎯 Es el Producto original (sin errores). Contra él se mide la cobertura y se
   comparan los mutantes de mutantes/.
   (Repaso de sus reglas: ver las notas de 03-pruebas-que-detectan/producto.py.)

📊 Qué cubre cada archivo de pruebas (con --cov-branch):
   tests/test_recorre_todo.py   → 100 %  (pasa por TODAS las líneas… sin comprobar casi nada)
   tests/test_con_aserciones.py →  94 %  (no llama a __repr__ ni a __str__: líneas 52 y 55)
   💡 El que tiene MENOS cobertura es el que SÍ detecta los mutantes.
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
        self.existencias -= cantidad
        # 📝 ⭐ La línea que borra mutante_1 (y la que el README te pide borrar a mano).
        return self.existencias

    def necesita_pedido(self):
        return self.existencias <= self.alerta_stock
        # 📝 ⭐ mutante_2 cambia "<=" por "<". Solo se nota con el BORDE: existencias == 3.

    def __repr__(self):  # para quien programa: sin ambigüedad
        return f"Producto(sku={self.sku!r}, existencias={self.existencias})"

    def __str__(self):   # para quien usa el sistema: legible
        return f"{self.nombre}: {self.existencias} unidades"

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué test_con_aserciones.py deja sin cubrir __repr__ y __str__? ¿Importa para el negocio?
# 2. Si una prueba llama a registrar_salida(3) sin assert, ¿la línea del descuento cuenta como cubierta?
