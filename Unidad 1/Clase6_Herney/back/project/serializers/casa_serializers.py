from rest_framework import serializers
from api.models.casa import Casa

class CasaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Casa
