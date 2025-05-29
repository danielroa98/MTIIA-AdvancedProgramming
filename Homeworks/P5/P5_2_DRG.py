"""
Práctica 5, Ejercicio 2

Daniel Roa
00574499

Fecha de entrega: 02/06/2025

Dada una lista de diccionarios que representan productos con nombre (llave
en el diccionario) y precio (valor de la llave en el diccionario), filtre
los productos que cuestan más de $200, y aplique un descuento del 10%.
Finalmente calcule el total de los productos que tienen descuento.
"""
productos = [
    {"Cable USB-C": 165},
    {"Dock Hub USB-C": 1200},
    {"Cuaderno Moleskine": 250},
    {"Plumas Pilot G-2": 350},
    {"Adaptador Corriente USB-C": 100},
    {"Audifonos Inalámbricos": 1500},
]

precios_mayores = list(filter(lambda x: list(x.values())[0] > 200, productos))

descuentos = list(
    map(lambda x: {list(x.keys())[0]: list(x.values())[0] * 0.9},
        precios_mayores)
)

precios_descuentos = list(map(lambda x: list(x.values())[0], descuentos))
descuento_total = sum(precios_descuentos)

print(
    "Productos con un valor mayor a $200 son:",
)
for i, producto in enumerate(precios_mayores):
    print(f"{i+1}) {list(producto.keys())[0]} - ${list(producto.values())[0]}")

print(f"{'*-'*25}*")
print(f"El descuento total final es de: ${descuento_total:.2f}")
