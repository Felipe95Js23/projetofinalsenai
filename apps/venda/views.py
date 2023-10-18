from django.shortcuts import render
from .models import *
# Create your views here.
def VendasView(request):
    lista_vendas = compra.objects.all()
    return render (request, '', {'vendas': lista_vendas})