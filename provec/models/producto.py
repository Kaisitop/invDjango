from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField(default=0)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    codigo_barra = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nombre

