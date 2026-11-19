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
        if len(self.inscritos) >= self.cupo:
            raise InscripcionRechazada(f"{self.nombre} no tiene cupos ({self.cupo})")
        self.inscritos.append(persona)
        return self.cupo - len(self.inscritos)

    def __repr__(self):
        return f"Taller({self.nombre!r}, cupo={self.cupo}, inscritos={len(self.inscritos)})"


guitarra = Taller("Guitarra básica", cupo=3)
for persona in ["Valentina", "Samuel", "Valentina", "Luisa", "Andrés"]:
    try:
        quedan = guitarra.inscribir(persona)
        print(f"ACEPTADA  {persona}: quedan {quedan} cupos")
    except InscripcionRechazada as error:
        print(f"RECHAZADA {persona}: {error}")

guitarra.cupo = 5
print("Cupo ampliado:", guitarra)
try:
    guitarra.cupo = 1
except InscripcionRechazada as error:
    print("RECHAZADO:", error)
print(guitarra)


# Reto: ¿herencia o composición para la lista de espera?
class TallerConEspera(Taller):
    """Herencia que contradice el contrato: inscribir ya no rechaza por cupo."""

    def __init__(self, nombre, cupo):
        super().__init__(nombre, cupo)
        self.espera = []

    def inscribir(self, persona):
        try:
            return super().inscribir(persona)
        except InscripcionRechazada:
            self.espera.append(persona)
            return 0  # quien usa Taller espera un rechazo y recibe "0 cupos": el contrato cambió
