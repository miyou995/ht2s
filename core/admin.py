from django.contrib import admin
from core.models import  Service, Contact, Quote, Hiring, About, Service, Company, CompanyItem
from django.utils.html import format_html
# from modeltranslation.admin import TranslationAdmin
# from modeltranslation.admin import TranslationAdmin


Service._meta.verbose_name = "content"

class CompanyItemInline(admin.TabularInline):
    model = CompanyItem
    raw_id_fields = ["company"]
        
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "order", 
    ]
    inlines = [CompanyItemInline]
    list_per_page = 30

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name')
    list_per_page = 40
admin.site.register(Service, ServiceAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    exclude= ('name_fr','about_high_fr', 'about_low_fr', 'title_fr')
    list_display_links = ('id','name')
    list_per_page = 40
admin.site.register(About, AboutAdmin)


admin.site.register(Contact) 
admin.site.register(Quote) 
admin.site.register(Hiring) 