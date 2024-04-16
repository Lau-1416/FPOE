from rest_framework import serializers
from api.models.bafle import Bafle

class BafleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bafle  
        #exclude = ['is_removed', 'created', 'modified']