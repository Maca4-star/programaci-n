class deporte:
    def __init__(self, nomdeporte, jugadores, equipos, cancha):
        self.nomdeporte= nomdeporte
        self.jugadores= jugadores
        self.equipos= equipos
        self.cancha= cancha
       
    def mostrar(self):
        print("   ✧⁀➷    ")
        print("Deporte:",self.nomdeporte,"Jugadores:",self.jugadores,"\nEquipos:", self.equipos,"\n(medida en metros) Cancha:",self.cancha)
       
Deporte1= deporte("Voley",6,2, 90)
Deporte2= deporte("Futbol",11,2,120)
Deporte3= deporte("Beisbol",9,2,100)

Deporte1.mostrar()
Deporte2.mostrar()
Deporte3.mostrar()
