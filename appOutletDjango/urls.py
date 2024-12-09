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
    ConcertarCitaView,
    filtrar_coches_ajax,  # AJAX incluido en las mismas rutas
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('marcas/', MarcaListView.as_view(), name='listar_marcas'),
    path('marcas/<int:pk>/', MarcaDetailView.as_view(), name='show_marca'),
    path('categorias/', CategoriaListView.as_view(), name='listar_categorias'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='show_categoria'),
    path('coches/', CocheListView.as_view(), name='listar_coches'),
    path('coches/<int:pk>/', CocheDetailView.as_view(), name='show_coche'),
    path('ofertasCoche/', OfertaCocheListView.as_view(), name='listar_ofertasCoche'),
    path('ofertasCoche/<int:pk>/', OfertaCocheDetailView.as_view(), name='show_ofertaCoche'),
    path('ofertasDestacadas/', OfertaDestacadaListView.as_view(), name='listar_ofertas_destacadas'),
    path('citas/nueva/<int:oferta_id>/', ConcertarCitaView.as_view(), name='nueva_cita'),
    path('coches/filtrar/', filtrar_coches_ajax, name='filtrar_coches'),  # Ruta AJAX
]
