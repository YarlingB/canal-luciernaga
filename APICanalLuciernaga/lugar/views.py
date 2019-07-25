from django.shortcuts import render
from rest_framework import viewsets
from .models import Pais
from .serializers import PaisSerializer
# Create your views here.
class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
