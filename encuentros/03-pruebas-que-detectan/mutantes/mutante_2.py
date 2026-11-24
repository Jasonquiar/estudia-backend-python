"""Encuentro 2 · Solución de referencia del taller."""
"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

⚠️ SPOILER: aquí está marcado el error escondido. Si quieres cazar "a ciegas",
   corre primero python cazar_mutantes.py y lee esto después.

🧟 Mutante 2: le FALTA una validación completa.
🔍 Comparar con taller.py: ¿qué if no está?
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
        # 📝 🧟 EL ERROR: aquí faltan las dos líneas que rechazan a una persona ya inscrita.
        #    Valentina puede inscribirse dos veces y ocupar 2 cupos.
        #    ⚠️ Con solo las dos pruebas de la práctica (válida + sin cupo) este
        #    mutante SOBREVIVE: ninguna intenta inscribir a la misma persona dos veces.
        #    🎯 Lo mata: una prueba de la regla 1 (ver notas de taller.py).
        if len(self.inscritos) >= self.cupo:
            raise InscripcionRechazada(f"{self.nombre} no tiene cupos ({self.cupo})")
        self.inscritos.append(persona)
        return self.cupo - len(self.inscritos)

    def __repr__(self):
        return f"Taller({self.nombre!r}, cupo={self.cupo}, inscritos={len(self.inscritos)})"
