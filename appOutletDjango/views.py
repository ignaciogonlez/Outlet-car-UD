from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Categoria, Marca, Coche, OfertaCoche
from django.http import JsonResponse

# Vista para la página principal (Index)
class IndexView(View):
    def get(self, request):
        # Filtra una oferta por cada marca, elige la oferta más barata o la más destacada, por ejemplo.
        ofertas_por_marca = []
        marcas = Marca.objects.all()
        for marca in marcas:
            oferta = OfertaCoche.objects.filter(coche__marca=marca).order_by('precio').first()  # Oferta más barata
            if oferta:
                ofertas_por_marca.append(oferta)

        context = {
            'ofertas_por_marca': ofertas_por_marca
        }
        return render(request, 'appOutletDjango/index.html', context)

# Listar las marcas
class MarcaListView(ListView):
    model = Marca
    template_name = 'appOutletDjango/listar_marcas.html'
    context_object_name = 'marcas'
    ordering = ['nombre']

# Listar categorías
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'appOutletDjango/listar_categorias.html'
    context_object_name = 'categorias'

# Listar coches
class CocheListView(ListView):
    model = Coche
    template_name = 'appOutletDjango/listar_coches.html'
    context_object_name = 'coches'
    ordering = ['modelo']
    queryset = Coche.objects.prefetch_related('categorias').all()

def filtrar_coches_ajax(request):
    kilometraje_max = request.GET.get('kilometraje_max', None)
    if kilometraje_max:
        try:
            kilometraje_max = int(kilometraje_max)
            coches = Coche.objects.filter(kilometraje__lte=kilometraje_max).select_related('marca').prefetch_related('categorias')
            data = [
                {
                    'id': coche.id,
                    'marca': coche.marca.nombre,
                    'modelo': coche.modelo,
                    'anio': coche.anio,
                    'kilometraje': coche.kilometraje,
                    'color': coche.color,
                    'combustible': coche.combustible,
                    'categorias': [categoria.nombre for categoria in coche.categorias.all()]
                }
                for coche in coches
            ]
            return JsonResponse({'coches': data})
        except ValueError:
            return JsonResponse({'error': 'Kilometraje inválido'}, status=400)
    return JsonResponse({'error': 'Falta el parámetro kilometraje_max'}, status=400)

# Mostrar los detalles de un coche
class CocheDetailView(DetailView):
    model = Coche
    template_name = 'appOutletDjango/detalles_coche.html'
    context_object_name = 'coche'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = self.object.categorias.all()
        return context

# Mostrar los detalles de una oferta de coche
class OfertaCocheDetailView(DetailView):
    model = OfertaCoche
    template_name = 'appOutletDjango/detalles_oferta.html'
    context_object_name = 'ofertaCoche'

# Mostrar los detalles de una marca y los coches asociados
class MarcaDetailView(DetailView):
    model = Marca
    template_name = 'appOutletDjango/detalles_marca.html'
    context_object_name = 'marca'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coches'] = Coche.objects.filter(marca=self.object)
        return context

# Listar ofertas destacadas
class OfertaDestacadaListView(ListView):
    model = OfertaCoche
    template_name = 'appOutletDjango/listar_ofertas_destacadas.html'
    context_object_name = 'ofertas'

    def get_queryset(self):
        return OfertaCoche.objects.filter(destacada=True)

# Mostrar los detalles de una categoría y los coches asociados
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'appOutletDjango/listar_coches_categoria.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añadimos los coches de la categoría al contexto
        context['coches'] = Coche.objects.filter(categorias=self.object)
        return context

# Listar ofertas de coches
class OfertaCocheListView(ListView):
    model = OfertaCoche
    template_name = 'appOutletDjango/listar_ofertas.html'
    context_object_name = 'ofertasCoche'

