from django.contrib import admin
from .models import Marca, Categoria, Coche, OfertaCoche, Cita

# Admin para Marca
admin.site.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen', 'fundacion')  # Mostrar estos campos en la lista de marcas
    search_fields = ('nombre', 'pais_origen')  # Buscar por nombre o país de origen

# Admin para Categoria
admin.site.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Mostrar solo el nombre de la categoría
    search_fields = ('nombre',)  # Permitir búsqueda por nombre de categoría

# Admin para Coche
admin.site.register(Coche)
class CocheAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'kilometraje', 'color', 'combustible')  # Mostrar estos campos en la lista de coches
    list_filter = ('marca', 'categorias', 'combustible')  # Filtros para facilitar la búsqueda
    search_fields = ('modelo', 'marca__nombre', 'color')  # Buscar por modelo, marca o color
    filter_horizontal = ('categorias',)  # Mejorar la selección de categorías

# Admin para OfertaCoche
admin.site.register(OfertaCoche)
class OfertaCocheAdmin(admin.ModelAdmin):
    list_display = ('coche', 'precio', 'descuento', 'disponible', 'destacada')  # Mostrar estos campos en la lista de ofertas
    list_filter = ('coche__marca', 'disponible', 'destacada')  # Filtros para facilitar la búsqueda
    search_fields = ('coche__modelo', 'coche__marca__nombre')  # Buscar por modelo o marca
    list_editable = ('precio', 'descuento', 'disponible', 'destacada')  # Permitir editar directamente desde la lista

# Admin para Cita
admin.site.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'oferta', 'fecha_cita', 'hora_cita')  # Mostrar estos campos en la lista de citas
    list_filter = ('fecha_cita', 'hora_cita')  # Filtrar por fecha y hora
    search_fields = ('nombre', 'email', 'telefono', 'oferta__coche__modelo')  # Buscar por nombre, email, teléfono o modelo del coche
    date_hierarchy = 'fecha_cita'  # Navegación jerárquica por fecha
