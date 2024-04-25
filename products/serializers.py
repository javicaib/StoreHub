from rest_framework import serializers
from .models import Product, DEFAULT_IMAGE_URL


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['is_active']

    def create(self, validated_data):

        # Si el campo image_url está en blanco, establece la URL predeterminada
        if not validated_data.get('image_url'):
            url = f'{DEFAULT_IMAGE_URL}{validated_data.get("name")}'
            validated_data['image_url'] = url
        return super().create(validated_data)
