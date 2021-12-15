from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('categories/',views.CategoriesList.as_view(), name="categories"),
    path('categorie/<int:pk>/',views.categorie, name="categorie"),
    path('prueba/',views.form_view, name="prueba"),

]