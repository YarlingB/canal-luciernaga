from django.urls import path
from .views import en_vivo

urlpatterns = [
	path('',en_vivo,name='en_vivo'),
]