# myapp/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from censo.api import MoradorViewSet

router = DefaultRouter()
router.register(r'moradores', MoradorViewSet, basename='morador')

urlpatterns = [
    path('', include(router.urls)),
]