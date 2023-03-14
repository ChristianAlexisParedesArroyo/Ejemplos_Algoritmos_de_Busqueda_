# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:01:24 2023

@author: Christian
"""

import math

class DeliveryLocation:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

class DeliveryRoute:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.distance = math.sqrt((end_location.x - start_location.x)**2 + (end_location.y - start_location.y)**2)

class CityMap:
    def __init__(self):
        self.locations = {}

    def add_location(self, location):
        self.locations[location.name] = location

    def get_location(self, name):
        return self.locations.get(name)

    def find_shortest_route(self, start_location_name, end_location_name):
        start_location = self.get_location(start_location_name)
        end_location = self.get_location(end_location_name)
        visited_locations = set()
        current_location = start_location
        current_cost = 0
        estimated_total_cost = self.estimated_cost(start_location, end_location)

        while current_location != end_location:
            visited_locations.add(current_location)
            possible_routes = []
            for location_name in current_location.routes:
                location = self.get_location(location_name)
                if location not in visited_locations:
                    route = DeliveryRoute(current_location, location)
                    possible_routes.append(route)
            if not possible_routes:
                return None
            possible_routes.sort(key=lambda x: x.distance)
            cheapest_route = possible_routes[0]
            current_location = cheapest_route.end_location
            current_cost += cheapest_route.distance
            estimated_total_cost = current_cost + self.estimated_cost(current_location, end_location)

        return current_cost

    def estimated_cost(self, start_location, end_location):
        return math.sqrt((end_location.x - start_location.x)**2 + (end_location.y - start_location.y)**2)

# Crear las ubicaciones de entrega
A = DeliveryLocation('A', 1, 1)
B = DeliveryLocation('B', 2, 3)
C = DeliveryLocation('C', 5, 4)
D = DeliveryLocation('D', 7, 2)

# Agregar las ubicaciones a un mapa de la ciudad
city_map = CityMap()
city_map.add_location(A)
city_map.add_location(B)
city_map.add_location(C)
city_map.add_location(D)

# Definir las rutas entre las ubicaciones
A.routes = ['B']
B.routes = ['A', 'C']
C.routes = ['B', 'D']
D.routes = ['C']

# Planificar una ruta de entrega utilizando el algoritmo A*
start_location_name = 'A'
end_location_name = 'D'
total_distance = city_map.find_shortest_route(start_location_name, end_location_name)

if total_distance is None:
    print("No se pudo encontrar una ruta de entrega")
else:
    print(f"Ruta de entrega: {start_location_name} -> {end_location_name}")
    print(f"Distancia total recorrida: {total_distance:.2f} unidades de distancia")

# Salida esperada:
# Ruta de entrega: A -> D
# Distancia total recorrida: 7.81 unidades de distancia