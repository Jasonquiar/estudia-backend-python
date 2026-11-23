"""Encuentro 2 · Solución de referencia del taller."""


class InscripcionRechazada(Exception):
    """Rechazo de negocio."""


class Taller:
    def __init__(self, nombre, cupo):
        self.nombre = nombre
        self.inscritos = []
        self.cupo = cupo  # después de crear inscritos: el setter los necesita

    @property
    def cupo(self):
        return self._cupo

    @cupo.setter
    def cupo(self, valor):
        if valor < len(self.inscritos):  # REGLA: nunca más inscritos que cupos
            raise InscripcionRechazada(
                f"No se puede dejar {valor} cupos con {len(self.inscritos)} inscritos"
            )
        self._cupo = valor

    def inscribir(self, persona):
        if persona in self.inscritos:
            raise InscripcionRechazada(f"{persona} ya está inscrita en {self.nombre}")
        if len(self.inscritos) > self.cupo:
            raise InscripcionRechazada(f"{self.nombre} no tiene cupos ({self.cupo})")
        self.inscritos.append(persona)
        return self.cupo - len(self.inscritos)

    def __repr__(self):
        return f"Taller({self.nombre!r}, cupo={self.cupo}, inscritos={len(self.inscritos)})"
