from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Categoria, Marca, Coche, OfertaCoche

# Vista para la página principal
def index(request):
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

# Vista para listar las marcas
def listar_marcas(request):
    # Obtener todas las marcas
    marcas = Marca.objects.all().order_by('nombre')

    # Renderizar el contenido con el contexto
    return render(request, 'appOutletDjango/listar_marcas.html', {'marcas': marcas})

# Vista para listar las ofertas de coches
def listar_ofertasCoche(request):
    # Obtener todas las ofertas de coches
    ofertasCoche = OfertaCoche.objects.all()
    context = {
        'ofertasCoche': ofertasCoche
    }
    return render(request, 'appOutletDjango/listar_ofertas.html', context)

# Vista para listar los coches
def listar_coches(request):
    # Obtener todos los coches, junto con sus categorías (prefetch_related evita consultas adicionales para categorías)
    coches = Coche.objects.prefetch_related('categorias').all().order_by('modelo')
    
    # Generar el contexto con los coches
    contexto = {
        'coches': coches,
    }

    # Renderizar la plantilla con los coches ordenados
    return render(request, 'appOutletDjango/listar_coches.html', contexto)

# Vista para listar categorías
def listar_categorias(request):
    # Obtener todas las categorías
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'appOutletDjango/listar_categorias.html', context)

# Vista para mostrar los detalles de una categoría y todos los coches asociados
def show_categoria(request, categoria_id):
    # Obtener la categoría o devolver un 404 si no existe
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    # Obtener todos los coches asociados a la categoría
    coches = Coche.objects.filter(categorias=categoria)

    context = {
        'categoria': categoria,
        'coches': coches,
    }
    return render(request, 'appOutletDjango/listar_coches_categoria.html', context)

# Vista para mostrar los detalles de un coche
def show_coche(request, coche_id):
    # Obtener el coche o devolver un 404 si no existe
    coche = get_object_or_404(Coche, pk=coche_id)
    categorias = coche.categorias.all()  # Obtenemos todas las categorías del coche

    context = {
        'coche': coche,
        'categorias': categorias,
    }
    return render(request, 'appOutletDjango/detalles_coche.html', context)

# Vista para mostrar los detalles de una oferta de coche
def show_ofertaCoche(request, ofertaCoche_id):
    # Usar get_object_or_404 para asegurar la existencia de la oferta de coche
    ofertaCoche = get_object_or_404(OfertaCoche, pk=ofertaCoche_id)

    context = {
        'ofertaCoche': ofertaCoche,
    }
    return render(request, 'appOutletDjango/detalles_oferta.html', context)

# Vista para mostrar los detalles de una marca y los coches asociados
def show_marca(request, marca_id):
    # Obtener la marca o devolver un 404 si no existe
    marca = get_object_or_404(Marca, pk=marca_id)
    # Obtener todos los coches asociados con esta marca
    coches = Coche.objects.filter(marca=marca)
    # Pasar la marca y los coches al contexto
    context = {
        'marca': marca,
        'coches': coches
    }
    # Renderizar la plantilla de detalles de la marca
    return render(request, 'appOutletDjango/detalles_marca.html', context)

# Vista para listar ofertas destacadas
def listar_ofertas_destacadas(request):
    # Filtra solo las ofertas donde 'destacada' es True
    ofertas_destacadas = OfertaCoche.objects.filter(destacada=True)

    # Añade estas ofertas al contexto para la plantilla HTML
    context = {
        'ofertas': ofertas_destacadas,
    }

    # Renderiza la plantilla de ofertas con las ofertas destacadas
    return render(request, 'appOutletDjango/listar_ofertas_destacadas.html', context)

