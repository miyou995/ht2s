
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from core.sitemaps import StaticSitemap
from django.contrib.sitemaps.views import sitemap
from config import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

sitemaps = {
    'static': StaticSitemap,
}

urlpatterns = [
path('i18n/', include('django.conf.urls.i18n')),                            
                            
                            
]
   

urlpatterns  += i18n_patterns(
    path('robots.txt',TemplateView.as_view(template_name='robots.txt', content_type='text/plain')), 
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('', include("core.urls")),
    path('', include("business.urls")),
    path('translation/', include('rosetta.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += i18n_patterns(path('admin/', admin.site.urls),)

else: 
    urlpatterns +=  i18n_patterns(
        path('admin-zone/', admin.site.urls),
        )