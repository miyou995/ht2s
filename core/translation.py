from modeltranslation.translator import translator, TranslationOptions
from .models import Service , Solution






class ServiceTranslationOptions(TranslationOptions):
     fields =('name','about_high')

translator.register(Service,ServiceTranslationOptions)



class SolutionTranslationOptions(TranslationOptions):
     fields =('name', 'title', 'text', 'description')

translator.register(Solution,SolutionTranslationOptions)



