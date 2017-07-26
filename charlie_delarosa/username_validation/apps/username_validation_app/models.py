from __future__ import unicode_literals
from django.db import models
from validate_email import validate_email
#Our new manager!
#No methods in our new manager should ever catch the whole request object with a
#parameter!!! (just parts, like request.POST)

class UserManager(models.Manager):
    def login(self, email):
        is_valid = validate_email(email)

        if len(email) > 8:
            if len(email) < 26:
                if is_valid:
                    return True

        return False

    # def register(self, postData):
        # print ("Register a user here")
        # print ("If successful, maybe return {'theuser':user} where user is a user object?")
        # print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")

class User(models.Model):
    email = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    userManager = UserManager()
    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
