from django import forms
from provec.models.compra import Compra
from provec.models.detallecompra import DetalleCompra


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        exclude =['fecha_compra', 'total']

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad', 'precio_unitario']

DetalleCompraFormSet = forms.inlineformset_factory(
    Compra, DetalleCompra, form=DetalleCompraForm, extra=1, can_delete=True
)