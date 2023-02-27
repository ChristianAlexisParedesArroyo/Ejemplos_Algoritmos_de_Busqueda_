# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 22:56:33 2023

@author: Christian
"""

class RedContactos:
    def __init__(self, contactos):
        self.contactos = contactos

    def buscar_persona(self, inicio, objetivo):
        # Creamos un conjunto para guardar los nodos visitados
        visitados = set()

        # Función recursiva para la búsqueda en profundidad
        def dfs(persona):
            visitados.add(persona)
            if persona == objetivo:
                return [persona]
            for vecino in self.obtener_vecinos(persona):
                if vecino not in visitados:
                    resultado = dfs(vecino)
                    if resultado is not None:
                        resultado.insert(0, persona)
                        return resultado
            return None

        # Llamamos a la función recursiva desde la persona de inicio
        resultado = dfs(inicio)

        return resultado

    def obtener_vecinos(self, persona):
        # Obtiene los vecinos de una persona en la red de contactos
        return self.contactos[persona]
    
contactos = {
    'Juan': ['Maria', 'Pedro', 'Sofia'],
    'Maria': ['Juan', 'Sofia', 'Luis'],
    'Pedro': ['Juan', 'Sofia'],
    'Sofia': ['Juan', 'Maria', 'Luis', 'Pedro'],
    'Luis': ['Maria', 'Sofia']
}

red = RedContactos(contactos)
camino = red.buscar_persona('Maria', 'Pedro')
print(camino)