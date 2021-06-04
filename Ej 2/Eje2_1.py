
def ingreso(lista):
    x = 0
    while(x < 5):
        pais = input("Ingrese el nombre del pais: ")
        habitantes = int(input(f"Ingrese la cantidad de habitantes de {pais}: "))
        if(len(pais) > 0 and habitantes > 0):
            lista.append(tuple((pais,habitantes)))
            x+=1
        else:
            print("Un dato es erroneo, no voy a contar esta vuelta")

def mostrarLista(lista):
    for dato in lista:
        print(f"El pais {dato[0]} tiene {dato[1]} habitantes")

def getMayor(lista):
    aux = tuple()
    mayor = 0
    for dato in lista:
        if(dato[1] > mayor):
            aux = dato
            mayor = dato[1]
    print(f"El pais {aux[0]} es el que tiene mas habitantes, con {aux[1]} ")

if __name__ == "__main__":    
    lista= list()
    ingreso(lista)
    mostrarLista(lista)
    getMayor(lista)
