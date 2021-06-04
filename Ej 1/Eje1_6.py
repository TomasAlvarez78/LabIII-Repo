import os
from operaciones import mayor,menor,totalLista

def menu():
    opciones = {0,1,2,3,4}
    while(1):
        print("===Menu===")
        print("1 - Mayor de la lista")
        print("2 - Menor de la lista")
        print("3 - Suma total de la lista")
        print("4 - Limpiar lista")
        print("0 - Salir")
        val = int(input("Ingrese la opcion: "))
        if(val in opciones):
            return val
        else:
            print("Ingreso un valor invalido, intentelo denuevo!")
            input("Presione ENTER para continuar")
            os.system('cls')

def main():
    lista = []
    x = 0
    bandera = 0
    counter = 0
    print("Ingrese -1 para terminar el ingreso de datos")
    while(1):
        if(bandera != 1):
            x = int(input(f"Ingrese el valor numero {counter}: "))
            counter+=1
            if(x > 0):
                lista.append(x)
            if(x == -1):
                bandera = 1
                print("Ingreso de elementos finalizado")
                input("Presione ENTER para ir a menu")
        else:    
            os.system('cls')
            val = menu()
            if(val == 1):
                print(f"El mayor numero de la lista es: {mayor(lista)}")
            elif(val == 2):
                print(f"El menor numero de la lista es: {menor(lista)}")
            elif(val == 3):
                print(f"La suma de la lista es: {totalLista(lista)}")
            elif(val == 4):
                lista.clear()
                bandera = 0
                counter = 0
                print("La lista ahora esta vacia")
            else:
                print("Adios!")
                return
            input("Presione ENTER para ir a menu")


if __name__ == "__main__":    
    os.system('cls')
    main()