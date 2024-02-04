from django import template


register = template.Library()

@register.filter(name='charcut')
def charcut(value, arg):
    """
    This cuts all chars in arg from string. 
    """

    return value.replace(arg, '')