from persona import persona

class profesor(persona):

    def apartamento(self):

     return f"{self.nombre} Informacion del profesor"

    def obtener_detalles(self):
        
        return f"nombre:{self.nombre},identificacion:{self.identificacion}"


