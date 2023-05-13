from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='orders')
    phone_number = models.CharField(max_length=20, default=None)
    date = models.DateField(auto_now_add=True)
    TYPE_STATUS_CHOICES = (
        ('avia', 'Avia'),
        ('train', 'Train'),
        ('track', 'Track'),
    )
    status = models.CharField(max_length=10, choices=TYPE_STATUS_CHOICES,
                              default='track')
    ADDRESS = (
        ("kz", "KZ"),
        ("ru", "RU"),
        ("uz", "UZ"),
    )
    address_type = models.CharField(
        max_length=20, choices=ADDRESS, verbose_name=_("Address Type"), default="kz"
    )

    quantity = models.DecimalField(max_digits=10, decimal_places=2,
                                   default=0)
    date_end = models.DateField(null=True)
    STATUS_CHOICES = (
        ('past', 'Past'),
        ('now', 'Now'),
    )
    date_status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                                   default='now')

    def __str__(self):
        return self.number

#
# Первая строка импортирует модуль models из библиотеки Django, который позволяет определять модели базы данных.
#
# Вторая строка импортирует функцию gettext_lazy из модуля django.utils.translation и переименовывает её в _.
#
# Третья строка определяет модель Product, которая наследуется от models.Model. В модели определены поля name (CharField), description (TextField) и price (DecimalField), а также метод str для строкового представления объекта модели.
#
# Четвертая строка определяет модель Order, которая наследуется от models.Model. В модели определены поля product (ForeignKey), phone_number (CharField), date (DateField), status (CharField с выбором из заданных значений), address_type (CharField с выбором из заданных значений и переводом с помощью _), quantity (DecimalField), date_end (DateField) и date_status (CharField с выбором из заданных значений).
#
# Пятая строка определяет метод str для модели Order, который возвращает значение поля number, которое не определено в модели.