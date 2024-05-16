from django.shortcuts import render
import json
from django.http import JsonResponse
# Create your views here.

## from .models import Publicacion

def buscarPublicaciones(request):
    if 'q' in request.GET:
        query = request.GET['q']
        resultados = Publicacion.objects.filter(titulo__icontains=query)
    else:
        resultados = None
    return render(request, 'buscar_publicaciones.html', {'resultados': resultados})

def buscarPublicacionesJSON(request):
     
    #  with open('publicaciones.json') as f:
    #     publicaciones = json.load(f)
        
    #     if 'q' in request.GET:
    #         query = request.GET['q'].lower()
    #         resultados = [publicacion for publicacion in publicaciones if query in publicacion['nombre'].lower()]
    #     else:
    #         resultados = None
    
    #     return JsonResponse(resultados, safe=False)
     return render(request, '.templates/BuscarPublicacion/buscarPublicaciones.html')
