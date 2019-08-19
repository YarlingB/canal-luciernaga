from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import ComunicacionSerializer, CategoriaSerializer, ClasificacionSerializer

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
	latest_video = Video.objects.order_by('-id')[:10]
	series_list = Video.objects.filter(tipo=1).order_by('-id')
	peli_list = Video.objects.filter(tipo=2).order_by('-id')
	doc_list = Video.objects.filter(tipo=3).order_by('-id')
	bann_vid = Video.objects.filter(portada=True).order_by('-id')[:3]

	# bann_serie = bann_vid.

	return render(request,template,locals())

def news(request,template='news.html'):
	news_list = Comunicacion.objects.order_by('-id')
	thematic_list = Categoria.objects.order_by('id')
	ids = news_list.values_list('id',flat=True)
	common_tags = Comunicacion.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request,template,locals())

def news_detail(request,slug,template='news_detail.html'):
	object = Comunicacion.objects.get(slug=slug)
	news_list = Comunicacion.objects.order_by('-id')
	thematic_list = Categoria.objects.order_by('id')
	ids = news_list.values_list('id',flat=True)
	common_tags = Comunicacion.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request,template,locals())

