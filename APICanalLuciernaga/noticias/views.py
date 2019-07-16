from django.shortcuts import render
from rest_framework import viewsets
from .models import Comunicacion
from .serializers import ComunicacionSerializer

# Create your views here.
class ComunicacionViewSet(viewsets.ModelViewSet):
    queryset = Comunicacion.objects.all()
    serializer_class = ComunicacionSerializer

