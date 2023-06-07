from django.shortcuts import render
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
