from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Marca, Coche
from django.shortcuts import render, get_object_or_404


from django.http import HttpResponse
from .models import Marca

def index(request):
    # Obtener la primera marca (o la marca con id=1)
    try:
        marca = Marca.objects.get(pk=1)  # O ajusta la lógica según tus necesidades
        enlace = f'<a href="/marcas/{marca.id}/">marcas</a>'
    except Marca.DoesNotExist:
        enlace = 'marcas (no disponible)'
    
    return HttpResponse(
        f'Bienvenido a Outlet de Coches. Navega a {enlace} para ver la lista de marcas disponibles.'
    )

def listar_marcas(request):
    marcas = Marca.objects.all()  # Obtenemos todas las marcas
    context = {'marcas': marcas}
    return render(request, 'appOutletDjango/listar_marcas.html', context)

#devuelve el listado de categorias
def index_categorias(request):
	categorias = Categoria.objects.order_by('nombre')
	output = ', '.join([d.nombre for d in categorias])
	return HttpResponse(output)

#devuelve los datos de una categoria
def show_categoria(request, categoria_id):
	categoria = Categoria.objects.get(pk=categoria_id)
	output = f'Detalles de la categoria: {categoria.id}, {categoria.nombre}, {categoria.target}'
	return HttpResponse(output)

#devuelve los coches de una categorias
def index_coches(request, categoria_id):
	categorias = Categoria.objects.get(pk=categoria_id)
	output = ', '.join([e.nombre for e in categoria.coche_set.all()])
	return HttpResponse(output)

#devuelve los detalles de un coche
def show_coche(request, coche_id):
	coche = Coche.objects.get(pk=coche_id)
	output = f'Detalles del coche: {coche.id}, {coche.nombre}, {coche.fecha_matriculacion}, {coche.kilometros}, {str(coche.categoria)}. Marcas: {[m.nombre for m in coche.marcas.all()]}'
	return HttpResponse(output)

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