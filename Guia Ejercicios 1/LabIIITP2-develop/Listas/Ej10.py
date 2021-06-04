listaT = []
listaM = []
for x in range(4):
    sueldo  = float (input(f"Ingrese el sueldo del empleado {x + 1} de la manana: "))
    listaM.append(sueldo)

for i in range(4):
    sueldo  = float (input(f"Ingrese el sueldo del empleado {i+ 1} de la tarde: "))
    listaT.append(sueldo)

print("Sueldos Manana: ")
for x in  range(0,len(listaM)):
    print(f"Empleado {x + 1}: {listaM[x]}")

print("Sueldos Tarde: ")
for x in  range(0,len(listaT)):
    print(f"Empleado {x + 1}: {listaT[x]} ")
