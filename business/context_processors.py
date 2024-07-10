from django.shortcuts import render , get_object_or_404
from .models import Business

def infos(request):
    business = Business.objects.all().first()
    context = {
            'business' : business,
        }
    return context
    

