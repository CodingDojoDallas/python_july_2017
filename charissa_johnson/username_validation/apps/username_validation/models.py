from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def validate(self, form_data):

		errors = []

		if len(form_data['username']) < 8:
			errors.append("Invalid username")

		if len(form_data['username']) > 26:
			errors.append("Invlaid username - too many characters")

		return errors

class Username(models.Model):
	username = models.CharField(max_length=255)
	usernameManager = UserManager()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()