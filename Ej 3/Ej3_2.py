class Triangulo:
    def __init__(self, lado1: int, lado2: int, lado3: int):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def lado_mayor(self):
        if(self.lado1 > self.lado2 and self.lado1 > self.lado3 ):
            print(f"El lado mayor es el: 1 con {self.lado1} cm")
        elif(self.lado2 > self.lado1 and self.lado2 > self.lado3):
            print(f"El lado mayor es el: 2 con {self.lado2} cm")
        elif(self.lado3 > self.lado1 and self.lado3 > self.lado2):
            print(f"El lado mayor es el: 3 con {self.lado3} cm")
        else:
            print("Todos los lados son iguales")

    def equilatero(self):
        if(self.lado1 == self.lado2  and self.lado1 == self.lado3 and self.lado2 == self.lado3):
            print("El triangulo es equilatero")
        else:
            print("EL triangulo no es equilatero")
    

triangulo1 = Triangulo(4,4,4)

triangulo1.lado_mayor()
triangulo1.equilatero()

print("\n")

triangulo2 = Triangulo(8,7,6)
triangulo2.lado_mayor()
triangulo2.equilatero()
