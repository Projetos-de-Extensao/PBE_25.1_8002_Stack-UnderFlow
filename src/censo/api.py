# minhaapp/api.py
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from censo.models import DadosCenso
from censo.serializers import DadosCensoSerializer

class DadosCensoViewSet(viewsets.ModelViewSet):
    queryset = DadosCenso.objects.all()
    serializer_class = DadosCensoSerializer

    @action(detail=False, methods=['get'])
    def dados_existentes(self, request):
        dados = DadosCenso.objects.all()
        serializer = self.get_serializer(dados, many=True)
        return Response(serializer.data)