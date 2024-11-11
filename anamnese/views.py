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
    fichas = Ficha.objects.all()
    contexto = {
        'fichas':fichas
    }
    return render(request,'anamnese/ficha.html', contexto)

def examess (request):
    return render (request, 'anamnese/exames.html')




def login (request):
    return render (request, 'anamnese/login.html')



def cadastross(request):
    print("Acessou a view cadastross") 
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome_usuario = form.cleaned_data['nome_usuario']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            CPF = form.cleaned_data['CPF']
            
            cadastro = Cadastro.objects.create(
                nome_usuario=nome_usuario,
                email=email,
                senha=senha,
                CPF=CPF
            )

            Ficha.objects.create(usuario=cadastro)
    else:
        print("-entrou primeiro aqui")
        form = CadastroForm()
    
    return render(request,'modals/cadastro_modal.html', {'form': form})
