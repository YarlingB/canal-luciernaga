from rest_framework import viewsets
from .models import Video, Episodio,Tipo, Categoria
from .serializers import VideoSerializer, EpisodioSerializer, CategoriaSerializer, TipoSerializer

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
	