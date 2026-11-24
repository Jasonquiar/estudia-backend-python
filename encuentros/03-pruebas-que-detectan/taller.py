"""Encuentro 2 · Solución de referencia del taller."""
"""
📝 MIS NOTAS (Encuentro 3 · Pruebas que detectan · 23 nov 2026)

🎯 Idea central:
   Es la solución del Encuentro 2 (solucion/taller_solucion.py), copiada como
   módulo importable. Este es el Taller "BUENO": contra él deben PASAR tus pruebas
   de test_taller_practica.py. Los mutantes/ son copias de este archivo con UN error.

📋 Las 3 reglas que tiene (y que tus pruebas deberían vigilar):
   1) ❌ La misma persona no se inscribe dos veces.
   2) ❌ No se inscribe nadie si inscritos ya llegó al cupo (>=).
   3) ❌ No se puede bajar el cupo por debajo de los inscritos (setter).
   ✅ Una inscripción válida agrega a la persona y devuelve cuántos cupos quedan.

🔗 Viene de / lleva a:
   ⬅️ Viene de 02-donde-vive-la-regla/solucion/taller_solucion.py.
   ➡️ Lo prueban test_taller_practica.py y cazar_mutantes.py.
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
        # 📝 Regla 3. Ejemplo → cupo 2 con 2 inscritos; taller.cupo = 1 → rechaza.

    def inscribir(self, persona):
        if persona in self.inscritos:
            raise InscripcionRechazada(f"{persona} ya está inscrita en {self.nombre}")
            # 📝 Regla 1. Mensaje: "... ya está inscrita en ..."
        if len(self.inscritos) >= self.cupo:
            raise InscripcionRechazada(f"{self.nombre} no tiene cupos ({self.cupo})")
            # 📝 Regla 2. Con cupo 2: la 3.ª persona → 2 >= 2 → rechaza.
            #    Mensaje: "... no tiene cupos (2)"
        self.inscritos.append(persona)
        return self.cupo - len(self.inscritos)
        # 📝 ✅ Con cupo 2: 1.ª persona → devuelve 1; 2.ª persona → devuelve 0.

    def __repr__(self):
        return f"Taller({self.nombre!r}, cupo={self.cupo}, inscritos={len(self.inscritos)})"

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. Escribe las 3 reglas del Taller con tus palabras y un ejemplo que rompa cada una.
# 2. ¿Cuántas pruebas necesitarías, como mínimo, para vigilar las 3 reglas y el caso válido?
