"""E01 · Práctica guiada (caso nuevo: reservas).

Sala de ensayo musical de una casa de la cultura. Horas enteras, formato 24 h.
Ya existe una reserva de 18 a 19.

Paso 1: para cada solicitud escribe en el documento: entrada, resultado esperado y motivo.
Paso 2: completa el método reservar() para que acepte o rechace.
Paso 3: ANTES de ejecutar, escribe qué esperas que imprima. Después compara.
"""


class ReservaRechazada(Exception):
    """Rechazo de negocio: la reserva choca con otra existente."""


class Sala:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []  # lista de tuplas (inicio, fin, responsable)

    def reservar(self, inicio, fin, responsable):
        # TODO 1: rechaza un dato inválido (por ejemplo, inicio >= fin) con ValueError
        # TODO 2: rechaza con ReservaRechazada si se cruza con una reserva existente
        # TODO 3: si todo está bien, guarda la reserva y devuélvela
        pass


if __name__ == "__main__":
    sala = Sala("Sala de ensayo 2")
    sala.reservas.append((18, 19, "Coro Voces del Barrio"))

    solicitudes = [
        (19, 20, "Banda Los del Barrio"),   # caso A
        (18, 20, "Dúo Acústico La Ceiba"),    # caso B
    ]
    for inicio, fin, responsable in solicitudes:
        try:
            sala.reservar(inicio, fin, responsable)
            print(f"ACEPTADA  {responsable}: {inicio}-{fin}")
        except ReservaRechazada as error:
            print(f"RECHAZADA {responsable} (regla): {error}")
        except ValueError as error:
            print(f"RECHAZADA {responsable} (dato inválido): {error}")
