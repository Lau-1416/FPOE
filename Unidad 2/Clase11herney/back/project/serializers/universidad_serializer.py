from rest_framework import serializers
from api.models.Universidad import Universidad


class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = '__all__'
        