# tienda/forms.py
from django import forms
from .models import Producto, Categoria, Etiqueta, DetalleProducto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','categoria','etiquetas','imagen']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']

class DetalleProductoForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = ['dimensiones','peso','producto']
