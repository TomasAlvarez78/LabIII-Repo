from pathlib import Path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeVista.as_view(), name="home"),
    path('categories/',views.Categories.as_view(), name="categories"),
    path('categorie/<int:pk>/',views.Categorie.as_view(), name="categorie"),
    path('bebida/<int:pk>/',views.BebidaVista.as_view(), name="bebida"),
    path('karmapos/<int:pk>', views.KarmaPostPos, name="karmapos"),
    path('karmaneg/<int:pk>', views.KarmaPostNeg, name="karmaneg"),
    path('random/', views.B_random.as_view(), name="random"),

]