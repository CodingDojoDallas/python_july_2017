from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.CharField(max_length=4)
    category = models.CharField(max_length=100)
    in_print = models.BooleanField(default=True)
