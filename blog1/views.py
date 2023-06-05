from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


from .models import Blog, Dono, Autor, Artigo, Comentario, Area

from .forms import AutorForm, ArtigoForm


def index_view(request):
    return render(request, 'indexBlog.html', {
        'blog': Blog.objects.all(),
        'dono': Dono.objects.all(),
        'autores': Autor.objects.all(),
        'artigos': Artigo.objects.all(),
        'comentarios': Comentario.objects.all(),
        'areas': Area.objects.all(),

    })


def formulario_autor_view(request):
    form1 = AutorForm()

    if request.method == 'POST':
        form1 = AutorForm(request.POST)
        if form1.is_valid():
            form1.save()
        else:
            context1 = {'form1': form1, 'erro': 'Campos inválidos'}
            return render(request, 'novoAutor.html', context1)

    context1 = {'form1': form1}
    return render(request, 'novoAutor.html', context1)


def formulario_artigo_view(request):
    form2 = ArtigoForm()

    if request.method == 'POST':
        form2 = ArtigoForm(request.POST)
        if form2.is_valid():
            form2.save()
        else:
            context2 = {'form2': form2, 'erro': 'Campos inválidos', 'artigos': Artigo.objects.all()}
            return render(request, 'novoArtigo.html', context2)

    context2 = {'form2': form2, 'artigos': Artigo.objects.all()}
    return render(request, 'novoArtigo.html', context2)


def edita_formulario_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    form3 = ArtigoForm(request.POST or None, instance=artigo)

    if form3.is_valid():
        form3.save()

    context = {'form3': form3, 'artigo_id': artigo_id, 'artigos': Artigo.objects.all()}
    return render(request, 'editaArtigo.html', context)


def apaga_tarefa_view(request, artigo_id):
    Artigo.objects.get(id=artigo_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))

