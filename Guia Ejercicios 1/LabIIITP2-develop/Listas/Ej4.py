lista = []
contador = 0
for x in range(8):
    numero = int(input("Ingrese el valor: "))
    lista.append(numero)
    if (numero > 100):
        contador = contador + 1

print("Valores lista:")

for x in range(8):
    print(lista[x],end=' ')
print("")
print(f"Valores mayor a 100: {contador}")