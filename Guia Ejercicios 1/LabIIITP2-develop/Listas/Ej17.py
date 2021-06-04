lista1 =  []
lista2 =  []
superlista = []
a = 0



print("Lista 1: ")

for x in range(5):
    valor  = float (input(f"Ingrese el valor {x + 1} de la lista 1: "))
    lista1.append(valor)

print("Lista 2: ")

for i in range(5):
    valor  = float (input(f"Ingrese el valor {i + 1} de la lista 2:  "))
    lista2.append(valor)

superlista.append(lista1)
superlista.append(lista2)

for suma in map(sum,superlista):
    print(f"Lista {a + 1} ")
    print(suma)
    a = a + 1

