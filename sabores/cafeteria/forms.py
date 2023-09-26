from django import forms
from .models import Usuario

class UsuarioForms(forms.ModelForms):
    class Meta:
        model = Usuario
        fields = ['pedido', 'nome', 'email', 'celular', 'endereco', 'combo']