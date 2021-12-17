from django.shortcuts import render, redirect
from django.views.generic import ListView, View, TemplateView
from DrinksAndPeople.forms import ComentarioForm
from DrinksAndPeople.models import Categoria, Bebida
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests



class HomeVista(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        # all_bebidas = Bebida.objects.all()[:3]
        # Reserved.objects.filter(client=client_id).order_by('-check_in')
        all_bebidas = Bebida.objects.all().order_by('karma')
        all_bebidas = list(reversed(all_bebidas))[:3]

        context['all_bebidas'] = all_bebidas
        return context
class BebidaVista(TemplateView):
    template_name = 'bebida.html'

    def get_context_data(self,pk,**kwargs):
        context =  super().get_context_data(**kwargs)
        bebida = Bebida.objects.get(id=pk)
        print(bebida)
        print(bebida.BebidaCocktailID)

        link_bebida = f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={bebida.BebidaCocktailID}'

        r = requests.get(link_bebida)
        json_bebida = r.json()['drinks'][0]
        if r.status_code == 200:
            context['bebida'] = bebida
            # print(json_bebida['strGlass'])
            context['vaso'] = json_bebida['strGlass']
            context['instrucciones'] = json_bebida['strInstructions']
            # context['vaso'] = json_bebida['drinks']

        return context


class Categorie(TemplateView):
    template_name = 'categorie.html'

    def get_context_data(self, pk,**kwargs):

        context =  super().get_context_data(**kwargs)
        all_bebidas = Bebida.objects.filter(categoria__id = pk)
        context['all_bebidas'] = all_bebidas
        return context


def form_view(request,):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('categories')
    else:
        form = ComentarioForm()  

    return render(request, 'prueba.html', {'form': form})

class Categories(TemplateView):

    template_name = 'categories.html'
    def get_context_data(self, **kwargs):
        print("prueba")
        context =  super().get_context_data(**kwargs)
        all_categories = Categoria.objects.all()
        context['all_categories'] = all_categories
        print(context)
        return context

def KarmaPostPos(request, pk):
    bebida = Bebida.objects.get(id=pk)
    bebida.karma = bebida.karma + 1
    bebida.save()
    # return HttpResponseRedirect(reverse('categories'))
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def KarmaPostNeg(request, pk):
    bebida = Bebida.objects.get(id=pk)
    bebida.karma = bebida.karma - 1 
    bebida.save()
    # return HttpResponseRedirect(reverse('categories'))
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    

#user = User.objects.get(username=self.request.user.username)
# user.profile.todos += 1
# user.profile.save()
