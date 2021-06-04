lista = []
acum = 0
contador=0
for x in range(5):
    altura = float(input("Ingrese la altura de la persona: "))
    lista.append(altura)

for x in range(0,len(lista)):
    print(f"Altura persona {x + 1}: {lista[x]}")
    acum = acum + lista[x]

promedio = acum / (len(lista))

for x in range(0,len(lista)):
    if(lista[x] > promedio):
        contador = contador  + 1
        
print(f"Promedio: {promedio}")
print(f"Personas que superan el promedio: {z}")

