lista  = []
for x in range(5):
    numero = int(input("Ingrese un entero: "))
    lista.append(numero)

for x in range(0,len(lista)):
    print(f"Numero: {lista[x]}",end=' ')