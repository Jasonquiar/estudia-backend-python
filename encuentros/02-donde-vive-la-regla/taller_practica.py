"""E02 · Práctica: los talleres de la Casa de la Cultura de Castilla.

Regla del negocio: un taller nunca tiene más inscritos que cupos.
"""
"""
📝 MIS NOTAS (Encuentro 2 · Dónde vive la regla · 18 nov 2026)

🎯 Idea central:
   inscribir() respeta la regla, pero el cupo se puede cambiar por fuera y dejar
   el taller en un estado imposible (3 inscritos en un taller de 1 cupo).
   Es el mismo hueco de inventario_hueco.py, ahora con talleres.

🏪 Analogía:
   La secretaria de la casa de la cultura revisa cada inscripción en la
   ventanilla. Pero el tablero con el número de cupos está en el pasillo y
   cualquiera puede borrar "3" y escribir "1"… aunque ya hay 3 personas inscritas.

🔗 Viene de / lleva a:
   ⬅️ Viene de inventario_hueco.py e inventario_property.py (hueco → property).
   ➡️ Lleva a taller_funcion.py (la misma práctica sin clase) y a
      solucion/taller_solucion.py (el cupo protegido con @property).

⚠️ OJO: el Paso 2 me pide escribir la @property. Las notas no la resuelven:
   la práctica es mía. La solución del profe está en solucion/.
"""


class InscripcionRechazada(Exception):
    """Rechazo de negocio."""


class Taller:
    def __init__(self, nombre, cupo):
        self.nombre = nombre
        self.cupo = cupo
        # 📝 ⚠️ Atributo normal: nadie lo vigila (como existencias en inventario_hueco.py).
        self.inscritos = []

    def inscribir(self, persona):
        # 📝 Dos rechazos de NEGOCIO (los dos datos son válidos, pero el negocio no los permite):
        #    1) ❌ La persona ya está en la lista → no se inscribe dos veces.
        if persona in self.inscritos:
            raise InscripcionRechazada(f"{persona} ya está inscrita en {self.nombre}")
        #    2) ❌ Ya se llenó → len(inscritos) llegó al cupo.
        #       Ejemplo → cupo 3, inscritos 3 → 3 >= 3 → rechaza.
        if len(self.inscritos) >= self.cupo:
            raise InscripcionRechazada(f"{self.nombre} no tiene cupos ({self.cupo})")
        self.inscritos.append(persona)
        return self.cupo - len(self.inscritos)
        # 📝 Devuelve cuántos cupos quedan después de inscribir.

    def __repr__(self):
        return f"Taller({self.nombre!r}, cupo={self.cupo}, inscritos={len(self.inscritos)})"


guitarra = Taller("Guitarra básica", cupo=3)

# Paso 1 · Antes de ejecutar, predigan qué imprime cada línea.
for persona in ["Valentina", "Samuel", "Valentina", "Luisa", "Andrés"]:
    try:
        quedan = guitarra.inscribir(persona)
        print(f"ACEPTADA  {persona}: quedan {quedan} cupos")
        # 📝 → ACEPTADA  Valentina: quedan 2 cupos
        # 📝 → ACEPTADA  Samuel: quedan 1 cupos
        # 📝 → ACEPTADA  Luisa: quedan 0 cupos
    except InscripcionRechazada as error:
        print(f"RECHAZADA {persona}: {error}")
        # 📝 → RECHAZADA Valentina: Valentina ya está inscrita en Guitarra básica  (2.ª vez)
        # 📝 → RECHAZADA Andrés: Guitarra básica no tiene cupos (3)              (ya había 3)

# Paso 2 · Un cambio válido y uno inválido. ¿Qué debería pasar con cada uno?
guitarra.cupo = 5
# 📝 ✅ VÁLIDO: 5 cupos con 3 inscritos → caben todos.
print("Cupo ampliado:", guitarra)
# 📝 → Cupo ampliado: Taller('Guitarra básica', cupo=5, inscritos=3)
guitarra.cupo = 1
# 📝 ❌ INVÁLIDO: 1 cupo con 3 inscritos rompe la regla… y Python lo acepta igual.
print("Cupo reducido:", guitarra)
# 📝 → Cupo reducido: Taller('Guitarra básica', cupo=1, inscritos=3)   ⚠️ ¡el hueco!

# 📝 Pistas para el Paso 2 (no es la solución):
#    - Copia el patrón de inventario_property.py: @property cupo + @cupo.setter.
#    - En el setter, la pregunta es: "¿el nuevo cupo alcanza para los que ya están inscritos?"
#    - "Cuidado con el orden en __init__" (dice el README): el setter necesita mirar
#      self.inscritos… ¿ya existe en el momento en que se asigna self.cupo?

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué Valentina es rechazada la segunda vez y Andrés también? ¿Es el mismo motivo?
# 2. ¿Por qué guitarra.cupo = 1 no lanza error si inscribir() sí respeta la regla?
# 3. Al proteger el cupo con @property, ¿por qué importa el orden de las líneas en __init__?
# 4. ¿Esos rechazos son de regla de negocio o de dato inválido? ¿Qué dato sería inválido aquí?
