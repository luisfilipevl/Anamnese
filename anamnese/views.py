from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .forms import * 
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

        return redirect('dadospessoais', cadastro_id=cadastro_id)  # Redireciona após salvar

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
            
            cadastro = Cadastro.objects.create(
                nome_usuario=nome_usuario,
                email=email,
                senha=senha,
                CPF=CPF
            )

            Ficha.objects.create(usuario=cadastro)
        if request.method =="GET":
            return render (request, 'index.html')
        else:   
            usuario = request.POST.get ('nome_usuario')
            cpf = request.POST.get ('CPF')
            email = request.POST.get ('email')
            senha = request.POST.get ('senha')

            user = User.objects.create_user(username=usuario, email=email, password=senha)
            user.save()
    else:
        print("-entrou primeiro aqui")
        form = CadastroForm()
    
    return render(request,'anamnese/index.html', {'form': form})

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

    if request.method == 'POST':
        form = CadastroForm(request.POST, instance=cadastro)
        if form.is_valid():
            form.save()
            return redirect('index_usuario', cadastro_id=cadastro_id)
    else:
        form = CadastroForm(instance=cadastro)

    return render(request, 'anamnese/cadastro_modal.html', {'form': form, 'cadastro_id': cadastro_id})