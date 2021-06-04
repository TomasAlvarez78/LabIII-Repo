class Punto:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def cuadrante(self):
        if(self.x > 0 and self.y > 0):
            print("Se encuentra en el primer cuadrante")
        if(self.x < 0 and self.y > 0):
            print("Se encuentra en el segundo cuadrante")
        if(self.x < 0 and self.y < 0):
            print("Se encuentra en el tercer cuadrante ")
        if(self.x > 0 and self.y < 0):
            print("Se encuentra en el cuarto cudrante")

punto1 = Punto(4,4)
punto2 = Punto(-4,4)
punto3 = Punto(-4,-4)
punto4 = Punto(4,-4)

punto1.cuadrante()
punto2.cuadrante()
punto3.cuadrante()
punto4.cuadrante()