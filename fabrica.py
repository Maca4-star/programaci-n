#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clas
# las cuales son Moto y Carro.
#Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
# Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.
#Agregar una funcion que determine un descuento del 10% en el precio de llanta mayor a 100.000 pesos
class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar(self):
        print("Llantas:",self.llantas)
        print ("   ✧⁀➷   ")
        print("Color:",self.color)
        print ("   ✧⁀➷   ")
        print("Precio:",self.precio," pesos")
        print ("   ✧⁀➷   ")

    def descuento(self):
        if self.precio > 100000:
            self.precio *= 0.9
            print("Se aplicó un descuento del 10% al precio, por lo tanto queda en:")
        else:
            print("No se aplicó descuento al precio")


class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

x1=Moto(2, "Rojo", 80000)
x2=Carro(4, "Azul", 150000)

print("Moto:")
x1.mostrar()
x1.descuento()
x1.mostrar()

print("\nCarro:")
x2.mostrar()
x2.descuento()
x2.mostrar()