from django.db import models

# Create your models here.
class Estoque(models.Model):
    nomeProduto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    codigo = models.IntegerField()

    def __str__(self):
        return self.nomeProduto