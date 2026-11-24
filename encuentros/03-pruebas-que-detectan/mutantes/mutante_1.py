"""Encuentro 2 · Solución de referencia del taller."""
"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

⚠️ SPOILER: aquí está marcado el error escondido. Si quieres cazar "a ciegas",
   corre primero python cazar_mutantes.py y lee esto después.

🧟 Mutante 1: un error de BORDE (un solo carácter cambiado).
🔍 Comparar con taller.py, línea por línea, para encontrarlo.
"""


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
        # 📝 🧟 EL ERROR: ">" en vez de ">=".
        #    Con cupo 2 y 2 inscritos: 2 > 2 es False → deja entrar a una 3.ª persona.
        #    🎯 Lo mata: una prueba que llene el taller y espere el rechazo de la siguiente.
        #    (Es el mismo tipo de defecto que el README sugiere: "un < por <=".)
        self.inscritos.append(persona)
        return self.cupo - len(self.inscritos)

    def __repr__(self):
        return f"Taller({self.nombre!r}, cupo={self.cupo}, inscritos={len(self.inscritos)})"
