
from django.urls import path, re_path
from .views import IndexView, AboutView, RecruitingView, ContactView, QuoteoView,  ServiceView, ServiceDetail  
from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('services', ServiceView.as_view(), name='services'),
    path('about', AboutView.as_view(), name='about'),
    path('service_detail/<slug:slug>/', ServiceDetail.as_view(), name='service_detail'),
    path('hiring', RecruitingView.as_view(), name='hiring'),
    path('contact', ContactView.as_view(), name='contact'),
    path('quote', QuoteoView.as_view(), name='quote'),
    # path('<str:language>/contact/', views.contact, name='contact'),
    # path('<str:language>/about/', views.about, name='about'),
    # path('<str:language>/hiring/', views.hiring, name='hiring'),
    # path('<str:language>/services/', views.services, name='services'),
    # path('<str:language>/index/', views.index, name='index'),
    # path('switch_language/', views.switch_language, name='switch_language'),
]
