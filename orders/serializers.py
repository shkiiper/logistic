from rest_framework import serializers
from .models import Order, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'phone_number', 'date', 'product', 'status', 'address_type', 'quantity', 'date_end', 'date_status', 'total_price')

    def get_total_price(self, obj):
        # calculate the total price based on the product's price and quantity
        return obj.product.price * obj.quantity

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product = Product.objects.get(id=product_data['id'])
        order = Order.objects.create(product=product, **validated_data)
        return order
