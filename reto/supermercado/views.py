from django.shortcuts import render,redirect
from .models import Producto, carrito 
from .forms import ProductoForm, carritoForm
# Create your views here.

def listarProducto(request):
    productos = Producto.objects.all()
    context = {
        'titulo': 'Productos',
        'productos': productos
    }
    return render(
        request,
        'cuerpo/listar.html',
        context
    )
    
def principal(request):
    productos = Producto.objects.all()
    context ={
        'titulo':'loby',
        'productos': productos
    }
    return render(
        request,
        'cuerpo/principal.html',
        context
    )
def agregarProducto(request):
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listar/','/')
    else:
        formulario = ProductoForm()
    context = {
        'titulo':'Agregar Producto',
        'formulario':formulario
    }    
    return render(
        request,
        'cuerpo/agregar.html',
        context
    )
def modificarProducto(request,id_producto):
    productoRecibido = Producto.objects.get(pk=id_producto)
    formulario = None
    if request.method =='POST':
        formulario = ProductoForm(request.POST, instance=productoRecibido)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listar/')
    else:
        formulario = ProductoForm(instance=productoRecibido)
    context = {
        'titulo':'Modificar Producto',
        'formulario':formulario
    }    
    return render(
        request,
        'cuerpo/modificar.html',
        context
    )
def eliminarProducto(request,id_producto):
    productoEliminado = Producto.objects.get(pk = id_producto)
    productoEliminado.delete()
    return (redirect('/listar/'))

