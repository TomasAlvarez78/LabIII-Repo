lista1 = [1,]
lista2 = [1,2]
lista3 = [1,2,3]
lista4 = [1,2,3,4]
lista5 = [1,2,3,4,5]

acum = 0

superlista = []
superlista.append(lista1)
superlista.append(lista2)
superlista.append(lista3)
superlista.append(lista4)
superlista.append(lista5)


print(superlista)

for suma in map(sum,superlista):
    acum = acum + suma

print(f"La suma total es: {acum}")