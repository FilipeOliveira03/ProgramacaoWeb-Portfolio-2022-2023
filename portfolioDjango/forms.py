from django.forms import ModelForm
from django import forms
from .models import cadeira, facto, projeto


class CadeiraForm(ModelForm):
    class Meta:
        model = cadeira
        fields = '__all__'


class FactoForm(ModelForm):
    class Meta:
        model = facto
        fields = '__all__'


class ProjetoForm(ModelForm):
    class Meta:
        model = projeto
        fields = '__all__'
