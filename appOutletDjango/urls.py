from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta raíz
    path('marcas/', views.listar_marcas, name='listar_marcas'),  # Ruta para listar marcas
    path('marcas/<int:marca_id>/', views.show_marca, name='show_marca'),  # Detalles de una marca
    path('categorias/', views.listar_categorias, name='listar_categorias'),  # Ruta para listar marcas
    path('categorias/<int:categoria_id>/', views.show_categoria, name='show_categoria'),  # Detalles de una marca
    path('coches/', views.listar_coches, name='listar_coches'),  # Ruta para listar marcas
    path('coches/<int:coche_id>/', views.show_coche, name='show_coche'),  # Detalles de una marca
    path('ofertasCoche/', views.listar_ofertasCoche, name='listar_ofertasCoche'),  # Ruta para listar marcas
    path('ofertasCoche/<int:ofertaCoche_id>/', views.show_ofertaCoche, name='show_ofertaCoche'),  # Detalles de una marca

]