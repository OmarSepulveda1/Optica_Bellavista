from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Etiqueta
from config.forms import ProductoForm, CategoriaForm, EtiquetaForm
from django.db.models import Avg
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})


def index(request):
    return render(request, 'index.html')

def lista_productos(request):
    nombre = request.GET.get('nombre')
    categoria_id = request.GET.get('categoria')
    page_number = request.GET.get('page')

    try:
        productos = Producto.objects.filtrar_por_nombre_y_categoria(nombre=nombre, categoria_id=categoria_id)
        categorias = Categoria.objects.all()

        paginator = Paginator(productos, 9)  # 9 productos por página
        page_obj = paginator.get_page(page_number)
    except Exception as e:
        messages.error(request, f'Error al cargar productos: {str(e)}')
        page_obj = None
        categorias = []

    return render(request, 'tienda/productos/lista.html', {
        'page_obj': page_obj,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id,
        'nombre': nombre
    })


# PRODUCTOS 
@login_required
def crear_producto(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Producto creado exitosamente.')
        return redirect('lista_productos')
    return render(request, 'tienda/productos/crear.html', {'form': form})


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'tienda/productos/detalle.html', {'producto': producto})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if form.is_valid():
        form.save()
        messages.success(request, 'Producto editado exitosamente.')
        return redirect('lista_productos')
    return render(request, 'tienda/productos/editar.html', {'form': form})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('lista_productos')
    return render(request, 'tienda/productos/eliminar.html', {'producto': producto})

# CATEGORÍAS
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'tienda/categorias/lista.html', {'categorias': categorias})


@user_passes_test(lambda u: u.is_staff)
def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_categorias')
    return render(request, 'tienda/categorias/formulario.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('lista_categorias')
    return render(request, 'tienda/categorias/formulario.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'tienda/categorias/eliminar.html', {'categoria': categoria})

# ETIQUETAS
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'tienda/etiquetas/lista.html', {'etiquetas': etiquetas})


@user_passes_test(lambda u: u.is_staff)
def crear_etiqueta(request):
    form = EtiquetaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_etiquetas')
    return render(request, 'tienda/etiquetas/formulario.html', {'form': form})


@login_required
def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    form = EtiquetaForm(request.POST or None, instance=etiqueta)
    if form.is_valid():
        form.save()
        return redirect('lista_etiquetas')
    return render(request, 'tienda/etiquetas/formulario.html', {'form': form})


@login_required
def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')
    return render(request, 'tienda/etiquetas/eliminar.html', {'etiqueta': etiqueta})
