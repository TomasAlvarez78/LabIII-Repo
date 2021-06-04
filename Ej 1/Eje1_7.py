import os

def listade5():
    lista = []
    i = 0
    while i < 5:
        x = int(input(f"Ingrese el valor numero {i+1}: "))
        if(x < 1):
            print("Numero no valido! No lo voy a tomar en cuenta >:C")
        else:
            lista.append(x)
            i+=1
    return lista

def main():
    print(listade5())


if __name__ == "__main__":    
    os.system('cls')
    main()