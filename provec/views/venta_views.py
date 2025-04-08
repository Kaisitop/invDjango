from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from provec.forms.venta_form import VentaForm, VentaDetalleFormSet
from provec.models.venta import Venta
from provec.models.detalleventa import DetalleVenta


def listar_venta(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/listar.html', {'ventas': ventas})


def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        formset = VentaDetalleFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            try:
                # Guardamos la venta
                venta = form.save()

                # Guardamos los detalles
                for detalle_form in formset:
                    if detalle_form.cleaned_data:
                        detalle = detalle_form.save(commit=False)
                        detalle.venta = venta
                        # Asignamos el precio de venta del producto
                        detalle.precio_unitario = detalle.producto.precio_venta
                        detalle.save()  # Las señales se encargan del subtotal, total y stock

                messages.success(request, 'Venta registrada correctamente')
                return redirect('listar_ventas')
            except Exception as e:
                messages.error(
                    request, f'Error al registrar la venta: {str(e)}')
        else:
            messages.error(
                request, 'Por favor, corrige los errores en el formulario')
    else:
        form = VentaForm()
        formset = VentaDetalleFormSet()

    return render(request, 'ventas/form.html', {'form': form, 'formset': formset})


def editar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)

    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        formset = VentaDetalleFormSet(request.POST, instance=venta)

        if form.is_valid() and formset.is_valid():
            try:
                # Guardamos la venta
                form.save()

                # Guardamos los detalles - las señales manejan todo lo demás
                for form_detalle in formset:
                    if form_detalle.cleaned_data:
                        if form_detalle.instance.pk is None:  # Si es un nuevo detalle
                            detalle = form_detalle.save(commit=False)
                            detalle.precio_unitario = detalle.producto.precio_venta
                            detalle.save()
                        else:
                            form_detalle.save()  # Si es un detalle existente

                # Elimina los detalles marcados para eliminar
                formset.save()

                messages.success(request, 'Venta editada con éxito')
                return redirect('listar_ventas')
            except Exception as e:
                messages.error(request, f'Error al editar la venta: {str(e)}')
        else:
            messages.error(
                request, 'Por favor, corrige los errores en el formulario')
    else:
        form = VentaForm(instance=venta)
        formset = VentaDetalleFormSet(instance=venta)

    return render(request, 'ventas/form.html', {'form': form, 'formset': formset})


def eliminar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)

    try:
        # La eliminación de la venta causará la eliminación en cascada de sus detalles
        # Las señales se encargarán de actualizar el stock
        venta.delete()
        messages.success(request, 'Venta eliminada con éxito')
    except Exception as e:
        messages.error(request, f'Error al eliminar la venta: {str(e)}')

    return redirect('listar_ventas')


def detalle_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    detalles = DetalleVenta.objects.filter(venta=venta)
    return render(request, 'ventas/detalle.html', {'venta': venta, 'detalles': detalles})
