from django.db import models
from apps.produto.models import Product

# Create your models here.
class Carrinho(models.Model):
    adicionar_pedido = models.BooleanField(null=True, blank=True)
    produto = models.ForeignKey(Product, on_delete= models.CASCADE)


    def __str__(self):
        return f"{self.adicionar_pedido}"
    