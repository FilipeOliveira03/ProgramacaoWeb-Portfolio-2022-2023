from django.contrib import admin

# Register your models here.

from .models import Blog, Dono, Autor, Artigo, Comentario, Area

# Register your models here.

admin.site.register(Blog)
admin.site.register(Dono)
admin.site.register(Autor)
admin.site.register(Artigo)
admin.site.register(Comentario)
admin.site.register(Area)
