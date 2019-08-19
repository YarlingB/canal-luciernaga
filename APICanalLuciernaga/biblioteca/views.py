from django.shortcuts import render
from rest_framework import viewsets
from .models import Biblioteca, Categoria
from .serializers import BibliotecaSerializer, CategoriaSerializer

# Create your views here.

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer 

class CategoriaBibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

def Biblioteca_list(request,template='biblioteca.html'):
	b_list = Biblioteca.objects.order_by('-id')
	return render(request,template,locals())
