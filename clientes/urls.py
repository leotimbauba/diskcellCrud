from django.urls import path
from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView
)

urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='listar_clientes'),
    path('clientes/novo/', ClienteCreateView.as_view(), name='criar_cliente'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='editar_cliente'),
    path('clientes/<int:pk>/excluir/', ClienteDeleteView.as_view(), name='excluir_cliente'),
]
