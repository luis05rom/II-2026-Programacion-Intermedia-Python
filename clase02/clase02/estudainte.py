from persona import persona#apara importar la clase persona al documento

class estudiante(persona):
    def carrera(self):

        return f"{self.nombre}Informacion del estudiante"

    def obtener_detalles(self):
        
        return f"nombre:{self.nombre},identificacion:{self.identificacion}"
