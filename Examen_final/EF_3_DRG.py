"""
Examen final, Ejercicio 3

Daniel Roa
00574499

Fecha de entrega: 23/06/2025

Utilice los datos del archivo adjunto ejercico3.csv y
guardelos en un DataFrame. Los datos tienen algunos valores
faltantes. Realice lo siguiente:
• Encuentre cuantos valores faltantes hay en total en el DataFrame inicial.
• Rellene los valores faltantes con el valor medio de cada columna.
• Haga un histograma con las calificaciones contenidas en los datos.
• Elimine las filas que contengan los valores faltantes.
"""

import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "./data/ejercicio3.csv"

# Started reading the file
test_df = pd.read_csv(FILE_PATH)  # noqa

manipulated_df = test_df.copy()

print("---Dataframe---")
print(test_df)

# print("---Data types---")
# print(test_df.dtypes)

print("---Validating blank values---")
print(test_df.isna().sum())

print("---Filling blank values---")
manipulated_df["Calificación"] = manipulated_df["Calificación"].fillna(
    manipulated_df["Calificación"].mean()
)
manipulated_df["Edad"] = manipulated_df["Edad"].fillna(
    manipulated_df["Edad"].mean()
)

print("---Dataframe after filling blank values---")
print(manipulated_df)

print("---Histogram of grades---")
plt.hist(manipulated_df["Calificación"], bins=10)
plt.show()

print("---Removing rows with blank values---")
test_df.dropna(inplace=True)

print("---Dataframe after removing rows with blank values---")
print(test_df)

print("---Validating blank values---")
print(test_df.isna().sum())
