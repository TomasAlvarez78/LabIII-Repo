class Calculadora:

    valor1 = None
    valor2 = None

    def set_carga_valor1(self,numero):
        self.valor1 = numero
    
    def set_carga_valor2(self,numero):
        self.valor2 = numero

    def suma(self):
        print(f"Resultado Suma: {self.valor1 + self.valor2}")

    def resta(self):
        print(f"Resultado Resta: {self.valor1 - self.valor2}")

calculadora= Calculadora()

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

calculadora.set_carga_valor1(numero1)
calculadora.set_carga_valor2(numero2)

calculadora.resta()
calculadora.suma()