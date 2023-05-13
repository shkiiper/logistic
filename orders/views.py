from requests import Response
from rest_framework import viewsets, request
from rest_framework.permissions import AllowAny
from datetime import timedelta, timezone
from orders.models import Product, Order
from orders.serializers import ProductSerializer, OrderSerializer


# Первая строка импортирует класс Response из модуля requests, который используется для отправки HTTP-ответов в клиентское приложение.
# Вторая строка импортирует класс viewsets из rest_framework, который предоставляет общие методы для работы с моделями Django в REST API.
# Третья строка импортирует класс request из rest_framework, который используется для обработки HTTP-запросов.
# Четвертая строка импортирует класс AllowAny из rest_framework.permissions, который разрешает доступ к API для всех пользователей без проверки аутентификации.
# Пятая строка импортирует класс timedelta из модуля datetime, который представляет разницу между двумя датами или временем.
# Шестая строка импортирует модели Product и Order из приложения orders.
# Седьмая строка импортирует соответствующие сериализаторы для моделей Product и Order. Сериализаторы используются для преобразования данных из модели в формат, понятный клиентскому приложению.

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


# Этот код определяет класс ProductViewSet, который является ViewSet для модели Product.
# ViewSet - это класс, который определяет различные методы HTTP (например, GET, POST, PUT, DELETE), которые можно использовать для взаимодействия с моделью через REST API.
# Переменная permission_classes задает список разрешений, которые позволяют доступ к ProductViewSet для всех пользователей без проверки аутентификации.
# Переменная queryset определяет список объектов модели Product, которые будут доступны через ProductViewSet.
# Переменная serializer_class определяет класс сериализатора ProductSerializer, который будет использоваться для преобразования данных из модели Product в формат, понятный клиентскому приложению.
# Метод perform_create сохраняет новый объект Product с использованием переданного сериализатора.
# Метод perform_update сохраняет измененный объект Product с использованием переданного сериализатора.
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

        if order.date_end < timezone.now().date():
            order.date_status = 'past'
        else:
            order.date_status = 'now'

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

# OrderViewSet унаследован от viewsets.ModelViewSet и определяет операции, которые можно выполнять с заказами. В данном случае это create и perform_update.
# permission_classes определяет права доступа для этого представления. В данном случае это AllowAny, что означает, что любой пользователь может создавать и обновлять заказы.
# queryset определяет объекты, с которыми будет работать представление. В данном случае это все заказы, которые есть в базе данных.
# serializer_class указывает класс сериализатора, который будет использоваться для преобразования объектов в формат JSON и обратно.
# Метод create создает новый заказ на основе данных, полученных от клиента. Он использует OrderSerializer для сериализации данных заказа в JSON-формат и возвращает его в ответ на запрос.
# Метод perform_update обновляет заказ на основе данных, полученных от клиента. Он также использует OrderSerializer для сериализации данных заказа в JSON-формат и возвращает его в ответ на запрос. Если клиент также отправляет данные о товаре, метод находит этот товар в базе данных и обновляет связь заказа с товаром.
