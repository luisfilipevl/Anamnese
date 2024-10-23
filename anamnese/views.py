from django.shortcuts import render, redirect
from datetime import date
from .forms import * 

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

def login (request):
    return render (request, 'anamnese/login.html')

def cadastross (request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('index')
            
    else:
        form = CadastroForm()
    return render(request,'anamnese/cadastro.html', {'form': form})


