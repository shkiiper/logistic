from rest_framework import routers, serializers, viewsets
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'order', 'amount', 'payment_date')

    amount = serializers.SerializerMethodField()

    def get_amount(self, obj):
        return obj.order.products.all()[0].price * obj.order.all()[0].quantity
