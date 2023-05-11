from django.db import models
from orders.models import Order
from datetime import date


class Delivery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=0)
    date_from = models.DateField(null=True)
    date_to = models.DateField(null=True)
    STATUS_CHOICES = (
        ('past', 'Past'),
        ('now', 'Now'),
        ('planned', 'Planned'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='now')

    def __str__(self):
        return self.name
