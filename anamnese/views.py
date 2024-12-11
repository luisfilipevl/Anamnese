from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .forms import * 
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'anamnese/index.html')

@login_required
def index_usuario(request, cadastro_id):
    # Busque o objeto `Cadastro` correspondente, ou redirecione se não existir
    try:
        cadastro = Cadastro.objects.get(id=cadastro_id)
    except Cadastro.DoesNotExist:
        return redirect('home')  # Redireciona para a página inicial se o `cadastro_id` não existir

    # Renderiza uma página de boas-vindas ou redireciona para uma página inicial personalizada
    return render(request, 'anamnese/index_usuario.html', {'cadastro': cadastro})

@login_required
def dadospessoais(request, cadastro_id):
    ficha = get_object_or_404(Ficha, usuario__id=cadastro_id)  # Localiza a ficha pelo ID do usuário

    if request.method == 'POST':
        # Recupera os valores do formulário
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        sexo = request.POST.get('sexo')
        estado_civil = request.POST.get('estado_civil')
        profissao = request.POST.get('profissao')

        # Atualiza os campos no modelo
        ficha.nome = nome
        ficha.endereco = endereco
        ficha.usuario.email = email
        ficha.data_nascimento = data_nascimento
        ficha.sexo = sexo
        ficha.estado_civil = estado_civil
        ficha.profissao = profissao

        # Salva as mudanças no banco de dados
        ficha.usuario.save()  # Salva o cadastro (atualizando email, por exemplo)
        ficha.save()  # Salva os dados da ficha

        
    return render(request, 'anamnese/dadospessoais.html', {
        'ficha': ficha,
        'cadastro_id': cadastro_id
    })

@login_required
def historicodoenças(request, cadastro_id):
    ficha = get_object_or_404(Ficha, usuario__id=cadastro_id)  # Localizar a ficha pelo ID do usuário

    if request.method == 'POST':
        doencas_atual = request.POST.get('doencas_atual')
        
        ficha.doencas_atual = doencas_atual
        ficha.save()
        
        return redirect('historicodoenças', cadastro_id=cadastro_id)  # Redireciona após salvar

    return render(request, 'anamnese/historicodoença.html', {
        'ficha': ficha,
        'cadastro_id': cadastro_id
    })

@login_required
def historicofamiliar(request, cadastro_id):
    ficha = get_object_or_404(Ficha, usuario__id=cadastro_id)  # Localizar a ficha pelo ID do usuário

    if request.method == 'POST':
        doencas_familiares = request.POST.get('doencas_familiares')
        
        ficha.doencas_familiares = doencas_familiares
        ficha.save()
        
        return redirect('historicofamiliar', cadastro_id=cadastro_id)  # Redireciona após salvar

    return render(request, 'anamnese/historicoFamiliar.html', {
        'ficha': ficha,
        'cadastro_id': cadastro_id
    })

def sintomas (request):
    return render (request, 'anamnese/sintomasqueixas.html')

@login_required
def fficha(request, cadastro_id):
    ficha = Ficha.objects.get(id=cadastro_id)
    contexto = {
        'ficha': ficha,
        'cadastro_id': cadastro_id  # Inclui 'cadastro_id' no contexto
    }
    return render(request, 'anamnese/ficha.html', contexto)

def examess (request):
    return render (request, 'anamnese/exames.html')


def cadastross(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome_usuario = form.cleaned_data['nome_usuario']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            CPF = form.cleaned_data['CPF']
            
            # Verifica se já existe um cadastro com o mesmo nome de usuário, e-mail ou CPF
            if Cadastro.objects.filter(nome_usuario=nome_usuario).exists():
                messages.error(request, 'Nome de usuário já cadastrado.')
            elif Cadastro.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já cadastrado.')
            elif Cadastro.objects.filter(CPF=CPF).exists():
                messages.error(request, 'CPF já cadastrado.')
            else:
                try:
                    # Cria o cadastro e a ficha associada
                    cadastro = Cadastro.objects.create(
                        nome_usuario=nome_usuario,
                        email=email,
                        senha=senha,
                        CPF=CPF
                    )
                    Ficha.objects.create(usuario=cadastro)
                    messages.success(request, 'Cadastro realizado com sucesso!')
                    return redirect('index')  # Redireciona para a página inicial ou outra página
                except IntegrityError:
                    messages.error(request, 'Ocorreu um erro ao salvar os dados.')
        else:
            messages.error(request, 'Formulário inválido.')
    else:
        form = CadastroForm()

    return render(request, 'anamnese/index.html', {'form': form})

def login2(request):
    if request.method == "POST":
        # Obtém os dados enviados pelo formulário
        usuario = request.POST.get('nome_usuario')
        senha = request.POST.get('senha')

        # Autentica o usuário pelo modelo User do Django
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            login(request, user)

            # Tenta buscar o cadastro correspondente pelo nome do usuário
            try:
                cadastro = Cadastro.objects.get(nome_usuario=usuario)
                # Armazena o ID do cadastro na sessão
                request.session['cadastro_id'] = cadastro.id
                return redirect(f'/{cadastro.id}/')  # Redireciona para a página inicial do usuário
            except Cadastro.DoesNotExist:
                messages.error(request, "Cadastro não encontrado. Entre em contato com o suporte.")
                return redirect('login2')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return redirect('login2')
    else:
        # Renderiza a página de login em caso de requisição GET
        return render(request, 'home')
    
def logout_(request):
    logout(request)
    return redirect('home')

@login_required
def excluir_cadastro(request, cadastro_id):
    cadastro = get_object_or_404(Cadastro, id=cadastro_id)
    cadastro.delete()
    return redirect('home')

@login_required
def atualizar_cadastro(request, cadastro_id):
    cadastro = get_object_or_404(Cadastro, id=cadastro_id)
    user = cadastro.usuario  # Presume que `Cadastro` tem um relacionamento com User

    if request.method == 'POST':
        form = CadastroForm(request.POST, instance=cadastro, user_instance=user)
        if form.is_valid():
            # Atualiza os dados do Cadastro
            cadastro = form.save()
            
            # Atualiza os campos do User
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()

            return redirect('anamnese:index_usuario', cadastro_id=cadastro.id)
    else:
        form = CadastroForm(instance=cadastro, user_instance=user)

    return render(request, 'anamnese/cadastro_modal.html', {'form': form, 'cadastro_id': cadastro_id})



def atualizar_triglicerideos(request, cadastro_id):
    ficha = get_object_or_404(Ficha, usuario__id=cadastro_id)
    if request.method == 'POST':
        nivel_triglicerideos = request.POST.get('nivel_triglicerideos')
        if nivel_triglicerideos:  # Verifica se o valor foi enviado
            ficha.nivel_triglicerideos = float(nivel_triglicerideos)
            ficha.save()
        
    return render(request, 'anamnese/index_usuario.html', {
        'ficha': ficha,
        'cadastro_id': cadastro_id
    })