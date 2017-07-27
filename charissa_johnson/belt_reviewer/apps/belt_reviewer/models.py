from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
	def validatedRegistration(self, form_data):
		errors = []

		if len(form_data['first_name']) == 0:
			errors.append("First name is required")
		if len(form_data['last_name']) == 0:
			errors.append("Last name is required")
		if len(form_data['email']) == 0:
			errors.append("Email is required")
		if len(form_data['password']) == 0:
			errors.append("Password is required")
		if form_data['password'] != form_data['password_confirm']:
			errors.append("Passwords do not match!")

		return errors

	def validateLogin(self, form_data):
		errors = []

		if len(form_data['email']) == 0:
			errors.append("Email is required")
		if len(form_data['password']) == 0:
			errors.append("Password is required")

		return errors

	def createUser(self, form_data):
		password = str(form_data['password'])
		hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
		user = User.objects.create(
				first_name = form_data['first_name'],
				last_name = form_data['last_name'],
				email = form_data['email'],
				password = hashed_pw
			)

		return user

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

class BookManager(models.Manager):
	def validateBook(self, form_data):
		errors = []

		if len(form_data['book_title']) == 0:
			errors.append("Book title cannot be empty")
		if len(form_data['author']) == 0:
			errors.append("Author name cannot be empty")
		if len(form_data['review']) == 0:
			errors.append("Review field cannot be empty")
		if len(form_data['rating']) == 0:
			errors.append("Rating cannot be empty")

		return errors

	def createBook(self, form_data, user):
		book = Book.objects.create(
				title = form_data['book_title'],
				author = form_data['author'],
				review = form_data['review'],
				rating = form_data['rating'],
				user = user
			)
		return book

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	review = models.TextField()
	rating = models.DecimalField(max_digits=3, decimal_places=2)
	user = models.ForeignKey(User, related_name='books')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = BookManager()