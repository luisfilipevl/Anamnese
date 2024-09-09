from django.shortcuts import render
from datetime import date
from .models import *

def index(request):
    return render(request, 'anamnese/index.html')

def dadospessoais (request):
    return render(request, 'anamnese/dadospessoais.html')

def historicodoenças (request):
    return render(request, 'anamnese/historicodoença.html')

def historicofamiliar (request):
    return render (request, 'anamnese/historicoFamiliar.html')

def sintomas (request):
    return render (request, 'anamnese/sintomasqueixas.html')

def fficha (request):
    return render (request, 'anamnese/ficha.html')

def examess (request):
    return render (request, 'anamnese/exames.html')

def cadastross (request):
    return render (request,'anamnese/cadastro.html' )


