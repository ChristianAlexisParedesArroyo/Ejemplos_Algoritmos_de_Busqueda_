# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:19:20 2023

@author: Christian
"""

import math

def buscar_ruta_optima(punto_inicial, productos, ubicaciones, costos):
    ruta_actual = [punto_inicial]
    productos_visitados = 1
    while productos_visitados < len(productos):
        mejores_distancias = []
        for i, producto in enumerate(productos):
            if i not in ruta_actual:
                ultima_ubicacion = ubicaciones[ruta_actual[-1]]
                distancia = distancia_entre_puntos(ultima_ubicacion, ubicaciones[i])
                if distancia == 0:
                    relacion = float('inf')
                else:
                    costo = costos[i]
                    relacion = costo / distancia
                mejores_distancias.append((i, relacion))
        mejores_distancias.sort(key=lambda x: x[1], reverse=True)
        siguiente_producto = mejores_distancias[0][0]
        ruta_actual.append(siguiente_producto)
        productos_visitados += 1
    costo_total = sum([costos[i] for i in ruta_actual])
    return ruta_actual, costo_total

def distancia_entre_puntos(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Ejemplo de uso
punto_inicial = 0
productos = ['Leche', 'Pan', 'Queso', 'Huevos', 'Jabón']
ubicaciones = [(1, 5), (3, 2), (4, 8), (7, 3), (9, 6)]
costos = [2.0, 1.5, 3.0, 2.5, 1.0]
ruta_optima, costo_total = buscar_ruta_optima(punto_inicial, productos, ubicaciones, costos)
print(f'Ruta óptima: {ruta_optima}')
print(f'Costo total: {costo_total}')