from django.db import models
from produtos.models import Produto  # Relacionado ao módulo de produtos

FORMA_PAGAMENTO = (
    ('dinheiro', 'Dinheiro'),
    ('pix', 'PIX'),
    ('cartao', 'Cartão'),
)

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_fornecedor = models.DecimalField(max_digits=10, decimal_places=2)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=10, choices=FORMA_PAGAMENTO)

    data = models.DateTimeField(auto_now_add=True)

    def lucro(self):
        return (self.valor_final - self.valor_fornecedor) * self.quantidade

    def total_venda(self):
        return self.valor_final * self.quantidade

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}x"
