"""
    Práctica 3, Ejercicio 1

    Daniel Roa
    00574499

    Fecha de entrega: dd/mm/aaaa

    Escriba una clase llamada vector que deberá tener dos propiedades
    x, y para almacenar la posición del vector en el plano cartesiano.
    Además debe tener un método que calcule la magnitud del vector,
    uno que determine el ángulo en radianes y otro método que determine el
    ángulo en grados. La clase debe utilizar la función str() para mostrar
    la representación del vector de la forma (x, y).

    La clase también debe utiluizar la función add para la suma de vectores.
    Recuerde que la suma de dos vectores se hace
    por compontentes x y por componentes y.
    La suma debe devolver el resultado como vector en la forma (x, y).
"""
import math


class Vector:
    """
    Representa un vector bidimensional con coordenadas x e y.

    Esta clase permite realizar operaciones básicas con vectores, como
    calcular su magnitud, ángulo y sumarlos.

    Attributes:
        x (float): La coordenada x del vector.
        y (float): La coordenada y del vector.
    """
    def __init__(self, x, y):
        """ Inicialización de un vector. """
        self.x = x
        self.y = y

    def magnitud(self):
        """ Calcula la magnitud del vector. """
        return math.sqrt(self.x**2 + self.y**2)

    def angulo_radianes(self):
        """ Calcula el ángulo del vector en radianes. """
        return math.atan2(self.y, self.x)

    def angulo_grados(self):
        """ Calcula el ángulo del vector en grados. """
        return math.degrees(self.angulo_radianes())

    def __str__(self):
        """ Devuelve una representación en cadena del vector. """
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """ Suma dos vectores. """
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("El objeto a sumar debe ser un vector")


if __name__ == "__main__":
    # Ejemplo de uso
    p = Vector(3, 4)
    q = Vector(1, 2)

    # print("**"*20)
    print("--"*30)
    print("Valores ingresados:")

    # Impresión de los vectores
    print(f"\tVector p: {p}")
    print(f"\tVector q: {q}")
    print("--"*30)

    # Cálculo e impresión de la magnitud y ángulo de P
    print("Cálculo de la magnitud y ángulo de P:")
    print(f"\tMagnitud de p: {p.magnitud()}")
    print(f"\tÁngulo de p en grados: {p.angulo_grados()}")
    print(f"\tÁngulo de p en radianes: {p.angulo_radianes()}")
    print("--"*30)

    # Cálculo e impresión de la magnitud y ángulo de Q
    print("Cálculo de la magnitud y ángulo de Q:")
    print(f"\tMagnitud de q: {q.magnitud()}")
    print(f"\tÁngulo de q en grados: {q.angulo_grados()}")
    print(f"\tÁngulo de q en radianes: {q.angulo_radianes()}")
    print("--"*30)

    # Suma de los vectores
    print("Operaciones entre los vectores P y Q:")
    print(f"\tSuma de p y q: {p + q}")
