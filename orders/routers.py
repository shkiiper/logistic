from rest_framework import routers
from .views import ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'Product', ProductViewSet)
router.register(r'Order', OrderViewSet)
