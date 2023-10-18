from django.shortcuts import render

# Create your views here.
from .models import *
# Create your tests here.
def EstoqueView(request):
    Produtos_estoque = Estoque.objects.all()
    return render (request,'', {'almoxarife': Produtos_estoque})