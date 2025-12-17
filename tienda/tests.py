from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Producto, Categoria, Etiqueta

class ProductoModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Lentes')
        self.producto = Producto.objects.create(
            nombre='Lentes de sol',
            descripcion='Lentes oscuros',
            precio=100.00,
            categoria=self.categoria
        )

    def test_producto_str(self):
        self.assertEqual(str(self.producto), 'Lentes de sol')

    def test_precio_positivo(self):
        self.assertGreater(self.producto.precio, 0)

class ProductoViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.categoria = Categoria.objects.create(nombre='Lentes')
        self.producto = Producto.objects.create(
            nombre='Lentes de sol',
            descripcion='Lentes oscuros',
            precio=100.00,
            categoria=self.categoria
        )

    def test_lista_productos_view(self):
        response = self.client.get(reverse('lista_productos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lentes de sol')

    def test_crear_producto_view_requires_login(self):
        response = self.client.get(reverse('crear_producto'))
        self.assertRedirects(response, '/login/?next=/productos/crear/')

    def test_crear_producto_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('crear_producto'), {
            'nombre': 'Nuevo producto',
            'descripcion': 'Descripción',
            'precio': 50.00,
            'categoria': self.categoria.id
        })
        self.assertRedirects(response, reverse('lista_productos'))
        self.assertEqual(Producto.objects.count(), 2)
