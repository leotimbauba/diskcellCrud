# cliente/forms.py
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'id': 'telefone', 'placeholder': '(xx) xxxxx-xxxx'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        