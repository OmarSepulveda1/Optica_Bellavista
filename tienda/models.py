from django.db import models

class ProductoManager(models.Manager):
    def filtrar_por_nombre_y_categoria(self, nombre=None, categoria_id=None):
        productos = self.all().order_by('id')  # Ordenar por id para consistencia en paginación
        if nombre:
            productos = productos.filter(nombre__icontains=nombre)
        if categoria_id:
            productos = productos.filter(categoria_id=categoria_id)
        return productos

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
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    objects = ProductoManager()

    def __str__(self):
        return self.nombre


class DetalleProducto(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    dimensiones = models.CharField(max_length=100)
    peso = models.CharField(max_length=50)

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"
