# tienda/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    imagen = models.ImageField(
        upload_to="productos/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre

class DetalleProducto(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='detalle')
    dimensiones = models.CharField(max_length=100, blank=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"