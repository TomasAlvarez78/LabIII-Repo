# <center>TRABAJO FINAL

## <center>Drinks & People
![cocktail.ico](https://raw.githubusercontent.com/TomasAlvarez78/LabIII-Repo/master/TP-6/static/assets/cocktail.ico)

  ***<center>**Integrantes**: Bustos Rios Lucas Nicolas, Alvarez Tomas Ignacio, Madruga Savino Bautista.


# <center>INTRODUCCION

En nuestro proyecto final "Drinks & People" creamos una aplicacion de Django en la cual utilizamos una api de recopilacion de datos sobre bebidas y cockteles de todo el mundo. Algunos datos consumidos desde la api los guardamos en una base de datos (sqlite3) para luego ser mostrados en nuestra pagina y otros de los datos los usamos directamente desde la api al abrir una de nuestras paginas.
Para crear nuestras paginas web utilizamos el lenguaje HTML importando e implementando biblioteca de BOOTSTRAP v5.0


# <center>DOCUMENTACION

 -[Pagina Oficial Requests](https://docs.python-requests.org/en/latest/),
 -[Pagina Oficial API](https://www.thecocktaildb.com/),
 -[Documentacion BOOTSTRAP](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
 -[Documentacion DJANGO](https://docs.djangoproject.com/en/4.0/)

 # <center>INSTALACION
 
Creamos un entorno virtual con virtualenvwrapper
```mkvirtualenv <nombre>```

Ingresamos dentro del virtualenv recien creado
```workon <nombre>```

Instalamos los requerimientos (Django y requests) en nuestro entorno virtual con el comando en consola 
```pip install -r "requirements.txt"```

 # <center>EJECUTAR SERVIDOR

```python3 manage.py runserver```
