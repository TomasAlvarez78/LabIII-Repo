from django import forms
from django.forms import widgets

from DrinksAndPeople.models import Comentario


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario

        fields = '__all__'
        
        label = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'descripcion': 'Descripcion',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }


#class ComentarioForm(forms.Form):
#
#    nombre = forms.CharField(label= "Nombre", max_length=100, required=True)
#    apellido = forms.CharField(label= "Apellido", max_length=100, required=True)
#    descripcion = forms.CharField(label="Comentario", required=True, widget=forms.Textarea())