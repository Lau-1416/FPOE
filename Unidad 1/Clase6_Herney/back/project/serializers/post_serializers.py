from rest_framework import serializers
from api.models.post import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post  
        exclude = ['is_removed', 'created', 'modified']
