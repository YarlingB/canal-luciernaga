from rest_framework import viewsets
from .models import Video, Episodio
from .serializers import VideoSerializer, EpisodioSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class  = VideoSerializer

class EpisodioViewSet(viewsets.ModelViewSet):
    queryset = Episodio.objects.all()
    serializer_class = EpisodioSerializer
