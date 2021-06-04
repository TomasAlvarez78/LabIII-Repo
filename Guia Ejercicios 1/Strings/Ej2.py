b = 0
c = 1
vocales = ['A','a','E','e','I','i','O','o','U','u']
while(c == 1):
    nombre = input("Ingrese su nombre en minusculas: ")
    if(nombre == nombre.lower()):
        c = 0
    else:
        print("Vuelva a ingresar el nombre")

for x in nombre:
    if nombre[0] in vocales:
        b = 1

if b == 1:
    print("El nombre comienza con vocal")
else:
    print("El nombre no comienza con vocal")

print(f"El largo del nombre es: {len(nombre)}")

