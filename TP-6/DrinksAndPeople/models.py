from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400,
                                    default=None,
                                    null=True,
                                    blank=True)
    imagen = models.ImageField(upload_to='categoriaImagenes/',
                                null=True,
                                default=None,
                                blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    def __str__(self):
        return self.nombre

class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    BebidaCocktailID = models.IntegerField()
    categoria = models.ForeignKey(Categoria,null=False,on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente,
                                            verbose_name='Ingredientes',
                                            default=None,
                                            blank=True,
                                            related_name='mis_ingredientes')
    imagen = models.ImageField(upload_to='bebidasImagenes/')
    # imagen_url = models.CharField(max_length=512)
    
    class Meta:
        verbose_name = 'Bebida'
        verbose_name_plural = 'Bebidas'

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    nombre =  models.CharField(max_length=100)
    apellido =  models.CharField(max_length=100)
    descripcion = models.TextField(max_length=600)