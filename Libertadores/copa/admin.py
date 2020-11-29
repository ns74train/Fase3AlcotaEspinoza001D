from django.contrib import admin

# Register your models here.
from . models import Usuario
from . models import Comentario

admin.site.register(Usuario)
admin.site.register(Comentario)