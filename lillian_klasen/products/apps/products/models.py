from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    weight = models.IntegerField(5)
    price = models.IntegerField(5)
    cost = models.IntegerField(5)
    category = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
