def getArticulo(lista):
    articulo = input("Ingrese el articulo: ")
    precio = int(input("Ingrese su precio: "))
    if(len(articulo) > 0 and precio > 0):
        lista[articulo] = precio
        print(lista)
    else:
        print("Ese articulo/cantidad son invalidos!")

def printLista(lista):
    for articulo in lista:
        print(f"{articulo} vale ${lista[articulo]}")

def printMayor(lista):
    for articulo in lista:
        if(lista[articulo] > 100):
            print(f"{articulo} vale ${lista[articulo]}")

if __name__ == "__main__":
    lista = {}
    while(len(lista) < 5):
        getArticulo(lista)
    print("==============================================")
    print("Ha cargado todos los articulos")
    input("Presione ENTER para seguir")
    print("==============================================")
    print("Mostrando todos los articulos")
    printLista(lista)
    input("Presione ENTER para seguir")
    print("==============================================")
    print("Mostrando mayores a 100")
    printMayor(lista)