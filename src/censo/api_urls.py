# myapp/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from censo.api import DadosCensoViewSet

router = DefaultRouter()
router.register(r'dados', DadosCensoViewSet, basename='dado')

urlpatterns = [
    path('', include(router.urls)),
]