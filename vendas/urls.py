from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_vendas, name='lista_vendas'),
    path('nova/', views.nova_venda, name='nova_venda'),
    path('editar/<int:pk>/', views.editar_venda, name='editar_venda'),
    path('excluir/<int:pk>/', views.excluir_venda, name='excluir_venda'),
]
