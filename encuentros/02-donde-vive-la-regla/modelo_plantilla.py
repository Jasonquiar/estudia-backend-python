"""MI BRIEF

Actor: quién usa el servicio.
Operación: qué quiere hacer (registrar, consultar o modificar algo).
Recursos: qué información guarda el servicio.
Regla: qué no debe permitir nunca.
Exclusiones: lo que dejo para después.
Primer flujo verificable: con esta entrada, espero este resultado.

¿Clase o función? Escribe aquí por qué. Pista: ¿hay estado que cambia y una regla que lo protege?
"""
"""
📝 MIS NOTAS (Encuentro 2 · Dónde vive la regla · 18 nov 2026)

🎯 Idea central:
   Es un MOLDE para el src/modelo.py de mi proyecto: junta todo lo visto
   (excepción propia + @property con la regla + ValueError para datos inválidos).
   Solo hay que cambiar nombres y la regla.

🏪 Analogía:
   Un formulario en blanco de "cómo abrir una tienda": ya trae las casillas
   (portero, cuaderno protegido, mostrador). Yo solo escribo QUÉ vendo y CUÁL es mi regla.

🔗 Viene de / lleva a:
   ⬅️ Viene de inventario_property.py (mismo patrón, con nombres genéricos).
   ➡️ Lleva a MI repositorio (src/modelo.py) y al Encuentro 3, donde los casos
      aceptado/rechazado se vuelven pruebas automáticas.

✍️ El docstring "MI BRIEF" de arriba lo lleno con los datos de MI proyecto
   (actor, operación, recursos, regla, exclusiones y primer flujo).
"""


class OperacionRechazada(Exception):
    """Rechazo de negocio: cambia el nombre por el de tu regla."""
    # 📝 Ej.: ReservaRechazada, PedidoRechazado, TurnoNoDisponible…


class Recurso:  # cambia el nombre: Reserva, Pedido, Turno, Producto…
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad  # pasa por el setter: la regla se aplica desde el inicio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        # 📝 👮 Aquí vive la regla (como en inventario_property.py).
        #    ✅ cantidad = 2 → guarda    ❌ cantidad = -8 → OperacionRechazada
        if valor < 0:  # REGLA: cámbiala por la tuya
            raise OperacionRechazada(f"Cantidad inválida: {valor}")
        self._cantidad = valor

    def operar(self, valor):  # cambia el nombre por tu operación
        # 📝 Mismo orden de siempre: 1) ¿el DATO tiene sentido? → ValueError
        #                            2) la REGLA la revisa el setter → OperacionRechazada
        if valor <= 0:
            raise ValueError(f"Dato inválido: {valor}")
        self.cantidad -= valor  # si rompe la regla, el setter lo rechaza
        # 📝 Ejemplo → cantidad 2, operar(10) → 2 - 10 = -8 → el setter rechaza
        #    ANTES de guardar, así que la cantidad sigue en 2.
        return self.cantidad

    def __repr__(self):
        return f"Recurso({self.nombre!r}, cantidad={self.cantidad})"

    def __str__(self):
        return f"{self.nombre}: {self.cantidad}"


if __name__ == "__main__":
    recurso = Recurso("Ejemplo", 5)

    # Dos casos: uno que se acepta y uno que se rechaza. Escribe antes qué esperas.
    for valor in [3, 10]:
        try:
            print("ACEPTADO ", valor, "->", recurso.operar(valor))
            # 📝 → ACEPTADO  3 -> 2            (5 - 3 = 2 ✅)
        except OperacionRechazada as error:
            print("RECHAZADO", valor, "->", error)
            # 📝 → RECHAZADO 10 -> Cantidad inválida: -8   (2 - 10 = -8 ❌)
        # 📝 ⚠️ No hay except ValueError: si agregas un 0 o un -1 a la lista, el
        #    programa se detiene con un traceback. Para mi proyecto conviene atraparlo.
    print(recurso)
    # 📝 → Ejemplo: 2     (usa __str__; el rechazo no cambió la cantidad)

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Qué tres cosas tengo que renombrar o cambiar para adaptar esta plantilla a mi proyecto?
# 2. ¿Por qué la cantidad final es 2 y no -8, si se intentó restar 10?
# 3. ¿Qué pasaría con valor = 0 en el for? ¿Es regla de negocio o dato inválido?
# 4. ¿Qué es mejor para tu proyecto, clase o función? Escríbelo en el docstring MI BRIEF.
