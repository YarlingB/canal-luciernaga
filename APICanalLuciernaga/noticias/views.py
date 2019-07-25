from django.shortcuts import render
from rest_framework import viewsets
from .models import Comunicacion, Categoria, Clasificacion
from .serializers import ComunicacionSerializer, CategoriaSerializer, ClasificacionSerializer

# Create your views here.
class ComunicacionViewSet(viewsets.ModelViewSet):
    queryset = Comunicacion.objects.all()
    serializer_class = ComunicacionSerializer

class CategoriaNoticiaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ClasificacionNoticiaViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer