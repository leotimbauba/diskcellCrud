from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Produto
from .forms import ProdutoForm
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q, Sum, Avg # 👈 ESTA LINHA É ESSENCIAL


class DashboardView(TemplateView):
    template_name = 'produtos/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produtos = Produto.objects.all()
        context['total_produtos'] = produtos.count()
        context['estoque_total'] = produtos.aggregate(Sum('estoque'))['estoque__sum'] or 0
        context['valor_total'] = produtos.aggregate(Sum('preco'))['preco__sum'] or 0
        context['media_preco'] = produtos.aggregate(Avg('preco'))['preco__avg'] or 0

        # Gráfico
        context['nomes_produtos'] = [produto.nome for produto in produtos]
        context['valores_estoque'] = [produto.estoque for produto in produtos]

        # Últimos produtos
        context['ultimos_produtos'] = produtos.order_by('-criado_em')[:5]

        return context

def produtos_json(request):
    produtos = Produto.objects.all().order_by('id')
    data = serializers.serialize('json', produtos)
    return JsonResponse(data, safe=False)



class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/lista.html'
    context_object_name = 'produtos'
    def get_queryset(self):
        busca = self.request.GET.get('q')
        if busca:
            return Produto.objects.filter(Q(nome__icontains=busca))
        return Produto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

class ProdutoCreateView(SuccessMessageMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/formulario.html'
    success_url = reverse_lazy('produto_listar')
    success_message = 'Produto criado com sucesso!'

class ProdutoUpdateView(SuccessMessageMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/formulario.html'
    success_url = reverse_lazy('produto_listar')
    success_message = 'Produto atualizado com sucesso!'

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/confirmar_exclusao.html'
    success_url = reverse_lazy('produto_listar')
