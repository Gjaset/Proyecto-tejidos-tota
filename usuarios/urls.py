from django.urls import path
from usuarios.views import cusuario, tusuario,Editarusuario, vusuario
urlpatterns = [
    path('crearusuario/', cusuario, name='usuario-crearUsuario'),
    path('tablausuario/', tusuario, name='usuario-tablaUsuario'),
    path('verusuario/<int:pk>', vusuario, name='usuario-verusuario'),
    path('editarusuario/<int:pk>', Editarusuario, name='usuario-editarusuario'),
]