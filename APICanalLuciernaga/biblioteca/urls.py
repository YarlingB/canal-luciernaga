from django.urls import path
from .views import Biblioteca_list

urlpatterns = [
	path('',Biblioteca_list,name='biblioteca_list'),
]
