"""
Práctica 2, Ejercicio 2

Daniel Roa
00574499

Fecha de entrega: dd/mm/aaaa

Dada la matriz tridimensional H:
H = ([1, 2, 3],    [7, 8, 9],
     [4, 5, 6],    [10, 11, 12])
Calcula la transpuesta de cada ”plano” dentro
de la matriz tridimensional H.
Guarde su programa enun archivo con extensi´on .py.
"""

import numpy as np

H = np.array([[[1, 2, 3],
               [4, 5, 6]],
              [[7, 8, 9],
               [10, 11, 12]]])

print(f"Dimensiones del arreglo original {H.shape}")

H_transpuesta = np.transpose(H, (0, 2, 1))
print(f"Dimensiones del arreglo transpuesto {H_transpuesta.shape}")

print(f"Matriz original:\n{H}")
print(f"\nMatriz transpuesta:\n{H_transpuesta}")
