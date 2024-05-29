from rest_framework import serializers
from api.models.models_ropa import Ropa

class ropaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ropa  
        fields = [ 'id', 'material', 'color', 'marca', 'talla']