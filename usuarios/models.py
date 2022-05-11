from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Usuario(models.Model):

    class Codigo(models.TextChoices):
        C0='N/A',_('N/A')
        C1='1', _('1')
        C2='2', _('2')
        C3='3', _('3')
        C4='4', _('4')
        C5='5', _('5')
    codigo= models.CharField(max_length=3, choices=Codigo.choices, verbose_name="Codigo")
    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Proveedor='Proveedor', _('Proveedor')
        Asociada='Asociada', _('Asociada')
        Cliente='Cliente', _('Cliente')
    rol= models.CharField(max_length=13, choices=Rol.choices, verbose_name="rol")
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    apellido=models.CharField(max_length=50, verbose_name="Apellido")
    documento=models.CharField(unique=True,max_length=10)
    celular=models.CharField(unique=True,max_length=10)
    class Tipo_documento(models.TextChoices):
        Cedula_ciudadania='C.C', _('C.C')
        Tarjeta_identidad='T.I', _('T.I')
        Cedula_extranjeria='C.E', _('C.E')
    tipo_documento= models.CharField(max_length=3, choices=Tipo_documento.choices, verbose_name="Tipo documento")  
    def __str__(self) -> str:
        return "%s"% (self.nombre)
    def clean(self):
        self.nombre= self.nombre.title()
    
class Uadministrador(models.Model):
    class Codigo(models.TextChoices):
        C0='N/A',_('N/A')
        C1='1', _('1')
        C2='2', _('2')
        C3='3', _('3')
        C4='4', _('4')
        C5='5', _('5')
    codigo= models.CharField(max_length=3, choices=Codigo.choices, verbose_name="Codigo")
    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Proveedor='Proveedor', _('Proveedor')
        Asociada='Asociada', _('Asociada')
        Cliente='Cliente', _('Cliente')
    rol= models.CharField(max_length=13, choices=Rol.choices, verbose_name="rol")  
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    apellido=models.CharField(max_length=50, verbose_name="Apellido")
    documento=models.CharField(unique=True,max_length=10)
    celular=models.CharField(unique=True,max_length=10)
    class Tipo_documento(models.TextChoices):
        Cedula_ciudadania='C.C', _('C.C')
        Tarjeta_identidad='T.I', _('T.I')
        Cedula_extranjeria='C.E', _('C.E')
    tipo_documento= models.CharField(max_length=3, choices=Tipo_documento.choices, verbose_name="Tipo documento")
    
    def __str__(self) -> str:
        return "%s"% (self.nombre, self.apellido)
    def clean(self):
        self.nombre= self.nombre.capitalize()
        self.apellido= self.apellido.capitalize()