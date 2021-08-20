b = 0
while(True):
    mensaje= input("Ingrese una contrasena: ")
    b = len(mensaje)

    if(b > 10 and b <= 20):
        print("Contrasena cargada con exito")
        break

    print("Vuelva a ingresar la contrasena, no cumple con lo solicitado")
