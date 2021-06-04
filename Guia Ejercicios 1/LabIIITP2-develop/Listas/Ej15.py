lista= []
mayor = 0
for x in range(5):
    sueldo  = float (input(f"Ingrese el sueldo del empleado {x + 1} de la manana: "))
    lista.append(sueldo)

for i in range(0,len(lista)):
    if(lista[i]>mayor):
        mayor= lista[i]
        pos = i

lista.insert(5,mayor)
lista.pop(pos)

print(lista)