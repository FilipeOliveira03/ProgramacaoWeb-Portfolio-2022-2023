from django.http import HttpResponse
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
