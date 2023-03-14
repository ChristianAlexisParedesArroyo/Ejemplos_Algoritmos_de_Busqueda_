# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:42:28 2023

@author: Christian
"""

import random

# Definir las rutas y sus respectivos tiempos de viaje y costos
rutas = {
    'ruta1': {'tiempo': 40, 'costo': 3},
    'ruta2': {'tiempo': 35, 'costo': 4},
    'ruta3': {'tiempo': 30, 'costo': 5},
    'ruta4': {'tiempo': 45, 'costo': 2}
}

# Definir la función que evalúa una ruta en función de su tiempo de viaje y costo
def evaluar_ruta(ruta):
    return ruta['tiempo'] + ruta['costo']

# Definir la función de ascenso de la colina
def ascenso_colina(rutas):
    ruta_actual = random.choice(list(rutas.keys()))
    evaluacion_actual = evaluar_ruta(rutas[ruta_actual])
    while True:
        vecinos = []
        for ruta in rutas:
            if ruta != ruta_actual:
                vecinos.append(ruta)
        mejor_vecino = None
        mejor_evaluacion = evaluacion_actual
        random.shuffle(vecinos)  # Aleatorizar la lista de vecinos para variar la selección
        for vecino in vecinos:
            evaluacion_vecino = evaluar_ruta(rutas[vecino])
            if evaluacion_vecino < mejor_evaluacion:
                mejor_vecino = vecino
                mejor_evaluacion = evaluacion_vecino
        if mejor_evaluacion >= evaluacion_actual:
            break
        ruta_actual = mejor_vecino
        evaluacion_actual = mejor_evaluacion
    return ruta_actual

# Establecer una semilla aleatoria diferente en cada ejecución
random.seed()

# Llamar a la función de ascenso de la colina para encontrar la mejor ruta
mejor_ruta = ascenso_colina(rutas)
print('La mejor ruta es:', mejor_ruta)