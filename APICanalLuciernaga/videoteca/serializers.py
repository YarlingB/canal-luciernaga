from rest_framework import serializers
from .models import Video, Tipo, Categoria, Director,Temporada,Episodio
from lugar.models import Pais

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id','nombre')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nombre')

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id','nombre')

class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = ('id','nombre')

class EpisodioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodio 
        fields = ('id','nombre')

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id','nombre')
        
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    tipo = TipoSerializer()
    categoria = CategoriaSerializer()
    director = DirectorSerializer()
    pais = PaisSerializer()


    class Meta:
        model = Video
        fields = ('id','tipo', 'categoria', 'nombre', 'sinopsis', 'fecha', 'director','produccion', 'pais','url')

class TemporadaSerializer(serializers.ModelSerializer):
    video = VideoSerializer()
    class Meta:
        model = Temporada
        fields = ('id','video','temporada')

class EpisodioSerializer(serializers.HyperlinkedModelSerializer):
    temporada = TemporadaSerializer()
    
    class Meta:
        model = Episodio
        fields = ('id','temporada','link','titulo','sinopsis')