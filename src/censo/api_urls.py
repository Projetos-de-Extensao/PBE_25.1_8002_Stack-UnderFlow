# myapp/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from censo.api import MoradorViewSet, IndicadoresViewSet

router = DefaultRouter()
router.register(r'moradores', MoradorViewSet, basename='morador')
router.register(r'indicadores', IndicadoresViewSet, basename='indicadores')

urlpatterns = [
    path('', include(router.urls)),
]