from django.db import models


# Create your models here.
class portfolio(models.Model):
    ID_port = models.IntegerField()
    nome_utilizador = models.CharField(max_length=100)


class tecnologias(models.Model):
    ID_tecn = models.IntegerField()
    nome = models.CharField(max_length=100)
    descrição = models.CharField(max_length=1000)
    imagem = models.CharField(max_length=100)
    portfolio = models.ForeignKey(portfolio, on_delete=models.CASCADE, related_name='tecnologias')


class factos(models.Model):
    ID_fact = models.IntegerField()
    titulo = models.CharField(max_length=100)
    conteudo = models.CharField(max_length=100)
    portfolio = models.ForeignKey(portfolio, on_delete=models.CASCADE, related_name='factos')


class licenciatura(models.Model):
    ID_licen = models.IntegerField()
    nome_licenciatura = models.CharField(max_length=100)
    portfolio = models.OneToOneField(portfolio, on_delete=models.CASCADE, related_name='licenciatura')


class cadeiras(models.Model):
    ID_cad = models.IntegerField()
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    coordenador = models.CharField(max_length=100)
    nota = models.IntegerField()
    rating = models.CharField(max_length=10)
    licneciatura = models.ForeignKey(licenciatura, on_delete=models.CASCADE, related_name='cadeiras')


class projetos(models.Model):
    ID_proj = models.IntegerField()
    titulo = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    descricao = models.CharField(max_length=2000)
    linguagem_programacao = models.CharField(max_length=10)
    cadeira = models.OneToOneField(cadeiras, on_delete=models.CASCADE, related_name='cadeira')
    portfolio = models.ForeignKey(portfolio, on_delete=models.CASCADE, related_name='projetos')
