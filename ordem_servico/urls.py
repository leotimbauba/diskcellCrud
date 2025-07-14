from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_os, name='lista_os'),
    path('nova/', views.nova_os, name='nova_os'),
    path('editar/<int:pk>/', views.editar_os, name='editar_os'),
    path('excluir/<int:pk>/', views.excluir_os, name='excluir_os'),
]
