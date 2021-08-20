def capicua(palabra):
	palabra = palabra.lower()
	alreves = palabra[::-1]
	print(palabra)
	print(alreves)
	if(palabra == alreves):
		print("Es capicua")
	else:
		print("No es capicua")

if __name__ == "__main__":
	estado = 0
	while(estado == 0):
		palabra = input("Ingrese una palabra: ")
		if(palabra == '-1'):
			print("Adios!")
			break
		elif(len(palabra) > 0):
			capicua(palabra)
		else:
			print("Ingreso una palabra incorrecta")
	