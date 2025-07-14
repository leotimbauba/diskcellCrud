from django.contrib import admin
from .models import OrdemServico

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'produto', 'valor', 'status', 'criado_em')
    search_fields = ('cliente', 'produto')
    list_filter = ('status',)
