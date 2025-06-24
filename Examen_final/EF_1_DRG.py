"""
Examen final, Ejercicio 1

Daniel Roa
00574499

Fecha de entrega: 23/06/2025

Desarrolle una clase llamada funcion que debe tener las siguientes funcionalidades:
    - Un constructor __init__ que reciba como argumento la definición de la
    función. En la creación de la instancia pase como parámetro la función anónima
    empleando __lambda__.
    - Un método __call__ que permita evaluar un valor recibido como argumento en
    la función recibida.
    - Un método llamado tabular que reciba como argumentos a, b y n. El método
    debe crear un intervalo desde a hasta b con un número de particiones n (utilice
    el método linspace de numpy para ello). Se debe evaluar e imprimir todos los
    valores del intervalo en la función f(x).
    - Un método llamado graficar que reciba como argumetos a, b y n. El método
    debe crear un intervalo x desde a hasta b con un número de particiones n
    (utilice el método linspace de numpy para ello). Cree un intervalo y donde
    se evalúe cada valor de x en la función. Construya una gráfica con los
    valores en x y y empleando matplotlib.pyplot. Agregue algunas propiedades
    visuales de apoyo al gráfico.
    - Un método derivada que reciba como argumento x0 y h. El valor de h debe
    tener un valor predefinido de 1e-10. El método debe devolver la aproximación a
    la derivada de la función f(x) evaluada en x0. El cálculo se debe realizar mediante
    la fórmula:
    f'(x0) = (1/12) * (-f(x0-2h) + 8f(x0-h) - 8f(x0+h) + f(x0+2h))  
"""

import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable


class funcion:
    """
    Una clase para encapsular una función matemática y realizar operaciones
    como tabular, graficar y calcular su derivada numérica.
    """

    def __init__(self, __lambda__):
        """
        Constructor de la clase.

        Args:
            __lambda__ (function): Una función, preferiblemente lambda, que define
                                  la operación matemática a realizar.
        """
        self.f = __lambda__

    def __call__(self, x):
        """
        Permite que la instancia de la clase sea 'callable' (se pueda llamar como
        una función), evaluando la función almacenada.
        """
        return self.f(x)

    def tabular(self, a, b, n):
        """
        Crea un intervalo y evalúa la función en cada punto e imprime los resultados.
        """
        table = PrettyTable()
        table.field_names = ["x", "f(x)"]
        x_valores = np.linspace(a, b, n)
        for x in x_valores:
            y = self(x)
            table.add_row([x, y])
        print(table)

    def graficar(self, a, b, n):
        """
        Crea y muestra una gráfica de la función en el intervalo [a, b].
        """
        x_valores = np.linspace(a, b, n)
        y_valores = self(x_valores)

        plt.figure(figsize=(10, 6))
        plt.plot(x_valores, y_valores, label="f(x)", color="blue", linewidth=2)
        plt.title("Gráfica de la Función", fontsize=16)
        plt.xlabel("Eje X", fontsize=12)
        plt.ylabel("Eje Y", fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        plt.legend()
        plt.show()

    def derivada(self, x0, h=1e-10):
        """
        Calcula la derivada numérica de la función en el punto x0.
        """
        numerador = (
            self(x0 - 2 * h) - 8 * self(x0 - h) + 8 * self(x0 + h) - self(x0 + 2 * h)
        )
        denominador = 12 * h
        return numerador / denominador


# --------------------------------------------------------------------------
#                      El uso de la clase no cambia
# --------------------------------------------------------------------------

# Al crear la instancia, simplemente pasas la función lambda como argumento posicional.
# El nombre del parámetro (__lambda__) solo es relevante dentro del método __init__.
f_ejemplo = funcion(lambda x: x**2 * np.sin(x))

# El resto del código funciona exactamente igual
print(f"El valor de f(pi/2) es: {f_ejemplo(np.pi/2):.4f}")

f_ejemplo.tabular(0, 2 * np.pi, 20)

derivada_en_pi = f_ejemplo.derivada(np.pi)
print(f"La derivada en x=pi es aproximadamente: {derivada_en_pi:.8f}")

f_ejemplo.graficar(0, 2 * np.pi, 200)
