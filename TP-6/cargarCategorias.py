import requests
from DrinksAndPeople.models import Categoria

def cargarCategoriasHelper():
    api_link = 'https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list'
    categorias = []
    # Listo las categorias
    r = requests.get(api_link)
    respuesta = r.json()
    if r.status_code == 200:
        for obj in respuesta['drinks']:
            categorias.append(obj['strCategory'])
    return categorias

#!/usr/bin/env python
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
import django
django.setup()
categorias = cargarCategoriasHelper()
from DrinksAndPeople.models import Categoria    
for cat in categorias:
    m = Categoria(
                nombre = cat
              )
    m.save()