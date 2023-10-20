from django.db import models
from django.contrib.auth.models import User
from apps.venda.models import Compra

# Create your models here.

class DadosPessoais(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    Compra = models.ForeignKey(Compra, on_delete= models.CASCADE)
    


    def __str__(self):
        return f'{self.usuario}'