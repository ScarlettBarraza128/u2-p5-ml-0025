import numpy as np
import pandas as pd

# Emily Barraza NC = 0025

# Datos de una matriz de 4 x 3
print("---datos de los estudiantes de una matriz 4 x 3")
datos_alumnos = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]

# Poner nombre a las columnas y almacenar la variable df
df = pd.DataFrame(datos_alumnos, columns=["ci", "marcas", "paquetes"])

print(df)

# Datos a partir de un diccionario
print("----datos de los estudiantes de un diccionario---")
alumno_diccionario = {
    "nombre": ["Erika", "Miguel", "Alfredo", "Camila", "Fernanda"],
    "califa": [60, 90, 70, 80, 100],
    "edad": [14, 15, 16, 16, 17]
}

estudiantes = pd.DataFrame(alumno_diccionario)

print(estudiantes)
print("Emily Barraza NC = 0025")
