class Person: #mismo #atributos      #GENERAL
  def __init__(self, fname, lname):  #funcion constructora 
    self.firstname = fname #parametros (nombre)
    self.lastname = lname #parametros (apellida)

  #funcion/metodo para mostrar
  def printname(self): #polimorfismo=VARIAS funciones con la misma clase
    print(self.firstname, self.lastname) #define que hay que mostrar

#otra tabla de datos
class Student(Person):#hija de persona #ESPECIALIZADA (no en este caso)
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) #hereda los atributos de persona
 
  def printname(self): #polimorfismo
    #super hereda todos los metodos y propiedades de funcion padre
    super().printname()

   
x1 = Student("Juana", "León") #valores
x1.printname() #llamamos la funcion de mostrar

x2 = Student("Pedro", "Lopez")
x2.printname()

x3 = Student("Ana", "Martinez")
x3.printname()