class Alumno:
    
    def inicializar(self, nombre: str, nota: int):
        self.nombre = nombre
        self.nota = nota

    def printAtributos(self):
        print(f"Nombre: {self.nombre} ")
        print(f"Nota: {self.nota}")
         
    def estado(self):
        if self.nota >= 4:
            print(f"El alumno {self.nombre} esta regular")
        else:
            print(f"El alumno {self.nombre} no esta regular")


alumno = Alumno()

alumno.inicializar("Pedro",7)
alumno.printAtributos()
alumno.estado()

alumno2 = Alumno()

alumno2.inicializar("Joaquin",3)
alumno2.printAtributos()
alumno2.estado()