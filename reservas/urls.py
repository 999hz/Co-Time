from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path("", views.index, name="index"),
    path("crear/", views.crear, name="crear"),
    path("agenda/", views.agenda, name="agenda"),
    path("eliminar/<int:id>/", views.eliminar_reserva, name="eliminar"),
    path("editar/<int:id>/", views.editar_reserva, name="editar"),
    path("api/eventos/", views.api_eventos, name="api_eventos"),
]