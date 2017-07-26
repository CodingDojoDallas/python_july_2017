from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    weight = models.IntegerField()
    price = models.IntegerField()
    cost = models.IntegerField()
    category = models.CharField(max_length=100)
