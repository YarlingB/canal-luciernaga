from django.shortcuts import render,get_object_or_404
from django.http import Http404

from rest_framework import viewsets
from .serializers import HoraProgramacionSerializer
from .models import HoraProgramacion,Programacion
import datetime

# Create your views here.
class HoraProgramacionViewSet(viewsets.ModelViewSet):
    queryset = HoraProgramacion.objects.all()
    serializer_class = HoraProgramacionSerializer


def en_vivo(request,template='en_vivo.html'):
	fecha_hoy = datetime.date.today()
	
 	# v_directo = get_object_or_404(Programacion,)
	v_directo = Programacion.objects.filter(fecha = fecha_hoy)
	return render(request,template,locals())