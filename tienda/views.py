# tienda/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Etiqueta
from .forms import ProductoForm, CategoriaForm, EtiquetaForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def registro(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse_lazy('login'))
    return render(request, 'registration/registro.html', {'form': form})

def index(request):
    return render(request, "index.html")

def lista_productos(request):
    nombre = request.GET.get('nombre','')
    categoria_id = request.GET.get('categoria','')

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    if nombre:
        productos = productos.filter(nombre__icontains=nombre)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    return render(request, 'tienda/productos/lista.html', {
        'productos': productos,
        'categorias': categorias,
        'nombre': nombre,
        'categoria_seleccionada': categoria_id
    })

@login_required
@permission_required('tienda.add_producto', raise_exception=True)
def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tienda:lista_productos')
    return render(request, 'tienda/productos/crear.html', {'form': form})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'tienda/productos/detalle.html', {'producto': producto})

@login_required
@permission_required('tienda.change_producto', raise_exception=True)
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('tienda:lista_productos')
    return render(request, 'tienda/productos/editar.html', {'form': form})

@login_required
@permission_required('tienda.delete_producto', raise_exception=True)
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('tienda:lista_productos')
    return render(request, 'tienda/productos/eliminar.html', {'producto': producto})


# Categorías
@login_required
@permission_required('tienda.view_categoria', raise_exception=True)
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'tienda/categorias/lista.html', {'categorias': categorias})

@login_required
@permission_required('tienda.add_categoria', raise_exception=True)
def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tienda:lista_categorias')
    return render(request, 'tienda/categorias/formulario.html', {'form': form})

@login_required
@permission_required('tienda.change_categoria', raise_exception=True)
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('tienda:lista_categorias')
    return render(request, 'tienda/categorias/formulario.html', {'form': form})

@login_required
@permission_required('tienda.delete_categoria', raise_exception=True)
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('tienda:lista_categorias')
    return render(request, 'tienda/categorias/eliminar.html', {'categoria': categoria})


# Etiquetas (similar)
@login_required
@permission_required('tienda.view_etiqueta', raise_exception=True)
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'tienda/etiquetas/lista.html', {'etiquetas': etiquetas})

@login_required
@permission_required('tienda.add_etiqueta', raise_exception=True)
def crear_etiqueta(request):
    form = EtiquetaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tienda:lista_etiquetas')
    return render(request, 'tienda/etiquetas/formulario.html', {'form': form})

@login_required
@permission_required('tienda.change_etiqueta', raise_exception=True)
def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    form = EtiquetaForm(request.POST or None, instance=etiqueta)
    if form.is_valid():
        form.save()
        return redirect('tienda:lista_etiquetas')
    return render(request, 'tienda/etiquetas/formulario.html', {'form': form})

@login_required
@permission_required('tienda.delete_etiqueta', raise_exception=True)
def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('tienda:lista_etiquetas')
    return render(request, 'tienda/etiquetas/eliminar.html', {'etiqueta': etiqueta})
