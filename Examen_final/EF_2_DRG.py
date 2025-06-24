"""
Examen final, Ejercicio 2

Daniel Roa
00574499

Fecha de entrega: 23/06/2025

Use los datos en el archivo adjunto ejercicio2.csv que contienen información de
empleados con columnas: Nombre, Salario, y Departamento. Realice las siguientes
tareas:
• Filtre los empleados que ganan más de 5000.
• Ordene a los empleados por Salario de forma descendente.
• Filtre empleados que trabajen en el departamento de "Ventas" y ganen más de
4000.
• Haga un gráfico de dispersión de Nombre vs. Salario. Utlice una paleta de
    colores, leyendas de los colores, etiquetas en los ejes y una malla.
"""

import csv
import matplotlib.pyplot as plt

# No viene en los requisitos del examen, pero preferí ponerlo
# para mantener buenas prácticas y porque el linter me regañana
# si no lo pongo.
from typing import Any

FILE_PATH = "./data/ejercicio2.csv"


def read_csv_file(file_path: str) -> list[dict[Any, Any]] | None:
    """Gets the employees data from a CSV file."""
    employees = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Clean up keys and values
                    cleaned_row = {k.strip(): v.strip()
                                   for k, v in row.items()}
                    cleaned_row['Salario'] = float(cleaned_row['Salario'])
                    employees.append(cleaned_row)
                except (ValueError, KeyError) as e:
                    msg = f"Advertencia: Omitiendo fila: {row}, err: {e}"
                    print(msg)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en: {file_path}")
        return None
    return employees


def print_employees(employees: list[dict[Any, Any]], title: str) -> None:
    """Prints a list of employees in a readable format."""
    print(f"\n--- {title} ---")
    for emp in employees:
        print(
            f"Nombre: {emp['Nombre']}, Salario: {emp['Salario']:.2f}, "
            f"Dpto: {emp['Departamento']}"
        )


def filter_by_salary(employees: list[dict[Any, Any]],
                     base_salary: int = 5000) -> list[dict[Any, Any]]:
    """Filters employees that earn more than a minimum salary."""
    return [emp for emp in employees if emp['Salario'] > base_salary]


def sort_by_salary(employees: list[dict[Any, Any]]) -> list[dict[Any, Any]]:
    """Sorts employees by salary in descending order."""
    return sorted(employees, key=lambda x: x['Salario'], reverse=True)


def filter_by_department_and_salary(employees: list[dict[Any, Any]],
                                    department: str,
                                    base_salary: int = 4000) -> list[dict[Any, Any]]:  # noqa
    """Filters employees by department and salary."""
    return [
        emp for emp in employees
        if emp['Departamento'] == department and emp['Salario'] > base_salary
    ]


def plot_salary_distribution(employees: list[dict[Any, Any]]) -> None:
    """Creates a scatter plot of Salary vs. Name."""
    departamentos = [emp['Departamento'] for emp in employees]

    unique_departments = sorted(list(set(departamentos)))
    colors = plt.get_cmap('viridis', len(unique_departments))

    dept_color_map = {
        dept: colors(i) for i, dept in enumerate(unique_departments)
    }

    plt.figure(figsize=(12, 8))

    for dept in unique_departments:
        dept_employees = [
            emp for emp in employees if emp['Departamento'] == dept
        ]
        dept_nombres = [emp['Nombre'] for emp in dept_employees]
        dept_salarios = [emp['Salario'] for emp in dept_employees]
        plt.scatter(
            dept_nombres, dept_salarios, color=dept_color_map[dept], label=dept
        )

    plt.xlabel("Nombre del Empleado")
    plt.ylabel("Salario")
    plt.title("Distribución de Salarios por Empleado y Departamento")
    plt.xticks(rotation=90)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(title="Departamentos")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    try:
        employees_data = read_csv_file(FILE_PATH)
        print(f"File found at {FILE_PATH}")
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en: {FILE_PATH}")
        exit(1)

    # Getting the employees that earn more than 5000
    better_paid = filter_by_salary(employees_data, 5000)  # type: ignore
    print_employees(better_paid, "Empleados con salario > 5000")

    # Sorting the employees by salary
    sorted_employees = sort_by_salary(employees_data)  # type: ignore
    print_employees(sorted_employees, "Empleados ordenados por salario")

    # Getting the employees that work in the sales department
    # and earn more than 4000
    sales_high_earners = filter_by_department_and_salary(
        employees_data, "Ventas", 4000  # type: ignore
    )
    print_employees(
        sales_high_earners,
        "Empleados de Ventas con salario > 4000"
    )

    # Plotting the salary distribution
    plot_salary_distribution(employees_data)  # type: ignore
