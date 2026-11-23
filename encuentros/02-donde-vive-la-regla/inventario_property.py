"""E02 · La regla vive en el objeto: una property protege las existencias."""
"""
📝 MIS NOTAS (Encuentro 2 · Dónde vive la regla · 18 nov 2026)

🎯 Idea central:
   Con @property la regla se pega AL DATO: cualquier línea que escriba
   cafe.existencias = algo pasa obligatoriamente por el setter, donde vive la regla.

🏪 Analogía:
   El cuaderno de existencias ahora está en una caja y solo el bodeguero lo
   puede escribir. Tú le dices "pon -5" y él revisa antes de anotar: "no, eso
   no se puede". (Aunque, si alguien rompe la caja (_existencias), igual
   puede escribir. Mira el final del archivo.)

🔗 Viene de / lleva a:
   ⬅️ Viene de inventario_hueco.py, donde cafe.existencias = -5 pasaba sin control.
   ➡️ Lleva a estrategias.py (herencia y composición) y a taller_practica.py,
      donde TÚ proteges el cupo con una @property.

📚 Además se ven: atributo de CLASE vs. de INSTANCIA, y __str__ vs. __repr__.
"""


class MovimientoInvalido(Exception):
    """Rechazo de negocio: el movimiento dejaría el inventario en un estado no permitido."""


class Producto:
    alerta_stock = 3  # atributo de CLASE: el mismo para todos los productos
    # 📝 Vive en la CLASE, no en cada objeto. cafe y panela lo comparten.
    #    Si lo cambias en la clase (Producto.alerta_stock = 1), cambia para TODOS.

    def __init__(self, sku, nombre, existencias):
        self.sku = sku            # atributos de INSTANCIA: propios de cada producto
        self.nombre = nombre
        self.existencias = existencias  # pasa por el setter: la regla se aplica desde el inicio
        # 📝 Este "=" no guarda directo: llama al SETTER de abajo.
        #    ❌ Producto("x", "X", -1) → el setter lanza MovimientoInvalido.
        #    💡 Diferencia con el Encuentro 1: allá un stock inicial negativo era
        #    ValueError; aquí el setter usa MovimientoInvalido para todos los casos.

    @property
    def existencias(self):
        # 📝 GETTER: se ejecuta cuando alguien LEE → print(cafe.existencias)
        #    Devuelve el valor "real", guardado en _existencias (con guion bajo).
        return self._existencias

    @existencias.setter
    def existencias(self, valor):
        # 📝 SETTER: se ejecuta cuando alguien CAMBIA → cafe.existencias = algo
        #    👮 Aquí vive la regla. Es el ÚNICO lugar donde está escrita.
        #    ✅ cafe.existencias = 4 → guarda 4    ❌ cafe.existencias = -5 → rechaza
        if valor < 0:  # REGLA: nunca quedar con stock negativo
            raise MovimientoInvalido(f"Existencias inválidas: {valor}")
        self._existencias = valor
        # 📝 Guarda en _existencias y NO en self.existencias. Si escribiera
        #    self.existencias = valor, se llamaría a sí mismo para siempre (RecursionError).

    def registrar_salida(self, cantidad):
        # 📝 Este método sigue teniendo sus controles (dato y stock), pero ya no
        #    es la única defensa: aunque alguien olvide usarlo, el setter protege.
        if cantidad <= 0:
            raise ValueError(f"Cantidad inválida: {cantidad}. Debe ser positiva")
        if cantidad > self.existencias:
            raise MovimientoInvalido(f"Stock insuficiente: hay {self.existencias}, se piden {cantidad}")
        self.existencias -= cantidad
        # 📝 Esto también pasa por el getter (leer) y luego por el setter (escribir).
        return self.existencias

    def necesita_pedido(self):
        # 📝 True si quedan pocas unidades. Lee alerta_stock con self.: como panela
        #    no tiene uno propio, Python lo busca en la CLASE.
        return self.existencias <= self.alerta_stock

    def __repr__(self):  # para quien programa: sin ambigüedad
        return f"Producto(sku={self.sku!r}, existencias={self.existencias})"

    def __str__(self):   # para quien usa el sistema: legible
        return f"{self.nombre}: {self.existencias} unidades"
    # 📝 __str__ = versión "bonita" para el usuario (print(cafe)).
    #    __repr__ = versión "técnica" para quien programa (listas, depuración, repr()).


cafe = Producto("cafe-500g", "Café molido 500 g", 10)
panela = Producto("panela-1kg", "Panela 1 kg", 2)

print(cafe)            # usa __str__
# 📝 → Café molido 500 g: 10 unidades
print([cafe, panela])  # dentro de una lista se usa __repr__
# 📝 → [Producto(sku='cafe-500g', existencias=10), Producto(sku='panela-1kg', existencias=2)]

try:
    cafe.existencias = -5
    # 📝 La MISMA línea que en inventario_hueco.py… pero ahora pasa por el setter.
except MovimientoInvalido as error:
    print("RECHAZADO:", error)
    # 📝 → RECHAZADO: Existencias inválidas: -5
    #    ✅ El hueco está tapado: cafe sigue con 10.

print("¿Pedir panela?", panela.necesita_pedido())
# 📝 → ¿Pedir panela? True       (2 <= 3)
Producto.alerta_stock = 1
# 📝 Cambia el atributo de CLASE → afecta a cafe y a panela al mismo tiempo.
print("¿Pedir panela con alerta 1?", panela.necesita_pedido())
# 📝 → ¿Pedir panela con alerta 1? False   (2 <= 1 es False)

# El guion bajo es una convención, no una cerradura:
cafe._existencias = -5
# 📝 Escribe DIRECTO en el atributo "real" y se salta el setter.
#    En Python el "_" significa "privado, no toques", pero no lo impide de verdad.
#    La property protege contra errores normales, no contra alguien que quiere saltársela.
print("Saltando la property:", repr(cafe))
# 📝 → Saltando la property: Producto(sku='cafe-500g', existencias=-5)

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Qué se ejecuta cuando escribes cafe.existencias = -5? ¿Y cuando lees cafe.existencias?
# 2. ¿Por qué el setter guarda en self._existencias y no en self.existencias?
# 3. Si en vez de Producto.alerta_stock = 1 escribes panela.alerta_stock = 1,
#    ¿cambia también para cafe? Predice antes de probar.
# 4. ¿Qué diferencia hay entre print(cafe) y print([cafe])? ¿Qué método usa cada uno?
