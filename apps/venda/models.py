from django.db import models
from apps.carrinho.models import *

# Create your models here.
class Compra(models.Model):
    forma_pagamento = [
        ('boleto', 'boleto'),
        ('cartao', 'cartao'),
        ('pix', 'pix'),

    ]

    ValorCompra = models.DecimalField(decimal_places=2, max_digits=10)
    FormaPagamento = models.CharField(max_length=10, choices=forma_pagamento)
    pedido = models.ForeignKey(Pedido, on_delete= models.CASCADE)


    def __str__(self):
        return f'{self.ValorCompra}'

