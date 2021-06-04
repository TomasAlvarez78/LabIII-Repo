from operaciones import mayor
import os

def main():
    lista = []
    counter = 0
    while(1):
        x = int(input(f"Ingrese un valor numero {counter}: "))
        print(x)
        counter+=1
        if(x > -1):
            lista.append(x)
        if(x == -1):
            val = mayor(lista)
            if(val != -1):
                print(f"El valor mas alto de la lista es {val}")
            print("Adios!")
            return


if __name__ == "__main__":    
    os.system('cls')
    print("Ingrese todos los numeros que quiera")
    print("Ingrese -1 para salir")
    main()
