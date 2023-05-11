from django.db import models
from orders.models import Order


class Delivery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name
