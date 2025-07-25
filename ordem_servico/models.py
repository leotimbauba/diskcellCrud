from django.db import models
from clientes.models import Cliente
from produtos.models import Produto
from app_marca.models import Marca, Modelo

class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
     # Novos campos
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, blank=True)
    
    problema = models.TextField('Problema relatado')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='aberto')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OS #{self.pk} - {self.cliente.nome}"
