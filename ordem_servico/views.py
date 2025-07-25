from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import OrdemServico
from .forms import OrdemServicoForm

from django.shortcuts import render
from .models import OrdemServico


def lista_os(request):
    status_filter = request.GET.get('status')
    q = request.GET.get('q', '')
    
    os_list = OrdemServico.objects.all().order_by('-criado_em')
    
    if status_filter:
        os_list = OrdemServico.objects.filter(status=status_filter)
    if q:
        os_list = os_list.filter(cliente__nome__icontains=q)
    
    paginator = Paginator(os_list, 8)  # 10 OS por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ordem_servico/lista_os.html', {
        'page_obj': page_obj,
        'status_filter': status_filter,
        'q': q,
    })

def nova_os(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_os')
    else:
        form = OrdemServicoForm()
    return render(request, 'ordem_servico/nova_os.html', {'form': form})

def editar_os(request, pk):
    os = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST, instance=os)
        if form.is_valid():
            form.save()
            return redirect('lista_os')
    else:
        form = OrdemServicoForm(instance=os)
    return render(request, 'ordem_servico/editar_os.html', {'form': form, 'os': os})

def excluir_os(request, pk):
    os = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        os.delete()
        return redirect('lista_os')
    return render(request, 'ordem_servico/confirmar_exclusao.html', {'os': os})
