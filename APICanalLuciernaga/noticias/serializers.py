from rest_framework import serializers
from .models import Comunicacion, Categoria
from lugar.models import Pais

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nombre')

# class ClasificacionSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = Clasificacion
#         fields = ('id', 'nombre')

class PaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'nombre')

class ComunicacionSerializer(serializers.HyperlinkedModelSerializer):
    categoria = CategoriaSerializer()
    # clasificacion = ClasificacionSerializer()
    pais = PaiSerializer()

    class Meta:
        model = Comunicacion
        fields = ('id','tipo', 'titulo','clasificacion','categoria','autor','fecha','foto','descripcion','pais','fuente','ultimo_momento')