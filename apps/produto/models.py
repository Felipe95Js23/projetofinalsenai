from django.db import models
from apps.estoque.models import *


# Create your models here.
class Product(models.Model):
    nome= models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade = models.BigIntegerField()
    estoque = models.OneToOneField(Estoque, on_delete= models.CASCADE)
    

    def __str__(self):
        return self.nome