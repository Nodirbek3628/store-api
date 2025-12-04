from rest_framework import serializers
from .models import Product


class ProductSerialer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FilterProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    min_price = serializers.FloatField(required=False)
    max_price = serializers.FloatField(required=False)
    stock = serializers.CharField(required=False)
    create_at = serializers.DateField(required=False)