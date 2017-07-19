from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    published_date = models.DateField()
    category = models.CharField(max_length=30)
    in_print = models.BooleanField()
