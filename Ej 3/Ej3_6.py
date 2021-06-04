import random

class Dado:

    valor = None

    def tirar(self):
        self.valor = random.randint(1,6)
    
    def retornar_valor(self):
        return self.valor


class JuegoDeDados:

    def __init__(self, dado1: Dado, dado2: Dado, dado3: Dado):
        self.dado1 = dado1
        self.dado2 = dado2
        self.dado3 = dado3

    def jugar(self):
        self.dado1.tirar()
        self.dado2.tirar()
        self.dado3.tirar()
        print(f"Dado 1: {self.dado1.retornar_valor()}")
        print(f"Dado 2: {self.dado2.retornar_valor()}")
        print(f"Dado 3: {self.dado3.retornar_valor()}")
        if (self.dado1 == self.dado2 and self.dado1 == self.dado3 and self.dado2 == self.dado3):
            print("Ganaste")
        else:
            print("Perdiste")

Dado1 = Dado()
Dado2 = Dado()
Dado3 = Dado()

x = True

while(x!=False):

    Juego = JuegoDeDados(Dado1,Dado2,Dado3)
    Juego.jugar()
    rta = input("Quieres  tirar los dados? Si/No: ")
    if rta == 'No' or rta == 'no':
        x = False

