from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Dono, Autor, Artigo, Comentario, Area
from .forms import AutorForm, ArtigoForm, ComentarioForm


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


def apaga_artigo_view(request, artigo_id):
    Artigo.objects.get(id=artigo_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def incrementar_likes(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    artigo.likes += 1
    artigo.save()
    return redirect(request.META.get('HTTP_REFERER'))


def formulario_comentario_view(request):
    form4 = ComentarioForm()

    if request.method == 'POST':
        form4 = ComentarioForm(request.POST)
        if form4.is_valid():
            form4.save()
        else:
            context1 = {'form4': form4, 'erro': 'Campos inválidos'}
            return render(request, 'novoComentario.html', context1)

    context1 = {'form4': form4}
    return render(request, 'novoComentario.html', context1)



