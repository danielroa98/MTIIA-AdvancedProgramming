"""
    Práctica 2, Ejercicio 1

    Daniel Roa
    00574499

    Fecha de entrega: dd/mm/aaaa

    Desarrolle un programa en Python que genere una arreglo NumPy
    tridimensional de tamaño $5x4x3$ con valores aleatorios entre 0 y 100.
    Posteriormente el programa debe encontrar el elemento más pequeño y el
    más grande e indicar la ubicación de dichos elementos dentro del arreglo.
    Imprima la matriz, los valores menor y mayor, así como sus ubicaciones.
    Guarde su programa en un archivo con extensión `.py`.
"""

import numpy as np

arr = np.random.randint(0, 101, size=(5, 4, 3))

min_val = np.min(arr)
max_val = np.max(arr)

pos_min = np.argwhere(arr == min_val)[0]
pos_max = np.argwhere(arr == max_val)[0]

print("Arreglo generado:\n", arr)
print(f"\nValor mínimo: {min_val} en la posición: {tuple(pos_min)}")
print(f"\nValor máximo: {max_val} en la posición: {tuple(pos_max)}")
