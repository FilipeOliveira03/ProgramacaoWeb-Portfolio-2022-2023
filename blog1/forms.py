from django.forms import ModelForm
from django import forms
from .models import Autor, Artigo


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ('nome', 'areas', 'blog',)

        widgets = {
            'areas': forms.CheckboxSelectMultiple,
        }

        labels = {
            'nome': 'Nome',
            'areas': 'Áreas',
        }


class ArtigoForm(ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'
        exclude = ('likes', 'data',)

        widgets = {
            'areas': forms.CheckboxSelectMultiple,
            'autor': forms.CheckboxSelectMultiple,
        }
