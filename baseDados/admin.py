from django.contrib import admin
from .models import portfolio, tecnologias, factos, licenciatura, cadeiras, projetos

# Register your models here.

admin.site.register(portfolio)
admin.site.register(tecnologias)
admin.site.register(factos)
admin.site.register(licenciatura)
admin.site.register(cadeiras)
admin.site.register(projetos)
