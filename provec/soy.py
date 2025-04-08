from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from provec.models.detalleventa import DetalleVenta

@receiver([post_save, post_delete], sender=DetalleVenta)
def actualizar_total_venta(sender, instance, **kwargs):
    venta = instance.venta
    detalles = venta.detalle.all()
    venta.total = sum(detalle.subtotal for detalle in detalles)
    venta.save()