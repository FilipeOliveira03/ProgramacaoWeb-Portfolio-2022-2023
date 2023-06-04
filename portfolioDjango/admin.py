from django.contrib import admin

# Register your models here.
from .models import portfolio, tecnologia, facto, licenciatura, cadeira, projeto

# Register your models here.

admin.site.register(portfolio)
admin.site.register(tecnologia)
admin.site.register(facto)
admin.site.register(licenciatura)
admin.site.register(cadeira)
admin.site.register(projeto)
