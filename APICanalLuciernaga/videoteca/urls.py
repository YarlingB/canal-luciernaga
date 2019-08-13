from django.urls import path
from .views import Movies,Series

urlpatterns = [
	path('peliculas/',Movies, name='movies'),
	path('series/',Series,name='series'),
]