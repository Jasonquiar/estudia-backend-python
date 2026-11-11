"""E01 · Demo v2: una entidad (Producto) y una operación que rechaza un cambio inválido.

Distingue dos tipos de rechazo:
- dato inválido (la solicitud está mal formada)  -> ValueError
- regla de negocio (la solicitud es válida, pero el negocio no la permite) -> MovimientoInvalido
"""


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
            raise MovimientoInvalido(
                f"Stock insuficiente: hay {self.existencias}, se piden {cantidad}"
            )
        self.existencias -= cantidad
        return self.existencias

    def __repr__(self):
        return f"Producto(sku={self.sku!r}, existencias={self.existencias})"


if __name__ == "__main__":
    cafe = Producto("cafe-500g", "Café molido 500 g", 10)

    solicitudes = [
        ("Tienda Doña Rosa", 6),   # se espera ACEPTAR
        ("Tienda El Paisa", 6),    # se espera RECHAZAR por regla
        ("Tienda La Esquina", -3), # se espera RECHAZAR por dato inválido
    ]

    for tienda, cantidad in solicitudes:
        try:
            quedan = cafe.registrar_salida(cantidad)
            print(f"ACEPTADA  {tienda}: retira {cantidad} -> quedan {quedan}")
        except MovimientoInvalido as error:
            print(f"RECHAZADA {tienda} (regla de negocio): {error}")
        except ValueError as error:
            print(f"RECHAZADA {tienda} (dato inválido): {error}")

    print(cafe)
