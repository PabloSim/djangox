from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    parentezco = models.CharField(max_length=40)
    dni = models.IntegerField()
    