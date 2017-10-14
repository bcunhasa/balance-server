from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    """Image model serializer"""
    
    # image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Image
        depth = 1
        fields = ['id', 'image']
