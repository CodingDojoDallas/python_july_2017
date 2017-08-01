from __future__ import unicode_literals
from django.db import models
from validate_email import validate_email

#Our new manager!
#No methods in our new manager should ever catch the whole request object with a
#parameter!!! (just parts, like request.POST)

class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []

        if len(form_data['first_name'])==0:
            errors.append("First Name is required")
        if len(form_data['last_name'])==0:
            errors.append("Last Name is required")
        if len(form_data['email'])==0:
            errors.append("Email is required")
        if len(form_data['password'])==0:
            errors.append("Password is required")
        if form_data['password']!= form_data['password_confirmation']:
            errors.append("Password confirmation must match password.")
        return errors
        #print "inside the validate method"
    def validate_login(self, form_data):
        errors = []

        if len(form_data['email'])==0:
            errors.append("Email is required")
        if len(form_data['password'])==0:
            errors.append("Password is required")

        return errors

    def login(self, form_data):
        errors = self.validate_login(form_data)
        if not errors:
            user = User.objects.filter(email = form_data['email']).first()

            print user
            if user:
                if form_data['password'] == user.password:
                    return user
            errors.append('Invalid Account Information')

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.EmailField(max_length = 45)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!

    def __str__(self):
        string_output = "id: {} first_name: {} last_name: {} email: {} password: {}"
        return string_output.format(
            self.id,
            self.first_name,
            self.last_name,
            self.email,
            self.password,
        )
