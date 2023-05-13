from django.urls import path, include
from .routers import router

urlpatterns = [
    path('', include(router.urls)),
]


# Этот код определяет URL-маршруты для приложения Django, используя маршрутизатор, определенный в файле routers.py.
# Первая строка импортирует модуль path и include из django.urls, которые используются для определения URL-маршрутов.
# Вторая строка импортирует объект router из файла routers.py.
# Третья строка определяет список urlpatterns, который содержит один элемент. Этот элемент вызывает функцию include(), которая включает все URL-маршруты, определенные в router.urls. Пустая строка в path() указывает на корневой URL-адрес.
# Таким образом, при обращении к корневому URL-адресу сайта, все URL-маршруты, определенные в маршрутизаторе router, будут включены в обработку. В данном случае, если ProductViewSet и OrderViewSet были зарегистрированы в маршрутизаторе соответственно на URL-адресах 'Product/' и 'Order/', то эти маршруты будут доступны по адресу '/Product/' и '/Order/'.