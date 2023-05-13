from django.contrib import admin

from orders.models import Order, Product

admin.site.register(Order)
admin.site.register(Product)



# Этот код регистрирует модели Order и Product в административном интерфейсе Django.
# Первая строка импортирует модуль admin из django.contrib, который содержит функционал для создания административных интерфейсов.
# Вторая строка импортирует модели Order и Product из orders.models.
# Третья строка вызывает функцию register() объекта admin.site и передает ей модель Order, что регистрирует эту модель в административном интерфейсе.
# Четвертая строка аналогично регистрирует модель Product в административном интерфейсе.
# Теперь модели Order и Product будут отображаться в административном интерфейсе Django, где можно создавать, изменять и удалять их записи.