from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def validate(self, form_data):

		errors = []

		if len(form_data['first_name']) < 2:
			errors.append("First name must be longer than 2 characters")
		
		if form_data['first_name'].isalpha() == False:
			errors.append("First name in invalid format")
		
		if len(form_data['last_name']) < 2:
			errors.append("Last name must be longer than 2 characters")
		
		if form_data['last_name'].isalpha() == False:
			errors.append("First name in invalid format")
		
		if not EMAIL_REGEX.match(form_data['email']):
			errors.append("Invalid email")
		
		if len(form_data['email']) == 0:
			errors.append("Email cannot be blank")
		
		if len(form_data['password']) < 8:
			errors.append("Password must be at least 8 characters")
		
		if form_data['password_confirm'] != form_data['password']:
			errors.append("Passwords must match!")

		return errors

	def validate_login(self, form_data):
		errors = []

		if len(form_data['email']) == 0:
			errors.append("Email is not registered")
		if len(form_data['password']) == 0:
			errors.append("Please enter your password")

		return errors

	def login(self, form_data):
		errors = self.validate_login(form_data)

		if not errors:
			user = User.objects.filter(email=form_data['email']).first()

			if user:
				if str(form_data['password']) == user.password:
					return user
							
			errors.append('Invalid username or password')

		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	userManager = UserManager()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()