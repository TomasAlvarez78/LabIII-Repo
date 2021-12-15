from django.shortcuts import render, redirect
from django.views.generic import ListView
from DrinksAndPeople.forms import ComentarioForm
from DrinksAndPeople.models import Categoria, Bebida





def home(request):
    return render(request, "home.html")

def categories(request,id=None, *args, **kwargs):

    return render(request, "categorias.html")

def categorie(request,pk):

    #bebida = Bebida.objects.get(id=pk)
    #print(pk)
    #categoria__id = Categoria.objects.get(id=pk)
    bebida = Bebida.objects.filter(categoria__id = pk)
    context = {'bebida': bebida}
    print(bebida)
    return render(request,"categorie.html",context)
    #id = id
    #bebida_obj = None
    #if id is not None:
    #    bebida_obj = Bebida.objects.get(id=id)
    #context = {'object':bebida_obj}

#def form_view(request):
#
#    form = ComentarioForm()
#
#    return render(request, 'prueba.html', {'form': form})

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

class CategoriesList(ListView):
    model = Categoria
    template_name = 'categories.html'


#def my_view(request, A_pk):
#       
#    a = Categoria.objects.get(pk=A_pk)    
#    
#    return render('pruebacategoria.html', {'a': a})