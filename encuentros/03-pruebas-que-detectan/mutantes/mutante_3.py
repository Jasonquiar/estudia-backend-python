"""Encuentro 2 · Solución de referencia del taller."""
"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

⚠️ SPOILER: aquí está marcado el error escondido. Si quieres cazar "a ciegas",
   corre primero python cazar_mutantes.py y lee esto después.

🧟 Mutante 3: el error está en el SETTER del cupo (no en inscribir).
🔍 Comparar con taller.py. Ojo: el comentario de la regla sigue igual… pero el código no.
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
        if valor < 0:  # REGLA: nunca más inscritos que cupos
            # 📝 🧟 EL ERROR: compara con 0 en vez de con len(self.inscritos).
            #    Con 2 inscritos, guitarra.cupo = 1 se ACEPTA → vuelve el hueco del Encuentro 2.
            #    💡 Lección extra: el comentario dice una cosa y el código hace otra.
            #    Las pruebas revisan el código, no los comentarios.
            #    ⚠️ Con solo las dos pruebas de la práctica también SOBREVIVE:
            #    ninguna intenta bajar el cupo.
            #    🎯 Lo mata: una prueba de la regla 3 (ver notas de taller.py).
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
