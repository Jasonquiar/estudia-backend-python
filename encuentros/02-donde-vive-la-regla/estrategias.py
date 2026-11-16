"""E02 · Herencia con super() y composición con dos estrategias pequeñas."""


class MovimientoInvalido(Exception):
    pass


class Producto:
    def __init__(self, nombre, existencias, precio, politica):
        self.nombre = nombre
        self.existencias = existencias
        self.precio = precio
        self.politica = politica  # COMPOSICIÓN: el producto TIENE una política de precio

    def registrar_salida(self, cantidad):
        if cantidad > self.existencias:
            raise MovimientoInvalido(f"Stock insuficiente: hay {self.existencias}, se piden {cantidad}")
        self.existencias -= cantidad
        return self.politica.total(cantidad, self.precio)


class ProductoPerecedero(Producto):
    """HERENCIA: un producto perecedero ES un producto, con una regla más."""

    def __init__(self, nombre, existencias, precio, politica, dias_para_vencer):
        super().__init__(nombre, existencias, precio, politica)
        self.dias_para_vencer = dias_para_vencer

    def registrar_salida(self, cantidad):  # OVERRIDE: mismo nombre, regla adicional
        if self.dias_para_vencer <= 0:
            raise MovimientoInvalido(f"{self.nombre} está vencido")
        return super().registrar_salida(cantidad)  # reutiliza la regla del padre


# Dos estrategias pequeñas: mismo método, cálculo distinto (polimorfismo)
class PrecioDetal:
    def total(self, cantidad, precio):
        return cantidad * precio


class PrecioMayorista:
    def total(self, cantidad, precio):
        descuento = 0.10 if cantidad >= 12 else 0
        return round(cantidad * precio * (1 - descuento))


cafe = Producto("Café 500 g", 40, 18000, PrecioDetal())
leche = ProductoPerecedero("Leche 1 L", 30, 4500, PrecioMayorista(), dias_para_vencer=3)
yogur = ProductoPerecedero("Yogur 1 L", 10, 7000, PrecioDetal(), dias_para_vencer=0)

for producto, cantidad in [(cafe, 12), (leche, 12), (yogur, 2)]:
    try:
        total = producto.registrar_salida(cantidad)
        print(f"ACEPTADA  {producto.nombre} x{cantidad}: ${total:,}".replace(",", "."))
    except MovimientoInvalido as error:
        print(f"RECHAZADA {producto.nombre} x{cantidad}: {error}")
