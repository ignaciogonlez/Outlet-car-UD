from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta raíz
    path('marcas/', views.listar_marcas, name='listar_marcas'),  # Ruta para listar marcas
    path('marcas/<int:marca_id>/', views.show_marca, name='show_marca'),  # Detalles de una marca
]
