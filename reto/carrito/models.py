from django.db import models
from supermercado.models import Producto
from usuario.models import Usuario

# Create your models here.
class Lista(models.Model):
    nombreLista = models.CharField(max_length = 100, null= False, blank = False)
    productos = models.ManyToManyField(Producto)
    user = models.OneToOneField(Usuario, on_delete = models.CASCADE)