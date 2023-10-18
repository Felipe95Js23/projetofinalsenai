from django.shortcuts import render
from .models import *

# Create your views here.
def ProdutoView(request):
    Lista_Produtos = Product.objects.all()
    return render (request, '', {'produtos':Lista_Produtos})