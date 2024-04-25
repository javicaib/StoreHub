from rest_framework import serializers
from .models import Product, DEFAULT_IMAGE_URL, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',
                  'purchase_price', 'quantity', 'image_url', 'tags']

    def create(self, validated_data):

        # Si el campo image_url está en blanco, establece la URL predeterminada
        if not validated_data.get('image_url'):
            url = f'{DEFAULT_IMAGE_URL}{validated_data.get("name")}'
            validated_data['image_url'] = url
        return super().create(validated_data)
