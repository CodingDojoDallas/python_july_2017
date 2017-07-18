from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create a new model called Product
# add fields for name, description, weight, price
# cost, and category
class Products(models.Model):
	product_name = models.CharField(max_length=30)
	product_description = models.TextField(max_length=1000)
	product_weight = models.IntegerField()
	product_price = models.IntegerField()
	product_cost = models.IntegerField()
	product_category = models.CharField(max_length=30)