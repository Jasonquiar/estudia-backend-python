"""E02 · El Producto del encuentro 1. ¿Dónde vive la regla?"""


class MovimientoInvalido(Exception):
    """Rechazo de negocio: el movimiento dejaría el inventario en un estado no permitido."""


class Producto:
    def __init__(self, sku, nombre, existencias):
        if existencias < 0:
            raise ValueError("Las existencias iniciales no pueden ser negativas")
        self.sku = sku
        self.nombre = nombre
        self.existencias = existencias

    def registrar_salida(self, cantidad):
        if cantidad <= 0:
            raise ValueError(f"Cantidad inválida: {cantidad}. Debe ser positiva")
        if cantidad > self.existencias:  # REGLA: nunca quedar con stock negativo
            raise MovimientoInvalido(f"Stock insuficiente: hay {self.existencias}, se piden {cantidad}")
        self.existencias -= cantidad
        return self.existencias

    def __repr__(self):
        return f"Producto(sku={self.sku!r}, existencias={self.existencias})"


cafe = Producto("cafe-500g", "Café molido 500 g", 10)
print("Salida de 6 ->", cafe.registrar_salida(6))

# Un ajuste de inventario escrito por otra parte del programa
cafe.existencias = -5
print("Después del ajuste:", cafe)
