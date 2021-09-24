from pyside import *

def main():
    print("Main started")

    ventana = QApplication(sys.argv)
    app = PyMain()
    app.show()
    ventana.exec_()

# La aplicación me debe entregar un semáforo con el top 10 de los paises con menos muertes por candidad de habitantes.
# El periodo de tiempo es desde que inicio la pandemia. 
# El criterio de separación para el semáforo lo pueden establecer ustedes. 
# Debe ser configurable a través de un settings.py.

if __name__ == "__main__":
    main()