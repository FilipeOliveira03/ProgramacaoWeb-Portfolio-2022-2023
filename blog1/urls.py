"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.index_view),
   path('novoAutor/', views.formulario_autor_view, name='novo_autor'),
   path('novoArtigo/', views.formulario_artigo_view, name='novo_artigo'),
   path('editaArtigo/<int:artigo_id>/', views.edita_formulario_artigo_view, name='edita_artigo'),
   path('apagaArtigo/<int:artigo_id>', views.apaga_artigo_view, name='apaga_artigo'),
   path('incrementar_likes/<int:artigo_id>/', views.incrementar_likes, name='incrementar_likes'),
   path('novoComentario/', views.formulario_comentario_view, name='novo_comentario'),
]
