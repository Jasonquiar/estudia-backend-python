"""Tarifa de un domicilio en Medellín, en pesos colombianos.

Reglas, en este orden:
1. Distancia: hasta 2 km, 4.000; hasta 5 km, 6.000; hasta 10 km, 9.000; más de 10 km,
   9.000 más 1.200 por cada km adicional (se cobra completo). Más de 25 km no se atiende.
2. Comuna: El Poblado y Laureles, +1.500; Santa Elena, +3.000; Belén, +500.
3. Lluvia: +2.000.
4. Hora: de 10 p. m. a 6 a. m., +25 %; de 12 a 2 p. m. y de 6 a 8 p. m., +10 %.
5. Cliente: frecuente, -10 %; empresa, -15 % hasta 10 km y -5 % si es más lejos;
   nuevo, gratis hasta 2 km.
El valor final se redondea a la centena; si queda justo a la mitad, a la centena par (7.650 → 7.600).
"""
from math import ceil


class FueraDeCobertura(Exception):
    """El domicilio queda más lejos de lo que se atiende."""


def calcular_tarifa(distancia_km, comuna, hora, cliente, llueve=False):
    if distancia_km <= 0:
        raise ValueError(f"Distancia inválida: {distancia_km}. Debe ser positiva")
    if distancia_km > 25:
        raise FueraDeCobertura(f"{distancia_km} km queda fuera de cobertura (máximo 25)")

    if distancia_km <= 2:
        tarifa = 4000
    elif distancia_km <= 5:
        tarifa = 6000
    elif distancia_km <= 10:
        tarifa = 9000
    else:
        tarifa = 9000 + 1200 * ceil(distancia_km - 10)

    if comuna == "El Poblado" or comuna == "Laureles":
        tarifa += 1500
    elif comuna == "Santa Elena":
        tarifa += 3000
    elif comuna == "Belén":
        tarifa += 500

    if llueve:
        tarifa += 2000

    if hora >= 22 or hora < 6:
        tarifa = tarifa * 1.25
    elif 12 <= hora < 14 or 18 <= hora < 20:
        tarifa = tarifa * 1.10

    if cliente == "frecuente":
        tarifa = tarifa * 0.90
    elif cliente == "empresa":
        if distancia_km <= 10:
            tarifa = tarifa * 0.85
        else:
            tarifa = tarifa * 0.95
    elif cliente == "nuevo":
        if distancia_km <= 2:
            tarifa = 0

    return int(round(tarifa / 100.0) * 100)
