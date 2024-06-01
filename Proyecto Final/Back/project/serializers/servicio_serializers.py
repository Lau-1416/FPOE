from rest_framework import serializers
from api.models.Servicios import Servicio


class ServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicio  
        fields = '__all__'


