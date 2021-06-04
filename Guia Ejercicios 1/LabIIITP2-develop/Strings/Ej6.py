oracion = input("Ingrese una oracion: ")
b = 0
vocales = ['A','a','E','e','I','i','O','o','U','u']

for x in range(len(oracion)):
    if oracion[x] in vocales:
        b = b + 1

print(f"Cantidad de vocales: {b}")
print(oracion.lower())