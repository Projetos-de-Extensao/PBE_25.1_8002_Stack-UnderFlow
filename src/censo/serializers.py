from rest_framework import serializers
from censo.models import DadosCenso

class DadosCensoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosCenso
        fields = ['id', 'nome', 'conteudo', 'categorias']
        read_only_fields = ['id']
        
         