from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from provec.models.venta import Venta
from provec.models.pagos import Pago
from provec.forms.pago_form import PagoForm

def registrar_pago(request, id):
    venta = get_object_or_404(Venta, id=id)

    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.venta = venta
            pago.save()
            messages.success(request, "Pago registrado con exito")
            return redirect('detalle_venta', id=id)
    else:
        form = PagoForm()
    return render(request, 'pago/form.html',{'form': form, 'venta': venta})