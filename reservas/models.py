from django.db import models
from django.conf import settings

class Espacio(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()          
    hora_fin = models.TimeField()      
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, default=1)

    def __str__(self):
        return f"{self.id} | {self.espacio.nombre} | {self.usuario.username}"