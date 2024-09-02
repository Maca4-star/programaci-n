#PROGRAMACIÓN ORIENTADA A OBJETOS
#clase=molde
class Person:
    #def=función/#name, age son atributos/propiedades/variables
  def __init__(self, name, age):
    #self significa el mismo
    self.name = name #ingresamos el valor de la variable name
    self.age = age
  def mostrar(self): #funcion que lo muestra
     print(self.name,self.age)


p1 = Person("José", 16)#OBJETO DE LA CLASE Person
p1.mostrar()
