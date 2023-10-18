from django.shortcuts import render
from .models import *
# Create your views here.

def CadastroView(request):
    lista = DadosPessoais.objects.all()
    return render (request, '', {'cadastre-se':lista})