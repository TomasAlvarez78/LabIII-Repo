lista  = []
numero = 99
while(numero != 0):
    numero = int(input("Ingrese un valor: "))
    if(numero!=0):
        lista.append(numero)
    
for x in range(0,len(lista)):1
    print(f"Numero: {lista[x]}",end=' ')