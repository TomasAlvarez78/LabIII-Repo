from django.urls import path
from DrinksAndPeople.views import HomeVista
from . import views

urlpatterns = [
    path('',HomeVista.as_view(), name="home"),
    path('categories/',views.Categories.as_view(), name="categories"),
    path('categorie/<int:pk>/',views.Categorie.as_view(), name="categorie"),
    path('prueba/',views.form_view, name="prueba"),

]