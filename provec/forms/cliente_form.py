from django import forms
from provec.models.cliente import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "identificacion", "telefono", "email"]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 focus:outline-none transition-colors duration-200',
                'placeholder': 'Ingrese el nombre completo',
                'required': True
            }),
            'identificacion': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 focus:outline-none transition-colors duration-200',
                'placeholder': 'Ingrese la identificación',
                'required': True
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 focus:outline-none transition-colors duration-200',
                'placeholder': 'Ej: +56 9 1234 5678',
                'pattern': '[\+]?[\d\s-]{8,}',
                'title': 'Ingrese un número de teléfono válido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 focus:outline-none transition-colors duration-200',
                'placeholder': 'ejemplo@correo.com'
            })
        }
