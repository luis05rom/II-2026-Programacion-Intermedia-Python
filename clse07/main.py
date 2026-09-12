#gradio es una libreria para crear interfaces de usuario de manera sencilla
import gradio as gr 
#pandas para manejar datos de estiudiantes
import pandas as pd
#usar la clese estudiante del otro archivo estudiante.py
from Estudiante import Estudiante
# crear una lista vacia para almacenar los estudiantes
# lista de estudiantes de prueba """ """
estudiantes = [
    Estudiante("Ana", 19, 1.60, 3, 58),
    Estudiante("Luis", 20, 1.75, 5, 65),
    Estudiante("María", 21, 1.62, 7, 72),
    Estudiante("Carlos", 22, 1.80, 9, 78),
    Estudiante("Sofía", 20, 1.68, 11, 84),
    Estudiante("Diego", 23, 1.77, 13, 88),
    Estudiante("Laura", 24, 1.64, 15, 94),
    Estudiante("Andrés", 21, 1.82, 8, 75),
    Estudiante("Valeria", 25, 1.59, 17, 97),
    Estudiante("José", 26, 1.73, 12, 86),
    Estudiante("Daniela", 19, 1.70, 4, 61),
    Estudiante("Roberto", 27, 1.78, 18, 98)
]
#estudiantes = []#para cargar los estudiantes esta vacia para agregar estudiantes


#agrgar un estudiante a la lista de estudiantes y devolver la lista de estudiantes y la correlacion
def agregar_estudiante(nombre, edad, estatura, horas_estudio, calificacion):
    estudiante = Estudiante(
        nombre,
        edad,
        estatura,
        horas_estudio,
        calificacion
    )
    estudiantes.append(estudiante)
    return obtener_estudiantes(), calcular_correlacion(), obtener_estudiantes()
#fuente para obtener los estudiantes en un dataframe de pandas
def obtener_estudiantes():
    df = []
    for estudiante in estudiantes:
        df.append(estudiante.__dict__)
    return pd.DataFrame(df)
#funcion para calcular la correlacion entre las variables de los estudiantes
def calcular_correlacion():
    #se nesecita al menos 2 estudiantes para calcular la correlacion
    if len(estudiantes) < 2:
        return None
    df = obtener_estudiantes()
    #calcular la correlacion entre las variables numericas del dataframe
    correlacion = df.corr(numeric_only=True)
    correlacion.insert(
        0,
        "Variable",
        correlacion.index
    )
    return correlacion.reset_index(drop=True)

with gr.Blocks() as app:#se agrega un titulo centrado a la aplicacion
    gr.Markdown("<h1 style='text-align: center;'>Sistema de Estudiantes</h1>")#el estitulo de la aplicacion 
    with gr.Row():
        with gr.Column():#el inicio de la columna para agregar estudiantes
            gr.Markdown("## Agregar Estudiante")
            nombre = gr.Textbox(label="Nombre")
            edad = gr.Number(label="Edad")
            estatura = gr.Number(label="Estatura")
            horas_estudio = gr.Number(label="Horas de Estudio")
            calificacion = gr.Number(label="Calificación")
            boton = gr.Button("Agregar estudiante", variant="primary")
        with gr.Column():#garfico de las correlaciones
            gr.Markdown("## Lista de Estudiantes")
            tabla = gr.DataFrame(value=obtener_estudiantes())
    with gr.Row():
        with gr.Column():
            # Correlacion
            gr.Markdown("## Correlaciones")
            correlacion = gr.DataFrame(
                value=calcular_correlacion()
            )

        # Grafico de correlaciones
        with gr.Column():
            gr.Markdown("### Gráfico de dispersión")
            scatter_plot = gr.ScatterPlot(
                value=obtener_estudiantes(),
                x="horas_estudio",
                y="calificacion",
                x_lim = [0, 20],
                y_lim = [0, 100],
            )
    boton.click(
        fn=agregar_estudiante,
        inputs=[
            nombre,
            edad,
            estatura,
            horas_estudio,
            calificacion
        ],
        outputs=[tabla, correlacion, scatter_plot]
    )#outputs de la funcion agregar estudiante, se actualiza la tabla, la correlacion y el grafico de dispersión

app.launch()#para lanzar la aplicacion