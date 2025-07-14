from django.contrib import admin
from .models import Venda

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'forma_pagamento', 'valor_final', 'valor_fornecedor', 'lucro', 'data')
    search_fields = ('produto__nome',)
    list_filter = ('forma_pagamento', 'data')
