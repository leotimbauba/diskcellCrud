from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'endereco', 'data_criacao')
    search_fields = ('nome', 'email')
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)
    