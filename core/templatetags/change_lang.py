from django import template
from django.template.defaultfilters import register
from django.urls import translate_url


register = template.Library()


@register.simple_tag()
def change_lang(path, lang):
    return translate_url(path, lang)