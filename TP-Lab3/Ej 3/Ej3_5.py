from os import system

class Agenda:

    def __init__(self):
        self.agenda = []


    def ingresar_datos(self):
        nombre = input("Ingrese el nombre: ")
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el telefono: ")
        self.agenda.append([nombre,email,telefono])
    
    def imprimir(self):
        print("---------------------------------- ")
        for persona in self.agenda:
            print(f"Nombre: {persona[0]}")
            print(f"Mail: {persona[1]}")
            print(f"Telefono: {persona[2]}")
            print("-------------------------------")


    def consultar_nombre(self):
        x = 0
        print("-----------------------------------")
        nombre = input("Que persona desea buscar?")
        for persona in self.agenda:
            if persona[0] == nombre:
                print(f"{persona[0]} se encuentra en la agenda ")
                x = 1
        if x != 1:
            print(f" {persona[0]} no se encuentra en la agenda")
                
    def modificar_datos(self):
        x = 0
        print("-----------------------------------")
        nombre = input(" A que persona desea cambiarle sus datos? ")
        for persona in self.agenda:
            if persona[0] == nombre:
                print(f"{persona[0]} se encuentra en la agenda ")
                email = input("Ingrese el nuevo email: ")
                persona[1] = email
                telefono = input("Ingrese el nuevo telefono: ")
                persona[2] =  telefono
                print("Datos modificados!!")
                x = 1
        if x != 1:
            print("La persona no se encuentra en la agenda")

agenda = Agenda()
salir = False
x = 5
while (salir != True):
    
    print("1 - Cargar contacto en la agenda.")
    print("2 - Listar agenda.")
    print("3 - Buscar persona en la agenda.")
    print("4 - Modificar datos de la persona.")
    print("5 - Salir. ")
    x = int(input("Ingrese una opcion: "))
    if x==1:
        agenda.ingresar_datos()
        system("clear")    
    elif x==2:
        agenda.imprimir()
    elif x==3:
        agenda.consultar_nombre()
        
    elif x==4:
        agenda.modificar_datos()
    
    elif x==5:
        salir = True
        
    elif x<1 or x>5:        
        system("clear")
        print("Ingrese una opcion valida\n")


