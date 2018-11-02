from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='img_url')
@stringfilter
def img_url(img, ext):
    """ Build the full Marvel thumbnail URL """
    return img + '.' + ext