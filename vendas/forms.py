from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['produto', 'quantidade', 'valor_fornecedor', 'valor_final', 'forma_pagamento']
        widgets = {
            'forma_pagamento': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_fornecedor': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
        }
