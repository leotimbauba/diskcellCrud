from django.urls import path
from .views import *

urlpatterns = [
    # Marca
    path('marca/', MarcaListView.as_view(), name='marca_list'),
    path('marca/novo/', MarcaCreateView.as_view(), name='marca_create'),
    path('marca/editar/<int:pk>/', MarcaUpdateView.as_view(), name='marca_update'),
    path('marca/excluir/<int:pk>/', MarcaDeleteView.as_view(), name='marca_delete'),

    # Modelo
    path('modelo/', ModeloListView.as_view(), name='modelo_list'),
    path('modelo/novo/', ModeloCreateView.as_view(), name='modelo_create'),
    path('modelo/editar/<int:pk>/', ModeloUpdateView.as_view(), name='modelo_update'),
    path('modelo/excluir/<int:pk>/', ModeloDeleteView.as_view(), name='modelo_delete'),
]
