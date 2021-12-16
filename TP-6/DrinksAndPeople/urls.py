from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeVista.as_view(), name="home"),
    path('categories/',views.Categories.as_view(), name="categories"),
    path('categorie/<int:pk>/',views.Categorie.as_view(), name="categorie"),
    path('prueba/',views.form_view, name="prueba"),

]