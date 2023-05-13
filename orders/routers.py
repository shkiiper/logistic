from rest_framework import routers
from .views import ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'Product', ProductViewSet)
router.register(r'Order', OrderViewSet)


# Этот код определяет маршрутизатор для REST API с использованием фреймворка Django REST Framework.
# Первая строка импортирует модуль routers из rest_framework.
# Вторая строка импортирует классы ProductViewSet и OrderViewSet из модуля .views в текущем пакете.
# Третья строка создает объект маршрутизатора DefaultRouter, который предоставляет автоматические маршруты для стандартных действий CRUD (Create, Retrieve, Update, Delete).
# Четвертая строка вызывает метод register() объекта маршрутизатора router, чтобы зарегистрировать ProductViewSet с URL-адресом 'Product/' и OrderViewSet с URL-адресом 'Order/'. Таким образом, при обращении к URL-адресу 'Product/' будет выполняться соответствующий метод ProductViewSet, а при обращении к URL-адресу 'Order/' - метод OrderViewSet.
# После этого маршруты API, связанные с ProductViewSet и OrderViewSet, будут доступны по URL-адресам '/Product/' и '/Order/' соответственно.