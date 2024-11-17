from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Marca, Coche, OfertaCoche
from django.shortcuts import get_object_or_404


from django.http import HttpResponse
from .models import Marca

def index(request):
    # Obtener la primera marca (o la marca con id=1)
    try:
        marca = Marca.objects.get(pk=1)  # O ajusta la lógica según tus necesidades
        enlace = f'<a href="/marcas/{marca.id}/">marcas</a>'
    except Marca.DoesNotExist:
        enlace = 'marcas (no disponible)'
    context = {
        'enlace': enlace,
    }
    return render(request, 'appOutletDjango/index.html', context)

def listar_marcas(request):
    # Obtener todas las marcas
    marcas = Marca.objects.all().order_by('nombre')

    # Renderizar el contenido con el contexto
    return render(request, 'appOutletDjango/listar_marcas.html', {'marcas': marcas})

def listar_ofertasCoche(request):
    # Obtener todas las marcas
    ofertasCoche = OfertaCoche.objects.all()
    context = {
        'ofertasCoche': ofertasCoche
    }
    return render(request, 'appOutletDjango/listar_ofertas.html', context)


def listar_coches(request):
    # Obtener todas las marcas
    coches = Coche.objects.prefetch_related('categoria').all().order_by('modelo') 
     # Generar el contexto con los coches
    contexto = {
        'coches': coches,
    }

    # Renderizar la plantilla con los coches ordenados
    return render(request, 'appOutletDjango/listar_coches.html', contexto)


def listar_categorias(request):
    # Obtener todas las marcas
    categorias = Categoria.objects.all()

    # Generar el contenido dinámico con un for
    contenido = "<h1>Lista de Categorias</h1><ul>"
    context = {'categorias': categorias}
    return render(request, 'appOutletDjango/listar_categorias.html', context)

#devuelve el listado de categorias
def index_categorias(request):
	categorias = Categoria.objects.order_by('nombre')
	output = ', '.join([d.nombre for d in categorias])
	return HttpResponse(output)

# Muestra los detalles de una categoría y todos los coches asociados
def show_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    coches = Coche.objects.filter(categoria=categoria)
    
    context = {
        'categoria': categoria,
        'coches': coches
    }
    return render(request, 'appOutletDjango/listar_coches_categoria.html', context)

#devuelve los coches de una categorias
def index_coches(request, categoria_id):
	categorias = Categoria.objects.get(pk=categoria_id)
	output = ', '.join([e.nombre for e in categoria.coche_set.all()])
	return HttpResponse(output)

#devuelve los detalles de un coche
def show_coche(request, coche_id):
    coche = get_object_or_404(Coche, pk=coche_id)
    context = {'coche': coche}
    return render(request, 'appOutletDjango/detalles_coche.html', context)


def show_ofertaCoche(request, ofertaCoche_id):
	ofertaCoche = OfertaCoche.objects.get(pk=ofertaCoche_id)
	return HttpResponse(f"Detalles de la oferta de coche: {ofertaCoche.coche}, {ofertaCoche.precio}, {ofertaCoche.descuento}, {ofertaCoche.disponible}, {ofertaCoche.destacada}")



#devuelve los detalles de una marca
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

#devuelve las ofertas destacadas
def listar_ofertas_destacadas(request):
    # Filtra solo las ofertas donde 'destacada' es True
    ofertas_destacadas = OfertaCoche.objects.filter(destacada=True)

    # Añade estas ofertas al contexto para la plantilla HTML
    context = {
        'ofertas': ofertas_destacadas,
    }

    # Renderiza la plantilla de ofertas con las ofertas destacadas
    return render(request, 'appOutletDjango/listar_ofertas_destacadas.html', context)

