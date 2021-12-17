from django.core.management.base import BaseCommand
from DrinksAndPeople.models import  *
from django.core.management import call_command

import os
import sys
import requests
import glob

from urllib.request import AbstractDigestAuthHandler, urlopen

class Command(BaseCommand):
    def handle(self, *args, **options):

        bebidas_por_categoria = 3

        try:
            Bebida.objects.all().delete()
            Categoria.objects.all().delete()
            Ingrediente.objects.all().delete()
        except:
            print("No hay base de datos")
            
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
                    if i > bebidas_por_categoria:
                        break
                    i = i + 1
                    print(bebida)
                    bebidaId = bebida['idDrink']

                    # Creo y guardo las bebidas sin ingredientes
                    img_url = bebida['strDrinkThumb']

                    b = Bebida(
                        nombre = bebida['strDrink'],
                        BebidaCocktailID = bebidaId,
                        categoria = Categoria.objects.get(nombre=cat),
                        imagen_url = img_url,
                        karma = 0,
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