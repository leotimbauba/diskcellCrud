from django import forms
from .models import OrdemServico

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['cliente', 'produto', 'problema', 'valor', 'status']
