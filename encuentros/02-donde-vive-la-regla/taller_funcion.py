"""E02 · Práctica, paso 3: la misma operación escrita como función."""
"""
📝 MIS NOTAS (Encuentro 2 · Dónde vive la regla · 18 nov 2026)

🎯 Idea central:
   La misma regla se puede escribir con una función y un diccionario. Es más
   simple de leer, pero el dato queda totalmente desprotegido: la regla solo
   se cumple si TODOS recuerdan usar la función.

🏪 Analogía:
   En vez de una secretaria con su archivador (clase), hay una hoja suelta
   (diccionario) y un instructivo pegado en la pared (función). Si alguien sigue
   el instructivo, todo bien; si alguien escribe directo en la hoja, nadie lo detiene.

🔗 Viene de / lleva a:
   ⬅️ Viene de taller_practica.py (la versión con clase).
   ➡️ Lleva a modelo_plantilla.py, donde decides: ¿clase o función para MI proyecto?
"""


def inscribir(taller, persona):
    """taller es un diccionario: {"nombre": str, "cupo": int, "inscritos": list}."""
    # 📝 Las mismas dos reglas de Taller.inscribir, pero sin excepciones:
    #    devuelve una TUPLA (aceptada, mensaje) → (True, "...") o (False, "...").
    #    ⚠️ Quien llama TIENE que revisar el True/False. Si lo olvida, nadie se entera
    #    del rechazo (con una excepción, el programa se detiene si no la atrapas).
    if persona in taller["inscritos"]:
        return False, f"{persona} ya está inscrita en {taller['nombre']}"
    if len(taller["inscritos"]) >= taller["cupo"]:
        return False, f"{taller['nombre']} no tiene cupos ({taller['cupo']})"
    taller["inscritos"].append(persona)
    return True, f"quedan {taller['cupo'] - len(taller['inscritos'])} cupos"


guitarra = {"nombre": "Guitarra básica", "cupo": 3, "inscritos": []}
# 📝 El "taller" es solo un diccionario: datos sin comportamiento y sin reglas propias.

for persona in ["Valentina", "Samuel", "Valentina", "Luisa", "Andrés"]:
    aceptada, mensaje = inscribir(guitarra, persona)
    # 📝 Desempaqueta la tupla: aceptada = True/False, mensaje = el texto.
    print("ACEPTADA " if aceptada else "RECHAZADA", persona, "->", mensaje)
    # 📝 "X if condición else Y" = un if en una sola línea.
    # 📝 → ACEPTADA  Valentina -> quedan 2 cupos
    # 📝 → ACEPTADA  Samuel -> quedan 1 cupos
    # 📝 → RECHAZADA Valentina -> Valentina ya está inscrita en Guitarra básica
    # 📝 → ACEPTADA  Luisa -> quedan 0 cupos
    # 📝 → RECHAZADA Andrés -> Guitarra básica no tiene cupos (3)
    #    (Mismos resultados que taller_practica.py.)

guitarra["cupo"] = 1
# 📝 ❌ El mismo cambio inválido. Con un diccionario NO hay forma de ponerle
#    una @property: cualquiera puede escribir cualquier llave.
print("Cupo reducido:", guitarra)
# 📝 → Cupo reducido: {'nombre': 'Guitarra básica', 'cupo': 1, 'inscritos': ['Valentina', 'Samuel', 'Luisa']}

# 📝 ¿CLASE O FUNCIÓN? (Paso 3 del README)
#    Función + dict ✅ más corta y fácil de leer   ❌ no protege el dato
#    Clase + property ✅ la regla viaja con el dato  ❌ más código y conceptos
#    Pista del profe (modelo_plantilla.py): si hay ESTADO QUE CAMBIA y una REGLA
#    que lo protege, la clase suele ganar.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Qué devuelve inscribir() en esta versión y qué devolvía en la versión con clase?
# 2. ¿Qué pasa si alguien llama inscribir() y no revisa el True/False?
#    ¿Pasaría lo mismo con una excepción?
# 3. ¿Por qué aquí no se puede tapar el hueco de guitarra["cupo"] = 1 con @property?
# 4. Para tu proyecto, ¿elegirías clase o función? Da una razón.
