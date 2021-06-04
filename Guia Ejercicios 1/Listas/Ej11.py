lista = []
mayor = 0

for x in range(5):
    numero = int(input("Ingrese un valor:"))
    lista.append(numero)

for i in range(0,len(lista)):
    if(lista[i]>mayor):
        mayor= lista[i]

print(f"El mayor numero es: {mayor}")
