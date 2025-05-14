from rest_framework import serializers
from censo.models import Morador, Indicadores

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = "__all__"
        
class IndicadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicadores
        fields = "__all__"
