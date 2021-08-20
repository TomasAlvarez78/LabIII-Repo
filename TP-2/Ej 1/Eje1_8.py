import os
def getNombre(lista):
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese su edad: "))
    if(len(nombre) > 0 and edad > 0):
        lista[nombre] = edad
        print(lista)
    else:
        print("Ese nombre/edad es invalido!")

def printLista(lista):
    for persona in lista:
        print(f"{persona} tiene {lista[persona]} años")

if __name__ == "__main__":
    lista = {}
    while(len(lista) < 5):
        getNombre(lista)
    printLista(lista)

#Un diccionario no es la mejor forma de implementarlo, tambien se podrian usar tuplas
    