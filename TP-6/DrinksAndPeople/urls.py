from django.urls import path
from DrinksAndPeople.views import HomeVista
from . import views

urlpatterns = [
    path('',HomeVista.as_view(), name="home"),
    path('categories/',views.categories, name="categories"),
    path('categorie/<int:pk>/',views.categorie, name="categorie"),
    path('prueba/',views.form_view, name="prueba"),
    # path('bebidas/<int:id>',BebidasView.as_view(), name="bebidas"),
    path('random/', views.random, name="random"),

]