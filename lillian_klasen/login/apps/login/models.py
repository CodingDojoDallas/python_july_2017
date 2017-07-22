from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, form_data):

        errors = []

        # first name must be no fewer than 2 characters
        if len(form_data['first_name']) < 2:
            errors.append("First name must be at least 2 characters")

        # first name must be letters only
        if form_data['first_name'].isalpha() == False:
            errors.append("Invalid first name")

        # last name must be no fewer than 2 characters
        if len(form_data['last_name']) < 2:
            errors.append("Last name must be at least 2 characters")

        # last name must be letters only
        if form_data['last_name'].isalpha() == False:
            errors.append("Invalid last name")

        # email cant be blank
        if len(form_data['email']) == 0:
            errors.append("Email cannot be blank")

        # email must be in valid format
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append("Invalid email address")

        # password must be at least 8 characters
        if len(form_data['password']) < 8:
            errors.append("Invalid password")

        # password and confirm_password must match
        if form_data['password'] != form_data['confirm_password']:
            errors.append("Passwords must match")

        return errors

    def validate_login(self, form_data):

        errors = []

        user = User.objects.filter(email=form_data['email']).first()

        if len(form_data['email']) == 0:
            errors.append("Email can't be blank")

        if len(form_data['password']) == 0:
            errors.append("Password can't be blank")

        return errors

    def login(self, form_data):
        errors = []


        if not errors:
            user = User.objects.filter(email=form_data['email']).first()

        if user:
            if str(form_data['password']) != user.password:

                errors.append("Invalid password")

        return errors



class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    userManager = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        string_output = "first_name: {} last_name: {} email: {} password: {}"
        return string_output.format(
            self.first_name,
            self.last_name,
            self.email,
            self.password
        )
