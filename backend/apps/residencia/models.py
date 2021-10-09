from django.db import models

class Edificio(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    cant_pisos = models.IntegerField()
    cant_habitaciones_piso = models.IntegerField()


class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    capacidad = models.IntegerField()
    piso = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)