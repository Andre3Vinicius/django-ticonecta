from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, 'As senhas não correspondem.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            user = User.objects.create_user(username=username, password=password)
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

def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('login')

def recuperar_senha(request):
    return redirect('recuperar_senha')
