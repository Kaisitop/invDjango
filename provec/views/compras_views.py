from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from provec.models.compra import Compra
from provec.models.detallecompra import DetalleCompra
from provec.forms.compra_form import CompraForm, DetalleCompraFormSet
from provec.models.producto import Producto


def listar_compra(request):
    compras = Compra.objects.all()
    return render(request, 'compras/listar.html', {'compras': compras})


def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        formset = DetalleCompraFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            # Guardamos la compra
            compra = form.save()

            # Guardamos los detalles
            for detalle_form in formset:
                if detalle_form.cleaned_data:
                    detalle = detalle_form.save(commit=False)
                    detalle.compra = compra
                    detalle.save()

            # Las señales ya se encargaron de calcular subtotales y actualizar el total

            messages.success(request, 'Compra registrada con éxito')
            return redirect('listar_compras')

    else:
        form = CompraForm()
        formset = DetalleCompraFormSet()

    return render(request, 'compras/form.html', {'form': form, 'formset': formset})


def editar_compra(request, id):
    compra = get_object_or_404(Compra, id=id)

    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        formset = DetalleCompraFormSet(request.POST, instance=compra)

        try:
            if form.is_valid() and formset.is_valid():
                # Guardamos la compra
                compra = form.save()

                # Guardamos los detalles
                formset.save()

                # Las señales se encargan de actualizar subtotales y total automáticamente

                # Ajustamos el stock si es necesario
                for detalle_form in formset:
                    if detalle_form.cleaned_data:
                        if detalle_form.has_changed() and 'cantidad' in detalle_form.changed_data:
                            detalle = detalle_form.instance

                            # Si es un detalle existente, obtenemos la cantidad anterior
                            if detalle.id:
                                detalle_original = DetalleCompra.objects.get(
                                    id=detalle.id)
                                cantidad_anterior = detalle_original.cantidad

                                # Ajustar stock correctamente
                                diferencia_cantidad = detalle.cantidad - cantidad_anterior
                                detalle.producto.stock += diferencia_cantidad
                                detalle.producto.save()

                messages.success(request, 'Compra actualizada con éxito')
                return redirect('listar_compras')
            else:
                messages.error(
                    request, 'Por favor, corrige los errores en el formulario.')

        except Exception as e:
            messages.error(
                request, f'Ocurrió un error al actualizar la compra: {str(e)}')

    else:
        form = CompraForm(instance=compra)
        formset = DetalleCompraFormSet(instance=compra)

    return render(request, 'compras/form.html', {'form': form, 'formset': formset})


def eliminar_compra(request, id):
    compra = get_object_or_404(Compra, id=id)
    compra.delete()
    messages.success(request, 'Compra eliminada con éxito')
    return redirect('listar_compras')

def detalle_compra(request, id):
    compra = get_object_or_404(Compra, id=id)
    detalles = DetalleCompra.objects.filter(compra=compra)
    return render(request, 'compras/detalle.html',{'compra': compra,'detalles': detalles})