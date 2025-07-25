from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')),
    path('clientes/', include('clientes.urls')),
    path('vendas/', include('vendas.urls')),
    path('ordem_servico/', include('ordem_servico.urls')),
    path('app_marca/', include('app_marca.urls')),
]