import os
opciones = {0,1,2}

def sumar(n1,n2):
    return n1 + n2

def restar(n1,n2):
    return n1 - n2

def multiplicar(n1,n2):
    return n1 * n2

def dividir(n1,n2):
    if (n2 != 0):
        return n1 / n2
    else:
        print("No me siento capacitado para resolver el mismo infinito!\n (No se puede dividir por 0)")

def totalLista(lista):
    acum = 0
    for i in lista:
        acum += i
    return acum

def mayor(lista):
    if(len(lista) > 0):
        return max(lista)
    else:
        print("Esta lista no tiene elementos :C")
        return -1

def menor(lista):
    if(len(lista) > 0):
        return min(lista)
    else:
        print("Esta lista no tiene elementos :C")
        return -1

def perimetroCuadrado(lista):
    z = 0
    for num in lista:
        z += num*2
    return z

def areaCuadrado(lista):
    return lista[0] * lista[1]

def getChar(string1):
    return len(string1.strip())
    

# def menu():
#     while(1):
#         print("===Menu===")
#         print("1 - Sumar")
#         print("0 - Salir")
#         val = int(input("Ingrese la opcion: "))
#         if(val in opciones):
#             return val
#         else:
#             print("Ingreso un valor invalido, intentelo denuevo!")
#             input("Presione ENTER para continuar")
#             os.system('cls')
            
