# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect
from .models import Cliente
from .forms import ClienteForm


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/listar_clientes.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        busca = self.request.GET.get('q')
        if busca:
            return Cliente.objects.filter(
                Q(nome__icontains=busca) | Q(email__icontains=busca)
            )
        return Cliente.objects.all()

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/form_cliente.html'
    success_url = reverse_lazy('listar_clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/form_cliente.html'
    success_url = reverse_lazy('listar_clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/confirmar_exclusao.html'
    success_url = reverse_lazy('listar_clientes')

