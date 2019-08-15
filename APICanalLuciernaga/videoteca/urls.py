from django.urls import path
from .views import Movies,Series,GetVideoInfo

urlpatterns = [
	path('peliculas/',Movies, name='movies'),
	path('series/',Series,name='series'),
	path('ajax/video_info/',GetVideoInfo,name='get_video_info'),

]