from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    weight = models.DecimalField(decimal_places=2, max_digits = 5)
    price = models.DecimalField(decimal_places=2, max_digits = 6)
    sellerCost = models.DecimalField(decimal_places=2, max_digits = 6)
    category = models.CharField(max_length=255)
