from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publishedDate = models.IntegerField()
    category = models.CharField(max_length=50)
    in_print = models.IntegerField(max_length=1, default = 1)
