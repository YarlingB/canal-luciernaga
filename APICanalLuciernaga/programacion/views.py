from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HoraProgramacionSerializer
from .models import HoraProgramacion

# Create your views here.
class HoraProgramacionViewSet(viewsets.ModelViewSet):
    queryset = HoraProgramacion.objects.all()
    serializer_class = HoraProgramacionSerializer