from django.db import models
from django.utils.translation import gettext_lazy as _

class Talla(models.Model):
    class Tipo_talla(models.TextChoices):
        Numero='Numero', _('Numero')
        Letra='Letra', _('Letra')
    tipo_talla= models.CharField(max_length=8, choices=Tipo_talla.choices, verbose_name="Tipo talla")
    nombre=models.CharField(max_length=10, verbose_name="nombre")
    def __str__(self) -> str:
        return "%s"% (self.nombre)
    def clean(self):
        self.Tipo_talla= self.nombre.capitalize()

class Marca(models.Model):
    nombre=models.CharField(max_length=20, verbose_name="Nombre")
    def __str__(self) -> str:
        return '%s' % (self.nombre)
    def clean(self):
        self.nombre= self.nombre.capitalize()

class Color(models.Model):
    nombre=models.CharField(max_length=20, verbose_name="Nombre")
    def __str__(self) -> str:
        return '%s' % (self.nombre)
    def clean(self):
        self.nombre= self.nombre.capitalize()


class Producto(models.Model):
    class Rol(models.TextChoices):
        ASOCIADA='Asociada',_('Asociada')
        PROVEEDOR='Proveedor',_('Proveedor')   
    rol=models.CharField(max_length=10, choices=Rol.choices, verbose_name="rol")
    
    class Categoria(models.TextChoices):
        TEJIDOS='Tejidos',_('Tejidos')
        ROPA='Ropa',_('Ropa')   
        CALZADO='Calzado',_('Calzado')  
    categoria=models.CharField(max_length=10, choices=Categoria.choices, verbose_name="categoria")
    nombre=models.CharField(max_length=50, verbose_name="Nombre ")
    cantidad=models.IntegerField(verbose_name="Cantidad")
    precio= models.IntegerField(verbose_name="Precio")
    
    talla= models.ForeignKey(Talla, on_delete=models.SET_NULL, null=True, verbose_name=u"Talla")
    marca= models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, verbose_name=u"Marca")
    color= models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name=u"Color")
    def __str__(self)-> str:
        return '%s'%(self.nombre)
    def clean(self):
        self.nombre= self.nombre.title()

       

