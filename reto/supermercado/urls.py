from django.urls import path
from .views import principal, listarProducto, agregarProducto,modificarProducto,eliminarProducto
urlpatterns = [
    path("listar/", listarProducto, name='listar'),
    path('',principal, name='loby'),
    path('agregar/',agregarProducto, name='agregar'),
    path('modificar/<int:id_producto>',modificarProducto, name='modificar'),
    path('eliminar/<int:id_producto>',eliminarProducto, name='eliminar'),
]