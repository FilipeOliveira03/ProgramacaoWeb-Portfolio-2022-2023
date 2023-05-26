from django.contrib import admin
from jornal.models import Author
from jornal.models import Family
from jornal.models import Article
# Register your models here.

admin.site.register(Author)
admin.site.register(Family)
admin.site.register(Article)
