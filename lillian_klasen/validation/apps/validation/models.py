from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validateRegistration(self, form_data):
        errors = []

        if len(form_data['first_name']) == 0:
            errors.append("First name is required")

        if len(form_data['last_name']) == 0:
            errors.append("Last name is required")

        if len(form_data['email']) == 0:
            errors.append("Email is required")

        if len(form_data['password']) == 0:
            errors.append("Password is required")

        if form_data['password'] != form_data['confirm_password']:
            errors.append("Passwords do not match")

        return errors

class User(models.Model):
    email = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
