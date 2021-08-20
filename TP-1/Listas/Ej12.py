lista = []

for x in range(5):
    numero = int(input("Ingrese un valor:"))
    lista.append(numero)

menor = lista[0]

for i in range(0,len(lista)):
    if(lista[i] < menor):
        menor= lista[i]

print(f"El menor numero es: {menor}")
