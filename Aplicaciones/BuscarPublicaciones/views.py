from django.shortcuts import render
import json
from django.http import JsonResponse
import os
from django.conf import settings
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
     # Obtiene la ruta absoluta del archivo JSON
     json_file_path = os.path.join(settings.BASE_DIR, 'aplicaciones', 'buscarPublicaciones', 'data', 'publicaciones.json')
     with open(json_file_path, encoding='utf-8') as f:
        publicaciones = json.load(f)
        
        # if 'q' in request.GET:
        #     query = request.GET['q'].lower()
        #     resultados = [publicacion for publicacion in publicaciones if query in publicacion['nombre'].lower()]
        # else:
        #     resultados = None

        resultados = publicaciones
    
        return render(request, 'buscarPublicaciones.html', {'resultados': resultados})
