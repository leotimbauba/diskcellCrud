from django.contrib import admin
from .models import OrdemServico

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'marca', 'modelo', 'produto', 'status', 'valor', 'criado_em')
    list_filter = ('status', 'marca', 'modelo')
    search_fields = ('cliente__nome', 'modelo__nome', 'marca__nome')
