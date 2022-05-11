from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import  Usuario
from productos.models import Producto

class Factura(models.Model):
    fecha=models.DateField(verbose_name="Fecha de factura", help_text=u"MM/DD/AAAA")
    class Tipousuario(models.TextChoices):
        Asociada='Asociada', _('Asociada')
        Proveedor='Proveedor', _('Proveedor')
    tipousuario= models.CharField(max_length=10, choices=Tipousuario.choices, verbose_name="Tipo de usuario")
    usuario=models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True,verbose_name="Nombre")
    producto=models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True,verbose_name="Producto")
    cantidad=models.IntegerField()
    class Tipofactura(models.TextChoices):
        Compra='Compra', _('Compra')
        Venta='Venta', _('Venta')
    tipofactura= models.CharField(max_length=10, choices=Tipofactura.choices, verbose_name="Tipo de factura")
# Create your models here.