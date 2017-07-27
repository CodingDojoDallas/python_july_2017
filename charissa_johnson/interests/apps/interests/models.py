from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def createUser(self, name):
		name = str(name).lower()
		user = self.userExists(name)

		if not user: 
			user = User.objects.create(
				name = name
			)
		return user

	def userExists(self, name):
		user = User.objects.filter(name=name).first()

		return user 

class User(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

class InterestManager(models.Manager):
	def createInterest(self, interest):
		name = str(interest).lower()
		interest = self.interestExists(name)

		if not interest:
			interest = Interest.objects.create(
				name = name
			)

		return interest

	def interestExists(self, interest):
		interest = Interest.objects.filter(name=interest).first()

		return interest

class Interest(models.Model):
	name = models.CharField(max_length=255)
	users = models.ManyToManyField(User, related_name="interests")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = InterestManager()