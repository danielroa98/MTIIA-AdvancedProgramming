"""
Práctica 5, Ejercicio 1

Daniel Roa
00574499

Fecha de entrega: 02/06/2025

Dada una lista de números enteros cualquiera, utilice los métodos map,
filter y reduce para filtrar los números impares de la lista y calcular
la suma de sus cuadrados.
"""

import random
from functools import reduce

# Decidí usar `random` para que las pruebas sean más variadas
# y no dependan de una lista fija.
nums = list(random.randint(0, 101) for _ in range(10))

print(f"Lista para evaluar: {nums}")

nums_impares = list(filter(lambda x: x % 2 != 0, nums))

cuadrados = list(map(lambda x: x**2, nums_impares))

suma_cuadrados = reduce(lambda x, y: x + y, cuadrados)
print(f"{'*-'*30}*")
print("Resultados:")
print("1) Lista original:", nums)
print("2) Números impares:", nums_impares)
print("3) Cuadrados de los impares:", cuadrados)
print("4) Suma de los cuadrados:", suma_cuadrados)
