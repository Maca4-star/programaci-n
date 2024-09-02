class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        return self.nota

    def aprobo(self):
        if self.nota >= 7:
            return "Aprobó"
        else:
            return "No aprobó"


x1 = Alumno("Angela", 4)
x2 = Alumno("José", 8)
x3 = Alumno("Tomás", 6.5)

students = [x1, x2, x3]
sorted_students = sorted(students, key=lambda x: x.mostrar(), reverse=True)


for student in sorted_students:
    print(f"El alumno {student.nombre} ha sacado: {student.mostrar()} - {student.aprobo()}")