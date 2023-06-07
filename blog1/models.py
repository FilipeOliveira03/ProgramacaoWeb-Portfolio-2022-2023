from django.db import models
from datetime import date


class Blog(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Dono(models.Model):
    nome = models.CharField(max_length=100)
    link_repo = models.CharField(max_length=500)
    pythonanywhere = models.CharField(max_length=500)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome


class Area(models.Model):
    nome = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    areas = models.ManyToManyField(Area, related_name='areas_interesse')

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=1000)
    link = models.CharField(max_length=500)
    data = models.DateField(default=date.today)
    likes = models.IntegerField(default=0)
    areas = models.ManyToManyField(Area, related_name='areas')
    autor = models.ManyToManyField(Autor, related_name='autores')

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    criador = models.CharField(max_length=100)
    texto = models.CharField(max_length=500)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='artigos')

    def __str__(self):
        return self.criador
