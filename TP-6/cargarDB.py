#!/usr/bin/env python
import os
import sys
import requests
from PIL import Image
import glob

from urllib.request import AbstractDigestAuthHandler, urlopen

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
import django

django.setup()
from DrinksAndPeople.models import Categoria,Ingrediente,Bebida

print("Listando las categorias")

link_Cat = 'https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list'
categorias = []

# Listo las categorias
r = requests.get(link_Cat)
json_Cat = r.json()
if r.status_code == 200:
    for cat in json_Cat['drinks']:
        categorias.append(cat['strCategory'])

# Cargo las categorias
cat_imagen = 1
for cat in categorias:
    m = Categoria(
                nombre = cat,
                descripcion = "Descripcion default",
                imagen = glob.glob(f'media/categoriaImagenes/{cat_imagen} -*.jpg')[0]
    )
    cat_imagen = cat_imagen + 1
    m.save()

print("Las categorias han sido obtenidas")
print("Listando ingredientes")
ingredientes = []
objetos_ingredientes = []

# Empiezo buscando 3 bebidas por categoria
# Para poder guardar primero sus ingredientes si no existen
# Para despues guardar el cocktail
for cat in categorias:
    try:
        link_BebidaCat = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c={cat}'
        r2 = requests.get(link_BebidaCat)
        json_BebidaCat = r2.json()
        i = 0
        for bebida in json_BebidaCat['drinks']:
            if i > 3:
                break
            i = i + 1
            print(bebida)
            bebidaId = bebida['idDrink']

            # Creo y guardo las bebidas sin ingredientes
            # img = urlopen(bebida['strDrinkThumb']).read()
            # img_name = 'media/bebidasImagenes/' + bebida['strDrink'].replace("/","-") + ".jpg"
            # open(img_name,"wb").write(img)
            # img = Image.open(img_name)
            img_url = bebida['strDrinkThumb']

            b = Bebida(
                nombre = bebida['strDrink'],
                BebidaCocktailID = bebidaId,
                categoria = Categoria.objects.get(nombre=cat),
                imagen_url = img_url,
                #imagen_url = Image.open(requests.get(bebida['strDrinkThumb'], stream=True).raw)
                # im = Image.open(requests.get(url, stream=True).raw)
                # imagen = bebida['strDrinkThumb']
            )

            b.save()

            link_BebidaID = f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={bebidaId}'
            r3 = requests.get(link_BebidaID)
            json_BebidaID = r3.json()
            bebida = json_BebidaID['drinks']
            
            # Guardo los ingredientes en objetos y en lista
            # para no repetirlos
            for key, value in bebida[0].items():
                if('strIngredient' in key):
                    if value is not None and value != "":
                        if value not in ingredientes:
                            ing = Ingrediente(
                                    nombre = value
                            )
                            ing.save()
                            ingredientes.append(value)
                            print("Ingrediente!")
                        objetos_ingredientes.append(ing)
                    else:
                        print("Salto")
                        break
            
            # Asigno los ingredientes por cada bebida
            for ing in objetos_ingredientes:
                b.ingredientes.add(ing)
            
            objetos_ingredientes.clear()

            print("")
    except Exception:
        continue
