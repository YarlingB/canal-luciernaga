from rest_framework import serializers
from .models import HoraProgramacion, Programacion

class ProgramacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programacion
        fields = ('id','titulo','link')


class HoraProgramacionSerializer(serializers.HyperlinkedModelSerializer):
    programacion = ProgramacionSerializer()

    class Meta:
        model = HoraProgramacion
        fields = ('id', 'programacion', 'titulo','hora_inicio','hora_fin')