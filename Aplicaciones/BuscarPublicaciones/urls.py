# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('buscar-publicaciones/', views.buscarPublicacionesJSON, name='buscar_publicaciones'),
]
