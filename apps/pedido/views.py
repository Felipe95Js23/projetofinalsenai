from django.shortcuts import render
from .models import *
# Create your views here.
def PedidoView(request):
    Carrinhos = Pedido.objects.all()
    return render (request, '', {'pedidos':Carrinhos})