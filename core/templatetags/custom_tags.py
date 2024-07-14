from django import template
from django.template.defaultfilters import register
from django.urls import translate_url


register = template.Library()


@register.simple_tag()
def change_lang(path, lang):
    return translate_url(path, lang)



@register.filter
def regroup_by(value, n):
    result = []
    group = []
    for i, item in enumerate(value):
        group.append(item)
        if (i + 1) % n == 0:
            result.append(group)
            group = []
    if group:
        result.append(group)
    return result

