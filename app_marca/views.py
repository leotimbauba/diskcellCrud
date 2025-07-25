from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Marca, Modelo
from .forms import MarcaForm, ModeloForm

# CRUD Marca
class MarcaListView(ListView):
    model = Marca
    template_name = 'app_marca/marca_list.html'

class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'app_marca/marca_form.html'
    success_url = reverse_lazy('marca_list')

class MarcaUpdateView(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'app_marca/marca_form.html'
    success_url = reverse_lazy('marca_list')

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'app_marca/marca_confirm_delete.html'
    success_url = reverse_lazy('marca_list')

# CRUD Modelo
class ModeloListView(ListView):
    model = Modelo
    template_name = 'app_marca/modelo_list.html'

class ModeloCreateView(CreateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'app_marca/modelo_form.html'
    success_url = reverse_lazy('modelo_list')

class ModeloUpdateView(UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'app_marca/modelo_form.html'
    success_url = reverse_lazy('modelo_list')

class ModeloDeleteView(DeleteView):
    model = Modelo
    template_name = 'app_marca/modelo_confirm_delete.html'
    success_url = reverse_lazy('modelo_list')
