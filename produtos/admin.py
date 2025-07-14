from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome', 'descricao')
    ordering = ('-criado_em',)
