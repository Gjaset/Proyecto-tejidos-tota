from tkinter import Widget
from django import forms
from facturas.models import Factura

class FacturaForm(forms.ModelForm):
    class Meta: 
        model = Factura
        fields = ['fecha', 'tipousuario', 'usuario', 'producto', 'cantidad', 'tipofactura']
        widgets = {
            'fecha':forms.DateInput(format=('%m/%d/%Y'), 
                                    attrs={'class':'form-control',
                                    'placeholder':'Seleccione una fecha',
                                    'type':'date'})
        }       
