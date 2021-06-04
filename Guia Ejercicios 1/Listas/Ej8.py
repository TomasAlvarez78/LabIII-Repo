lista = []
for x in range(5):
    altura = float(input("Ingrese la altura de la persona: "))
    lista.append(altura)

for x in range(0,len(lista)):
    print(f"Altura persona {x + 1}: {lista[x]}")


