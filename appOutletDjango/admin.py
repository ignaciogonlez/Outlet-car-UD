from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Marca, Coche
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Coche)