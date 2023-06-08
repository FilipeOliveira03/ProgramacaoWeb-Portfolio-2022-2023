from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import tecnologia, facto, cadeira, projeto


# Create your views here.
def index_view(request):
    return render(request, 'index.html', {
        'factos': facto.objects.all(),
        'cadeiras': cadeira.objects.all(),
        'tecnologias': tecnologia.objects.all(),
        'projetos': projeto.objects.all(),

    })


def calculadora_view(request):
    return render(request, 'calculadora.html')


def imagem_view(request):
    return render(request, 'imagem.html')


def index_login_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "adminPage.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index_login'))
        else:
            return render(request, 'login.html', {
                'message': "Credenciais inválidas."
            })

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'login.html', {
        "message": "Logged out."
    })
