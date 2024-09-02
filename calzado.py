#Crear una clase calzado que contenga fecha de creacion, origen, marca, tipo, suela, numero
#crear una clase hija zapatilla que contenga modelo, materiales y si muestre si hay stock, si tiene detalle
class Calzado:
    def __init__(self, tipo, fecha_creacion, origen, marca, suela, numero):
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.origen = origen
        self.marca = marca
        self.suela = suela
        self.numero = numero
    
    def mostrar(self):
        print("Tipo de calzado:",self.tipo,"\nFecha de creación:", self.fecha_creacion, "\nMade in:", self.origen, "\nMarca:", self.marca,"\nTipo de suela:", self.suela, "\nNúmero de clase:", self.numero)

class Zapatilla(Calzado):
    def __init__(self, tipo, fecha_creacion, origen, marca, suela, numero, modelo, materiales, stock, detalle=None):
        super().__init__(tipo, fecha_creacion, origen, marca, suela, numero)
        self.modelo = modelo
        self.materiales = materiales
        self.stock = stock
        self.detalle = detalle

    def mostrar(self):
        if self.stock <= 2 and self.stock > 0:
            print("Hay stock disponible")
        elif self.stock == 1:
            print("Hay un solo par")
        else:
            print("No hay stock disponible")
        
        print("Modelo:", self.modelo, "\nMateriales:", self.materiales, "\nDetalle:", self.detalle)
        super().mostrar()

x1=Calzado("Botas","19 De Junio de 2011","Inglaterra","Desconocida","Usadas",36)
x1.mostrar()
x2=Zapatilla("Deportivas","20 de Enero de 2019","Argentina","Nike","Nueva",40,"Urbano","Telas",2,"Sin detalles")
x2.mostrar()