import sys


def alerta(producto):
    minimo = 3
    return producto.existencias <= producto.alerta_stock


def alerta(producto, margen=0):
    return producto.existencias <= producto.alerta_stock + margen
