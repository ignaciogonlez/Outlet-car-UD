from django.urls import path
from .views import (
    IndexView,
    MarcaListView,
    MarcaDetailView,
    CategoriaListView,
    CategoriaDetailView,
    CocheListView,
    CocheDetailView,
    OfertaCocheListView,
    OfertaCocheDetailView,
    OfertaDestacadaListView,
    filtrar_coches_ajax
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Ruta raíz
    path('marcas/', MarcaListView.as_view(), name='listar_marcas'),  # Ruta para listar marcas
    path('marcas/<int:pk>/', MarcaDetailView.as_view(), name='show_marca'),  # Detalles de una marca
    path('categorias/', CategoriaListView.as_view(), name='listar_categorias'),  # Ruta para listar categorías
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='show_categoria'),  # Detalles de una categoría
    path('coches/', CocheListView.as_view(), name='listar_coches'),  # Ruta para listar coches
    path('coches/filtrar/', filtrar_coches_ajax, name='filtrar_coches'),  # Nueva ruta para AJAX
    path('coches/<int:pk>/', CocheDetailView.as_view(), name='show_coche'),  # Detalles de un coche
    path('ofertasCoche/', OfertaCocheListView.as_view(), name='listar_ofertasCoche'),  # Ruta para listar ofertas de coches
    path('ofertasCoche/<int:pk>/', OfertaCocheDetailView.as_view(), name='show_ofertaCoche'),  # Detalles de una oferta de coche
    path('ofertasDestacadas/', OfertaDestacadaListView.as_view(), name='listar_ofertas_destacadas'),  # Ruta para listar ofertas destacadas
]
