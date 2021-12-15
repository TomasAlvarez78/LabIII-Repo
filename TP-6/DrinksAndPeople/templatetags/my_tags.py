from django import template
from ..models import Categoria
register = template.Library()

@register.simple_tag
def get_obj(pk, attr):
    obj = getattr(Categoria.objects.get(pk=int(pk)), attr)
    return obj