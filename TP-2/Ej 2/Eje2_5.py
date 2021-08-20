def cargarProducto(lista):
	try:
		codigo = int(input("Ingrese el codigo del producto: "))
		if codigo == -1:
			print("Termino de cargar")
			return 1
		nombre = input("Ingrese el nombre del producto: ")
		precio = float(input("Ingrese el precio del producto: "))
		stock = int(input("Ingrese el stock del producto: "))
	except Exception:
		print("No seas malo :C")
		return 0
	if(codigo not in lista):
		lista[codigo] = [nombre,precio,stock]
		print(lista)
		return 0
	else:
		print("Un valor es invalido")
		return 0

def printLista(lista):
	print("Diccionario: ")
	for producto in lista:
		print(f"{producto} => {lista[producto][0]}\nPrecio: ${lista[producto][1]} -- Stock: {lista[producto][2]}")

def stockCero(lista):
	counter = 0
	for producto in lista:
		if(lista[producto][2] == 0):
			print(f"{producto} => {lista[producto][0]}\nPrecio: ${lista[producto][1]} -- Stock: {lista[producto][2]}")
			counter += 1
	if counter == 0:
		print("No hay productos con stock 0")

if __name__ == "__main__":
	lista = {}
	estado = 0
	print("Cargue los productos")
	while(estado == 0):
		estado = cargarProducto(lista)
	estado = 0
	input("Presione ENTER para seguir")
	print("==============================================")
	print("Mostrando todos los productos")
	printLista(lista)
	input("Presione ENTER para seguir")
	print("==============================================")
	print("Mostrando productos con stock cero")
	stockCero(lista)