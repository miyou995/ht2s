from django.utils.translation import *

def base_template(request):
    # base_template = 'rtl/base.html' if request.LANGUAGE_CODE == 'ar' else 'base.html'
    base_template = 'base.html'
    context = {
        'base_template' : base_template,
        'current_lang' : request.LANGUAGE_CODE,
    }

    return context


