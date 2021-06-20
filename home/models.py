from django.db import models
from django.contrib.auth.models import User

import string
import random


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

CHOICES = (
    ("Order Received", "Order Received"),
    ("Baking", "Baking"),
    ("Baked", "Baked"),
    ("Out for delivery", "Out for delivery"),
    ("Order delivered", "Order delivered"),
)

class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, blank=True)
    amount = models.IntegerField(default=100)
    status = models.CharField(max_length=100, choices=CHOICES, default="Order Received")
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not len(self.oredr_id):
            self.order_id = random_string_generator()
        super(Order, self).save(*args, **kwargs)

