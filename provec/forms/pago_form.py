from django import forms
from provec.models.pagos import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['monto', 'metodo_pago']
        widgets = {
            'monto': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 focus:outline-none transition-colors duration-200',
                'min': '0',
                'step': '0.01',
                'required': True,
                'placeholder': '0.00'
            }),
            'metodo_pago': forms.Select(attrs={
                'class': 'w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 focus:outline-none transition-colors duration-200',
                'required': True
            })
        }
        labels = {
            'monto': 'Monto a Pagar',
            'metodo_pago': 'Método de Pago'
        }