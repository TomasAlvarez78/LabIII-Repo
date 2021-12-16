from django.shortcuts import render, redirect
from django.views.generic import ListView, View, TemplateView
from DrinksAndPeople.forms import ComentarioForm
from DrinksAndPeople.models import Categoria, Bebida


class HomeVista(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        all_bebidas = Bebida.objects.all()[:3]
        context['all_bebidas'] = all_bebidas
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
