from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import ComunicacionSerializer, CategoriaSerializer, ClasificacionSerializer

from .views import *
from videoteca.models import Video,Temporada,Episodio

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

# Web Views
def home(request,template='index.html'):
	highlight_news = Comunicacion.objects.filter(ultimo_momento=1,tipo=1)[:5]
	latest_movies = Video.objects.order_by('-id')[:5]
	series_list = Video.objects.filter(tipo=1).order_by('-id')
	peli_list = Video.objects.filter(tipo=2).order_by('-id')
	doc_list = Video.objects.filter(tipo=3).order_by('-id')
	return render(request,template,locals())

