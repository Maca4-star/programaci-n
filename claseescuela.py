#Crear un programa que contenga los datos personales de personas que forman parte de una escuela: 
#estudiantes y docentes. Deberas identificar los siguientes atributos y aplicarlos a Clases en POO: 
#matricula, dni, nombreApellido, direccion, anioCurso, materias, cursosAcargo. 
# crear funciones para mostrar sus datos. Crear 3 objetos para cada clase
class Persona:
    def __init__(self, nmbA, dni, direccion, matricula):
        self.nmbA = nmbA
        self.dni = dni
        self.direccion = direccion
        self.matricula = matricula

    def mostrar(self):
        print("Nombre y Apellido:", self.nmbA, "\nDni:", self.dni, "\nDirección:", self.direccion, "\nMatricula:", self.matricula)

class Estudiantes(Persona):
    def __init__(self, nmbA, dni, direccion, matricula, anio, materias):
        super().__init__(nmbA, dni, direccion, matricula)
        self.anio = anio
        self.materias = materias

    def mostrar(self):
        print("..................")
        print(".   Estudiantes  .")
        print("..................")
        super().mostrar()
        print("Año del Curso:", self.anio, "\nMaterias:", self.materias)

class Docentes(Persona):
    def __init__(self, nmbA, dni, direccion, matricula, cursosAcargo):
        super().__init__(nmbA, dni, direccion, matricula)
        self.cursosAcargo = cursosAcargo

    def mostrar(self):
        print("..................")
        print(".    Docente     .")
        print("..................")
        super().mostrar()
        print("Años a Cargo:", self.cursosAcargo)

x1 = Estudiantes("José Alba", 48425669, "Manzana 2", 7284682, "Quinto (5)", 12)
x2 = Estudiantes("Andy Fernandez", 49017769, "Barrio Docente", 734694, "Cuarto(4)", 16)
x3 = Estudiantes("Morena Vera", 48669425, "Barrio Balneario A", 8372958, "Tercero(3)", 12)

y1 = Docentes("Emilse Bustos", 30632762, "Barrio Centro", 2286492, "3")
y2 = Docentes("Celeste Maitines", 29290740, "Barrio Los Altos", 843730, "5")
y3 = Docentes("Mario Aguirre", 30849830, "Barrio Balneario B", 8426863, "4")

x1.mostrar()
x2.mostrar()
x3.mostrar()

y1.mostrar()
y2.mostrar()
y3.mostrar()