def getPais(lista):
    pais = input("Ingrese el pais: ")
    habitantes = int(input("Ingrese sus habitantes: "))
    if(len(pais) > 0 and habitantes > 0):
        lista[pais] = habitantes
        print(lista)
    else:
        print("Ese pais/cantidad son invalidos!")

def printLista(lista):
    for pais in lista:
        print(f"{pais} tiene {lista[pais]} habitante/s")

if __name__ == "__main__":
    lista = {}
    while(len(lista) < 5):
        getPais(lista)
    printLista(lista)