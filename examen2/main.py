import ollama as ol
import gradio as gr

with gr.Blocks()as interfaz:
    respusta=gr.Texbox(label="Pregunta del cliente")
    btn=gr.Button("Recomendar")
    btn=gr.click(fn=recomendar,
    inputs=respuesta,
    outpusts=resultado,)
    

respuesta=ol.chat(
    model="llama3.2",
 messages=[
{"role":"system","content":"Trabajas en una tienda de videojuegos y tines que recomendar juegos dependiendo de las necesidades de los clientes,evitar recomendar juegos como servicio estos son gratis que su funcion principal se basa en los pagos de skins, como por ejemplo fornite,warzone,fifa,la recomendacion principal seria de juegos de modo historia de un jugador,como baldurs gate 3,kenshi,metal gear,cyberpunk2077,eldenring recomendar juegos parecidos a los antes mencionados  juegos de aventura,en juegos multijugador recomenda raimbow six sige o cs2 maximo de juegos recomendados son de 6 "}
 ,{
    "role":"user","content":"recomiendame un juego de estrategia  "
 }

 ]
)
print(respuesta["message"]["content"])
app.launch()