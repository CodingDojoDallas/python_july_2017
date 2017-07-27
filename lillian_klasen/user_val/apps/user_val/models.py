from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def validate(self, form_data):

        errors = []

        if len(form_data['username']) < 8:
            errors.append("Invalid username.")

        if len(form_data['username']) > 26:
            errors.append("Invalid username.")

        return errors


class User(models.Model):
    username = models.CharField(max_length=30)
    userManager = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
