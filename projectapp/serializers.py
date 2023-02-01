from rest_framework import serializers
from .models import ProductMainModel,ProductColourModel,ProductImageModel

class ProductMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMainModel
        fields = '__all__'

class ProductColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColourModel
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = '__all__'
