import json
from django.core.serializers.json import DjangoJSONEncoder
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='img_url')
@stringfilter
def img_url(img, ext):
    """ Build the full Marvel thumbnail URL """

    return img + '.' + ext

@register.filter(name='to_json')
def to_json(json_chunk):
    """ Serialize DOM objects for JS pass """

    return json.dumps(json_chunk, cls=DjangoJSONEncoder)