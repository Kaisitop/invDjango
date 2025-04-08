from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.identificacion}"