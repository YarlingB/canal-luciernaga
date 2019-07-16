from rest_framework import routers
from django.urls import path, include
from .views import BibliotecaViewSet


router = routers.DefaultRouter()
router.register(r'biblioteca', BibliotecaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]