from django.shortcuts import render
from .models import *
# Create your views here.
def PedidoView(request):
    Pedidos = Carrinho.objects.all()
    return render (request, '', {'pedidos':Pedidos})