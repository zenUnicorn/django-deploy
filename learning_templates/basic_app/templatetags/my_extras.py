from django import template

register = template.Library()

#custom filter using decorators
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of arg from the given string
    """
    return value.replace(arg,'')
#register.filter('cut',cut)
    
    