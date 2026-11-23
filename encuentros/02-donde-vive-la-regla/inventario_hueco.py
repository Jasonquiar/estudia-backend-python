"""E02 · El Producto del encuentro 1. ¿Dónde vive la regla?"""
"""
📝 MIS NOTAS (Encuentro 2 · Dónde vive la regla · 18 nov 2026)

🎯 Idea central:
   Si la regla solo vive DENTRO de un método (registrar_salida), cualquiera
   que cambie el atributo directamente se la salta. Eso es un "hueco".

🏪 Analogía:
   La bodega tiene un portero en la puerta principal (registrar_salida) que
   revisa cada salida. Pero el cuaderno de existencias está sobre una mesa
   y cualquiera puede borrar el número y escribir -5. El portero nunca se entera.

🔗 Viene de / lleva a:
   ⬅️ Viene de 01-reglas-de-un-servicio/inventario_v2.py: es el MISMO Producto.
   ➡️ Lleva a inventario_property.py, donde se tapa el hueco con @property.
"""


class MovimientoInvalido(Exception):
    """Rechazo de negocio: el movimiento dejaría el inventario en un estado no permitido."""


class Producto:
    # 📝 Clase copiada del Encuentro 1. Sus dos controles siguen funcionando,
    #    PERO solo si alguien pasa por __init__ o por registrar_salida.
    def __init__(self, sku, nombre, existencias):
        if existencias < 0:
            raise ValueError("Las existencias iniciales no pueden ser negativas")
        self.sku = sku
        self.nombre = nombre
        self.existencias = existencias
        # 📝 Atributo "normal": guarda el valor tal cual. No tiene a nadie vigilándolo.

    def registrar_salida(self, cantidad):
        # 📝 La regla vive AQUÍ y SOLO aquí. ⚠️ Ese "solo aquí" es el problema.
        if cantidad <= 0:
            raise ValueError(f"Cantidad inválida: {cantidad}. Debe ser positiva")
        if cantidad > self.existencias:  # REGLA: nunca quedar con stock negativo
            raise MovimientoInvalido(f"Stock insuficiente: hay {self.existencias}, se piden {cantidad}")
        self.existencias -= cantidad
        return self.existencias

    def __repr__(self):
        return f"Producto(sku={self.sku!r}, existencias={self.existencias})"


cafe = Producto("cafe-500g", "Café molido 500 g", 10)
print("Salida de 6 ->", cafe.registrar_salida(6))
# 📝 → Salida de 6 -> 4
#    ✅ Pasó por la puerta principal: 6 es positivo y 6 <= 10 → quedan 4.

# Un ajuste de inventario escrito por otra parte del programa
cafe.existencias = -5
# 📝 EL HUECO: aquí nadie llama registrar_salida, se escribe el atributo
#    directamente. Python lo permite sin preguntar.
#    ❌ cafe.existencias = -5 → nadie revisa → queda guardado -5.
print("Después del ajuste:", cafe)
# 📝 → Después del ajuste: Producto(sku='cafe-500g', existencias=-5)
#    ⚠️ Volvimos al problema del Encuentro 1 (stock negativo), y SIN ningún error.

# 📝 CONCLUSIÓN: la regla no vive en el lugar correcto. No basta con proteger UNA
#    operación; hay que proteger EL DATO, para que cualquier forma de cambiarlo
#    pase por la regla. Eso es lo que hace @property → inventario_property.py.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Por qué cafe.existencias = -5 no lanza error si la clase tiene una regla?
# 2. ¿Quién "se salta" la regla aquí? (Pista: "otra parte del programa".)
# 3. ¿Proteger un MÉTODO es lo mismo que proteger un DATO? Explícalo con este ejemplo.
# 4. Si el ajuste fuera cafe.existencias = 3, ¿habría algún problema? ¿Por qué no?
