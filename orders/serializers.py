from rest_framework import serializers
from .models import Order, Product
from decimal import Decimal


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id', 'phone_number', 'date', 'product', 'status', 'address_type', 'quantity', 'date_end',
            'date_status', 'total_price'
        )

    def get_total_price(self, obj):
        return obj.product.price * Decimal(obj.quantity)
