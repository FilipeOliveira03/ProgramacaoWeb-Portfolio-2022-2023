from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CadeiraForm, FactoForm, ProjetoForm

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


@login_required
def formulario_cadeira_view(request):
    form5 = CadeiraForm()

    if request.method == 'POST':
        form5 = CadeiraForm(request.POST)
        if form5.is_valid():
            form5.save()
        else:
            context1 = {'form5': form5, 'erro': 'Campos inválidos', 'cadeiras': cadeira.objects.all()}
            return render(request, 'cadeiras.html', context1)

    context1 = {'form5': form5, 'cadeiras': cadeira.objects.all()}
    return render(request, 'cadeiras.html', context1)


@login_required
def formulario_facto_view(request):
    form6 = FactoForm()

    if request.method == 'POST':
        form6 = FactoForm(request.POST)
        if form6.is_valid():
            form6.save()
        else:
            context1 = {'form6': form6, 'erro': 'Campos inválidos', 'factos': facto.objects.all()}
            return render(request, 'factos.html', context1)

    context1 = {'form6': form6, 'factos': facto.objects.all()}
    return render(request, 'factos.html', context1)


@login_required
def formulario_projeto_view(request):
    form7 = ProjetoForm()

    if request.method == 'POST':
        form7 = ProjetoForm(request.POST)
        if form7.is_valid():
            form7.save()
        else:
            context1 = {'form7': form7, 'erro': 'Campos inválidos', 'projetos': projeto.objects.all()}
            return render(request, 'projetos.html', context1)

    context1 = {'form7': form7, 'projetos': projeto.objects.all()}
    return render(request, 'projetos.html', context1)


@login_required
def update_cadeira_view(request, cadeira_id):
    Cadeira = cadeira.objects.get(id=cadeira_id)
    form8 = CadeiraForm(request.POST or None, instance=Cadeira)

    if form8.is_valid():
        form8.save()

    context = {'form8': form8, 'cadeira_id': cadeira_id, 'cadeiras': cadeira.objects.all()}
    return render(request, 'editaCadeiras.html', context)


@login_required
def update_facto_view(request, facto_id):
    Facto = facto.objects.get(id=facto_id)
    form9 = FactoForm(request.POST or None, instance=Facto)

    if form9.is_valid():
        form9.save()

    context = {'form9': form9, 'facto_id': facto_id, 'factos': facto.objects.all()}
    return render(request, 'editaFactos.html', context)


@login_required
def update_projeto_view(request, projeto_id):
    Projeto = projeto.objects.get(id=projeto_id)
    form10 = ProjetoForm(request.POST or None, instance=Projeto)

    if form10.is_valid():
        form10.save()

    context = {'form10': form10, 'projeto_id': projeto_id, 'projetos': projeto.objects.all()}
    return render(request, 'editaProjetos.html', context)


@login_required
def delete_cadeira_view(request, cadeira_id):
    cadeira.objects.get(id=cadeira_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_facto_view(request, facto_id):
    facto.objects.get(id=facto_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_projeto_view(request, projeto_id):
    projeto.objects.get(id=projeto_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))
