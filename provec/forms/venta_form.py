from django import forms
from django.core.exceptions import ValidationError
from provec.models.venta import Venta
from provec.models.detalleventa import DetalleVenta
from provec.models.producto import Producto

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'})
        }

class VentaDetalleForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'})
        }

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')

        if producto and cantidad:
            # Verificar que hay suficiente stock
            if cantidad > producto.stock:
                raise ValidationError(f"No hay suficiente stock. Disponible: {producto.stock}")
            
            # Verificar que la cantidad es positiva
            if cantidad <= 0:
                raise ValidationError("La cantidad debe ser mayor que cero")

        return cleaned_data

VentaDetalleFormSet = forms.inlineformset_factory(
    Venta, 
    DetalleVenta, 
    form=VentaDetalleForm, 
    extra=1,  # Número de formularios vacíos
    can_delete=True,  # Permitir eliminar detalles
    min_num=1,  # Mínimo número de formularios
    validate_min=True  # Validar el mínimo número de formularios
)