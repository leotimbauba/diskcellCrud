from django.urls import path
from .views import produtos_json
from .views import DashboardView, ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('produtos/', ProdutoListView.as_view(), name='produto_listar'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto_criar'),
    path('produtos/editar/<int:pk>/', ProdutoUpdateView.as_view(), name='produto_editar'),
    path('produtos/excluir/<int:pk>/', ProdutoDeleteView.as_view(), name='produto_excluir'),
]
