class Empleado:

    def __init__(self, nombre: str, sueldo: float):
        self.nombre = nombre
        self.sueldo = sueldo

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Sueldo: {self.sueldo}")

    def impuestos(self):
        if(self.sueldo > 3000):
            print(f"{self.nombre} debe pagar impuestos")
        else:
            print(f"{self.nombre} no debe pagar impuestos")


nombre = input("Ingrese el nombre del empleado: ")
sueldo = float(input("Ingrese el sueldo del empleado: "))

empleado = Empleado(nombre,sueldo)
empleado.imprimir()
empleado.impuestos()