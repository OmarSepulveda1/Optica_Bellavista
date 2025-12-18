# tienda/admin.py
from django.contrib import admin
from .models import Categoria, Etiqueta, Producto, DetalleProducto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields = ('nombre',)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','precio','categoria')
    search_fields = ('nombre',)
    list_filter = ('categoria',)

@admin.register(DetalleProducto)
class DetalleProductoAdmin(admin.ModelAdmin):
    list_display = ('producto','dimensiones','peso')
