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


def in_cadastro(request):
    novo_cadastro = Cadastro()
    novo_cadastro.nome_usuario = request.POST.get('Nome_user')
    novo_cadastro.email = request.POST.get('email')
    novo_cadastro.CPF = request.POST.get('CPF')
    novo_cadastro.senha = request.POST.get('senha')
    novo_cadastro.save()

    # Pegando o ID do cadastro recém-criado
    id_do_cadastro = novo_cadastro.id

    # Buscando a instância de Ficha correspondente ao ID do cadastro
    ficha = Ficha.objects.get(id=id_do_cadastro)

    # Atribuindo a instância de Ficha ao campo ficha
    novo_cadastro.ficha = ficha
    novo_cadastro.save()

    usuarios = {
        'usuarios': Cadastro.objects.all()
    }
    return render(request,'anamnese/test.html', usuarios)