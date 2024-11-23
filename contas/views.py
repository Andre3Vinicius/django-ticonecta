from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # Validação das senhas
        if password != password_confirm:
            messages.error(request, 'As senhas não correspondem.')
        # Verifica se o nome de usuário já existe
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
        # Verifica se o e-mail já está cadastrado
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
        else:
            # Cria o usuário com e-mail
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')

    return render(request, 'contas/cadastro.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'contas/login.html')


def home_view(request):
    return render(request, 'contas/home.html')
    

def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('login')

def recuperar_senha():
    return redirect('recuperar_senha')

def lojas_view(request):
    return render(request, 'contas/lojas.html')

def chats_view(request):
    return render(request, 'contas/chats.html')

def descubra_view(request):
    return render(request, 'contas/descubra.html')

def ticomunica_view(request):
    return render(request, 'contas/ticomunica.html')


def desenvolvedores_view(request):
    return render(request, 'contas/desenvolvedores.html')

def designers_view(request):
    return render(request, 'contas/designers.html')

def analista_dados_view(request):
    return render(request, 'contas/analista_dados.html')

def qas_view(request):
    return render(request, 'contas/qas.html')