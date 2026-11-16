"""E02 · Práctica, paso 3: la misma operación escrita como función."""


def inscribir(taller, persona):
    """taller es un diccionario: {"nombre": str, "cupo": int, "inscritos": list}."""
    if persona in taller["inscritos"]:
        return False, f"{persona} ya está inscrita en {taller['nombre']}"
    if len(taller["inscritos"]) >= taller["cupo"]:
        return False, f"{taller['nombre']} no tiene cupos ({taller['cupo']})"
    taller["inscritos"].append(persona)
    return True, f"quedan {taller['cupo'] - len(taller['inscritos'])} cupos"


guitarra = {"nombre": "Guitarra básica", "cupo": 3, "inscritos": []}

for persona in ["Valentina", "Samuel", "Valentina", "Luisa", "Andrés"]:
    aceptada, mensaje = inscribir(guitarra, persona)
    print("ACEPTADA " if aceptada else "RECHAZADA", persona, "->", mensaje)

guitarra["cupo"] = 1
print("Cupo reducido:", guitarra)
