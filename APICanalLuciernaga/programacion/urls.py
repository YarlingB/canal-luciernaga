from rest_framework import routers
from django.urls import path, include
from .views import HoraProgramacionViewSet


router = routers.DefaultRouter()
router.register(r'programaciones', HoraProgramacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]