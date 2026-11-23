"""E01 · Práctica guiada (caso nuevo: reservas).

Sala de ensayo musical de una casa de la cultura. Horas enteras, formato 24 h.
Ya existe una reserva de 18 a 19.

Paso 1: para cada solicitud escribe en el documento: entrada, resultado esperado y motivo.
Paso 2: completa el método reservar() para que acepte o rechace.
Paso 3: ANTES de ejecutar, escribe qué esperas que imprima. Después compara.
"""
"""
📝 MIS NOTAS (Encuentro 1 · Reglas de un servicio · 11 nov 2026)

🎯 Idea central:
   Es el mismo patrón de inventario_v2.py, pero con reservas: una entidad (Sala)
   que rechaza un DATO inválido con ValueError y una violación de la REGLA de
   negocio con su propia excepción (ReservaRechazada).

🏪 Analogía:
   El portero de la casa de la cultura tiene la agenda de la sala:
   1) "¿Ese horario existe?" → de 21 a 20 no tiene sentido → ValueError.
   2) "¿Choca con alguien que ya reservó?" → el coro tiene de 18 a 19 → si te
      montas encima, ReservaRechazada (regla de negocio).

🔗 Viene de / lleva a:
   ⬅️ Viene de inventario_v2.py (Producto + MovimientoInvalido = el modelo a copiar).
   ➡️ Lleva al Encuentro 2: "dónde vive la regla" (¿función o método de clase?).

⚠️ OJO: reservar() todavía NO está completo (solo tiene `pass`), por eso hoy
   acepta TODO. Las notas no lo resuelven: la práctica es mía.
"""


class ReservaRechazada(Exception):
    """Rechazo de negocio: la reserva choca con otra existente."""
    # 📝 Igual que MovimientoInvalido en v2: una excepción propia del negocio.
    #    El nombre ya dice qué pasó → el que llama puede atraparla aparte.


class Sala:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []  # lista de tuplas (inicio, fin, responsable)
        # 📝 La "agenda" de la sala. Ej: [(18, 19, "Coro Voces del Barrio")]

    def reservar(self, inicio, fin, responsable):
        # TODO 1: rechaza un dato inválido (por ejemplo, inicio >= fin) con ValueError
        # TODO 2: rechaza con ReservaRechazada si se cruza con una reserva existente
        # TODO 3: si todo está bien, guarda la reserva y devuélvela
        # 📝 Pistas (copiar el orden de Producto.registrar_salida):
        #    1) Primero el DATO: ¿inicio < fin? Si no → ValueError.
        #       ❌ (21, 20) → empieza después de terminar → dato inválido.
        #       ❌ (19, 19) → dura 0 horas → también es dato inválido (por eso >=).
        #    2) Después la REGLA: recorre self.reservas y pregúntate:
        #       "¿mi intervalo se monta encima de este?" Si sí → ReservaRechazada.
        #       🤔 Dibuja una línea de tiempo: 18──19──20.
        #          A (19–20) empieza justo cuando el coro TERMINA → ¿se tocan o se cruzan?
        #          B (18–20) ocupa la hora 18–19 del coro → ¿se cruzan?
        #    3) Solo si pasó ambos controles → append a self.reservas y return.
        #    👮 La regla debe vivir AQUÍ, no en el for de abajo.
        pass
        # 📝 `pass` = "no hagas nada". La función devuelve None sin lanzar error,
        #    así que el try de abajo SIEMPRE cree que salió bien.


if __name__ == "__main__":
    sala = Sala("Sala de ensayo 2")
    sala.reservas.append((18, 19, "Coro Voces del Barrio"))
    # 📝 Agrega la reserva existente directamente a la lista (sin pasar por reservar()).

    solicitudes = [
        (19, 20, "Banda Los del Barrio"),   # caso A
        (18, 20, "Dúo Acústico La Ceiba"),    # caso B
    ]
    # 📝 Mi tabla del Paso 1 (entrada · esperado · motivo):
    #    A) 19–20 · ✅ ACEPTA   · empieza justo cuando el coro termina, no se cruzan.
    #    B) 18–20 · ❌ RECHAZA  · la hora 18–19 ya es del coro → REGLA de negocio.
    #    Reto C) 21–20 · ❌ RECHAZA · fin antes que inicio → DATO inválido (ValueError).
    for inicio, fin, responsable in solicitudes:
        try:
            sala.reservar(inicio, fin, responsable)
            print(f"ACEPTADA  {responsable}: {inicio}-{fin}")
            # 📝 → HOY (con `pass`) salen las DOS como aceptadas:
            # 📝 → ACEPTADA  Banda Los del Barrio: 19-20
            # 📝 → ACEPTADA  Dúo Acústico La Ceiba: 18-20   ⚠️ ¡debería rechazarse!
        except ReservaRechazada as error:
            print(f"RECHAZADA {responsable} (regla): {error}")
            # 📝 → Cuando complete reservar(), el caso B debería salir por aquí.
        except ValueError as error:
            print(f"RECHAZADA {responsable} (dato inválido): {error}")
            # 📝 → Aquí caería el reto C (21–20) si lo agrego a solicitudes.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué hoy el caso B sale ACEPTADA si choca con el coro?
# 2. El caso C (21 a 20), ¿se rechaza por regla de negocio o por dato inválido? ¿Por qué?
# 3. ¿Por qué 19–20 NO choca con 18–19? Escribe la condición de "se cruzan" con
#    palabras antes de escribirla en Python.
# 4. ¿Qué control va primero en reservar(): el del dato o el de la regla? ¿Por qué?
