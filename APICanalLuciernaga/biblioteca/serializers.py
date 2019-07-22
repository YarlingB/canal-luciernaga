from rest_framework import serializers
from .models import Categoria, Biblioteca

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nombre')

class BibliotecaSerializer(serializers.HyperlinkedModelSerializer):
    categoria = CategoriaSerializer()

    class Meta:
        model = Biblioteca
        fields = ('id', 'nombre', 'categoria','descripcion','foto','archivo')