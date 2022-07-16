from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def cadastro(request):

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    try:
        pass
    except Exception as e:
        messages.error(request, 'email invalido')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não são iguais')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuario já existe')
        return render(request, 'accounts/cadastro.html')


    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe')
        return render(request, 'accounts/cadastro.html')
    return render(request, 'accounts/cadastro.html')


    messages.success(request, 'Usuario cadastrado')

    user = User.objects.create_user(username=usuario, email=email,
    password=senha, first_name=nome, last_name=sobrenome)

    user.save()

    return redirect('login')



def dashboard(request):
    return render(request, 'accounts/dashboard.html')
