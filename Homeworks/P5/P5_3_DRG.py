"""
Práctica 5, Ejercicio 3

Daniel Roa
00574499

Fecha de entrega: 02/06/2025

Existe un método llamado mínimos cuadrados que en su caso lineal permite
obtener una línea recta que se aproxima a una serie de $m$ puntos $(x, y)$.
La recta resultante del método es $y = a_0 + a_1x$, y para calcular los
coeficientes $a_0$ y $a_1$ se utilizan las siguientes fórmulas:

...

Desarrolle un programa en Python que realice el cálculo de las fórmulas,
utilice las funciones `lambda`, `map`, `filter` y/o `reduce` para el calculo
de las sumatorias según sea necesario. Considere que los puntos para el
cálculo se reciben como una lista de tuplas (cada tupla es un punto $(x, y)$)
y $m$ es el número de tuplas en la lista.

Considere este ejemplo del método como referencia:
...
"""

test_data = [
    (1, 1.3),
    (2, 3.5),
    (3, 4.2),
    (4, 5),
    (5, 7),
    (6, 8.8),
    (7, 10.1),
    (8, 12.5),
    (9, 13),
    (10, 15.6),
]

m = len(test_data)

sum_x = sum(map(lambda x: x[0], test_data))
sum_y = sum(map(lambda x: x[1], test_data))

sum_x_sq = sum(map(lambda x: x[0] ** 2, test_data))

sum_xy = sum(map(lambda x: x[0] * x[1], test_data))

den = m * sum_x_sq - sum_x**2

num_0 = sum_x_sq * sum_y - sum_xy * sum_x
num_1 = m * sum_xy - sum_x * sum_y

a_0 = num_0 / den
a_1 = num_1 / den

print(f"a_0: {a_0:.3f}, a_1: {a_1:.3f}")
print(f"y = {a_0:.3f} + {a_1:.3f}x")
