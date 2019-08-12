from rest_framework import viewsets
from .models import Video, Episodio,Tipo, Categoria
from .serializers import VideoSerializer, EpisodioSerializer, CategoriaSerializer, TipoSerializer
from django.shortcuts import render

class VideoViewSet(viewsets.ModelViewSet):
	queryset = Video.objects.all()
	serializer_class  = VideoSerializer

class EpisodioViewSet(viewsets.ModelViewSet):
	queryset = Episodio.objects.all()
	serializer_class = EpisodioSerializer

class CategoriaVideoTecaViewSet(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer

class TipoVideoTecaViewSet(viewsets.ModelViewSet):
	queryset = Tipo.objects.all()
	serializer_class = TipoSerializer

def Movies(request,template='movies.html'):
	videos_all = Video.objects.all()
	movies_by_cat = {}
	for x in Categoria.objects.all():
		filt_movies = Video.objects.filter(categoria=x,tipo=1).order_by('-id')
		if filt_movies.exists():
			movies_by_cat[x] = filt_movies

	return render(request,template,locals())

	