from django import forms
from usuarios.models import  Usuario




class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['codigo', 'rol','nombre','apellido','tipo_documento','documento','celular']
        