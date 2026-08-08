from persona import persona
from estudainte import estudiante
from profesor import profesor 

class imprimir_detalles:
    def imprimir_detalles(self, persona):
        print(persona.obtener_detalles())

        
    
estudiante1 = estudiante("Pedro", "1005")
estudiante2= estudiante("Juan", "1006")
profesor1 = profesor("Maria", "2007")
profesor2 = profesor("Jose", "2008")
 
 