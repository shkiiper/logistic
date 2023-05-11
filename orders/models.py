from django.db import models


class Order(models.Model):
    number = models.CharField(max_length=20,
                              unique=True)
    date = models.DateTimeField(
        auto_now=True)
    address = models.CharField(max_length=200)
    products = models.ManyToManyField('Product')
    TYPE_STATUS_CHOICES = (
        ('avia', 'Avia'),
        ('train', 'Train'),
        ('track', 'Track'),
    )
    status = models.CharField(max_length=10, choices=TYPE_STATUS_CHOICES,
                              default='track')

    def __str__(self):
        return self.number


class Product(models.Model):
    name = models.CharField(max_length=100)  # название продукта (строка длиной до 100 символов)
    description = models.TextField(blank=True, null=True)  # описание продукта (текстовое поле, необязательное)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)  # цена продукта (десятичное число с 10 знаками перед запятой и 2 знаками после)
    quantity = models.DecimalField(max_digits=10, decimal_places=2,
                                   default=0)  # количество продукта (десятичное число с 10 знаками перед запятой и 2 знаками после, по умолчанию 0)

    def __str__(self):
        return self.name
