# provec/signals/venta_signals.py
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from provec.models.venta import Venta
from provec.models.detalleventa import DetalleVenta

@receiver(pre_save, sender=DetalleVenta)
def calcular_subtotal_venta(sender, instance, **kwargs):
    """
    Calcula el subtotal de un detalle de venta antes de guardarlo.
    """
    instance.subtotal = instance.cantidad * instance.precio_unitario

@receiver(post_save, sender=DetalleVenta)
def actualizar_total_y_stock_al_guardar_venta(sender, instance, created, **kwargs):
    """
    Actualiza el total de la venta y el stock del producto cuando se guarda un detalle de venta.
    """
    # Actualizar el total de la venta
    venta = instance.venta
    total = venta.detalle.aggregate(total=Sum('subtotal'))['total'] or 0
    Venta.objects.filter(id=venta.id).update(total=total)
    
    # Actualizar el stock del producto (reducir stock en ventas)
    if not created:  # Si estamos actualizando un detalle existente
        try:
            old_instance = DetalleVenta.objects.get(id=instance.id)
            diferencia_cantidad = instance.cantidad - old_instance.cantidad
            
            if diferencia_cantidad != 0:
                producto = instance.producto
                # En ventas, aumentar cantidad reduce el stock
                producto.stock -= diferencia_cantidad
                producto.save()
        except DetalleVenta.DoesNotExist:
            pass
    else:  # Si es un nuevo detalle
        producto = instance.producto
        # Reducir stock al vender
        producto.stock -= instance.cantidad
        producto.save()

@receiver(post_delete, sender=DetalleVenta)
def actualizar_total_y_stock_al_eliminar_venta(sender, instance, **kwargs):
    """
    Actualiza el total de la venta y el stock del producto cuando se elimina un detalle de venta.
    """
    # Actualizar el total de la venta
    venta = instance.venta
    total = venta.detalle.aggregate(total=Sum('subtotal'))['total'] or 0
    Venta.objects.filter(id=venta.id).update(total=total)
    
    # Actualizar el stock (devolver al inventario)
    producto = instance.producto
    producto.stock += instance.cantidad  # Aumentamos stock al eliminar un detalle de venta
    producto.save()