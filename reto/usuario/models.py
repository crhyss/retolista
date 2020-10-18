from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 40, null = False, blank = False)
    apellido = models.CharField(max_length = 40, null = False, blank = False)
    edad = models.PositiveIntegerField()
    fecha_nacimiento = models.DateTimeField()
    genero = models.CharField(max_length = 30, null = False, blank = False)