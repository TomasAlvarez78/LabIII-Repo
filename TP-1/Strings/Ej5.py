oracion = input("Ingrese una oracion: ")
contador = 0

for x in oracion:
    if(x == " "):
        contador = contador + 1

print(f"La cantidad de espacios es: {contador}")

