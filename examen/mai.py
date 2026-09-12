class Pelicula:
    def _init_(self,titulo,genero,duracion,presupuesto,clasificacion):
        self.titulo=titulo
        self.genero=genero
        self.duracion=duracion
        self.presupuesto=presupuesto
        self.clasificacion=clasificacion

    def mostar_datos(self,Pelicula):
        return f"titulo:{self.titulo},genero:{self.genero},duracion:{self.duracion},presupuesto:{self.presupuesto},clasificacion:{self.clasificacion}"
     
    
 # lista de las peliculas 
#pelicula1 = Pelicula("Trasformers","Accion","200 min","150 millones","7.7")
pelicula2 = Pelicula("Intelestelar","Cinencia ficcion","190 min","120 millones","8.8")
pelicula3 = Pelicula("Lala land","Musical","130 min","90 milones","9.2")
pelicula4 = Pelicula("Cars","Aventura","90 min","84 milones","8.9")
pelicula5 = Pelicula("Batman","Accion","183 min","400 millones","9.5")

#imprimir

print(Pelicula.mostrar_datos())

