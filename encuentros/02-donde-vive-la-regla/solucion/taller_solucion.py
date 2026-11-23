"""Encuentro 2 · Solución de referencia del taller."""
"""
📝 MIS NOTAS (Encuentro 2 · Dónde vive la regla · 18 nov 2026)

🎯 Idea central:
   La solución protege el CUPO con @property: ni inscribir() ni un cambio
   directo (guitarra.cupo = 1) pueden dejar más inscritos que cupos.

🏪 Analogía:
   El tablero de cupos ahora está detrás del vidrio de la secretaría. Si alguien
   pide "deja 1 cupo", la secretaria mira la lista, ve 3 personas y dice "no se puede".

🔗 Viene de / lleva a:
   ⬅️ Viene de ../taller_practica.py (la misma clase, pero con el hueco).
   ➡️ Lleva al Encuentro 3: convertir estos casos aceptado/rechazado en pruebas.

💡 Úsala para COMPARAR con mi versión, línea por línea de la salida.
"""


class InscripcionRechazada(Exception):
    """Rechazo de negocio."""


class Taller:
    def __init__(self, nombre, cupo):
        self.nombre = nombre
        self.inscritos = []
        self.cupo = cupo  # después de crear inscritos: el setter los necesita
        # 📝 EL ORDEN IMPORTA: self.cupo = cupo llama al setter, y el setter usa
        #    len(self.inscritos). Si inscritos no existiera todavía → AttributeError.

    @property
    def cupo(self):
        return self._cupo

    @cupo.setter
    def cupo(self, valor):
        # 📝 👮 Aquí vive la regla. "¿El nuevo cupo alcanza para los que ya están?"
        #    ✅ cupo = 5 con 3 inscritos → 5 < 3 es False → guarda
        #    ❌ cupo = 1 con 3 inscritos → 1 < 3 es True → rechaza
        if valor < len(self.inscritos):  # REGLA: nunca más inscritos que cupos
            raise InscripcionRechazada(
                f"No se puede dejar {valor} cupos con {len(self.inscritos)} inscritos"
            )
        self._cupo = valor

    def inscribir(self, persona):
        # 📝 Igual que en la práctica. self.cupo ahora pasa por el getter.
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
        # 📝 → ACEPTADA  Valentina: quedan 2 cupos
        # 📝 → ACEPTADA  Samuel: quedan 1 cupos
        # 📝 → ACEPTADA  Luisa: quedan 0 cupos
    except InscripcionRechazada as error:
        print(f"RECHAZADA {persona}: {error}")
        # 📝 → RECHAZADA Valentina: Valentina ya está inscrita en Guitarra básica
        # 📝 → RECHAZADA Andrés: Guitarra básica no tiene cupos (3)

guitarra.cupo = 5
print("Cupo ampliado:", guitarra)
# 📝 → Cupo ampliado: Taller('Guitarra básica', cupo=5, inscritos=3)
try:
    guitarra.cupo = 1
except InscripcionRechazada as error:
    print("RECHAZADO:", error)
    # 📝 → RECHAZADO: No se puede dejar 1 cupos con 3 inscritos
    #    ✅ En la práctica esto pasaba sin error. Ahora el setter lo detiene.
print(guitarra)
# 📝 → Taller('Guitarra básica', cupo=5, inscritos=3)
#    El cupo sigue en 5: el rechazo no alcanzó a guardar el 1.


# Reto: ¿herencia o composición para la lista de espera?
class TallerConEspera(Taller):
    """Herencia que contradice el contrato: inscribir ya no rechaza por cupo."""
    # 📝 CONTRATO = lo que quien usa Taller espera que pase. Con Taller:
    #    "si no hay cupo, inscribir() lanza InscripcionRechazada".
    #    Esta hija ROMPE esa promesa: atrapa el rechazo y devuelve 0 en silencio.
    #    Un programa que usa Taller y recibe un TallerConEspera creería que la
    #    persona quedó inscrita. ❌ Por eso aquí la herencia es mala idea.
    #    💡 Con composición, la lista de espera sería un objeto aparte que USA un
    #    Taller, sin cambiar cómo se comporta inscribir().
    #    (Esta clase solo se define; no se ejecuta, así que no imprime nada.)

    def __init__(self, nombre, cupo):
        super().__init__(nombre, cupo)
        self.espera = []

    def inscribir(self, persona):
        try:
            return super().inscribir(persona)
        except InscripcionRechazada:
            self.espera.append(persona)
            return 0  # quien usa Taller espera un rechazo y recibe "0 cupos": el contrato cambió
            # 📝 ⚠️ También atrapa el rechazo por "ya inscrita": una persona repetida
            #    termina en la lista de espera aunque ya tenga cupo.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué self.inscritos = [] tiene que ir ANTES de self.cupo = cupo en __init__?
# 2. ¿Qué imprime el último print(guitarra) y por qué el cupo no quedó en 1?
# 3. ¿Qué significa que TallerConEspera "contradice el contrato" de Taller?
# 4. ¿Cómo harías la lista de espera con composición? Descríbelo con palabras.
