from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        output = "id : {}, title: {}, created_at: {}"

        return output.format(
            self.id,
            self.title,
            self.created_at
        )
class Description(models.Model):
    description = models.CharField(max_length=1000)
    course = models.ForeignKey(Course, related_name="descriptions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
