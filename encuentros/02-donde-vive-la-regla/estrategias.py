"""E02 · Herencia con super() y composición con dos estrategias pequeñas."""
"""
📝 MIS NOTAS (Encuentro 2 · Dónde vive la regla · 18 nov 2026)

🎯 Idea central:
   Hay dos formas de reutilizar y extender una clase:
   - HERENCIA ("ES UN"): un ProductoPerecedero ES un Producto, con una regla extra.
   - COMPOSICIÓN ("TIENE UN"): un Producto TIENE una política de precio que se
     puede cambiar por otra sin tocar la clase Producto.

🏪 Analogía:
   Herencia: la leche es un producto de la tienda como cualquier otro, pero el
   bodeguero además mira la fecha de vencimiento antes de despacharla.
   Composición: cada producto lleva pegada una tarjeta de precio, "detal" o
   "mayorista". Cambias la tarjeta y cambia el cálculo; el producto sigue igual.

🔗 Viene de / lleva a:
   ⬅️ Viene de inventario_property.py (la regla vive dentro del objeto).
   ➡️ Lleva al reto de taller_practica.py y solucion/taller_solucion.py:
      ¿lista de espera con herencia o con composición?
"""


class MovimientoInvalido(Exception):
    pass


class Producto:
    # 📝 Versión simplificada del Producto (sin property ni ValueError) para
    #    enfocarse en herencia y composición.
    def __init__(self, nombre, existencias, precio, politica):
        self.nombre = nombre
        self.existencias = existencias
        self.precio = precio
        self.politica = politica  # COMPOSICIÓN: el producto TIENE una política de precio
        # 📝 `politica` es OTRO objeto (PrecioDetal o PrecioMayorista).
        #    El producto no sabe cómo se calcula el precio: se lo pregunta a su política.

    def registrar_salida(self, cantidad):
        # 📝 1) Regla de stock (la de siempre). 2) Descuenta. 3) Le pide el total a la política.
        if cantidad > self.existencias:
            raise MovimientoInvalido(f"Stock insuficiente: hay {self.existencias}, se piden {cantidad}")
        self.existencias -= cantidad
        return self.politica.total(cantidad, self.precio)
        # 📝 DELEGA: "política, calcula tú". Producto no tiene ningún if de "detal/mayorista".


class ProductoPerecedero(Producto):
    """HERENCIA: un producto perecedero ES un producto, con una regla más."""
    # 📝 (Producto) entre paréntesis = hereda TODO de Producto: atributos y métodos.

    def __init__(self, nombre, existencias, precio, politica, dias_para_vencer):
        super().__init__(nombre, existencias, precio, politica)
        # 📝 super() = "la clase padre". Reutiliza el __init__ de Producto para
        #    no repetir las 4 líneas, y después agrega lo nuevo:
        self.dias_para_vencer = dias_para_vencer

    def registrar_salida(self, cantidad):  # OVERRIDE: mismo nombre, regla adicional
        # 📝 OVERRIDE = reemplaza el método del padre con uno del mismo nombre.
        #    Primero revisa SU regla extra (vencimiento)...
        #    ❌ dias_para_vencer = 0 → "está vencido", sin mirar siquiera el stock.
        if self.dias_para_vencer <= 0:
            raise MovimientoInvalido(f"{self.nombre} está vencido")
        return super().registrar_salida(cantidad)  # reutiliza la regla del padre
        # 📝 ...y después le pasa el trabajo al padre (stock + precio).
        #    La regla de stock sigue viviendo en UN solo lugar: Producto.


# Dos estrategias pequeñas: mismo método, cálculo distinto (polimorfismo)
# 📝 POLIMORFISMO: ambas clases tienen total(cantidad, precio). A Producto no le
#    importa cuál le toca; solo llama .total() y cada una responde a su manera.
class PrecioDetal:
    def total(self, cantidad, precio):
        return cantidad * precio
        # 📝 Precio normal → 12 × 18000 = 216000


class PrecioMayorista:
    def total(self, cantidad, precio):
        descuento = 0.10 if cantidad >= 12 else 0
        # 📝 10 % de descuento si llevan 12 o más. Si no, 0.
        return round(cantidad * precio * (1 - descuento))
        # 📝 12 × 4500 = 54000 → × 0.90 = 48600. round() lo deja como número entero.


cafe = Producto("Café 500 g", 40, 18000, PrecioDetal())
leche = ProductoPerecedero("Leche 1 L", 30, 4500, PrecioMayorista(), dias_para_vencer=3)
yogur = ProductoPerecedero("Yogur 1 L", 10, 7000, PrecioDetal(), dias_para_vencer=0)
# 📝 Fíjate en el último argumento de cafe/leche/yogur: la política se ESCOGE al crear.
#    Leche y yogur son perecederos, pero con políticas distintas: herencia y composición juntas.

for producto, cantidad in [(cafe, 12), (leche, 12), (yogur, 2)]:
    # 📝 El for no pregunta "¿eres perecedero?": llama registrar_salida y cada
    #    objeto ejecuta SU versión (otra vez polimorfismo).
    try:
        total = producto.registrar_salida(cantidad)
        print(f"ACEPTADA  {producto.nombre} x{cantidad}: ${total:,}".replace(",", "."))
        # 📝 {total:,} pone comas de miles (216,000) y .replace las vuelve puntos (216.000).
        # 📝 → ACEPTADA  Café 500 g x12: $216.000     (detal, sin descuento)
        # 📝 → ACEPTADA  Leche 1 L x12: $48.600       (mayorista, 10 % menos)
    except MovimientoInvalido as error:
        print(f"RECHAZADA {producto.nombre} x{cantidad}: {error}")
        # 📝 → RECHAZADA Yogur 1 L x2: Yogur 1 L está vencido
        #    Hay stock (10), pero la regla extra del perecedero lo rechaza primero.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. ¿Cuál es la diferencia entre "ES UN" (herencia) y "TIENE UN" (composición)?
#    Da un ejemplo de cada uno en este archivo.
# 2. ¿Qué hace super().registrar_salida(cantidad) y por qué no se copia el código del padre?
# 3. Si quisieras una política "PrecioPromo" (2×1), ¿qué clase tendrías que crear?
#    ¿Tendrías que tocar Producto? ¿Por qué no?
# 4. ¿Qué imprimiría la leche si se llevaran 11 en vez de 12? Predice antes de probar.
