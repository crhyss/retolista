from django import forms
from .models import Producto,carrito
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['foto','nombre','precio','stock']

class carritoForm(forms.ModelForm):
    class Meta:
        model = carrito
        fields = ['cantidad']

    
