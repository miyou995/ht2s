from django.contrib import admin
from business.models import Business,Slide
from django.utils.html import format_html

# from modeltranslation.admin import TranslationAdmin



Business._meta.verbose_name = "Informations "


@admin.register(Business)
class BusinesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')

    def has_add_permission(self, request):
        business = Business.objects.all()
        if business.count() > 1:
            return False
        else: 
            return True
        

admin.site.register(Slide) 