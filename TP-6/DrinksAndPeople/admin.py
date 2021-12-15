from django.contrib import admin
from DrinksAndPeople.models import Categoria,Ingrediente,Bebida,Comentario
# Register your models here.

admin.site.register(Categoria,)
admin.site.register(Ingrediente,)
admin.site.register(Bebida,)
admin.site.register(Comentario,)