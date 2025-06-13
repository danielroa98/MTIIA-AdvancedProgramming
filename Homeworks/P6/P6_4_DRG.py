"""
Práctica 6, Ejercicio 3

Daniel Roa
00574499

Fecha de entrega: 23/06/2025

Utiliza una expresión generadora para calcular la varianza de una
lista de números.

La varianza se calcula como la media de los cuadrados de las diferencias
con la media.

Ejemplo: Para la lista:

[1, 2, 3, 4, 5]

el resultado debería ser 2.0.
"""

test_lst = [1, 2, 3, 4, 5]

mu = sum(test_lst) / len(test_lst)
var = sum((x - mu) ** 2 for x in test_lst) / len(test_lst)

print(var)
