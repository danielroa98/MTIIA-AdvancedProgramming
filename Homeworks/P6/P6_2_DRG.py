"""
Práctica 6, Ejercicio 2

Daniel Roa
00574499

Fecha de entrega: 23/06/2025

Dada una lista de diccionarios que representan personas con claves
“nombre”, “edad” y “ciudad”, genera una nueva lista de nombres de
personas que tengan más de 30 años y vivan en “Madrid”.

Ejemplo: Para la lista

[
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Juan", "edad": 35, "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": 32, "ciudad": "Barcelona"}
]

el resultado debería ser `[“Juan”]`.
"""

people_lst = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Juan", "edad": 35, "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": 32, "ciudad": "Barcelona"},
]

filtered_people = [
    person["nombre"]
    for person in people_lst
    if person["ciudad"] == "Madrid" and person["edad"] > 30
]

print(filtered_people)
