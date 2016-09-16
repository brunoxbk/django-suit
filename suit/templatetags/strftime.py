
from django import template

register = template.Library()

@register.filter(name='strftime')
def strftime(value, str):
    return value.strftime(str)
