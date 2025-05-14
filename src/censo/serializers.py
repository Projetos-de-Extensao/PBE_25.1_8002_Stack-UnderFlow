from rest_framework import serializers
from censo.models import Morador

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = "__all__"


