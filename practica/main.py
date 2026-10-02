import gradio as gr


class Cliente:
    def __init__(self, nombre, marca, fecha_entrada, fecha_salida, numero_piezas, grado_dano):
        self.nombre = nombre
        self.marca = marca
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.numero_piezas = numero_piezas
        self.grado_dano = grado_dano

lista_clientes = [Cliente("Victor", "Hyundai", "2026-08-01", "2026-08-10", 4, "Moderado")]

def agregar_cliente(nombre, marca, fecha_entrada, fecha_salida, numero_piezas, grado_dano):
    if not nombre or not marca:
        return "Completar los datos"

    nuevo_cliente = Cliente(
        nombre,
        marca,
        fecha_entrada,
        fecha_salida,
        numero_piezas,
        grado_dano
    )
    lista_clientes.append(nuevo_cliente)


with gr.Blocks() as interfaz:
    gr.Markdown("Registro de clientes")

    nombre = gr.Textbox(label="Nombre del cliente")
    marca = gr.Textbox(label="Marca del vehículo")
    fecha_entrada = gr.Textbox(label="Fecha de entrada del vehículo")
    fecha_salida = gr.Textbox(label="Fecha de salida del vehículo")
    numero_piezas = gr.Textbox(label="Número de piezas a reparar")
    grado_daño = gr.Dropdow(choices=["Bajo", "Medio", "Alto", "Remplazo"], label="Grado de daño")
    resultado = gr.Textbox(label="Resultado")

    btn_agregar = gr.Button("Agregar cliente")
    btn_agregar.click(
        fn=agregar_cliente,
        inputs=[nombre, marca, fecha_entrada, fecha_salida, numero_piezas, grado_daño],
        outputs=resultado,
    )

   
    interfaz.launch()