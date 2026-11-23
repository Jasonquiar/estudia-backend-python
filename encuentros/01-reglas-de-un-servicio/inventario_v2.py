"""E01 · Demo v2: una entidad (Producto) y una operación que rechaza un cambio inválido.

Distingue dos tipos de rechazo:
- dato inválido (la solicitud está mal formada)  -> ValueError
- regla de negocio (la solicitud es válida, pero el negocio no la permite) -> MovimientoInvalido
"""
"""
📝 MIS NOTAS (Encuentro 1 · Reglas de un servicio · 11 nov 2026)

🎯 Idea central:
   La regla vive DENTRO del Producto, así que nadie puede dejar el stock en
   negativo. Además, el servicio dice POR QUÉ rechaza: un dato mal escrito no es
   lo mismo que algo que el negocio no permite.

🏪 Analogía:
   Ahora la bodega tiene un bodeguero con dos preguntas:
   1) "¿Lo que me pides tiene sentido?" → pedir -3 cafés es absurdo
      → ValueError (dato inválido: la solicitud está mal escrita).
   2) "¿Tengo suficiente?" → piden 6 y hay 4. La solicitud está bien escrita,
      pero el negocio no la puede cumplir → MovimientoInvalido (regla de negocio).

🔗 Viene de / lleva a:
   ⬅️ Viene de inventario_v1.py, donde El Paisa se llevaba 6 y quedaban -2.
   ➡️ Lleva a reservas_practica.py: el mismo patrón (ValueError + excepción
      propia) pero ahora lo escribes TÚ.
"""


class MovimientoInvalido(Exception):
    """Rechazo de negocio: el movimiento dejaría el inventario en un estado no permitido."""
    # 📝 Excepción PROPIA del negocio. Hereda de Exception y no necesita más código:
    #    lo que importa es el NOMBRE. Así el que llama puede atrapar justo
    #    este caso (except MovimientoInvalido) y tratarlo distinto a un ValueError.


class Producto:
    # 📝 Una ENTIDAD: guarda sus datos (sku, nombre, existencias) Y las
    #    operaciones que los cambian. La regla vive aquí, junto al dato que protege.
    def __init__(self, sku, nombre, existencias):
        # 📝 Primer control, al CREAR el producto: no puede nacer con stock negativo.
        #    ❌ Producto("x", "X", -5) → ValueError (dato inválido desde el inicio).
        if existencias < 0:
            raise ValueError("Las existencias iniciales no pueden ser negativas")
        self.sku = sku
        self.nombre = nombre
        self.existencias = existencias

    def registrar_salida(self, cantidad):
        # 📝 El ORDEN importa: primero valido el DATO y después la REGLA.
        #    Si la cantidad no tiene sentido, ni vale la pena revisar el stock.
        #
        # 📝 1) ¿El dato tiene sentido? Sacar 0 o un número negativo es absurdo.
        #    ❌ cantidad = -3 → ValueError (la solicitud está mal escrita)
        if cantidad <= 0:
            raise ValueError(f"Cantidad inválida: {cantidad}. Debe ser positiva")
        # 📝 2) La REGLA DE NEGOCIO. 👮 Aquí vive, y es el ÚNICO lugar donde está escrita.
        #    El dato es válido (6 es positivo), pero el negocio no lo permite.
        #    ✅ hay 10, piden 6 → pasa     ❌ hay 4, piden 6 → MovimientoInvalido
        if cantidad > self.existencias:  # REGLA: nunca quedar con stock negativo
            raise MovimientoInvalido(
                f"Stock insuficiente: hay {self.existencias}, se piden {cantidad}"
            )
        # 📝 3) Solo si pasó los dos controles, se toca el stock.
        #    Un raise corta la función, así que si hubo rechazo esta línea NUNCA corre.
        self.existencias -= cantidad
        return self.existencias

    def __repr__(self):
        # 📝 Define cómo se ve el objeto al imprimirlo: print(cafe).
        #    Sin esto, saldría algo feo como <__main__.Producto object at 0x7f...>.
        #    !r pone comillas al texto → sku='cafe-500g'.
        return f"Producto(sku={self.sku!r}, existencias={self.existencias})"


if __name__ == "__main__":
    # 📝 Este bloque solo corre si ejecutas ESTE archivo (python3 inventario_v2.py).
    #    Si otro archivo hace `import inventario_v2`, esta demo no se ejecuta.
    cafe = Producto("cafe-500g", "Café molido 500 g", 10)

    solicitudes = [
        ("Tienda Doña Rosa", 6),   # se espera ACEPTAR
        ("Tienda El Paisa", 6),    # se espera RECHAZAR por regla
        ("Tienda La Esquina", -3), # se espera RECHAZAR por dato inválido
    ]
    # 📝 Las mismas dos tiendas de v1, más un caso nuevo con un dato absurdo (-3).

    for tienda, cantidad in solicitudes:
        # 📝 try/except: "intenta esto y, si alguien lanza un error, atrápalo aquí".
        #    El Producto RECHAZA (raise) y el que llama DECIDE qué mostrar (except).
        #    Hay un except para cada tipo de rechazo → mensajes distintos.
        try:
            quedan = cafe.registrar_salida(cantidad)
            print(f"ACEPTADA  {tienda}: retira {cantidad} -> quedan {quedan}")
            # 📝 → ACEPTADA  Tienda Doña Rosa: retira 6 -> quedan 4
        except MovimientoInvalido as error:
            print(f"RECHAZADA {tienda} (regla de negocio): {error}")
            # 📝 → RECHAZADA Tienda El Paisa (regla de negocio): Stock insuficiente: hay 4, se piden 6
        except ValueError as error:
            print(f"RECHAZADA {tienda} (dato inválido): {error}")
            # 📝 → RECHAZADA Tienda La Esquina (dato inválido): Cantidad inválida: -3. Debe ser positiva

    print(cafe)
    # 📝 → Producto(sku='cafe-500g', existencias=4)
    #    ✅ Siguen siendo 4: los dos rechazos NO tocaron el stock. Compara con el -2 de v1.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Cuál es la diferencia entre un ValueError y un MovimientoInvalido? Da un
#    ejemplo de cada uno con este inventario.
# 2. ¿Por qué la regla vive DENTRO de registrar_salida y no en el for de abajo?
#    ¿Qué pasaría si otro programa usara Producto sin ese for?
# 3. Si inviertes el orden de los dos if y alguien pide -3, ¿cambia el resultado?
#    ¿Y si pide 0 con 0 existencias? Predice antes de probar.
# 4. ¿Por qué el último print muestra existencias=4 y no -2 ni -5?
