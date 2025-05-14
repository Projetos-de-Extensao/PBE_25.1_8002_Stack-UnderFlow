# minhaapp/api.py
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from censo.models import Morador
from censo.serializers import MoradorSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer

    @action(detail=False, methods=['get'])
    def dados_existentes(self, request):
        dados = Morador.objects.all()
        serializer = self.get_serializer(dados, many=True)
        return Response(serializer.data)