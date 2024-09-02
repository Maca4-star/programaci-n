class Animal:
    def __init__(self, especie, edad, color, tamañoCM):
        self.especie = especie
        self.edad = edad
        self.color = color
        self.tamañoCM = tamañoCM

    def mostrar(self):
        print("_________________________")
        print("Especie:",self.especie,"\nEdad:", self.edad, "\nColor:",self.color,"\nTamaño:",self.tamañoCM)
   
#Crear cuatro objetos de la clase Animal
animal1 = Animal("lechuza", 2,"marron con manchas grises",32)
animal2 = Animal("caracol", 1, "gris",5)
animal3 = Animal("toro", 4,"negro con manchas blancas",170)
animal4 = Animal( "delfin", 4,"blanca", 23 )

animal1.mostrar()
animal2.mostrar()
animal3.mostrar()
animal4.mostrar()