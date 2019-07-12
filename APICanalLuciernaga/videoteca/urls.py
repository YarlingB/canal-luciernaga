from rest_framework import routers
from django.urls import path, include
from .views import VideoViewSet, EpisodioViewSet


router = routers.DefaultRouter()
router.register(r'videoteca', VideoViewSet)
router.register(r'Episodio', EpisodioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]