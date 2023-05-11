from rest_framework import routers

from payments.views import PaymentViewSet

router = routers.DefaultRouter()

router.register(r'payment', PaymentViewSet)
