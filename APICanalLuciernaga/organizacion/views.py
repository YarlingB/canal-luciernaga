from django.shortcuts import render

from .models import *
from usuario.models import *

# Create your views here.
def index_org(request,template='index.html'):
	org = Organizacion.objects.order_by('-nombre')
	return render(request,template,locals())

def detail_org(request,slug,template='index.html'):
	object = Organizacion.objects.get(slug = slug)
	return render(request,template,locals())