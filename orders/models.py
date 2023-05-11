from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    phone_number = models.CharField(max_length=20, default=None)
    date = models.DateTimeField(
        auto_now=True)
    products = models.ManyToManyField('Product')
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


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # описание продукта (текстовое поле, необязательное)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name
