from django import forms
from tienda.models import Producto, Categoria, Etiqueta, DetalleProducto
from django.core.exceptions import ValidationError

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise ValidationError('El precio debe ser un número positivo mayor que cero.')
        return precio

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre.strip()) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre.strip()


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = '__all__'


class DetalleProductoForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = '__all__'
