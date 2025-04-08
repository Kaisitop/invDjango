from django.db import models
from provec.models.venta import Venta

class Pago(models.Model):
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=[
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
    ])
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pago de {self.monto} para venta {self.venta.id}'