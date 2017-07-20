from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books(models.Model):
    Title = models.CharField(max_length=1000)
    Author = models.CharField(max_length=1000)
    Category = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
