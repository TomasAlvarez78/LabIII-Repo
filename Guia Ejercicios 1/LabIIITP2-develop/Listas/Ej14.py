lista = []
mayor = 0
contador = 0
for x in range(5):
    numero = int(input("Ingrese un valor:"))
    lista.append(numero)

for i in range(0,len(lista)):
    if(lista[i]>mayor):
        mayor= lista[i]
    

contador = lista.count(mayor)     
        
print(f"El mayor numero es: {mayor}")

print(f"El valor mayor se esta en la lista  {contador} vez/veces")

