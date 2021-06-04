lista = []

for x in range(3):
    nombre = input("Ingrese el nombre de la persona: ")
    lista.append(nombre)

contador = 0
for x in range(0,len(lista)): 
    longitud = len(lista[x])
    if (longitud > 5):
        contador = contador + 1
   
print(f"Nombres con mas de 5 letras:{contador}")