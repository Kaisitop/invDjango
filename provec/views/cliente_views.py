from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from provec.models.cliente import Cliente
from provec.forms.cliente_form import ClienteForm


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente creado con exito")
            return redirect('listar_clientes')
        else:
            messages.error(request, 'Hubo un error al crear al cliente')
            for fields, errors in form.errors.items():
                for error in errors:
                    print(f"error en {fields}: {error}")
    else:
        form = ClienteForm()
    return render(request, 'clientes/form.html', {'form': form})


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente editado exitosamente')
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request,'clientes/form.html', {'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, 'Cliente eliminado con exito')
    return redirect('listar_clientes')

       
