from rest_framework import serializers
from logistics.models import Delivery
from .models import Order, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('date_end',)


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = 'id', 'phone_number', 'date', 'products', 'status', 'address_type', 'quantity', 'date_end', 'date_status'

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            Product.objects.create(order=order, **product_data)
        return order
