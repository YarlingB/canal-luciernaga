from rest_framework import routers
from django.urls import path, include
from .views import ComunicacionViewSet


router = routers.DefaultRouter()
router.register(r'noticia', ComunicacionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]