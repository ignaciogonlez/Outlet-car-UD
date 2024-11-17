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
    marcas = Marca.objects.all()

    # Generar el contenido dinámico con un for
    contenido = "<h1>Lista de Marcas</h1><ul>"
    for marca in marcas:
        contenido += f"<li>Detalles de la marca: {marca.nombre}</li>"
    contenido += "</ul>"

    # Devolver el contenido como respuesta
    return HttpResponse(contenido)

def listar_ofertasCoche(request):
    # Obtener todas las marcas
    ofertasCoche = OfertaCoche.objects.all()

    # Generar el contenido dinámico con un for
    contenido = "<h1>Lista de ofertasCoche</h1><ul>"
    for ofertaCoche in ofertasCoche:
        contenido += f"<li>Detalles de la oferta de coche: {ofertaCoche.coche}, {ofertaCoche.precio}, {ofertaCoche.descuento}, {ofertaCoche.disponible}, {ofertaCoche.destacada}</li>"
    contenido += "</ul>"

    # Devolver el contenido como respuesta
    return HttpResponse(contenido)


def listar_coches(request):
    # Obtener todas las marcas
    coches = Coche.objects.all()

    # Generar el contenido dinámico con un for
    contenido = "<h1>Lista de coches</h1><ul>"
    for coche in coches:
        contenido += f"<li>Detalles del coche: {coche.marca}, {coche.modelo}, {coche.anio}, {coche.kilometraje}, {coche.categoria}</li>"
    contenido += "</ul>"

    # Devolver el contenido como respuesta
    return HttpResponse(contenido)


def listar_categorias(request):
    # Obtener todas las marcas
    categorias = Categoria.objects.all()

    # Generar el contenido dinámico con un for
    contenido = "<h1>Lista de Categorias</h1><ul>"
    for categoria in categorias:
        contenido += f"<li>Detalles de la categoria: {categoria.nombre}</li>"
    contenido += "</ul>"

    # Devolver el contenido como respuesta
    return HttpResponse(contenido)

#devuelve el listado de categorias
def index_categorias(request):
	categorias = Categoria.objects.order_by('nombre')
	output = ', '.join([d.nombre for d in categorias])
	return HttpResponse(output)

#devuelve los datos de una categoria
def show_categoria(request, categoria_id):
	categoria = Categoria.objects.get(pk=categoria_id)
	return HttpResponse(f"Detalles de la categoria: {categoria.nombre}")

#devuelve los coches de una categorias
def index_coches(request, categoria_id):
	categorias = Categoria.objects.get(pk=categoria_id)
	output = ', '.join([e.nombre for e in categoria.coche_set.all()])
	return HttpResponse(output)

#devuelve los detalles de un coche
def show_coche(request, coche_id):
	coche = Coche.objects.get(pk=coche_id)
	return HttpResponse(f"Detalles del coche: {coche.marca}, {coche.modelo}, {coche.anio}, {coche.kilometraje}, {coche.categoria}")


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
    
    
    #Obtener la marca o devolver un 404 si no existe
    #marca = get_object_or_404(Marca, pk=marca_id)
    #return HttpResponse(f"Detalles de la marca: {marca.nombre}")