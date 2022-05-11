
from django.urls import path
from productos.views import talla, marca, color, productoT, producto, Verproducto, Editarproducto, Editartalla, Editarmarca

urlpatterns = [
    path('talla/', talla, name='producto-talla'),
    path('marca/', marca, name='producto-marca'),
    path('color/', color, name='producto-color'),
    path('producto/', productoT, name='producto-producto'),
    path('crearproducto/', producto, name='producto-crearproducto'),
    path('verproducto/<int:pk>', Verproducto, name='producto-verproducto'),
    path('editarproducto/<int:pk>', Editarproducto, name='producto-editarproducto'),
    path('editartalla/<int:pk>', Editartalla, name='producto-editartalla'),
    path('editarmarca/<int:pk>', Editarmarca, name='producto-editarmarca'),
]