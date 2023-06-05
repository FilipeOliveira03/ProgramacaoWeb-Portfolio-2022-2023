from django.db import models

# Create your models here.


# Create your models here.
class portfolio(models.Model):
    nome_utilizador = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_utilizador


class tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.CharField(max_length=1000)
    imagem = models.CharField(max_length=100)
    portfolio = models.ForeignKey(portfolio, on_delete=models.CASCADE, related_name='tecnologias')

    def __str__(self):
        return self.nome


class facto(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.CharField(max_length=2000)
    portfolio = models.ForeignKey(portfolio, on_delete=models.CASCADE, related_name='factos')

    def __str__(self):
        return self.titulo


class licenciatura(models.Model):
    nome_licenciatura = models.CharField(max_length=100)
    portfolio = models.OneToOneField(portfolio, on_delete=models.CASCADE, related_name='licenciatura')

    def __str__(self):
        return self.nome_licenciatura


class cadeira(models.Model):
    nome = models.CharField(max_length=100)
    link_site = models.CharField(max_length=100, default=True)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    etcs = models.IntegerField()
    coordenador = models.CharField(max_length=100)
    nota =  models.CharField(max_length=20)
    rating = models.CharField(max_length=10, null=True, blank=True)
    licenciatura = models.ForeignKey(licenciatura, on_delete=models.CASCADE, related_name='cadeiras')

    def __str__(self):
        return self.nome


class projeto(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    descricao = models.CharField(max_length=2000)
    linguagem_programacao = models.CharField(max_length=10)
    cadeira = models.OneToOneField(cadeira, on_delete=models.CASCADE, related_name='cadeira')
    portfolio = models.ForeignKey(portfolio, on_delete=models.CASCADE, related_name='projetos')
    link_associado = models.CharField(max_length=100, default=True, blank=True)

    def __str__(self):
        return self.titulo
