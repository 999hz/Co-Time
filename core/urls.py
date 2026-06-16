from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('mensajes-admin/', views.panel_mensajes, name='panel_mensajes'),
]