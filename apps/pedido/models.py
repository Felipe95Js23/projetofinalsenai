from django.db import models
from apps.produto.models import Product

# Create your models here.
class Pedido(models.Model):
    carrinho = models.BooleanField(default=True)
    produto = models.ForeignKey(Product, on_delete= models.CASCADE)


    def __str__(self):
        return f"{self.carrinho}"
    