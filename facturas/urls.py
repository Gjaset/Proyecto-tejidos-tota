from django.urls import path
from facturas.views import factura, tfactura, vfactura
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('crearfactura/', factura, name='factura-factura'),
    path('factura/', tfactura, name='factura-tfactura'),
    path('verfactura/<int:pk>', vfactura, name='factura-verfactura'),
]

 