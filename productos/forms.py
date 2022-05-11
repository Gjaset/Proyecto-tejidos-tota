from django import forms

from productos.models import Color, Talla, Marca, Color, Producto


class TallaForm(forms.ModelForm):
    class Meta:
        model = Talla
        fields= ['tipo_talla', 'nombre']

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields= ['nombre']

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields= ['nombre']
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields= ['rol','categoria', 'nombre','precio', 'cantidad','color','talla','marca'] 
        

