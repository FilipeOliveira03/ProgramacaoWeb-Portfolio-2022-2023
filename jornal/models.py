from django.db import models

# Create your models here.

class Family(models.Model):
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    brother_name = models.CharField(max_length=100)

    #def __str__(self):
    #   return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, null=False)
    birthDate = models.DateField()
    nacionality = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    family = models.OneToOneField(Family, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
