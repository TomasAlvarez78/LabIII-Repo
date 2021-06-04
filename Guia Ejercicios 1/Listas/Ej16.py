lista= []
mayor = 0
for x in range(5):
    sueldo  = float (input(f"Ingrese el sueldo del empleado {x + 1} de la manana: "))
    lista.append(sueldo)

lista.sort()
print(lista)