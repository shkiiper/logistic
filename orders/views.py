from requests import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from datetime import timedelta, timezone
from orders.models import Product, Order
from orders.serializers import ProductSerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        product_data = request.data.pop('product')
        product = Product.objects.get(id=product_data['id'])
        order = Order.objects.create(product=product, **request.data)
        if order.address_type == 'kz':
            if order.status == 'track':
                order.date_end = order.date + timedelta(days=3)
            elif order.status == 'train':
                order.date_end = order.date + timedelta(days=2)
            elif order.status == 'avia':
                order.date_end = order.date + timedelta(days=1)
        elif order.address_type == 'uz':
            if order.status == 'track':
                order.date_end = order.date + timedelta(days=10)
            elif order.status == 'train':
                order.date_end = order.date + timedelta(days=6)
            elif order.status == 'avia':
                order.date_end = order.date + timedelta(days=3)
        elif order.address_type == 'ru':
            if order.status == 'track':
                order.date_end = order.date + timedelta(days=15)
            elif order.status == 'train':
                order.date_end = order.date + timedelta(days=10)
            elif order.status == 'avia':
                order.date_end = order.date + timedelta(days=5)
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def perform_update(self, serializer):
        product_data = self.request.data.get('product')
        if product_data:
            product_id = product_data.get('id')
            product = Product.objects.get(id=product_id)
            serializer.save(product=product)
        else:
            serializer.save()

    def update_date_status(self, order):
        if order.date_end < timezone.now().date():
            order.date_status = 'past'
        else:
            order.date_status = 'now'