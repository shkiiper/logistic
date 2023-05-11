from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Delivery
from .serializers import DeliverySerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
