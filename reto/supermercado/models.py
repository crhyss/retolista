from django.db import models

# Create your models here.
class Producto(models.Model):
    foto = models.URLField(max_length=200, null = False, blank= False)
    nombre = models.CharField(max_length=50, null = False, blank = False)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

class carrito(models.Model):
    Producto = models.ForeignKey(Producto,on_delete= models.CASCADE)
    fechaCompra = models.DateField(auto_now= True)
    cantidad = models.PositiveIntegerField()
