from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def currentUser(self, request):
        id = request.session['user_id']

        return User.objects.get(id=id)

    def createUser(self, name):
        user = User.objects.filter(name=name).first()

        if not user:
            user = User.objects.create(
                name = name
            )
        return user

class InterestManager(models.Manager):
    def createInterest(self, interest):
        interest = Interest.objects.filter(name=interest).first()

        if not interest:
            interest = Interest.objects.create(
                name = name
            )
        return interest

class User(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Interest(models.Model):
    name = models.CharField(max_length=30)
    user = models.ManyToManyField(User, related_name="interests")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = InterestManager()
