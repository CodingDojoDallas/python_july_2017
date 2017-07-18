from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books(models.Model):
	title = models.CharField(max_length=30)
	author = models.CharField(max_length=30)
	category = models.CharField(max_length=30)
	published_date = models.DateTimeField(auto_now_add=True)
	in_print = models.BooleanField()