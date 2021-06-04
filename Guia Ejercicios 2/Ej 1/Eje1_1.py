from operaciones import sumar
import os

def pedirNumero():
    while(1):    
        try:
            n1 = int(input("Ingrese el 1er numero: "))
            n2 = int(input("Ingrese el 2do numero: "))
            return [n1,n2]
        except:
            print("Ingreso un valor invalido, intentelo denuevo!")
            input("Presione ENTER para continuar")
            os.system('cls')

def main():
    os.system('cls')
    print("Bienvenido!")
    n1,n2 = pedirNumero()
    print(f"La suma es {sumar(n1,n2)}")
    print("Adios")
    input("Presione ENTER para continuar")
    return
    

if __name__ == "__main__":    
    opciones = {0,1,2}
    main()
