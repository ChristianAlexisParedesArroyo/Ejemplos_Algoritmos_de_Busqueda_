# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 23:32:21 2023

@author: Christian
"""

from collections import deque

class RedTransporte:
    def __init__(self, conexiones):
        self.conexiones = conexiones

    def buscar_camino(self, origen, destino):
        # Creamos un diccionario para guardar los padres de cada nodo visitado
        padres = {origen: None}

        # Creamos una cola para realizar la búsqueda en amplitud
        cola = deque([origen])

        while cola:
            actual = cola.popleft()
            if actual == destino:
                # Construimos el camino desde el origen al destino
                camino = []
                while actual:
                    camino.insert(0, actual)
                    actual = padres[actual]
                return camino

            # Visitamos los vecinos del nodo actual
            for vecino in self.obtener_vecinos(actual):
                if vecino not in padres:
                    padres[vecino] = actual
                    cola.append(vecino)

        # Si no se encontró un camino, retornamos None
        return None

    def obtener_vecinos(self, ciudad):
        # Obtiene los vecinos de una ciudad en la red de transporte público
        return self.conexiones[ciudad]
    
conexiones = {
    'Parada 1': ['Parada 2', 'Parada 3'],
    'Parada 2': ['Parada 1', 'Parada 4'],
    'Parada 3': ['Parada 1', 'Parada 4', 'Parada 5'],
    'Parada 4': ['Parada 2', 'Parada 3', 'Parada 6'],
    'Parada 5': ['Parada 3', 'Parada 6'],
    'Parada 6': ['Parada 4', 'Parada 5']
}

red = RedTransporte(conexiones)
camino = red.buscar_camino('Parada 1', 'Parada 6')
print(camino)