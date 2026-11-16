"""MI BRIEF

Actor: quién usa el servicio.
Operación: qué quiere hacer (registrar, consultar o modificar algo).
Recursos: qué información guarda el servicio.
Regla: qué no debe permitir nunca.
Exclusiones: lo que dejo para después.
Primer flujo verificable: con esta entrada, espero este resultado.

¿Clase o función? Escribe aquí por qué. Pista: ¿hay estado que cambia y una regla que lo protege?
"""


class OperacionRechazada(Exception):
    """Rechazo de negocio: cambia el nombre por el de tu regla."""


class Recurso:  # cambia el nombre: Reserva, Pedido, Turno, Producto…
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad  # pasa por el setter: la regla se aplica desde el inicio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor < 0:  # REGLA: cámbiala por la tuya
            raise OperacionRechazada(f"Cantidad inválida: {valor}")
        self._cantidad = valor

    def operar(self, valor):  # cambia el nombre por tu operación
        if valor <= 0:
            raise ValueError(f"Dato inválido: {valor}")
        self.cantidad -= valor  # si rompe la regla, el setter lo rechaza
        return self.cantidad

    def __repr__(self):
        return f"Recurso({self.nombre!r}, cantidad={self.cantidad})"

    def __str__(self):
        return f"{self.nombre}: {self.cantidad}"


if __name__ == "__main__":
    recurso = Recurso("Ejemplo", 5)

    # Dos casos: uno que se acepta y uno que se rechaza. Escribe antes qué esperas.
    for valor in [3, 10]:
        try:
            print("ACEPTADO ", valor, "->", recurso.operar(valor))
        except OperacionRechazada as error:
            print("RECHAZADO", valor, "->", error)
    print(recurso)
