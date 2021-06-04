def getTraduccion(lista):
    espanol = input("Ingrese la palabra en español: ")
    ingles = input("Ingrese la palabra en ingles:  ")
    if(espanol == "-1" or ingles == "-1"):
        print("Termino de cargar el diccionario")
        return 1
    elif(len(espanol) > 0 and len(ingles) > 0):
        lista[espanol] = ingles
        print(lista)
        return 0
    else:
        print("Una de esas palabras es invalida!")
        return 0

def printLista(lista):
    print("Diccionario: ")
    for palabra in lista:
        print(f"{palabra} se traduce como {lista[palabra]}")

def buscarPalabra(lista):
    buscar = input("Ingrese la palabra que quiere traducir: ")
    if buscar == "-1":
        print("Termino de buscar")
        return 1
    elif buscar in lista:
        print(f"{buscar} se traduce como {lista[buscar]}")
    else:
        print(f"No tengo esa palabra en mi diccionario")
    return 0

if __name__ == "__main__":
    lista = {}
    estado = 0
    print("Ingrese palabras al diccionario")
    while(estado == 0):
        estado = getTraduccion(lista)
    estado = 0
    input("Presione ENTER para seguir")
    print("==============================================")
    print("Mostrando todas las traducciones")
    printLista(lista)
    input("Presione ENTER para seguir")
    print("==============================================")
    while(estado == 0):
        estado = buscarPalabra(lista)