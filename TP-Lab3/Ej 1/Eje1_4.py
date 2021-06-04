from operaciones import areaCuadrado,perimetroCuadrado
import os

def menu():
    opciones = {0,1,2}
    while(1):
        print("===Menu===")
        print("1 - Calcular perimetro")
        print("2 - Calcular superficie")
        print("0 - Salir")
        val = int(input("Ingrese la opcion: "))
        if(val in opciones):
            return val
        else:
            print("Ingreso un valor invalido, intentelo denuevo!")
            input("Presione ENTER para continuar")
            os.system('cls')

#Es un cuadrado, no un rectangulo
def main():
    lista = []
    x = 0
    x1 = 0
    while(1):
        if x < 1:
            print("Ingrese los lados del cuadrado")

            while x < 1:
                x = int(input(f"Ingrese el valor de la base: "))
                if(x < 1):
                    print("Ingreso un valor incorrecto!")
            
            while(x1 < 1):
                x1 = int(input(f"Ingrese el valor de la altura: "))
                if(x1 < 1):
                    print("Ingreso un valor incorrecto!")    
            lista.append(x)
            lista.append(x1)
            
        os.system('cls')
        val = menu()
        if(val == 1):
            print(f"El perimetro del cuadrado es: {perimetroCuadrado(lista)}")
        elif(val == 2):
            print(f"El area del cuadrado es: {areaCuadrado(lista)}")
        else:
            print("Adios!")
            return
        input("Presione ENTER para continuar")
        os.system('cls')


    
    

if __name__ == "__main__":    
    os.system('cls')
    main()
