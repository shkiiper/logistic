from django.db import models
from orders.models import Order
from datetime import date


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=0)
    date_end = models.DateField(null=True)
    STATUS_CHOICES = (
        ('past', 'Past'),
        ('now', 'Now'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='now')

    def __str__(self):
        return f"{self.order}, {self.date_end}, {self.status}"
