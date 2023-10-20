from django.shortcuts import render
from .models import *

# Create your views here.
def VendasView(request):
    lista_vendas = Compra.objects.all()
    return render (request, '', {'vendas': lista_vendas})