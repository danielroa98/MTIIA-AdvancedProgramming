"""
Práctica 6, Ejercicio 1

Daniel Roa
00574499

Fecha de entrega: 23/06/2025

Dadas dos listas de números, por ejemplo [1, 2, 3] y [4, 5, 6],
genera una nueva lista que contenga el producto de los elementos
correspondientes.
"""

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]

prod_lst = [a * b for a, b in zip(lst_1, lst_2)]

print(prod_lst)
