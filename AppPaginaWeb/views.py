from django.shortcuts import render
from AppPaginaWeb.models import *
from AppPaginaWeb.forms import *

def index (request):
    return render (request, 'index.html')

def aviso(request):
    return render (request, 'aviso.html')



def crear_libro(request):
    if request.method == 'POST':
        formulario=CrearLibroForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            libro = Libros(nombre=formulario_limpio['nombre'], autor=formulario_limpio['autor'])
            libro.save()
        return render (request, 'index.html')
    else:
        formulario = CrearLibroForm
    return render (request, 'crear_libro.html', {'formulario': formulario})

def crear_serie(request):
    if request.method == 'POST':
        formulario=CrearSerieForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            serie = Series(nombre=formulario_limpio['nombre'], genero=formulario_limpio['genero'])
            serie.save()
            return render (request, 'index.html')
    else:
        formulario = CrearSerieForm
    return render (request, 'crear_serie.html', {'formulario': formulario})

def crear_juego(request):
    if request.method == 'POST':
        formulario=CrearJuegoForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            juego = Juegos(nombre=formulario_limpio['nombre'], creador=formulario_limpio['creador'])
            juego.save()
        return render (request, 'index.html')
    else:
        formulario = CrearJuegoForm
    return render (request, 'crear_juego.html', {'formulario': formulario})




def buscar_libro(request):
    data = request.GET.get('autor', '')
    
    error = ''

    if data:
        try:
            libros = Libros.objects.get(autor = data)
            return render(request, 'buscar_libro.html', {'libro': libros, 'autor': data})
        except Exception as exc:
            error = 'No hay resultados'
    return render (request, 'buscar_libro.html', {'error':error})

def buscar_serie(request):
    data = request.GET.get('nombre', '')
    
    error = ''

    if data:
        try:
            series = Series.objects.get(nombre = data)
            return render(request, 'buscar_serie.html', {'series': series, 'nombre': data})
        except Exception as exc:
            error = 'No hay resultados'
    return render (request, 'buscar_serie.html', {'error':error})

def buscar_juego(request):
    data = request.GET.get('creador', '')
    
    error = ''

    if data:
        try:
            juegos = Juegos.objects.get(creador = data)
            return render(request, 'buscar_juego.html', {'juego': juegos, 'creador': data})
        except Exception as exc:
            error = 'No hay resultados'
    return render (request, 'buscar_juego.html', {'error':error})