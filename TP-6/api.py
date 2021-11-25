import requests
import os
import sys
# import django

# from DrinksAndPeople.models import Bebida, Categoria



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

# def cargarCategorias():
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
#     os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
#     django.setup()
#     categoria = cargarCategorias()
#     for cat in categoria:
#         c = Categoria(
#                     nombre = cat
#                 )
#         c.save()

def cargarCategoriasFormateado():
    api_link = 'https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list'
    categorias = []
    # Listo las categorias
    r = requests.get(api_link)
    respuesta = r.json()
    if r.status_code == 200:
        for obj in respuesta['drinks']:
            categorias.append(obj['strCategory'].replace(' ','_'))
    return categorias


# Cargo todos los dict segun su categoria
categorias = cargarCategoriasFormateado()
dict = {}
total = 0
# for cat in categorias:
    # r2 = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c={cat}')
r2 = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Ordinary_Drink')
if r2.status_code == 200:
    respuesta2 = r2.json()['drinks']
    i = 0
    for obj in respuesta2:
        if i > 0:
            break
        r3 = requests.get('https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={0}'.format(obj['idDrink']))
        if r3.status_code == 200:
            respuesta3 = r3.json()
            for obj2 in respuesta3['drinks']:
                print(obj2)

                # b = Bebida(
                #     nombre = obj2['strDrink'],
                #     BebidaCocktailID = obj2['idDrink'],
                #     categoria = cat,
                #     ingredientes = ,
                #     imagen = obj['strDrinkThumb']
                # )

        # if (cat in dict):
        #     dict[cat].append(obj['strDrink'])
        # else:
        #     dict[cat] = [obj['strDrink']]
        i = i + 1
        
# for key in dict:
#     print (f"Categoria {key}")
#     for values in dict[key]:
#         print(f"Cocktail {values}")
#         total = 1 + total
#     print("")

# print(f"Hay un total de {total} dict")

# ID
# Nombre
# Categoria
# Pasos?
# Ingredientes
# Peso
# Imagen