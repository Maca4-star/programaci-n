
class Empleado:
    def __init__(self,nombre,edad,salario):#polimorfismo
        self.nombre=nombre
        self.edad=edad
        self.salario=salario

    def detalles(self):#polimorfismo
        print("Nombre:",self.nombre,"\nEdad:",self.edad,"\nSalario:",self.salario)

class Gerente(Empleado):
    def __init__(self,nombre,edad,salario,departamento):#polimorfismo
      Empleado.__init__(self,nombre,edad,salario)
      self.departamento=departamento

    def detalles(self):#polimorfismo
        print("\nDepartamento:",self.departamento)
        return super().detalles()
        
class Ingeniero(Empleado):
     def __init__(self,nombre,edad,salario,especialidad):#polimorfismo
        Empleado.__init__(self,nombre,edad,salario)
        self.especialidad=especialidad

     def detalles(self): #polimorfismo
        print("\nEspecialidad:",self.especialidad)
        return super().detalles()


x1=Empleado("Jose",26,"13 mil")
x1.detalles()

x2=Gerente("More",26,"10 mil","Marketing")
x2.detalles()

x3=Ingeniero("Andy",25,"9 mil","Arte")
x3.detalles()