class Vehiculo:
    def __init__(self, marca, modelo, color, anio):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.anio=anio

    def mostrar(self): #polimorfismo
        print("Marca:",self.marca,"\nModelo:", self.modelo, "\nColor:",self.color,"\nAño:",self.anio)
        

class Auto(Vehiculo):
  def __init__(self, marca, modelo,color, anio,puertas,capacidadper, capacidadkm,estado ):
      super().__init__(marca, modelo,color,anio)
      self.puertas=puertas
      self.capacidadper=capacidadper
      self.capacidadkm=capacidadkm
      self.estado=estado
 
  def mostrar(self): #polimorfismo clase hija
    print ("Auto")
    return super().mostrar()
    print ("\nPuertas:",self.puertas,"\nCapacidad de personas:",self.capacidadper, "\nCapacidad de km:",self.capacidadkm,"\nEstado:",self.estado)
    print ("   ✧⁀➷   ")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo,color, anio,Estado,velocidad ):
      super().__init__(marca, modelo,color,anio)
      self.Estado=Estado
      self.velocidad=velocidad

    def mostrar(self): #polimorfismo clase hia
        print ("Motocicleta")
        print ("\nEstado:",self.Estado,"\nVelocidad:",self.velocidad)
        print ("   ✧⁀➷   ")
        return super().mostrar()

class Camion(Vehiculo):
    def __init__(self, marca, modelo,color, anio, cargas, recorrido):
      super().__init__(marca, modelo,color,anio)
      self.cargas=cargas
      self.recorrido=recorrido
      
    def mostrar(self): #polimorfismo clase hija
        print ("\nCamion")
        print ("Cargas:",self.cargas,"\nRecorrido:",self.recorrido)
        print ("   ✧⁀➷   ")
        return super().mostrar()

x1=Auto("Honda","CR-V","Azul",2023,4,5,"Alta","Nuevo")
x1.mostrar()

x2=Motocicleta("Kawasaki","KW 85","Rojo",2022,"Usada","Alcanza altas velocidades")
x2.mostrar()

x3=Camion("Mercedez Benz","D608","azul" ,1976, "1 tonelada","Corta distancia")
x3.mostrar()