# provec/signals/compra_signals.py

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from provec.models.compra import Compra
from provec.models.detallecompra import DetalleCompra

@receiver(pre_save, sender=DetalleCompra)
def calcular_subtotal(sender, instance, **kwargs):
    """
    Calcula el subtotal de un detalle de compra antes de guardarlo.
    """
    instance.subtotal = instance.cantidad * instance.precio_unitario

@receiver(post_save, sender=DetalleCompra)
def actualizar_total_y_stock_al_guardar(sender, instance, created, **kwargs):
    """
    Actualiza el total de la compra y el stock del producto cuando se guarda un detalle de compra.
    """
    # Actualizar el total de la compra
    compra = instance.compra
    total = compra.detalles.aggregate(total=Sum('subtotal'))['total'] or 0
    Compra.objects.filter(id=compra.id).update(total=total)
    
    # Actualizar el stock del producto
    if not created:  # Si estamos actualizando un detalle existente
        try:
            old_instance = DetalleCompra.objects.get(id=instance.id)
            diferencia_cantidad = instance.cantidad - old_instance.cantidad
            
            if diferencia_cantidad != 0:
                producto = instance.producto
                producto.stock += diferencia_cantidad
                producto.save()
        except DetalleCompra.DoesNotExist:
            pass
    else:  # Si es un nuevo detalle
        producto = instance.producto
        producto.stock += instance.cantidad
        producto.save()

@receiver(post_delete, sender=DetalleCompra)
def actualizar_total_y_stock_al_eliminar(sender, instance, **kwargs):
    """
    Actualiza el total de la compra y el stock del producto cuando se elimina un detalle de compra.
    """
    # Actualizar el total de la compra
    compra = instance.compra
    total = compra.detalles.aggregate(total=Sum('subtotal'))['total'] or 0
    Compra.objects.filter(id=compra.id).update(total=total)
    
    # Actualizar el stock
    producto = instance.producto
    producto.stock -= instance.cantidad
    producto.save()