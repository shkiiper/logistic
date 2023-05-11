from rest_framework import serializers

from orders.models import Order
from orders.serializers import ProductSerializer
from .models import Delivery


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order.id')
    order_phone_number = serializers.CharField(source='order.phone_number')
    order_date = serializers.DateField(source='order.date')
    order_status = serializers.CharField(source='order.status')
    order_address_type = serializers.CharField(source='order.address_type')
    order_quantity = serializers.IntegerField(source='order.quantity')
    products = ProductSerializer(many=True)

    class Meta:
        model = Delivery
        fields = ['id', 'order_id', 'order_phone_number', 'order_date', 'order_status', 'order_address_type', 'order_quantity', 'products', 'date_end', 'status']
