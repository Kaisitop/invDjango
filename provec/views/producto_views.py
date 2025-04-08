from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from provec.models.producto import Producto
from provec.forms.producto_form import ProductoForm


def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar.html', {'productos': productos})


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado exitosamente.")
            return redirect('listar_productos')
        else:
            messages.error(request, "Hubo un error al crear el producto.")
            for field, errors in form.errors.items():
                for error in errors:
                    # Muestra el error en la consola
                    print(f"Error en {field}: {error}")
    else:
        form = ProductoForm()

    return render(request, 'productos/form.html', {'form': form})


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid:
            form.save()
            messages.success(request, "Producto actualizado correctamente")
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/form.html', {'form': form})


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado exitosamente")
    return redirect('listar_productos')
