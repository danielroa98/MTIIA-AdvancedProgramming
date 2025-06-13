"""
Práctica 6, Ejercicio 3

Daniel Roa
00574499

Fecha de entrega: 23/06/2025

Dada una lista de listas de números, utiliza una expresión
generadora para calcular la media de todos los números.

Ejemplo: Para la lista:

[
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

el resultado debería ser 4.5.
"""

test_lst = [[1, 2, 3], [4, 5], [6, 7, 8]]

total_sum = sum(x for sublist in test_lst for x in sublist)
cont = sum(len(sublist) for sublist in test_lst)
avg = total_sum / cont

print(avg)
