from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from gestion.views import index, inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('inicio/',inicio, name="inicio"),
    path('factura/', include('facturas.urls')),
    path('usuario/', include ('usuarios.urls')),
    path('producto/', include('productos.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='usuario-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='usuario-logout'),
]
