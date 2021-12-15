from django.shortcuts import render, redirect

from DrinksAndPeople.forms import ComentarioForm
from DrinksAndPeople.models import Comentario



categories = [
    {'id': 1, 'name': 'Categorie 1'},
    {'id': 2, 'name': 'Categorie 2'},
    {'id': 3, 'name': 'Categorie 3'},
    #{'id': 7, 'name': 'Categorie 3'},
    #{'id': 8, 'name': 'Categorie 3'},
    #{'id': 9, 'name': 'Categorie '},
    #{'id': 10, 'name':'Categorie 10'},
    #{'id': 11, 'name':'Categorie 11'},
]

posts = [
    {
        'author': 'ASDSADASD',
        'title': 'Blog Post 1',
        'content' : 'First post content',
        'date_posted': 'NOv 20, 2011'
    },
    {
        'author': 'asdasd',
        'title': 'Blog Post 1',
        'content' : 'First post content',
        'date_posted': 'NOv 18, 2011'
    }
]

def home(request):
    return render(request, "home.html")

def categories(request):
    
    return render(request, "categories.html")

def categorie(request,pk):
    context = {'categories': categories}
    
    return render(request,"categorie.html", context)

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