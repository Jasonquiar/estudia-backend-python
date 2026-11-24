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
# 📝 MIS NOTAS (Encuentro 4 · Práctica: una función con muchas ramas · 23 nov 2026)
#
# 🎯 Idea central:
#    Una sola función, calcular_tarifa, con MUCHAS decisiones (if/elif/or/and).
#    Las pruebas actuales pasan, pero:
#    📊 la cobertura de ramas es 75 % (hay reglas que ninguna prueba ejecuta), y
#    🌳 Ruff dice: C901 `calcular_tarifa` is too complex (17 > 10).
#
# 🧮 Ejemplo calculado A MANO desde las reglas (no desde el código):
#    3 km, El Poblado, 10 a. m., regular, sin lluvia
#    → distancia 6.000 + comuna 1.500 = 7.500 → hora normal → regular → 7.500 ✅ (test_recargo_el_poblado)
#
# ⚠️ El ORDEN importa: los recargos fijos (comuna, lluvia) se suman ANTES de los porcentajes
#    (hora, cliente). Primero sumas, luego multiplicas.
#
# 🫵 Práctica (ver README). Las notas NO la resuelven: solo dejo pistas.
#    1. Leer el reporte de cobertura → elegir una rama sin cubrir → escribir su prueba.
#    2. UNA mejora: retornos tempranos, una tabla (diccionario) o extraer una función.
#    3. Repetir cobertura y ruff. Las pruebas deben seguir verdes.
#    📦 Entregable: complejidad antes/después, cobertura antes/después y qué prueba
#       les habría avisado si la mejora hubiera cambiado el comportamiento.
#
# ▶️ ruff check --isolated --select C901 --config 'lint.mccabe.max-complexity=1' \
#        --output-format concise src/tarifa.py
#    → src/tarifa.py:46:5: C901 `calcular_tarifa` is too complex (17 > 1)   (sale con código 1 a propósito)
#    🧮 ¿De dónde sale 17? 1 (el camino base) + 1 por cada if y cada elif (hay 16).
#       Ruff (mccabe) NO suma los "or"/"and": por eso no pasa de 17.
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
        # 📝 "Se cobra completo": 10,3 km → ceil(0,3) = 1 km adicional → 9.000 + 1.200.
        #    🔎 Ninguna prueba actual pasa de 10 km: esta línea sale en "Missing".

    # 📝 Comunas que no están en la lista (por ejemplo "Robledo", la de casi todas las pruebas): +0.
    #    🔎 Santa Elena y Belén no las prueba nadie todavía.
    if comuna == "El Poblado" or comuna == "Laureles":
        tarifa += 1500
    elif comuna == "Santa Elena":
        tarifa += 3000
    elif comuna == "Belén":
        tarifa += 500

    if llueve:
        tarifa += 2000

    # 📝 Bordes de hora: 22 SÍ es noche (>=), 6 NO es noche (<). 14 y 20 ya NO son hora pico.
    #    💡 Buenos candidatos para parametrize: 21/22, 5/6, 13/14, 19/20.
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
        # 📝 Cliente nuevo a MÁS de 2 km: no hay descuento (el if no hace nada).
        #    🔎 En el reporte sale como rama parcial: el "no" de este if nunca se probó.
    # 📝 Un cliente "regular" (el de casi todas las pruebas) no entra a ningún if: paga la tarifa completa.

    return int(round(tarifa / 100.0) * 100)
    # 📝 Redondeo a la centena. Python redondea "al par" en la mitad exacta:
    #    7.650 → round(76,5) = 76 → 7.600   ·   7.750 → round(77,5) = 78 → 7.800.
    #    ⚠️ Si al refactorizar cambias el redondeo (por ejemplo a "siempre hacia arriba"),
    #       cambias el comportamiento: eso NO es una mejora válida en esta práctica.
    #    💡 Ojo también con los decimales: 6.000 × 1,10 da 6600.000000000001 en Python;
    #       el redondeo final es el que lo deja en 6.600.

# ❓ PREGUNTAS DE REPASO (responde sin mirar arriba)
# 1. Calcula A MANO: 12 km, Santa Elena, 23 h, frecuente, con lluvia. ¿Cuánto da? Luego escribe la prueba.
# 2. ¿Por qué "el esperado sale de las reglas, no de leer el código"? ¿Qué pasa si lo sacas del código?
# 3. Si cambias los if de la comuna por un diccionario, ¿qué prueba te avisaría si se te olvida Laureles?
# 4. ¿Bajar la complejidad cambia la cobertura? ¿Y subir la cobertura cambia la complejidad?
