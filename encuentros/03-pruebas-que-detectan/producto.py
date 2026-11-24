"""E02 · La regla vive en el objeto: una property protege las existencias."""
"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   Es EXACTAMENTE el Producto de inventario_property.py (Encuentro 2), copiado
   aquí como módulo para que las pruebas puedan hacer: from producto import Producto.
   Hoy no cambiamos el código: hoy lo PROBAMOS.

🔗 Viene de / lleva a:
   ⬅️ Viene de 02-donde-vive-la-regla/inventario_property.py (sin los print de abajo).
   ➡️ Lo usan test_eco.py, test_producto.py, test_caja.py, test_orden.py,
      test_turno_rechazo.py y reabastecimiento.py.
   🆚 Compáralo con producto_con_defecto.py: le falta UNA línea.

📋 Las reglas que vamos a probar:
   ✅ registrar_salida(3) con 10 → devuelve 7 y existencias queda en 7
   ❌ cantidad <= 0              → ValueError "Debe ser positiva"       (dato inválido)
   ❌ cantidad > existencias     → MovimientoInvalido "Stock insuficiente" (regla de negocio)
   ❌ nacer con existencias < 0  → MovimientoInvalido "Existencias inválidas" (el setter)
   🔔 necesita_pedido()          → True si existencias <= 3
"""


class MovimientoInvalido(Exception):
    """Rechazo de negocio: el movimiento dejaría el inventario en un estado no permitido."""


class Producto:
    alerta_stock = 3  # atributo de CLASE: el mismo para todos los productos

    def __init__(self, sku, nombre, existencias):
        self.sku = sku            # atributos de INSTANCIA: propios de cada producto
        self.nombre = nombre
        self.existencias = existencias  # pasa por el setter: la regla se aplica desde el inicio
        # 📝 Por esto Producto("x", "X", -1) lanza MovimientoInvalido.
        #    Es justo lo que te toca probar en test_turno_rechazo.py.

    @property
    def existencias(self):
        return self._existencias

    @existencias.setter
    def existencias(self, valor):
        if valor < 0:  # REGLA: nunca quedar con stock negativo
            raise MovimientoInvalido(f"Existencias inválidas: {valor}")
            # 📝 Mensaje que puedes usar en match="Existencias inválidas".
        self._existencias = valor

    def registrar_salida(self, cantidad):
        if cantidad <= 0:
            raise ValueError(f"Cantidad inválida: {cantidad}. Debe ser positiva")
        if cantidad > self.existencias:
            raise MovimientoInvalido(f"Stock insuficiente: hay {self.existencias}, se piden {cantidad}")
        self.existencias -= cantidad
        # 📝 ⭐ Esta es la línea que NO está en producto_con_defecto.py.
        #    Sin ella, la salida se "acepta" pero el stock no baja.
        return self.existencias

    def necesita_pedido(self):
        return self.existencias <= self.alerta_stock
        # 📝 Borde: 3 → True (3 <= 3), 4 → False. Por eso test_alerta prueba 3 y 4.

    def __repr__(self):  # para quien programa: sin ambigüedad
        return f"Producto(sku={self.sku!r}, existencias={self.existencias})"

    def __str__(self):   # para quien usa el sistema: legible
        return f"{self.nombre}: {self.existencias} unidades"

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Qué dos tipos de error puede lanzar registrar_salida? ¿Cuál es de dato y cuál de negocio?
# 2. ¿Por qué el borde de necesita_pedido() se prueba con 3 y con 4, y no con 1 y 10?
