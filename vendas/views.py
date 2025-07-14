from django.shortcuts import render, redirect, get_object_or_404
from .models import Venda
from .forms import VendaForm
from django.core.paginator import Paginator

def lista_vendas(request):
    vendas = Venda.objects.all().order_by('-data')
    paginator = Paginator(vendas, 10)  # 10 por página
    page = request.GET.get('page')
    vendas = paginator.get_page(page)
    return render(request, 'vendas/lista.html', {'vendas': vendas})

def nova_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vendas')
    else:
        form = VendaForm()
    return render(request, 'vendas/form.html', {'form': form})

def editar_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('lista_vendas')
    else:
        form = VendaForm(instance=venda)
    return render(request, 'vendas/form.html', {'form': form})

def excluir_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        venda.delete()
        return redirect('lista_vendas')
    return render(request, 'vendas/confirmar_exclusao.html', {'venda': venda})
