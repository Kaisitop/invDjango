"""
URL configuration for pharmacy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from provec.views import home, producto_views, cliente_views, venta_views, pago_views, compras_views, proveedor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.inicio, name="home"),
    path('productos/', producto_views.listar_productos, name="listar_productos"),
    path('crear_producto/', producto_views.crear_producto, name="crear_producto"),
    path('editar_producto/<int:id>/',
         producto_views.editar_producto, name="editar_producto"),
    path('eliminar_producto/<int:id>/',
         producto_views.eliminar_producto, name="eliminar_producto"),
    path('clientes/', cliente_views.listar_clientes, name="listar_clientes"),
    path('crear_cliente/', cliente_views.crear_cliente, name="crear_cliente"),
    path('editar_cliente/<int:id>/',
         cliente_views.editar_cliente, name="editar_cliente"),
    path('eliminar_cliente/<int:id>/',
         cliente_views.eliminar_cliente, name="eliminar_cliente"),
    path('ventas/', venta_views.listar_venta, name="listar_ventas"),
    path('crear_venta/', venta_views.crear_venta, name="crear_venta"),
    path('editar_venta/<int:id>/', venta_views.editar_venta, name="editar_venta"),
    path('eliminar_venta/<int:id>/',
         venta_views.eliminar_venta, name="eliminar_venta"),
    path('detalle_venta/<int:id>/',
         venta_views.detalle_venta, name="detalle_venta"),
    path('ventas/<int:id>/pago/', pago_views.registrar_pago, name='registrar_pago'),
    path('compras/', compras_views.listar_compra, name="listar_compras"),
    path('crear_compra/', compras_views.crear_compra, name="crear_compra"),
     path('detalle_compra/<int:id>/',
         compras_views.detalle_compra, name="detalle_compra"),
    path('editar_compra/<int:id>/',
         compras_views.editar_compra, name="editar_compra"),
    path('eliminar_compra/<int:id>/',
         compras_views.eliminar_compra, name="eliminar_compra"),
    path('proveedores/', proveedor_views.listar_proveedores,
         name="listar_proveedores"),
    path('crear_proveedor/', proveedor_views.crear_proveedor, name="crear_proveedor"),
    path('editar_proveedor/<int:id>/',
         proveedor_views.editar_proveedor, name="editar_proveedor"),
    path('eliminar_proveedor/<int:id>/',
         proveedor_views.eliminar_proveedor, name="eliminar_proveedor"),

]
