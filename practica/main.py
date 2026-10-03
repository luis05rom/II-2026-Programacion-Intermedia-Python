import ollama as ol

respuesta = ol.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Trabajas en una biblioteca y tines que recomendar libros,el maximo de libroa a recomendar es de5"}
        ,{
          "role": "user", "content": "En que orde leer Barnd sanderson" 
        }
    ]
)
print(respuesta["message"]["content"])