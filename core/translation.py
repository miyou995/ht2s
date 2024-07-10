from modeltranslation.translator import translator, TranslationOptions
from .models import Service






class ServiceTranslationOptions(TranslationOptions):
     fields =('name','about_high')

translator.register(Service,ServiceTranslationOptions)



