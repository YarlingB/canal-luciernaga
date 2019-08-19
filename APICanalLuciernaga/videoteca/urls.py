from django.urls import path
from .views import Movies,Series,Documental,Video_detail,GetVideoInfo

urlpatterns = [
	path('peliculas/',Movies, name='movies'),
	path('series/',Series,name='series'),
	path('documentales/',Documental,name='documental'),
	path('detalle/<slug>/',Video_detail,name='Video_detail'),
	path('ajax/video_info/',GetVideoInfo,name='get_video_info'),

]