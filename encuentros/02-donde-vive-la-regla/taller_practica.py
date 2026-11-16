"""E02 · Práctica: los talleres de la Casa de la Cultura de Castilla.

Regla del negocio: un taller nunca tiene más inscritos que cupos.
"""


class InscripcionRechazada(Exception):
    """Rechazo de negocio."""


class Taller:
    def __init__(self, nombre, cupo):
        self.nombre = nombre
        self.cupo = cupo
        self.inscritos = []

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

# Paso 1 · Antes de ejecutar, predigan qué imprime cada línea.
for persona in ["Valentina", "Samuel", "Valentina", "Luisa", "Andrés"]:
    try:
        quedan = guitarra.inscribir(persona)
        print(f"ACEPTADA  {persona}: quedan {quedan} cupos")
    except InscripcionRechazada as error:
        print(f"RECHAZADA {persona}: {error}")

# Paso 2 · Un cambio válido y uno inválido. ¿Qué debería pasar con cada uno?
guitarra.cupo = 5
print("Cupo ampliado:", guitarra)
guitarra.cupo = 1
print("Cupo reducido:", guitarra)
