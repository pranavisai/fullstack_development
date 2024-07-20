from django import template

register = template.Library()

@register.filter(name = 'cut') #to register the custome filters
def cut(value, arg):
    """ 
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')


#register.filter('cut',cut)