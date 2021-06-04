
def ingresar():
    diccionario = {}
    fecha = input("Ingrese la fecha: ")
    actividad = input("Ingrese la actividad: ")
    horario= input("Ingrese el horario: ")
    diccionario[fecha] = [actividad,horario]

    return diccionario

def listar(diccionario):

    for fecha in diccionario:
        print(f"Fecha: {fecha} \n")
        print(f"Actividad: {fecha[0]}")
        print(f"Horario: {fecha[1]}")    

def consultar_fecha(diccionario):

    fecha = input("Ingrese la fecha que desea consultar: ")
    z = 1
    for x in diccionario:
        if fecha == x:
            print("La fecha existe")
            z = 0
    if z==1: 
        print("La fecha no existe")
    
diccionario = ingresar()
listar(diccionario)
consultar_fecha(diccionario)


