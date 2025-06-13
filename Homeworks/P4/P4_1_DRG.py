"""
Práctica 4, Ejercicio 1

Daniel Roa
00574499

Fecha de entrega: 26/05/2025

Implemente una clase Rectangulo que represente un rectángulo y que tenga dos
atributos base y altura. Use __eq__ para comparar si dos rectángulos son iguales
(misma base y altura) y __ne__ para verificar si son diferentes. Utilice los métodos
__gt__ y __lt__ para comparar el área de dos rectángulos, devuelva True o False
según sea el caso.
"""


class Rectangulo:
    """Clase Rectangulo que representa un rectángulo y permite comparar sus dimensiones."""

    def __init__(self, base, altura):
        """Inicializa un rectángulo con base y altura."""
        self.base = base
        self.altura = altura

    def __str__(self):
        """Devuelve una representación en cadena del rectángulo. DEBUGGING."""
        return f"Rectángulo con base={self.base} y altura={self.altura}"

    def __eq__(self, otro_rectangulo):
        """Compara si dos rectángulos son iguales en base y altura."""
        return (
            self.base == otro_rectangulo.base and self.altura == otro_rectangulo.altura
        )

    def __ne__(self, otro_rectangulo):
        """Compara si dos rectángulos son diferentes en base o altura."""
        return (
            self.base != otro_rectangulo.base or self.altura != otro_rectangulo.altura
        )

    def __gt__(self, otro_rectangulo):
        """Compara si el rectángulo actual es mayor que otro en base y altura."""
        return self.base > otro_rectangulo.base and self.altura > otro_rectangulo.altura

    def __lt__(self, otro_rectangulo):
        """Compara si el rectángulo actual es menor que otro en base y altura."""
        return self.base < otro_rectangulo.base and self.altura < otro_rectangulo.altura


if "__name__" == "__main__":
    # Creación de rectángulos
    r1 = Rectangulo(10, 20)
    r2 = Rectangulo(10, 20)  # Igual a r1
    r3 = Rectangulo(5, 15)   # Menor que r1 en ambas dimensiones
    r4 = Rectangulo(15, 25)  # Mayor que r1 en ambas dimensiones
    r5 = Rectangulo(10, 25)  # Solo altura diferente (mayor)
    r6 = Rectangulo(15, 20)  # Solo base diferente (mayor)
    r7 = Rectangulo(5, 20)   # Solo base diferente (menor)
    r8 = Rectangulo(10, 15)  # Solo altura diferente (menor)

    print(f"\nRectángulo 1: {r1}")
    print(f"Rectángulo 2 (igual a r1): {r2}")
    print(f"Rectángulo 3 (menor que r1): {r3}")
    print(f"Rectángulo 4 (mayor que r1): {r4}")
    print(f"Rectángulo 5 (altura > r1.altura, base == r1.base): {r5}")
    print(f"Rectángulo 6 (base > r1.base, altura == r1.altura): {r6}")

    # Pruebas de igualdad (==)
    print("\n--- Pruebas de Igualdad (__eq__) ---")
    print(f"r1 == r2 (esperado True): {r1 == r2}")
    print(f"r1 == r3 (esperado False): {r1 == r3}")

    # Pruebas de desigualdad (!=)
    print("\n--- Pruebas de Desigualdad (__ne__) ---")
    print(f"r1 != r2 (esperado False): {r1 != r2}")
    print(f"r1 != r3 (esperado True): {r1 != r3}")

    # Pruebas de mayor que (>)
    print("\n--- Pruebas de Mayor Que (__gt__) ---")
    print(f"r4 > r1 (esperado True): {r4 > r1}")  # 15,25 > 10,20
    print(f"r1 > r3 (esperado True): {r1 > r3}")  # 10,20 > 5,15
    print(f"r1 > r4 (esperado False): {r1 > r4}")
    print(f"r1 > r5 (esperado False, solo altura es mayor): {r1 > r5}")  # 10,20 > 10,25 -> False
    print(f"r5 > r1 (esperado False, solo altura es mayor): {r5 > r1}")  # 10,25 > 10,20 -> False
    print(f"r1 > r6 (esperado False, solo base es mayor): {r1 > r6}")    # 10,20 > 15,20 -> False
    print(f"r6 > r1 (esperado False, solo base es mayor): {r6 > r1}")    # 15,20 > 10,20 -> False

    # Pruebas de menor que (<)
    print("\n--- Pruebas de Menor Que (__lt__) ---")
    print(f"r3 < r1 (esperado True): {r3 < r1}")  # 5,15 < 10,20
    print(f"r1 < r4 (esperado True): {r1 < r4}")  # 10,20 < 15,25
    print(f"r1 < r3 (esperado False): {r1 < r3}")
    print(f"r1 < r7 (esperado False, solo base es menor): {r1 < r7}")  # 10,20 < 5,20 -> False
    print(f"r7 < r1 (esperado False, solo base es menor): {r7 < r1}")  # 5,20 < 10,20 -> False
    print(f"r1 < r8 (esperado False, solo altura es menor): {r1 < r8}")  # 10,20 < 10,15 -> False
    print(f"r8 < r1 (esperado False, solo altura es menor): {r8 < r1}")  # 10,15 < 10,20 -> False
