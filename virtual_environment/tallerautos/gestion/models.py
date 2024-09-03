from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Agenda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.usuario} - {self.servicio} - {self.fecha} {self.hora}"