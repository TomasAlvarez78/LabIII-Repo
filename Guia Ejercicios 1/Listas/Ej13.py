lista = []

for x in range(5):
    nombre = input(f"Ingrese el nombre de la persona {x+1}: ")
    lista.append(nombre)

lista.sort()

for i in range(5):
    print(f"Nombre: {lista[i]}")

