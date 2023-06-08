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
    path('calculadora', views.calculadora_view),
    path('imagem', views.imagem_view),
    path('indexLogin', views.index_login_view, name='index_login'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('cadeira/', views.formulario_cadeira_view, name='nova_cadeira'),
    path('facto/', views.formulario_facto_view, name='novo_facto'),
    path('projeto/', views.formulario_projeto_view, name='novo_projeto'),
    path('editaCadeira/<int:cadeira_id>/', views.update_cadeira_view, name='edita_cadeira'),
    path('editaFacto/<int:facto_id>/', views.update_facto_view, name='edita_facto'),
    path('editaProjeto/<int:projeto_id>/', views.update_projeto_view, name='edita_projeto'),
    path('apagaCadeira/<int:cadeira_id>', views.delete_cadeira_view, name='apaga_cadeira'),
    path('apagaFacto/<int:facto_id>', views.delete_facto_view, name='apaga_facto'),
    path('apagaProjeto/<int:projeto_id>', views.delete_projeto_view, name='apaga_projeto'),
]
