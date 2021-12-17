from django.shortcuts import render, redirect
from django.views.generic import ListView, View, TemplateView
from DrinksAndPeople.models import Categoria, Bebida
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
from django.db.models import Max
from random import randint

class HomeVista(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        all_bebidas = Bebida.objects.all().order_by('karma')
        all_bebidas = list(reversed(all_bebidas))[:3]

        context['all_bebidas'] = all_bebidas
        return context

class BebidaVista(TemplateView):
    template_name = 'bebida.html'

    def get_context_data(self,pk,**kwargs):
        context =  super().get_context_data(**kwargs)
        bebida = Bebida.objects.get(id=pk)

        link_bebida = f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={bebida.BebidaCocktailID}'

        r = requests.get(link_bebida)
        if r.status_code == 200:
            json_bebida = r.json()['drinks'][0]
            context['bebida'] = bebida
            context['vaso'] = json_bebida['strGlass']
            context['instrucciones'] = json_bebida['strInstructions']
        return context

class Categorie(TemplateView):
    template_name = 'categorie.html'

    def get_context_data(self, pk,**kwargs):
        context =  super().get_context_data(**kwargs)
        all_bebidas = Bebida.objects.filter(categoria__id = pk)
        context['all_bebidas'] = all_bebidas
        return context

class Categories(TemplateView):
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        all_categories = Categoria.objects.all()
        context['all_categories'] = all_categories
        return context

class B_random(TemplateView):
    template_name = 'random.html'
    
    def get_context_data(self, **kwargs):
        context = super(B_random, self).get_context_data(**kwargs)
        max_bebida = Bebida.objects.aggregate(Max('id'))
        bebida_random = randint(1, max_bebida['id__max'])
        bebida= Bebida.objects.get(id=bebida_random)
        context["bebida"] = bebida
        return context

def KarmaPostPos(request, pk):
    bebida = Bebida.objects.get(id=pk)
    bebida.karma = bebida.karma + 1
    bebida.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def KarmaPostNeg(request, pk):
    bebida = Bebida.objects.get(id=pk)
    bebida.karma = bebida.karma - 1 
    bebida.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    