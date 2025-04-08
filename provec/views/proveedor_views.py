from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from provec.models.proveedor import Proveedor
from provec.forms.proveedor_form import ProveedorForm


def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/listar.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor Registrado con exito')
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedor/form.html',{'form': form})

def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado con exito')
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedor/form.html', {'form': form})

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    messages.success(request, 'Proveedor eliminado')
    return redirect('listar_proveedores')