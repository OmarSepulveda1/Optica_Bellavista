from django.contrib import admin
from .models import Producto, Categoria, Etiqueta, DetalleProducto

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Etiqueta)
admin.site.register(DetalleProducto)
