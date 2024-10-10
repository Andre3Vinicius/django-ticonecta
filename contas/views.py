from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def cadastro(request):
    if request.method == 'POST':#Essa linha checa se a requisição recebida é do tipo POST, o que significa que o formulário foi enviado.
        form = UserCreationForm(request.POST)#Aqui, um formulário (UserCreationForm) é instanciado com os dados enviados no POST. O UserCreationForm é um formulário padrão do Django para criação de usuários.
        if form.is_valid():#Esta linha verifica se os dados do formulário são válidos (se, por exemplo, todos os campos obrigatórios foram preenchidos corretamente).
            form.save()#Se o formulário for válido, o método save() é chamado, o que cria um novo usuário no banco de dados.
            messages.success(request, 'Cadastro realizado com sucesso!')#Após o cadastro, uma mensagem de sucesso é adicionada à fila de mensagens do Django, informando que o cadastro foi realizado com sucesso.
            return redirect('login')#O usuário é redirecionado para a página de login após o cadastro bem-sucedido.
        else:
            form = UserCreationForm()#Se o formulário não for válido, ele reinicializa o formulário (embora isso seja redundante, pois já existe uma instância).
        return render(request, 'contas/cadastro.html', {'form': form})#Por fim, a função renderiza a página cadastro.html, passando o formulário (que pode conter erros de validação) para que os erros sejam exibidos. 
    
def login_view(request):
    if request.method == 'POST': #Assim como na função de cadastro, essa linha verifica se a requisição é do tipo POST, ou seja, se o formulário de login foi enviado.
        username=request.POST['username']#Aqui, o nome de usuário e a senha são extraídos dos dados enviados na requisição.
        password=request.POST['password']#Aqui, o nome de usuário e a senha são extraídos dos dados enviados na requisição.
        user = authenticate(request, username=username, password=password)#O método authenticate é utilizado para verificar se as credenciais (nome de usuário e senha) estão corretas. Se as credenciais forem válidas, o usuário autenticado é retornado; caso contrário, None é retornado.
        if user is not None:#Se a autenticação falhar (ou seja, o usuário ou a senha estão incorretos), uma mensagem de erro é adicionada, informando que as credenciais são inválidas.
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario ou senha inválidos')
    return render(request, 'contas/login.html')


def recuperar_senha(request):
    # Implementar lógica de recuperação de senha
    return render(request, 'contas/recuperar_senha.html')
