import os
from operaciones import getChar
def main():
    string1 = input("Ingrese el primer nombre: ")
    string2 = input("Ingrese el segundo nombre: ")
    x1 = getChar(string1)
    x2 = getChar(string2)

    if(x1 > x2):
        print(f"El string {string1} tiene mas caracteres que {string2}")
    elif(x2 > x1):
        print(f"El string {string2} tiene mas caracteres que {string1}")
    else:
        print("Los string tienen la misma cantidad de caracteres")
    

if __name__ == "__main__":    
    os.system('cls')
    main()