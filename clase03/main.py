
import pandas as pd
estudiantes = pd.read_csv('./clase03/Libro2.csv')
print(estudiantes.head(8))
print(estudiantes['edad'].max())
print(estudiantes['edad'].min())
print(estudiantes['altura'].max())
print(estudiantes['altura'].min())





