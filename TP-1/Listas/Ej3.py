lista = []

nombre = input("Nombre alumno: ")
lista.append(nombre)

nota1 = int (input("Primer nota: "))
lista.append(nota1)

nota2 = int (input("Segunda nota: "))
lista.append(nota2)

promedio = (nota1 + nota2)/2

print(f"Nombre: {lista[0]}")

print(f"Promedio: {promedio}")