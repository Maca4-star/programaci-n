#Actividad 1: Agregar a la clase padre los atributos: dni, dirección, código postal, fechaNacimiento
class Person:
  def __init__(self, nombre, apellido,dni, dirección,cp,nacim):
    self.nombre = nombre
    self.apellido = apellido
    self.dni= dni
    self.dirección=dirección
    self.cp= cp
    self.nacim= nacim

  def printname(self): #polimorfismo
    print("Nombre:",self.nombre, "\nApellido:",self.apellido, "\nDNI:",self.dni, "\nDireccion:",self.dirección,"\nCodigo Postal:",self.cp,"\nFecha de nacimiento:",self.nacim )
    print("...........")
#Actividad 2: Agregar a la clase hija Student los atributos: matrícula, curso, estado, añoIngreso.

class Student(Person):
  def __init__(self, nombre, apellido,dni, dirección,cp,nacim, matricula,curso,estado,ingresoaño ):
    Person.__init__(self, nombre, apellido,dni, dirección,cp,nacim)
    self.matricula=matricula
    self.curso=curso
    self.estado=estado
    self.ingresoaño=ingresoaño
 
  def mostrar(self):#polimorfismo clase hijo
    print ("Matricula:",self.matricula,"\nCurso:",self.curso, "\nEstado:",self.estado,"\nAño de Ingreso:",self.ingresoaño)
    print ("..........")
    return super().mostrar()


   
x1 = Student("Pepita ", " Lopez", 78999654 ,"nam nam nam 1234",5280 ," 05 de noviembre", 5555 ," 4to año"," asistencia perfecta",2022)
x1.printname()


x2 = Student("Jose ", "Alba", 455678899,"ñam ñam ñam 3456", 8052,"6 de junio", 6666 ," 5to año","asistencia media",2020)
x2.printname()


x3 = Student("Andy ", "Maitines",47865345,"ñam ñam ñam 678",4567,"30 de septiembre", 7777 ,"6to año","faltante",2019)
x3.printname()