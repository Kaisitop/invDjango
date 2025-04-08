from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre  


